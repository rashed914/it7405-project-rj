
Music Albums Review A Full Web Application Using Django, MongoDB (Djongo), and Modern UI for Browse albums, Search albums, Submit reviews (login required), Maintain a personal playlist (login required), Request new albums (login required), Admin dashboard for managing album requests (only for admin users)

(Features) #Album Browsing & Search: Search by title, artist, genre, or year, #Reviews:Users can post reviews after logging in, Star rating UI (1–5), #Playlists: Save albums to personal playlist, Remove albums anytime, #Album Requests: Users may request albums not in the system, Admin Dashboard to view or delete requests (Only admin accounts see the dashboard button)

Installation & Setup:

#Clone the Repository

git clone https://github.com/rashed914/it7405-project-rj.git

cd it7405-project-rj

#Create a Conda Environment

conda create -n web-it7405 python=3.10

conda activate web-it7405

#Install Dependencies

pip install -r requirements.txt

#Run Migrations

python manage.py makemigrations

python manage.py migrate

#Run Server

python manage.py runserver

#the app will run at:

http://127.0.0.1:8000/



-----------------

MongoDB Setup & Import Guide

#Install MongoDB + Compass

Download from:
https://www.mongodb.com/try/download/community


#Connect with Compass

Use this connection string:

mongodb://localhost:27017/


#Create Database

Name: music_db


#Import Collections

you will find the (db_seed) folder located in MusicAlbumsReview, and inside it you will find the json files:

   albums.json,
   reviews.json;
   playlists.json;
   album_requests.json

In Compass → Select each collection → IMPORT DATA → choose the json file.


#Run the App

Once data is imported:

python manage.py runserver

•the app will run at:

http://127.0.0.1:8000/
