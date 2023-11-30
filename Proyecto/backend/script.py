import os
import json
import codecs

archivo = open('spotify_songs.csv', encoding='utf-8')
i = 0
Ldatos = []

with codecs.open('spotify_songs.csv', 'r', encoding='utf-8', errors='replace') as archivo:
    for linea in archivo:
        if i > 0:
            datos = linea.split(",")
            objeto = {"track_id":datos[0],
                    "track_name":datos[1],
                    "track_artist":datos[2],
                    "track_popularity":datos[3],
                    "track_album_id":datos[4],
                    "track_album_name":datos[5],
                    "track_album_release_date":datos[6],
                    "playlist_name":datos[7],
                    "playlist_id":datos[8],
                    "playlist_genre":datos[9],
                    "playlist_subgenre":datos[10],
                    "danceability":datos[11],
                    "energy":datos[12],
                    "key":datos[13],
                    "loudness":datos[14],
                    "mode":datos[15],
                    "speechiness":datos[16],
                    "acousticness":datos[17],
                    "instrumentalness":datos[18],
                    "liveness":datos[19],
                    "valence":datos[20],
                    "tempo":datos[21],
                    "duration_ms":datos[22]
                    }
            Ldatos.append(objeto)
            print(objeto)
        i+=1

SalidaJson = json.dumps(Ldatos)
ArchivoJSON = open("data.json","w")
ArchivoJSON.write(SalidaJson)
ArchivoJSON.close
