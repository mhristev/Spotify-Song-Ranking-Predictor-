import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
from API.genres import categorize_genre, genre_classification
import time

cid = 'f4602a7273ef46bd81f5e718a801ee6a'
secret = '13f555c14d4a414db85af16647e1a785'
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def get_audio_analysis(df):
    for sp_id in df['spotify_id']:
        audio_analysis = spotify.audio_analysis(sp_id)['track']
        time.sleep(1)
        df.loc[df['spotify_id'] == sp_id, 'num_samples'] = audio_analysis['num_samples']
        df.loc[df['spotify_id'] == sp_id, 'end_of_fade_in'] = audio_analysis['end_of_fade_in']
        df.loc[df['spotify_id'] == sp_id, 'start_of_fade_out'] = audio_analysis['start_of_fade_out']

def create_audio_analysis_columns(df):
    df['num_samples'] = 0
    df['end_of_fade_in'] = 0
    df['start_of_fade_out'] = 0

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
    
def create_genre_columns(df):
    for category in genre_classification.keys():
        df[category] = 0
    
def classify_genres_of_track(df):
    print("Classifying genres of tracks...")
    for sp_id in df['spotify_id']:
        genres = get_genres(sp_id)
        time.sleep(1)
        for genre in genres:
            category = categorize_genre(genre)
            df.loc[df['spotify_id'] == sp_id, category] = 1


def main():
    df = pd.read_csv('../raw_data/universal_top_spotify_songs_2.csv')
    
    prepare_dataset(df)
    create_genre_columns(df)
    classify_genres_of_track(df)
    create_audio_analysis_columns(df)
    get_audio_analysis(df)

    df.to_csv('../raw_data/expanded_dataset.csv', index=False)

if __name__ == "__main__":
    main()