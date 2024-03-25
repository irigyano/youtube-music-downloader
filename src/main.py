from Youtube import YtVideo,YtPlaylist 
from Prompt import Prompt

if __name__ == "__main__":
    prompt = Prompt()
    answer,url = prompt.prompt()

    if answer == 'Video':
        yt = YtVideo(url)
        yt.download_music()
    elif answer == 'Playlist':
        yt = YtPlaylist(url)
        yt.download_musics()
