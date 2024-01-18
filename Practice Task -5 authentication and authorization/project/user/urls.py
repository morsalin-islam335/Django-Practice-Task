from django.urls import path

from user import views

urlpatterns = [
    path("", views.home, name = 'homepage'),
    path('signUp/', views.signUp, name = 'signUp'),
    path('login/', views.userLogin, name = 'login'),
    path("profile/", views.profile, name = 'profile'),
    path('logOut/', views.UserLogout, name = 'logout'),
    path("editInfo/", views.updateProfile, name = 'updateProfile'),
    path('changePassWithOldPass/', views.changePasswordWitOldPassword, name = 'changePass1'),
    path('changePassWithoutOld/', views.changePasswordWithoutOldPassword, name = 'changePass2'),
    
]