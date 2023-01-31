from typing import List

from selenium.webdriver.common.by import By

from base.seleniumbase import SeleniumBase


class SearchNav(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.__nav_links = 'div.border.rounded-2.p-3.mb-3.d-none.d-md-block>ul>li'

    def get_nav_links(self):
        return self.are_visible('css', self.__nav_links, 'Languages')

    def get_language_names(self) -> List:
        nav_links = self.get_nav_links()
        nav_links_text = [link.text for link in nav_links]
        ls = ''.join(nav_links_text)
        names = ''.join(letter for letter in ls if (letter < '0' or letter > '9') and letter != ',').split('\n')
        names.remove('')
        return names

    def get_click_language(self, find_ln):
        click_links = {
            'Python': '/html/body/div[1]/div[4]/main/div/div[2]/div[1]/ul/li[1]',
            'JavaScript': '/html/body/div[1]/div[4]/main/div/div[2]/div[1]/ul/li[2]',
            'Java': '/html/body/div[1]/div[4]/main/div/div[2]/div[1]/ul/li[3]',
            'HTML': '/html/body/div[1]/div[4]/main/div/div[2]/div[1]/ul/li[4]',
            'C++': '/html/body/div[1]/div[4]/main/div/div[2]/div[1]/ul/li[5]',
            'Jupyter Notebook': '/html/body/div[1]/div[4]/main/div/div[2]/div[1]/ul/li[6]',
            'C': '/html/body/div[1]/div[4]/main/div/div[2]/div[1]/ul/li[7]',
            'C#': '/html/body/div[1]/div[4]/main/div/div[2]/div[1]/ul/li[8]',
            'PHP': '/html/body/div[1]/div[4]/main/div/div[2]/div[1]/ul/li[9]',
            'CSS': '/html/body/div[1]/div[4]/main/div/div[2]/div[1]/ul/li[10]'

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