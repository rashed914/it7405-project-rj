from django.contrib import admin
from .models import Album, Review, Playlist, AlbumRequest


# ------------------------
# ALBUM ADMIN
# ------------------------
@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ("title", "artist", "genre", "year", "id_str")
    search_fields = ("title", "artist", "genre")
    list_filter = ("genre", "year")
    readonly_fields = ("_id",)
    ordering = ("title",)


# ------------------------
# REVIEW ADMIN
# ------------------------
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("username", "album", "rating", "_id")
    search_fields = ("username", "album__title")
    list_filter = ("rating",)
    readonly_fields = ("_id",)
    ordering = ("-rating",)


# ------------------------
# PLAYLIST ADMIN
# ------------------------
@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    list_display = ("user",)


# ------------------------
# ALBUM REQUEST ADMIN
# ------------------------
@admin.register(AlbumRequest)
class AlbumRequestAdmin(admin.ModelAdmin):
    list_display = ("requested_title", "requested_artist", "user", "created_at")
    search_fields = ("requested_title", "requested_artist", "user__username")
    list_filter = ("created_at",)   # Only valid field for filtering
    readonly_fields = ("_id", "created_at")
    ordering = ("-created_at",)
