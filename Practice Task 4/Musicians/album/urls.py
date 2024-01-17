from django.urls import path

from album import views
urlpatterns = [
    path("", views.home, name = 'homepage'),
    path("addMusician/", views.addMusician, name = 'adMusician'),
    path('addAlbum/', views.addAlbum, name =  'adAlbum'),
    path("EditMusician/<int:id>/", views.editMusician, name = 'editMusician'),
    path("deleteMusician/<int:id>/", views.deleteMusician, name = 'deleteMusician'),
    path("editAlbum/<int:id>/", views.editAlbum, name = 'editAlbum'),
    
]
