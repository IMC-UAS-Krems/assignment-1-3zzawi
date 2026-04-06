"""
tracks.py
---------
Implement the class hierarchy for all playable content on the platform.

Classes to implement:
  - Track (abstract base class)
    - Song
      - SingleRelease
      - AlbumTrack
    - Podcast
      - InterviewEpisode
      - NarrativeEpisode
    - AudiobookTrack
"""
class Track:
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

class Song(Track):
    def __init__(self, title, duration, artist, genre=None):
        super().__init__(title, duration)
        self.artist = artist
        self.genre = genre

class Podcast(Track): pass
class AudiobookTrack(Track): pass
