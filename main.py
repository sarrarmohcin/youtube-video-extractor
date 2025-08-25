from channel import YoutubeChannel 
from videos import YoutubeVideos
import asyncio
data = []

channelExtractor = YoutubeChannel(channel_id = "CHANNEL_ID", limit = 10)
channelExtractor.start()
videos = channelExtractor.videos


if videos is not None:
    for video in videos:
        videoExtractor = YoutubeVideos(video)
        asyncio.run(videoExtractor.start())
        data.append(videoExtractor.video)
        
        
        
print(data)
