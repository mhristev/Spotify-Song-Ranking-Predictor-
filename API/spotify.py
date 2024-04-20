import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
from genres import categorize_genre, genre_classification
import time
from dotenv import load_dotenv
import os

load_dotenv()

cid = os.getenv('CID')
secret = os.getenv('SECRET')
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def get_audio_analysis(df):
     count = 0
     import requests
     for sp_id in df['spotify_id']:
        while True:
            try:
                audio_analysis = spotify.audio_analysis(sp_id)['track']
                break
            except requests.exceptions.ReadTimeout:
                print("Timeout occurred for id: {}. Retrying...".format(sp_id))
                time.sleep(5)
        print(f'{count} tracks')
        count += 1
        df.loc[df['spotify_id'] == sp_id, 'num_samples'] = audio_analysis['num_samples']
        df.loc[df['spotify_id'] == sp_id, 'end_of_fade_in'] = audio_analysis['end_of_fade_in']
        df.loc[df['spotify_id'] == sp_id, 'start_of_fade_out'] = audio_analysis['start_of_fade_out']
        time.sleep(1)
    
     return df

def create_audio_analysis_columns(df):
    df['num_samples'] = float(0)
    df['end_of_fade_in'] = float(0)
    df['start_of_fade_out'] = float(0)

    return df

def get_genres(track_id):
    genres = set()
    track_info = spotify.track(track_id, market=None)

    for artist in track_info['artists']:
        artist_info = spotify.artist(artist['id'])
        genres.update(artist_info['genres'])
        
    return genres

def prepare_dataset(df):
    df = df[df['country'].isna()]
    idx = df.groupby("spotify_id")['daily_rank'].idxmin()
    df = df.loc[idx]
    print(f'Shape of the dataset => {df.shape}')
    return df
    
def create_genre_columns(df):
    for category in genre_classification.keys():
        df[category] = 0
    return df
    
def classify_genres_of_track(df):
    counter = 0
    my_set = set()
    
    print(df.shape[0])
    for sp_id in df['spotify_id']:
        print(f'{counter} tracks')
        genres = get_genres(sp_id)
        time.sleep(0.5)
        counter += 1
        for genre in genres:
            category = categorize_genre(genre)
            if category == 'Miscellaneous/Unique':
                my_set.add(genre)
            else:
                df.loc[df['spotify_id'] == sp_id, category] = 1
    print(my_set)
    return df


def main():
    df = pd.read_csv('../raw_data/expanded_dataset.csv')
    my_set = set()
    # df = prepare_dataset(df)
    # df = create_genre_columns(df)
    # df = classify_genres_of_track(df)
    df = create_audio_analysis_columns(df)
    df = get_audio_analysis(df)

    df.to_csv('../raw_data/expanded_dataset2.csv', index=False)

if __name__ == "__main__":
    main()