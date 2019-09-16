from pages.base_page import BasePage 
from lib.common import get_domain

class ViewPage(BasePage):

	def __init__(self,driver,goto=False):
		super(ViewPage,self).__init__(driver)
		self.url=get_domain()+''
		if goto:self.navigate()

	def view_title(self):
		return self.by_css('.entry-title')

	def view_content(self):
		return self.by_css('.entry-content')