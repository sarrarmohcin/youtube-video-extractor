import feedparser
from datetime import datetime

class YoutubeChannel:
    VIDEO_LIMIT = 1
    def __init__(self, channel_id):
        self.channel_id = channel_id
        self.videos = None
        
        
    def start(self):
        
        try:
            # start extracting source
            print(f"start extracting videos")
            
            # get videos data from RSS url
            videos = self.get_videos()
            
            # test if video not empty
            if len(videos) == 0:
                raise Exception(f"videos not Found")
            
            # limit number of videos
            self.videos = videos[:self.VIDEO_LIMIT]
        
        except Exception as e:
            print(f"Extracting videos from youtube channel failed : {str(e)}")
            return None
        
    
    # -----------------------------------------------------------------------------------------------------
    '''
    get videos from channel via RSS
    '''
    
    def get_videos(self):
        try:
            videos = []
            url = f"https://www.youtube.com/feeds/videos.xml?channel_id={self.channel_id}"
            rss = feedparser.parse(url)
            items = rss['entries']
            
            thumbnail = None
            try:
                thumbnail = item['media_thumbnail'][0]['url']
            except:
                thumbnail = None
            
            if items:
                for item in items:
                    videos.append({
                        'cahnnel_id' : self.channel_id,
                        'title' : item['title'],
                        'published' : item['published'],
                        'video_id' : item['yt_videoid'],
                        'video_url' : f"https://www.youtube.com/watch?v={item['yt_videoid']}",
                        'transcript' : None, 
                        'thumbnail' : thumbnail, 
                        'views': None, 
                        'likes': None, 
                        'comments': None, 
                        'video_length' : None, 
                    })

                    
            return videos
        except Exception as e:
            raise Exception(f"cant get videos from rss, {str(e)}")
        