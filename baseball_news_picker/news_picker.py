from urllib.request import urlopen

from bs4 import BeautifulSoup


class NewsPicker:

    def get_page(self, url):
        return BeautifulSoup(urlopen(url), "html.parser")
