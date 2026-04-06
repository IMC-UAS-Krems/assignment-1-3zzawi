"""
platform.py
-----------
Implement the central StreamingPlatform class that orchestrates all domain entities
and provides query methods for analytics.

Classes to implement:
  - StreamingPlatform
"""
from datetime import datetime
from src.streaming.tracks import Song

class StreamingPlatform:
    def __init__(self):
        self.tracks = []
        self.users = []
        self.artists = []
        self.albums = []
        self.playlists = []
        self.sessions = []

    def add_track(self, track): self.tracks.append(track)
    def add_user(self, user): self.users.append(user)
    def add_artist(self, artist): self.artists.append(artist)
    def add_album(self, album): self.albums.append(album)
    def add_playlist(self, playlist): self.playlists.append(playlist)
    def record_session(self, session): self.sessions.append(session)

    def total_listening_time_minutes(self, start, end):
        total = 0
        for s in self.sessions:
            if start <= s.timestamp <= end:
                total += s.duration
        return total / 60.0

    def avg_unique_tracks_per_premium_user(self, days=30): return 0.0
    def track_with_most_distinct_listeners(self): return None
    def avg_session_duration_by_user_type(self): return []
    def top_artists_by_listening_time(self, n=5): return []
    def user_top_genre(self, user_id): return None
    def collaborative_playlists_with_many_artists(self, threshold=3): return []
    def avg_tracks_per_playlist_type(self): return {"Playlist": 0.0, "CollaborativePlaylist": 0.0}
    def users_who_completed_albums(self): return []
