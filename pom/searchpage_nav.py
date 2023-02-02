from typing import List

from selenium.webdriver.common.by import By

from base.seleniumbase import SeleniumBase


class SearchNav(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_nav_links(self, dropdown, nav_links):
        dropdown.click()
        return self.are_present('xpath', nav_links, 'Languages')

    def get_dropdown_names(self, dropdown, nav_links):
        nav_links = self.get_nav_links(dropdown, nav_links)
        nav_links_text = [link.text for link in nav_links]
        names = ','.join(nav_links_text).split(',')
        if 'Any' in names:
            names.remove('Any')
        elif 'Best match' in names:
            names.remove('Best match')
        return names

    def get_click_language(self, find_ln):
        click_links = {
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
            'Best match': '//details[@id="codesearch_sort_repos"]//a[text()="Best match"]',
            'Most stars': '//details[@id="codesearch_sort_repos"]//a[text()="Most stars"]',
            'Fewest stars': '//details[@id="codesearch_sort_repos"]//a[text()="Fewest stars"]',
            'Most forks': '//details[@id="codesearch_sort_repos"]//a[text()="Most forks"]',
            'Fewest forks': '//details[@id="codesearch_sort_repos"]//a[text()="Fewest forks"]',
            'Recently updated': '//details[@id="codesearch_sort_repos"]//a[text()="Recently updated"]',
            'Least recently updated': '//details[@id="codesearch_sort_repos"]//a[text()="Least recently updated"]'
        }
        clickable = self.driver.find_element(By.XPATH, click_links[find_sort])
        return clickable.click()