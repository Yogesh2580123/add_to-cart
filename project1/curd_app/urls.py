from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('student/', views.StudentList.as_view(), name='list_url'),
    path('cv/', views.StudentCreate.as_view(), name='create_url'),
    path('rv/', views.StudentRetrieve.as_view(), name='retrieve_url'),
    path('uv/<int:pk>/', views.StudentUpdate.as_view(), name='update_url'),
    path('dv/<int:pk>/', views.StudentDelete.as_view(), name='delete_url'),
    path('sgv/', views.SignupView.as_view(), name='signup_url'),
    path('log/', LoginView.as_view(template_name='curd_app/login.html'), name='login_url'),
    path('out/', LogoutView.as_view(), name='logout_url'),

]