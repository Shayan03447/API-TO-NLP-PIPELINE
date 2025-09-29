import pandas as pd
import requests
import time

genre_url="https://api.themoviedb.org/3/genre/movie/list?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
genre_data=requests.get(genre_url).json()['genres']

# Dictionary for genres 
genre_map={}
for g in genre_data:
    genre_map[g["id"]]=g["name"]

movies=[]
for i in range (1, 429):
    movies_url="https://api.themoviedb.org/3/movie/top_rated?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US&page={}".format(i)
    reponse=requests.get(movies_url).json()
    if "results" not in reponse:
        break
    
    for m in reponse["results"]:
        title=m.get("title","")
        overview=m.get("overview","")
        genre_ids=m.get("genre_ids",[])

        # Genre Conversion
        genres=[]
        for g in genre_ids:
            if g in genre_map:
                genres.append(genre_map[g])
        genres=", ".join(genres)
        movies.append({
            "title":title,
            "overview":overview,
            "genres":genres
        })

# DataFrame
df=pd.DataFrame(movies)
print(df.head(2))
print(f"Total movies collected: {len(df)}")
df.to_csv("movies.csv", index=False, encoding="utf-8")
        



