from albums.mongo import db

sample_data = [
    {"title": "Thriller", "artist": "Michael Jackson"},
    {"title": "Back in Black", "artist": "AC/DC"},
]

db.albums.insert_many(sample_data)
print("Done!")
