from channel import YoutubeChannel 
from videos import YoutubeVideos
import asyncio

def positive_int(value):
    ivalue = int(value)
    if ivalue <= 0:
        raise argparse.ArgumentTypeError("%s is not a positive integer" % value)
    return ivalue

parser = argparse.ArgumentParser(description='Process some inputs.')

parser.add_argument(
    "-c", "--channel",
    type=str,
    required=True,
    help="Youtube channel ID (required)"
)

# Optional limit argument with -lm and --limit
parser.add_argument(
    "-l", "--limit",
    type=positive_int,
    default=10,
    help="Limit of videos (default: 10)"
)
args = parser.parse_args()

data = []

channelExtractor = YoutubeChannel(channel_id = args.channel, limit = args.limit)
channelExtractor.start()
videos = channelExtractor.videos


if videos is not None:
    for video in videos:
        videoExtractor = YoutubeVideos(video)
        asyncio.run(videoExtractor.start())
        data.append(videoExtractor.video)
        
        
        
print(data)
