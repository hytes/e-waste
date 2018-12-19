from django.conf.urls import url
from django.conf import settings
from.import views
app_name='ewaste'
urlpatterns = [
    
    url('signup/', views.signup, name='signup'),
    url('login/', views.signin, name='signin'),
    url('logout/', views.logout, name='logout'),
    url('password/', views.change_password, name='change_password'),
    url('detail/', views.detail, name='detail'),
    url('user/', views.user, name='user'),
    url('specific/', views.pick, name='specific'),
]