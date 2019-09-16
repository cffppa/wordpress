from pages.base_page import BasePage 

class DashBoardPage(BasePage):

	def __init__(self,driver,goto=False):#这里goto参数用来控制页面是否跳转
		super(DashBoardPage,self).__init__(driver)
		self.url='http://localhost/wordpress/wp-admin/'
		if goto:self.navigate()

	def my_account(self):
		return self.by_css('#wp-admin-bar-my-account .ab-item')