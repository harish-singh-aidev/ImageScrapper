from image_scrapper.web_request_handler import WebRequestHandler
from image_scrapper.directory_handler import DirectoryHandler
from search_engines.google_image_scrapper import GoogleImageScrapper
from search_engines.bing_image_scrapper import BingImageScrapper
from selenium import webdriver

import os


class ImageScrapper:
    def __init__(self, searchStr, imageCount, searchEngine):
        self.searchStr = searchStr
        self.imageCount = imageCount
        self.__DRIVER_PATH = './chromedriver.exe'
        self.dirHandlr = DirectoryHandler(searchStr)
        self.searchEngine = searchEngine
        self.__configre()

    def __configre(self):
        try:
            if self.searchEngine=='google':
                self.dirHandlr.setBaseDir('./GoogleImages')
                self.scrapper = GoogleImageScrapper(self.searchStr, self.imageCount)
            elif self.searchEngine=='bing':
                self.dirHandlr.setBaseDir('./BingImages')
                self.scrapper = BingImageScrapper(self.searchStr, self.imageCount)
            else:
                raise Exception(f"{self.searchEngine} search engined not configured!")

        except Exception as e:
            print(str(e))


    def scrapImage(self):
        try:
            imageUrls = self.__getImageUrls()

            if not self.dirHandlr.isPathExist():
                self.dirHandlr.createPath()

            counter = 0
            for elem in imageUrls:
                self.__persist_image(elem, counter)
                counter += 1
            return f"{len(imageUrls)} images of {self.searchStr} are saved on {self.dirHandlr.getPath()} location."
        except Exception as e:
            print(str(e))

    def __getImageUrls(self):
        try:
            return self.seleniumGetRequest()
        except Exception as e:
            print(str(e))



    def __persist_image(self, url: str, counter):
        try:
            image_content = WebRequestHandler(url).getRequest().content
        except Exception as e:
            print(f"ERROR - Could not download {url} - {e}")

        try:
            path = self.dirHandlr.getPath()
            f = open(os.path.join(path, 'jpg' + "_" + str(counter) + ".jpg"), 'wb')
            f.write(image_content)
            f.close()
            print(f"SUCCESS - saved {url} - as {self.dirHandlr.getPath()}")
        except Exception as e:
            print(f"ERROR - Could not save {url} - {e}")

    def seleniumGetRequest(self):
        try:
            with webdriver.Chrome(self.__DRIVER_PATH) as wd:
                return self.scrapper.fetch_image_urls(wd)
        except Exception as e:
            print(str(e))