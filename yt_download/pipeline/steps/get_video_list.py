from yt_download.pipeline.steps.step import Step

from pytube import Playlist


class GetVideoList(Step):
    def process(self, data, inputs, utils):
        channel_id = inputs['channel_id']
        playlist = Playlist(inputs['playlist_link'])

        # 如果video_list存在, 印出訊息
        if utils.video_list_file_exists(channel_id):
            print('Found existing video list for channel id')
            return self.read_file(utils.get_video_list_filepath(channel_id))

        print("Total video to download: ", len(playlist))
        print("\n\n youtube video Links \n")

        print(playlist)
        # 將影片清單寫入.txt檔
        self.write_to_file(playlist, utils.get_video_list_filepath(channel_id))
        return playlist

    def write_to_file(self, playlist, filepath):
        with open(filepath, 'w') as f:
            for url in playlist:
                f.write(url + '\n')

    def read_file(self, filepath):
        playlist = []
        with open(filepath, 'r') as f:
            for url in f:
                playlist.append(url.strip())
        return playlist
