from abc import ABC, abstractmethod


class ThirdPartyYoutubeLib(ABC):
    @abstractmethod
    def list_videos(self):
        pass

    @abstractmethod
    def get_video_info(self, id):
        pass

    @abstractmethod
    def download_video(self, id):
        pass


class ThirdPartyYoutubeClass(ThirdPartyYoutubeLib):
    def list_videos(self):
        print("ThirdPartyYoutubeClass: list_videos")
        return []

    def get_video_info(self, id):
        print("ThirdPartyYoutubeClass: get_video_info")
        return "video info"

    def download_video(self, id):
        print("ThirdPartyYoutubeClass: download_video")
        return "video"


class CachedYoutubeClass(ThirdPartyYoutubeLib):
    def __init__(self, service):
        self.service = service
        self.list_cache = None
        self.video_cache = {}

    def list_videos(self):
        if not self.list_cache:
            self.list_cache = self.service.list_videos()
        else:
            print("CachedYoutubeClass: list_videos")
        return self.list_cache

    def get_video_info(self, id):
        if not self.video_cache.get(id):
            self.video_cache[id] = self.service.get_video_info(id)
        else:
            print("CachedYoutubeClass: get_video_info")
        return self.video_cache[id]

    def download_video(self, id):
        if not self.video_cache.get(id):
            self.video_cache[id] = self.service.download_video(id)
        else:
            print("CachedYoutubeClass: download_video")
        return self.video_cache[id]


class YoutubeManager:
    def __init__(self, service):
        self.service = service

    def render_video_page(self, id):
        print("YoutubeManager: render_video_page")
        return self.service.get_video_info(id)


if __name__ == "__main__":
    service = CachedYoutubeClass(ThirdPartyYoutubeClass())
    manager = YoutubeManager(service)
    manager.render_video_page("video_id")
