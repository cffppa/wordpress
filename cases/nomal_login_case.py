#coding=utf-8
import unittest #引入测试框架
from selenium import webdriver
import time,os
from selenium.webdriver.support.ui import WebDriverWait
import lib.common
import lib.post_lib
from pages.login_page import LoginPage
from pages.dashboard_page import DashBoardPage

class NormalLoginCase(unittest.TestCase):

	domain=''
	dr=None
	

	def setUp(self):
		#self.domain=os.getenv('TEST_ENV','http://localhost/wordpress')   #读环境变量
		print ('start test')
		self.domain=lib.common.get_domain()
		self.dr=webdriver.Chrome()
		

	
	def test_login(self):
		
		username='chenff'
		password='Cisco_123456'

		#-----------------使用pageobject重构前--------------------------
		'''
		lib.common.login(self.dr,username,password)
		login_user=self.dr.find_element_by_css_selector('#wp-admin-bar-my-account .ab-item')
		'''
		#------------------------使用pageobject重构----------------------------------
		login_page=LoginPage(self.dr)
		login_page.login(username,password)
		dashboard_page=DashBoardPage(self.dr)
		login_user=dashboard_page.my_account()


		self.assertTrue('wp-admin' in self.dr.current_url) #为了避免线上环境url变化造成用例执行不了
		self.assertTrue('chenff' in login_user.text) 
		time.sleep(5)

	
	def tearDown(self):
		print('end test')
		self.dr.quit()

if __name__=='__main__':
	unittest.main()