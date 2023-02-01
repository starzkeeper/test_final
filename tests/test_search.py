import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from pom.searchpage_nav import SearchNav
import time
from selenium.webdriver.common.by import By
from urllib.parse import urlparse


@pytest.mark.usefixtures('setup')
class TestSearch:

    def test_language(self):
        names = SearchNav(self.driver)
        wait = WebDriverWait(self.driver, 20)
        urls = {
            'Python': 'l=Python',
            'JavaScript': 'l=JavaScript',
            'Java': 'l=Java',
            'HTML': 'l=HTML',
            'C++': 'l=C%2B%2B',
            'Jupyter Notebook': 'l=Jupyter+Notebook',
            'C': 'l=C',
            'C#': 'l=C%23',
            'PHP': 'l=PHP',
            'CSS': 'l=CSS'
        }
        url = self.driver.current_url
        q = urlparse(url).query.partition('&')[0]
        for el in urls.keys():
            names.get_click_language(el)
            wait.until(ec.url_changes(url))
            assert urls[el] in self.driver.current_url
            url = f'https://github.com/search?{urls[el]}&{q}&type=Repositories'
            time.sleep(7)

    def test_sort(self):
        sorts = SearchNav(self.driver)
        wait = WebDriverWait(self.driver, 20)
        url = 'https://github.com/search?q=code&ref=simplesearch'
        urls = {
            'Best match': 'https://github.com/search?o=desc&q=code&s=&type=Repositories',
            'Most stars': 'https://github.com/search?o=desc&q=code&s=stars&type=Repositories',
            'Fewest stars': 'https://github.com/search?o=asc&q=code&s=stars&type=Repositories',
            'Most forks': 'https://github.com/search?o=desc&q=code&s=forks&type=Repositories',
            'Fewest forks': 'https://github.com/search?o=asc&q=code&s=forks&type=Repositories',
            'Recently updated': 'https://github.com/search?o=desc&q=code&s=updated&type=Repositories',
            'Least recently updated': 'https://github.com/search?o=asc&q=code&s=updated&type=Repositories'
        }

        dropdown = self.driver.find_element(By.XPATH,
                                            '/html/body/div[1]/div[4]/main/div/div[3]/div/div[1]/details/summary/i')

        for el in urls.keys():
            dropdown.click()
            time.sleep(3)
            sorts.get_click_sort(el)
            wait.until(ec.url_changes(url))
            assert self.driver.current_url == urls[el]
            url = urls[el]
            dropdown = self.driver.find_element(By.XPATH,
                                                '/html/body/div[1]/div[4]/main/div/div[3]/div/div[1]/details/summary/i')
            time.sleep(7)
