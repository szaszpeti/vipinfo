
from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Document
from .forms import BlogDocumentForm, BlogCategoryForm
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse


# Create your views here.
def index(request):
    all_category = Category.objects.all()
    return render(request, 'blog_info/blog_index.html', {'all_category':all_category})

def details(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    documentId = Category.objects.get(pk=category_id)
    document = documentId.document_set.all()

    return render(request, 'blog_info/blog_details.html', {'category':category, 'document':document})

def read(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    documentId = Category.objects.get(pk=category_id)


    if request.method == "POST":
        selected_document = category.document_set.get(pk=request.POST['read'])
        read_doc = str(selected_document).split(' ')[0]

    return render(request, 'blog_info/documents/' + read_doc + '.html', {'doc':selected_document})



def blog_create(request):

    if request.method == 'POST':

        form = BlogCategoryForm(request.POST, request.FILES)

        if form.is_valid():

            topic = request.POST.get('topic')
            topic_info = request.POST.get('topic_info')
            # topic_logo = handle_uploaded_file(request.FILES['topic_logo'])
            #
            # print(topic, topic_info)

            instance = Category(topic=topic, topic_info=topic_info, topic_logo=request.FILES['topic_logo'])
            instance.save()


            return HttpResponseRedirect(reverse('blog_info:blog_index'))



    else:
        # Was not an HTTP post so we just render the forms as blank.
        form = BlogCategoryForm()

    return render(request, 'blog_info/blog_create.html', {'form':form})

def blog_new_document(request):

    if request.method == 'POST':

        form = BlogDocumentForm(request.POST, request.FILES)

        if form.is_valid():

            topic = request.POST.get('topic')
            document_title = request.POST.get('title')
            document_url = request.POST.get('url')


            instance = Document(topic=topic, document_title=document_title, document_url=document_url, document_logo=request.FILES['logo'])
            instance.save()


            return HttpResponseRedirect(reverse('blog_info:blog_index'))



    else:
        # Was not an HTTP post so we just render the forms as blank.
        form = BlogDocumentForm()

    return render(request, 'blog_info/blog_new_document.html', {'form':form})


def like(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    documentId = Category.objects.get(pk=category_id)
    document = documentId.document_set.all()

    if request.method == "POST":
        selected_documentLike = category.document_set.get(pk=request.POST['likePlus'])
        selected_documentLike.like += 1
        selected_documentLike.save()

        return render(request, 'blog_info/blog_details.html', {'category': category, 'document': document})


def dislike(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    documentId = Category.objects.get(pk=category_id)
    document = documentId.document_set.all()

    if request.method == "POST":
        selected_documentDislike = category.document_set.get(pk=request.POST['dislikePlus'])
        selected_documentDislike.dislike += 1
        selected_documentDislike.save()

        return render(request, 'blog_info/blog_details.html', {'category': category, 'document': document})

def delete(request, category_id):
    category = get_object_or_404(Category, pk=category_id)

    if request.method == "POST":
        selected_document = category.document_set.get(pk=request.POST['delete'])
        selected_document.delete()


        return redirect('blog_info:blog_index')

# def update(request, category_id):
#     category = get_object_or_404(Category, pk=category_id)
#
#     if request.method == "POST":
#         selected_document = category.document_set.get(pk=request.POST['update'])
#
#         form = BlogDocumentForm(request.POST, request.FILES)
#
#         if form.is_valid():
#
#             document_title = request.POST.get('title')
#             document_url = request.POST.get('url')
#
#             instance = Document(topic=topic, document_title=document_title, document_url=document_url,
#                                 document_logo=request.FILES['logo'])
#             instance.save()
#
#             return HttpResponseRedirect(reverse('blog_info:blog_index'))
#
#
#
#         else:
#             # Was not an HTTP post so we just render the forms as blank.
#             form = BlogDocumentForm()
#
#         return render(request, 'blog_info/blog_new_document.html', {'form': form})
#
#         category = form.save(commit=false)
#             category.save()
#
#
#
#             if request.method == "POST":
#                 selected_document = category.document_set.get(pk=request.POST['update'])
#
#
#             return render(request, 'blog_info/documents/blog_update.html', {'doc':selected_document, 'form':form})
