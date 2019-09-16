import unittest
from selenium import webdriver
from pages.login_page import LoginPage 
from lib.common import get_domain

class AbnormalLoginCase(unittest.TestCase):
	dr=None
	url=''
	data_for_test_login_failed=[
		{'name':'chenff','password':'','tips':'错误：密码一栏为空。'},
		{'name':'','password':'124134','tips':'错误：用户名一栏为空。'},
		{'name':'chenff','password':'123345','tips':'错误：为用户名chenff指定的密码不正确。 忘记密码？'},
		{'name':'error','password':'None','tips':'错误：无效用户名。 忘记密码？'}
	]


	def setUp(self):
		print ('start test')
		self.url=get_domain()+'/wp-login.php'
		self.dr=webdriver.Chrome()


	def test_login_failed(self):
		login_page=LoginPage(self.dr)
		for item in self.data_for_test_login_failed:
			username=item['name']
			password=item['password']
			error=item['tips']
			print (error)
			login_page.login(username,password)


			self.assertTrue(login_page.current_url() == self.url)
			if login_page.error_msg() != False:
				error_msg=login_page.error_msg().text
				self.assertTrue(error_msg==error)

	def tearDown(self):
		print ('start test')
		self.dr.quit()

if __name__=='__main__':
	unittest.main()