import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from pom.searchpage_nav import SearchNav
import time
from selenium.webdriver.common.by import By
from urllib.parse import urlparse


@pytest.mark.usefixtures('setup')
class TestSearch:

    # def test_language(self):
    #     names = SearchNav(self.driver)
    #     dropdown = self.driver.find_element(By.XPATH,
    #                                         '//details[@id="codesearch_select_language"]/summary[@role="button"]')
    #     nav_links = '//details[@id="codesearch_select_language"]/div/details-menu[@class="dropdown-menu dropdown-menu-se"]/a'
    #     languages = names.get_dropdown_names(dropdown, nav_links)
    #     if 'Any' in languages:
    #         languages.remove('Any')
    #     wait = WebDriverWait(self.driver, 20)
    #
    #     urls = {
    #         'Python': 'l=Python',
    #         'JavaScript': 'l=JavaScript',
    #         'Java': 'l=Java',
    #         'HTML': 'l=HTML',
    #         'C++': 'l=C%2B%2B',
    #         'Jupyter Notebook': 'l=Jupyter+Notebook',
    #         'C': 'l=C',
    #         'C#': 'l=C%23',
    #         'PHP': 'l=PHP',
    #         'CSS': 'l=CSS',
    #         'Go': 'l=Go',
    #         'Ruby': 'l=Ruby',
    #         'Scala': 'l=Scala',
    #         'TypeScript': 'l=TypeScript'
    #     }
    #     url = self.driver.current_url
    #     q = urlparse(url).query.partition('&')[0]
    #
    #     for el in languages:
    #         names.get_click_language(el)
    #         wait.until(ec.url_changes(url))
    #         assert urls[el] in self.driver.current_url
    #         url = f'https://github.com/search?{urls[el]}&{q}&type=Repositories'
    #         dropdown = self.driver.find_element(By.XPATH,
    #                                             '//details[@id="codesearch_select_language"]/summary[@role="button"]')
    #         time.sleep(7)
    #         dropdown.click()
    #
    # def test_sort(self):  # Not working with other requests
    #     sorts = SearchNav(self.driver)
    #     wait = WebDriverWait(self.driver, 20)
    #     url = 'https://github.com/search?q=code&ref=simplesearch'
    #     urls = {
    #         'Most stars': 'https://github.com/search?o=desc&q=code&s=stars&type=Repositories',
    #         'Fewest stars': 'https://github.com/search?o=asc&q=code&s=stars&type=Repositories',
    #         'Most forks': 'https://github.com/search?o=desc&q=code&s=forks&type=Repositories',
    #         'Fewest forks': 'https://github.com/search?o=asc&q=code&s=forks&type=Repositories',
    #         'Recently updated': 'https://github.com/search?o=desc&q=code&s=updated&type=Repositories',
    #         'Least recently updated': 'https://github.com/search?o=asc&q=code&s=updated&type=Repositories'
    #     }
    #
    #     dropdown = self.driver.find_element(By.XPATH,
    #                                         '//details[@id="codesearch_sort_repos"]/summary[@role="button"]')
    #
    #     for el in urls.keys():
    #         dropdown.click()
    #         time.sleep(3)
    #         sorts.get_click_sort(el)
    #         wait.until(ec.url_changes(url))
    #         assert self.driver.current_url == urls[el]
    #         url = urls[el]
    #         dropdown = self.driver.find_element(By.XPATH,
    #                                             '//details[@id="codesearch_sort_repos"]/summary[@role="button"]')
    #         time.sleep(7)


    def test_sort_names(self):
        sorts = SearchNav(self.driver)
        dropdown = self.driver.find_element(By.XPATH,
                                            '//details[@id="codesearch_sort_repos"]/summary[@role="button"]')
        nav_links = '//details[@id="codesearch_sort_repos"]/div/details-menu[@class="dropdown-menu dropdown-menu-se"]/a'
        sorts_names = sorts.get_dropdown_names(dropdown, nav_links)
        correct_sorts_names = ['Best match', 'Most stars', 'Fewest stars', 'Most forks', 'Fewest forks', 'Recently updated', 'Least recently updated']
        assert sorts_names == correct_sorts_names
