from yt_download.pipeline.steps.get_video_list import GetVideoList
from yt_download.pipeline.steps.step import StepException
from yt_download.pipeline.steps.prefilght import Preflight
from yt_download.pipeline.steps.postflight import Postflight

from yt_download.pipeline.pipeline import Pipeline
from yt_download.utils import Utils

playlistLink = "https://www.youtube.com/watch?v=DOzpsXZS-j0&list=PLB8Nt5W7hnKA_pG2qljWbgVmJPobrLTm4&ab_channel=MoriCalliopeCh.hololive-EN"
# CHANNEL_ID = playlistLink.split('channel=')[-1]


def main():
    inputs = {
        'playlist_link': playlistLink,
    }

    steps = [
        Preflight(),
        GetVideoList(),
        Postflight(),
    ]

    utils = Utils()
    p = Pipeline(steps)
    p.run(inputs, utils)


if __name__ == '__main__':
    main()
