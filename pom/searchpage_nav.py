from typing import List

from selenium.webdriver.common.by import By

from base.seleniumbase import SeleniumBase


class SearchNav(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.__nav_links = '//details[@id="codesearch_select_language"]/div/details-menu[@class="dropdown-menu dropdown-menu-se"]/a'

    def get_nav_links(self):
        dropdown = self.driver.find_element(By.XPATH,
                                            '//details[@id="codesearch_select_language"]/summary[@role="button"]')
        dropdown.click()
        return self.are_present('xpath', self.__nav_links, 'Languages')

    def get_language_names(self):
        nav_links = self.get_nav_links()
        nav_links_text = [link.text for link in nav_links]
        names = ','.join(nav_links_text).split(',')
        names.remove('Any')
        return names

    def get_click_language(self, find_ln):
        click_links = {
            'Any': '//details[@id="codesearch_select_language"]//a[text()="Any"]',
            'Python': '//details[@id="codesearch_select_language"]//a[text()="Python"]',
            'JavaScript': '//details[@id="codesearch_select_language"]//a[text()="JavaScript"]',
            'Java': '//details[@id="codesearch_select_language"]//a[text()="Java"]',
            'HTML': '//details[@id="codesearch_select_language"]//a[text()="HTML"]',
            'C++': '//details[@id="codesearch_select_language"]//a[text()="C++"]',
            'Jupyter Notebook': '//details[@id="codesearch_select_language"]//a[text()="Jupyter Notebook"]',
            'C': '//details[@id="codesearch_select_language"]//a[text()="C"]',
            'C#': '//details[@id="codesearch_select_language"]//a[text()="C#"]',
            'PHP': '//details[@id="codesearch_select_language"]//a[text()="PHP"]',
            'CSS': '//details[@id="codesearch_select_language"]//a[text()="CSS"]',
            'Go': '//details[@id="codesearch_select_language"]//a[text()="Go"]',
            'Ruby': '//details[@id="codesearch_select_language"]//a[text()="Ruby"]',
            'Scala': '//details[@id="codesearch_select_language"]//a[text()="Scala"]',
            'TypeScript': '//details[@id="codesearch_select_language"]//a[text()="TypeScript"]'
        }
        clickable = self.driver.find_element(By.XPATH, click_links[find_ln])
        return clickable.click()

    def get_click_sort(self, find_sort):
        click_links = {
            'Best match': '/html/body/div[1]/div[4]/main/div/div[3]/div/div[1]/details/details-menu/div[2]/a[1]/span',
            'Most stars': '/html/body/div[1]/div[4]/main/div/div[3]/div/div[1]/details/details-menu/div[2]/a[2]/span',
            'Fewest stars': '/html/body/div[1]/div[4]/main/div/div[3]/div/div[1]/details/details-menu/div[2]/a[3]/span',
            'Most forks': '/html/body/div[1]/div[4]/main/div/div[3]/div/div[1]/details/details-menu/div[2]/a[4]/span',
            'Fewest forks': '/html/body/div[1]/div[4]/main/div/div[3]/div/div[1]/details/details-menu/div[2]/a[5]/span',
            'Recently updated': '/html/body/div[1]/div[4]/main/div/div[3]/div/div[1]/details/details-menu/div[2]/a[6]/span',
            'Least recently updated': '/html/body/div[1]/div[4]/main/div/div[3]/div/div[1]/details/details-menu/div[2]/a[7]/span'
        }
        clickable = self.driver.find_element(By.XPATH, click_links[find_sort])
        return clickable.click()