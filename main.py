from channel import YoutubeChannel 
from videos import YoutubeVideos
import asyncio
data = []

channel_id = "UCvyivffb2WwNKonKiLwVAEQ"
channelExtractor = YoutubeChannel(channel_id)
channelExtractor.start()
videos = channelExtractor.videos


if videos is not None:
    for video in videos:
        videoExtractor = YoutubeVideos(video)
        asyncio.run(videoExtractor.start())
        data.append(videoExtractor.video)
        
        
        
print(data)