import time

class GoogleImageScrapper:
    def __init__(self, searchStr, imageCount):
        self.searchStr = searchStr
        self.imageCount = imageCount
        self.__SLEEP_TIME = 2
        self.__BASE_URL = 'https://www.google.com'


    def getSearchUrl(self):
        try:
            return f"{self.__BASE_URL}/search?safe=off&site=&tbm=isch&source=hp&q={self.searchStr}&oq={self.searchStr}&gs_l=img"
        except Exception as e:
            print(str(e))

    def __scrollWindow(self, wd):
        wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(self.__SLEEP_TIME)

    def fetch_image_urls(self, wd):
        wd.get(self.getSearchUrl())

        image_urls = set()
        image_count = 0
        results_start = 0

        while image_count < self.imageCount:
            self.__scrollWindow(wd)

            # get all image thumbnail results
            thumbnail_results = wd.find_elements_by_css_selector("img.Q4LuWd")
            number_results = len(thumbnail_results)

            print(f"Found: {number_results} search results. Extracting links from {results_start}:{number_results}")

            for img in thumbnail_results[results_start:number_results]:
                # try to click every thumbnail such that we can get the real image behind it
                try:
                    img.click()
                    time.sleep(self.__SLEEP_TIME)
                except Exception:
                    continue

                # extract image urls
                actual_images = wd.find_elements_by_css_selector('img.n3VNCb')
                for actual_image in actual_images:
                    if actual_image.get_attribute('src') and 'http' in actual_image.get_attribute('src'):
                        image_urls.add(actual_image.get_attribute('src'))

                image_count = len(image_urls)

                if len(image_urls) >= self.imageCount:
                    print(f"Found: {len(image_urls)} image links, done!")
                    break
            else:
                print("Found:", len(image_urls), "image links, looking for more ...")
                time.sleep(30)
                return
                load_more_button = wd.find_element_by_css_selector(".mye4qd")
                if load_more_button:
                    wd.execute_script("document.querySelector('.mye4qd').click();")

            # move the result startpoint further down
            results_start = len(thumbnail_results)

        return image_urls