
from db.run_sql import run_sql

from models.artist import Artist
from models.album import Album
import artist_repository

def save(artist):
    sql = "INSERT INTO artist (name) VALUES (%s) RETURNING *"
    values = [artist.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    artist.id = id
    return results