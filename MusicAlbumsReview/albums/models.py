from djongo import models
from bson import ObjectId
from django.contrib.auth.models import User

# ------------------------
# ALBUM MODEL
# ------------------------
class Album(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    genre = models.CharField(max_length=50)
    year = models.IntegerField()
    cover_url = models.CharField(max_length=500)

    class Meta:
        db_table = "albums"  # <-- Uses your existing MongoDB collection

    def __str__(self):
        return self.title

    # Helper so templates can safely use album.id_str
    @property
    def id_str(self):
        return str(self._id)


# ------------------------
# REVIEW MODEL
# ------------------------
class Review(models.Model):
    _id = models.ObjectIdField(primary_key=True)

    album = models.ForeignKey(
        Album,
        on_delete=models.CASCADE,
        related_name="reviews"
    )

    username = models.CharField(max_length=100)  # Comes from request.user.username
    rating = models.IntegerField()
    comment = models.TextField()

    class Meta:
        db_table = "reviews"  # <-- Uses existing reviews collection

    def __str__(self):
        return f"{self.username} ({self.rating}/5)"




class Playlist(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    albums = models.ArrayReferenceField(
        to=Album,
        on_delete=models.CASCADE,
        blank=True
    )

    class Meta:
        db_table = "playlists"

    def __str__(self):
        return f"{self.user.username}'s playlist"


class AlbumRequest(models.Model):
    _id = models.ObjectIdField(primary_key=True)

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    requested_title = models.CharField(max_length=200)
    requested_artist = models.CharField(max_length=200)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    STATUS_CHOICES = (
        ("pending", "Pending"),
        ("completed", "Completed"),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")

    class Meta:
        db_table = "album_requests"

    def __str__(self):
        return f"{self.requested_title} by {self.requested_artist}"

    @property
    def id_str(self):
        return str(self._id)

