"""projectname URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('register_action/', views.register_action, name='register_action'),
    path('register1/', views.register1, name='register1'),
    path('registeraction<int:id>/', views.registeraction, name='registeraction'),    
    path('login/', views.login, name='login'),
    path('file1/',views.file1,name='file1'),
    path('login_action', views.login_action, name='login_action'),
    path('view_user/', views.view_user, name='view_user'),
    path('delete<int:id>/', views.delete, name='delete'),
    path('edit<int:id>/', views.edit, name='edit'),
    path('edit_action/', views.edit_action, name='edit_action'),
    path('image_upload/', views.image_upload, name='image_upload'),
    path('upload_action/', views.upload_action, name='upload_action'),
    path('dropdownbinding/', views.dropdownbinding, name='dropdownbinding'),
    path('getstate/', views.getstate, name='getstate'),
    path('place_action/', views.place_action, name='place_action'),
    path('hide/', views.hide, name='hide'),
    path('click/', views.click, name='click'),
    path('jquery/', views.jquery, name='jquery'),
    path('login1/',views.login1,name='login1'),
    path('loginaction/', views.loginaction,name='loginaction'),
    path('deletemn<int:id>/',views.deletemn, name='deletemn'),
    path('Editmn<int:id>/',views.Editmn,name='Editmn'),
    path('file1action/',views.file1action,name='file1action')


]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)



