# shows acoustic features for tracks for the given artist

from spotipy.oauth2 import SpotifyClientCredentials
import json
import spotipy
import time
import sys


auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=auth_manager)
sp.trace = True

if len(sys.argv) > 1:
    tids = sys.argv[1:]
    print(tids)

    start = time.time()
    features = sp.audio_features(tids)
    delta = time.time() - start
    print(json.dumps(features, indent=4))
    print(f"features retrieved in {delta:.2f} seconds")
