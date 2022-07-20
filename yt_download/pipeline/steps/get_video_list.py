from yt_download.pipeline.steps.step import Step

from pytube import Playlist


class GetVideoList(Step):
    def process(self, data, inputs):
        playlist = Playlist(inputs['playlist_link'])

        print("Total video to download: ", len(playlist.video_urls))
        print("\n\n Links of the youtube videos\n")

        print(playlist)
        return playlist
