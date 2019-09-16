import unittest
from selenium import webdriver
import time,lib.common,lib.post_lib,os
from pages.login_page import LoginPage 
from pages.create_page import CreatePage 
from pages.home_page import HomePage 

class CreateCase(unittest.TestCase):
	domain=''
	dr=None

	def setUp(self):
		#self.domain=os.getenv('TEST_ENV','http://localhost/wordpress')   #读环境变量
		lib.common.get_domain()
		print ('start test')
		self.dr=webdriver.Chrome()

	
	def test_create_post(self):
		username='chenff'
		password='Cisco_123456'
		title='第一篇文章的第一个标题 %s' %time.strftime("%Y%m%d %H%M%S")

		#-----------------使用pageobject重构前--------------------------
		#lib.common.login(self.dr,username,password)
		#lib.post_lib.create(self.dr,title,None)
		#ele=self.dr.find_element_by_css_selector('.entry-title a')
		#get_title=ele.text
		
		#------------------------使用pageobject重构----------------------------------
		login_page=LoginPage(self.dr)
		login_page.login(username,password)
		
		create_page=CreatePage(self.dr)
		create_page.create(title,None)
		pid=create_page.get_pid()
		home_page=HomePage(self.dr)
		time.sleep(3)
		first_post=home_page.first_post()
		get_title=first_post.text
		
		print (get_title)
		#断言：发布成功：进入首页判断最新的文章href中是否含有文章标题。
		self.assertTrue(title == get_title)
	


	def shutdown(self):
		print('End test')
		self.dr.quit()

if __name__=='__main__':
	unittest.main()