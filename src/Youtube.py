from pytube import YouTube, Playlist
import os


class YtVideo:
    def __init__(self, url):
        self.yt = YouTube(url)

    def download_music(self):
        stream = self.yt.streams.get_audio_only()
        out_file = stream.download(output_path="./downloads")
        base, ext = os.path.splitext(out_file)
        new_filename = base + '.mp3'

        try:
            os.rename(out_file, new_filename)
        except FileExistsError:
            os.remove(new_filename)
            os.rename(out_file, new_filename)


class YtPlaylist:
    def __init__(self, url):
        self.yt = Playlist(url)

    def download_music(self, video: YouTube):
        stream = video.streams.get_audio_only()
        out_file = stream.download(output_path="./downloads")
        base, ext = os.path.splitext(out_file)
        new_filename = base + '.mp3'

        try:
            os.rename(out_file, new_filename)
        except FileExistsError:
            os.remove(new_filename)
            os.rename(out_file, new_filename)

        print(f'Downloaded: {stream.title}')

    def download_musics(self):
        for yt in self.yt.videos:
            self.download_music(yt)
