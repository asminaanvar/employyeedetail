from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('logout/',views.logoutPage,name='logout'),
    path('login/',views.loginPage,name='loginpage'),
    path('register/',views.registerUser,name='register'),
    path('index/',views.index,name='index'),
    path('',views.home,name='home'),
    path('create/',views.createfile,name='createfile'),
    path('uploadfile/',views.uploadfile,name='uploadfile'),
    path('deleteFile/<int:pk>/',views.deleteFile,name='delete_file'),
    path('view/<int:pk>/',views.view,name='view'),
    path('add/',views.add,name='add'),
    path('edit/<int:pk>/',views.edit,name='edit'),
    path('delete/<int:pk>/',views.delete,name='delete'),
]
urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)