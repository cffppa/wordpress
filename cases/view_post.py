import time,lib.common,lib.post_lib
import unittest
from selenium import webdriver
from pages.login_page import LoginPage 
from pages.create_page import CreatePage 
from pages.view_page import ViewPage 

class ViewCase(unittest.TestCase):
	domain=''
	dr=None

	def setUp(self):
		print('start test')
		lib.common.get_domain()
		self.dr=webdriver.Chrome()

	def test_view(self):
		username='chenff'
		password='Cisco_123456'
		title='第一篇文章的第一个标题 %s' %time.strftime("%Y%m%d %H%M%S")
		content='这是第一篇文章的内容 %s'  %time.strftime("%Y%m%d %H%M%S")

		#-----------------使用pageobject重构前--------------------------
		'''
		lib.common.login(self.dr,username,password)
		post_id='post-'+lib.post_lib.create(self.dr,title,content)
		self.dr.find_element_by_css_selector('[class="components-button is-button is-default"]').click()

		post=self.dr.find_element_by_id(post_id)
		title_get=post.find_element_by_css_selector('.entry-title').text
		content_get=post.find_element_by_css_selector('.entry-content').text
		print(title_read)
		print(content_read)
		'''
		#------------------------使用pageobject重构----------------------------------
		login_page=LoginPage(self.dr)
		login_page.login(username,password)
	
		create_page=CreatePage(self.dr)
		create_page.create(title,content)
		pid=create_page.get_pid()
		create_page.view_post().click()
		time.sleep(3)

		view_page=ViewPage(self.dr)
		title_get=view_page.view_title().text
		time.sleep(1)
		content_get=view_page.view_content().text
		time.sleep(2)

		
		self.assertTrue(title_get==title)
		self.assertTrue(content_get==content)

	def tearDown(self):
		print('End test')
		self.dr.quit()

if __name__=='__main__':
	unittest.main()