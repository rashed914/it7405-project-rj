from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Album, Review, Playlist, AlbumRequest
from bson import ObjectId
from django.db import models

from django.contrib.admin.views.decorators import staff_member_required
from .models import AlbumRequest







# ---------------------------------------------------
# HOME PAGE + SEARCH FUNCTION
# ---------------------------------------------------
def home(request):
    query = request.GET.get("q", "")

    if query:
        albums = Album.objects.filter(
            models.Q(title__icontains=query) |
            models.Q(artist__icontains=query) |
            models.Q(genre__icontains=query) |
            models.Q(year__icontains=query)
        )
    else:
        albums = Album.objects.all()

    return render(request, "albums/home.html", {
        "albums": albums,
        "query": query
    })


# ---------------------------------------------------
# ALBUM DETAIL PAGE
# ---------------------------------------------------
def album_detail(request, album_id):
    try:
        album = get_object_or_404(Album, _id=ObjectId(album_id))
    except:
        return redirect("home")

    reviews = Review.objects.filter(album=album)

    return render(request, "albums/album_detail.html", {
        "album": album,
        "album_id": str(album._id),
        "reviews": reviews
    })


# ---------------------------------------------------
# ADD REVIEW (LOGIN REQUIRED)
# ---------------------------------------------------
@login_required(login_url="login")
def add_review(request, album_id):
    try:
        album = get_object_or_404(Album, _id=ObjectId(album_id))
    except:
        return redirect("home")

    if request.method == "POST":
        rating = request.POST.get("rating")
        comment = request.POST.get("comment")

        if not rating or not comment:
            messages.error(request, "Please provide both rating and comment.")
            return redirect("add_review", album_id=album_id)

        Review.objects.create(
            album=album,
            username=request.user.username,
            rating=int(rating),
            comment=comment,
        )

        messages.success(request, "Your review has been submitted!")
        return redirect("album_detail", album_id=str(album._id))

    return render(request, "albums/add_review.html", {
        "album": album,
        "album_id": str(album._id)
    })


# ---------------------------------------------------
# USER REGISTRATION
# ---------------------------------------------------
def register_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        from django.contrib.auth.models import User

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect("register")

        User.objects.create_user(username=username, password=password)
        messages.success(request, "Account created successfully! You may now login.")
        return redirect("login")

    return render(request, "albums/register.html")


# ---------------------------------------------------
# LOGIN USER
# ---------------------------------------------------
def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")

        messages.error(request, "Invalid username or password.")

    return render(request, "albums/login.html")


# ---------------------------------------------------
# LOGOUT USER
# ---------------------------------------------------
def logout_user(request):
    logout(request)
    return redirect("home")


@login_required(login_url="login")
def save_to_playlist(request, album_id):
    album = get_object_or_404(Album, _id=ObjectId(album_id))
    playlist, created = Playlist.objects.get_or_create(user=request.user)

    # FIX ✔
    if not playlist.albums.filter(_id=album._id).exists():
        playlist.albums.add(album)

    messages.success(request, f"'{album.title}' added to your playlist!")
    return redirect("album_detail", album_id=album_id)





@login_required
def my_playlist(request):
    playlist, created = Playlist.objects.get_or_create(user=request.user)
    albums = playlist.albums.all()  # <-- FIX: use .all()
    return render(request, "albums/my_playlist.html", {
        "albums": albums
    })




@login_required(login_url="login")
def remove_from_playlist(request, album_id):
    playlist, created = Playlist.objects.get_or_create(user=request.user)
    album = get_object_or_404(Album, _id=ObjectId(album_id))

    if album in playlist.albums.all():
        playlist.albums.remove(album)
        playlist.save()

    messages.success(request, f"Removed '{album.title}' from your playlist.")
    return redirect("my_playlist")


@login_required(login_url="login")
def request_album(request):
    if request.method == "POST":
        title = request.POST.get("title")
        artist = request.POST.get("artist")
        message = request.POST.get("message")

        AlbumRequest.objects.create(
            user=request.user,
            requested_title=title,
            requested_artist=artist,
            message=message
        )

        from django.contrib import messages
        messages.success(request, "Your request has been submitted!")
        return redirect("request_album")

    return render(request, "albums/request_album.html")






@staff_member_required
def admin_request_list(request):
    requests_list = AlbumRequest.objects.all().order_by("-created_at")
    return render(request, "albums/admin_request_list.html", {
        "requests": requests_list
    })


@staff_member_required
def admin_delete_request(request, req_id):
    try:
        obj = AlbumRequest.objects.get(_id=ObjectId(req_id))
        obj.delete()
        messages.success(request, "Request deleted successfully!")
    except:
        messages.error(request, "Request not found.")

    return redirect("admin_request_list")









@staff_member_required
def admin_requests_dashboard(request):
    requests_list = AlbumRequest.objects.all().order_by("-created_at")
    return render(request, "albums/admin_requests_dashboard.html", {
        "requests": requests_list
    })


@staff_member_required
def admin_delete_album_request(request, req_id):
    try:
        req = AlbumRequest.objects.get(_id=ObjectId(req_id))
        req.delete()
        messages.success(request, "Album request deleted.")
    except:
        messages.error(request, "Request not found!")

    return redirect("admin_requests_dashboard")






@login_required
def admin_mark_completed(request, req_id):
    if not request.user.is_staff:
        return redirect("home")

    req = get_object_or_404(AlbumRequest, _id=ObjectId(req_id))
    req.status = "completed"
    req.save()

    messages.success(request, "Request marked as completed!")
    return redirect("admin_requests_dashboard")
