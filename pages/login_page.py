from pages.base_page import BasePage
import time
from lib.common import get_domain

class LoginPage(BasePage):

	def __init__(self,driver):

		super(LoginPage,self).__init__(driver)
		self.url=get_domain()+'/wp-login.php'
		self.navigate()

	def user_text_field(self):#定义用户名输入框元素
		return self.by_id('user_login')

	def password_text_field(self):
		return self.by_id('user_pass')

	def login_button(self):
		return self.by_id('wp-submit')

	def error_msg(self):
		try:
			return self.by_id('login_error')
		except:
			return False

	def login(self,username,password):
		self.user_text_field().clear()
		self.user_text_field().send_keys(username)
		time.sleep(2)
		self.password_text_field().send_keys(password)
		time.sleep(2)
		self.login_button().click()
		time.sleep(2)


