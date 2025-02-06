from selenium import webdriver


class BrowserFactory:

    @staticmethod
    def get_driver(options):
        return webdriver.Chrome(options=options)
