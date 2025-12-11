from django.urls import path
from . import views

urlpatterns = [

    # HOME PAGE
    path('', views.home, name='home'),

    # ALBUM DETAIL PAGE
    path('album/<str:album_id>/', views.album_detail, name='album_detail'),

    # ADD REVIEW PAGE
    path('album/<str:album_id>/add-review/', views.add_review, name='add_review'),

    # AUTHENTICATION
    path('login/', views.login_user, name='login'),
    path('register/', views.register_user, name='register'),
    path('logout/', views.logout_user, name='logout'),

    # ⭐ PLAYLIST ROUTES (MUST BE INSIDE urlpatterns)
    path("playlist/", views.my_playlist, name="my_playlist"),
    path('album/<str:album_id>/save/', views.save_to_playlist, name="save_to_playlist"),
    path('playlist/remove/<str:album_id>/', views.remove_from_playlist, name="remove_from_playlist"),

path("request-album/", views.request_album, name="request_album"),


# ADMIN REQUEST LIST
path("admin/requests/", views.admin_request_list, name="admin_request_list"),
path("admin/requests/delete/<str:req_id>/", views.admin_delete_request, name="admin_delete_request"),


# ADMIN DASHBOARD FOR REQUESTS
path("admin-dashboard/requests/", views.admin_requests_dashboard, name="admin_requests_dashboard"),
path("admin-dashboard/requests/delete/<str:req_id>/", views.admin_delete_album_request, name="admin_delete_album_request"),

path("admin-dashboard/requests/complete/<str:req_id>/", views.admin_mark_completed, name="admin_mark_completed"),

]
