import time

class BingImageScrapper:
    def __init__(self, searchStr, imageCount):
        self.searchStr = searchStr
        self.imageCount = imageCount
        self.__SLEEP_TIME = 0.5
        self.__BASE_URL = 'https://www.bing.com'

    def getSearchUrl(self):
        try:
            return f"{self.__BASE_URL}/images/search?view=detailV2&q={self.searchStr}s&form=HDRSC2&first=1&tsc=ImageBasicHover"
        except Exception as e:
            print(str(e))

    def fetch_image_urls(self, wd):
        wd.get(self.getSearchUrl())

        image_urls = set()
        image_count = 0

        time.sleep(2)
        while len(image_urls) < self.imageCount:
            self.__SLEEP_TIME = 0.5
            image_urls.add(wd.find_element_by_css_selector("img").get_attribute('src'))
            wd.find_element_by_id('navr').click()
        return image_urls