import time

class BingImageScrapper:
    def __init__(self, searchStr, imageCount):
        self.searchStr = searchStr
        self.imageCount = imageCount
        self.__SLEEP_TIME = 0.5
        self.__BASE_URL = 'https://www.bing.com'

    def getSearchUrl(self):
        """
        :return: bing search web url
        """
        try:
            return f"{self.__BASE_URL}/images/search?view=detailV2&q={self.searchStr}s&form=HDRSC2&first=1&tsc=ImageBasicHover"
        except Exception as e:
            print(str(e))

    def fetch_image_urls(self, wd):
        """
        Fetch images links from bing site
        :param wd: Selenium Web Driver
        :return: set of image links
        """
        wd.get(self.getSearchUrl())

        image_urls = set()
        image_count = 0

        time.sleep(5)
        while len(image_urls) < self.imageCount:
            self.__SLEEP_TIME = 1
            image_urls.add(wd.find_element_by_css_selector("img").get_attribute('src'))
            wd.find_element_by_id('navr').click()
        return image_urls