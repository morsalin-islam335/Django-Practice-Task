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
    path('addMusician/', views.addMusician, name = 'addMusician'),
    path('editMusician/<int:id>/', views.editMusician, name = 'editMusician'),
    path("deleteMusician/<int:id>/", views.deleteMusician, name = 'deleteMusician'),
    path("addAlbum/", views.addAlbum, name = 'addAlbum'),
    path("editAlbum/<int:id>/", views.editAlbum, name = 'editAlbum'),
    path("deleteAlbum/<int:id>/", views.deleteAlbum, name = 'deleteAlbum'),
    
    
]