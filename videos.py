
from bs4 import BeautifulSoup
import json
import re
import asyncio

from playwright.async_api import async_playwright

class YoutubeVideos:
    
    def __init__(self,video):
        self.video = video
        self.page_content = None
        self.transcript = None
    
    
    async def start(self):
        
        try:

            # start scraping
            print(f"start extracting video infos")
            await self.get_video()

            # get video data
            self.get_video_data()

        except Exception as e:
            print(f"Scaping videos from youtube channel failed : {str(e)}")
            return None
        
        
    
    '''
    get_video function : open the video url and extract data
    '''
    async def get_video(self):
        
        
        async with async_playwright() as p: 
                
            # create browser instance
            try:
                browser  = await p.firefox.launch(headless=True)
                context = await browser.new_context(
                    viewport={"width": 1475, "height": 1812}, locale='en-US',
                    )
            except Exception as e:
                raise Exception(f"Cant create browser : {str(e)}")

            try:
                
                page = await context.new_page()
                page.on("response", lambda response: self.get_videos_response(response=response))
                
                url = f"https://www.youtube.com/watch?v={self.video['video_id']}"
                await page.goto(url)
                await page.wait_for_load_state('domcontentloaded')
                await asyncio.sleep(4)
            except Exception as e:
                raise Exception(f"Cant access video URL : {str(e)}")
            
            # get transcript
            try:
                expand_description = page.locator("tp-yt-paper-button#expand[role='button']").first
                await expand_description.click()
                await asyncio.sleep(5)

                transcript_button = page.locator('ytd-video-description-transcript-section-renderer ytd-button-renderer button[aria-label]').first
                await transcript_button.click()
                await asyncio.sleep(5)
            except:
                print(f"No transcript for {self.video['video_id']}")
                
            # close playwright browser
            try:
                await context.close()
                await browser.close()
            except Exception as e:
                print(f"{self.source['source_name']} ({type}) : Cant close playwright browser")
                return None
            
            

    
    '''
    get_videos_response function : listen for response with "/watch"  "/get_transcript" url 
    and store response as text to data attribute
    '''
    async def get_videos_response(self, response):
        try:
            if(f"/watch?v={self.video['video_id']}" in response.url):
                self.page_content = await response.text()

            if("/get_transcript" in response.url):
                transcript_content = await response.text()
                transcript_content = json.loads(transcript_content)
                self.transcript = transcript_content
        except Exception as e:
            raise Exception(f"Cant get page content : {str(e)}")

    
    '''
    get_video_data function : when the broser is closed this function read data attribute
    and use BeautifulSoup to parse html content and extract video data
    '''
    def get_video_data(self):
        
        try:
            # test if page content exist
            if self.page_content is None:
                raise Exception(f"page content not found")
            
            
            # get content
            content = None
            try:
                content = self.get_video_transcript()
            except:
                content = None
            
                
            # get likes number
            likes = 0
            try:
                likes_text = self.find_attribute(r'"playerMicroformatRenderer"\s*:\s*\{[\s\S]*?"likeCount"\s*:\s*"(\d+)"', self.page_content, decode = False)
                
                if likes_text == None:
                    likes = 0
                else:
                    likes = self.string_to_int(likes_text)
            except:
                likes = 0
            
            
            # get comments number  
            comments = 0
            try:
                comments_text = self.find_attribute(r'"contextualInfo"\s*:\s*{[^}]*"runs"\s*:\s*\[\s*{[^}]*"text"\s*:\s*"([^"]+)"', self.page_content, decode = False)
                if comments_text == None:
                    comments = 0
                else:
                    comments = int(comments_text.replace(",", ""))
            except:
                comments = 0
            
            # get views
            views = 0
            try:
                views_text = self.find_attribute(r'"playerMicroformatRenderer"\s*:\s*\{[\s\S]*?"viewCount"\s*:\s*"(\d+)"', self.page_content, decode = False)
                
                if views_text == None:
                    views = 0
                else:
                    views = self.string_to_int(views_text)
            except:
                views = 0
                
                
            # get length
            length = 0
            try:
                length_text = self.find_attribute(r'"playerMicroformatRenderer"\s*:\s*\{[\s\S]*?"lengthSeconds"\s*:\s*"(\d+)"', self.page_content, decode = False)
                
                length = length_text
            except:
                length = 0
            
            
            self.video['views'] = views
            self.video['likes'] = likes
            self.video['comments'] = comments
            self.video['video_length'] = length
            self.video['transcript'] = content

            
        except Exception as e:
            raise Exception(f"Cant parse page transcript , {str(e)}")

    '''
    get_video_transcript function : parse transcript if exist
    '''
    def get_video_transcript(self):
        
        if self.transcript is None:
            print(f'transcript data not found')
            return None
            
        try:
            transcriptList = self.search_key_single_value(self.transcript,'initialSegments')
            texts = []
            for item in transcriptList:
                text = self.search_key_single_value(item,'text')
                texts.append(text)

            return ' '.join(texts)
        except:
            return None

    '''
    find_attribute function : get attribute inside page content via regex
    '''
    def find_attribute(self,pattern,content, decode = False):
        matches = re.findall(pattern, content, re.DOTALL)
        if matches:
            find = matches[0]
            if decode == True:
                find = find.encode().decode('unicode_escape')
            return find
        else:
            return None
    
    '''
    string_to_int function : transform K,M .. to int
    '''
    def string_to_int(self,s):
        s = s.strip().upper().replace(',', '.')
        multiplier = 1

        if s.endswith('K'):
            multiplier = 1_000
            s = s[:-1]
        elif s.endswith('M'):
            multiplier = 1_000_000
            s = s[:-1]
        elif s.endswith('B'):
            multiplier = 1_000_000_000
            s = s[:-1]

        try:
            return int(float(s) * multiplier)
        except ValueError:
            return None  # or raise an error
    
    
    def search_key_single_value(self, data, search_key):
        def search(data):
            if isinstance(data, dict):
                for key, value in data.items():
                    if key == search_key:
                        return value
                    elif isinstance(value, (dict, list)):
                        result = search(value)
                        if result is not None:
                            return result
            elif isinstance(data, list):
                for item in data:
                    result = search(item)
                    if result is not None:
                        return result
            return None

        return search(data)