from image_scrapper.image_scrapper import ImageScrapper

class Scrapper:
    def __init__(self, searchStr, imageCount, searchEngine='google'):
        self.searchStr = searchStr
        self.imageCount = imageCount
        self.searchEngine = searchEngine

    def imageScrap(self):
        try:
            return ImageScrapper(self.searchStr,self.imageCount, self.searchEngine).scrapImage()
        except Exception as e:
            print(str(e))