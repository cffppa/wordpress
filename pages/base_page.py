class BasePage(object):
	#basepage是所有页面的基类。
	url=None
	dr=None

	def __init__(self,driver):
		self.driver=driver

	def title(self):
		return self.driver.title

	def current_url(self):
		return self.driver.current_url

	def navigate(self):
		self.driver.get(self.url)

	def by_id(self,the_id):
		return self.driver.find_element_by_id(the_id)

	def by_css(self,css):
		return self.driver.find_element_by_css_selector(css)




