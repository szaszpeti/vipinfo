from django.conf.urls import url
from db_app import views

# SET THE NAMESPACE!
app_name = 'db_app'

urlpatterns=[
    url(r'^$',views.user_login,name='user_login'),
    url(r'^register/$',views.register,name='register'),
    url(r'^welcome_main/$',views.welcome_main,name='welcome_main'),
    url(r'^find_meditator/$',views.find_meditator,name='find_meditator'),
    url(r'^add_meditator/$',views.add_meditator,name='add_meditator'),
    url(r'^user_logout/$',views.user_logout,name='user_logout'),
    url(r'^find_meditator_byname/$',views.find_meditator_byname,name='find_meditator_byname'),
    url(r'^find_meditator_bycountry/$',views.find_meditator_bycountry,name='find_meditator_bycountry'),
    url(r'^find_meditator_byborn/$',views.find_meditator_byborn,name='find_meditator_byborn'),
    url(r'^find_meditator_byprofession/$',views.find_meditator_byprofession,name='find_meditator_byprofession'),
    url(r'^(?P<meditator_id>[0-9]+)/$', views.detail, name='detail'),


]
