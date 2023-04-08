import argparse
import logging

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


logger = logging.getLogger('examples.artist_recommendations')
logging.basicConfig(level='INFO')

auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=auth_manager)


def get_args():
    parser = argparse.ArgumentParser(description='Recommendations for the '
                                     'given artist')
    parser.add_argument('-a', '--artist', required=True, help='Name of Artist')
    return parser.parse_args()


def get_artist(name):
    results = sp.search(q=f'artist:{name}', type='artist')
    items = results['artists']['items']
    return items[0] if len(items) > 0 else None


def show_recommendations_for_artist(artist):
    results = sp.recommendations(seed_artists=[artist['id']])
    for track in results['tracks']:
        logger.info('Recommendation: %s - %s', track['name'],
                    track['artists'][0]['name'])


def main():
    args = get_args()
    artist = get_artist(args.artist)
    if artist:
        show_recommendations_for_artist(artist)
    else:
        logger.error("Can't find that artist", args.artist)


if __name__ == '__main__':
    main()
