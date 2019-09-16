from pages.base_page import BasePage 
from lib.common import get_domain

class HomePage(BasePage):

	def __init__(self,driver):
		super(HomePage,self).__init__(driver)
		self.url=get_domain()
		self.navigate()


	def get_post(self,pid):
		post_id='post-'+str(pid)
		return self.driver.find_element_by_id(post_id).find_element_by_css_selector('.entry-title a')

	def first_post(self):
		return self.by_css('.entry-title a')