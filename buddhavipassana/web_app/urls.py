from django.conf.urls import url
from web_app import views

# SET THE NAMESPACE!
app_name = 'web_app'

urlpatterns=[
    url(r'^$',views.intro_web, name='buddhavipassana_intro'),
    url(r'^AjahnTong/$',views.ajahn, name='ajahn'),
    url(r'^rolunk/$',views.rolunk, name='rolunk'),
    url(r'^oktatok/$',views.oktatok, name='oktatok'),
    url(r'^tanfolyamok/$',views.tanfolyamok, name='tanfolyamok'),
    url(r'^technikarol/$',views.technikarol, name='technikarol'),
    url(r'^gyik/$',views.gyik, name='gyik'),
    url(r'^kapcsolat/$',views.kapcsolat, name='kapcsolat'),
    url(r'^indexEng/$',views.indexEng, name='indexEng'),
    url(r'^ajahnEng/$',views.ajahnEng, name='ajahnEng'),
    url(r'^about/$',views.about, name='about'),
    url(r'^teachers/$',views.teachers, name='teachers'),
    url(r'^courses/$',views.courses, name='courses'),
    url(r'^technique/$',views.technique, name='technique'),
    url(r'^faq/$',views.faq, name='faq'),
    url(r'^contact/$',views.contact, name='contact'),
    url(r'^answere/$',views.answere, name='answere'),
    url(r'^valasz/$',views.valasz, name='valasz'),

]
