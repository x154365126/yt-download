from yt_download.pipeline.steps.get_video_list import GetVideoList
from yt_download.pipeline.steps.step import StepException
from yt_download.pipeline.pipeline import Pipeline

playlistLink = "https://www.youtube.com/watch?v=DOzpsXZS-j0&list=PLB8Nt5W7hnKA_pG2qljWbgVmJPobrLTm4&ab_channel=MoriCalliopeCh.hololive-EN"


def main():
    inputs = {
        'playlist_link': playlistLink
    }

    steps = [
        GetVideoList(),
    ]

    p = Pipeline(steps)
    p.run(inputs)


if __name__ == '__main__':
    main()
