import time,lib.common,lib.post_lib
import unittest
from selenium import webdriver
from pages.login_page import LoginPage 
from pages.create_page import CreatePage 
from pages.edit_post_page import EditPostPage 
from pages.home_page import HomePage 


class EditCase(unittest.TestCase):
	domain=''
	dr=None

	def setUp(self):
		print('start test')
		lib.common.get_domain()
		self.dr=webdriver.Chrome()

	def test_edit(self):
		username='chenff'
		password='Cisco_123456'
		title_new='编辑第一篇文章的第一个标题 %s' %time.strftime("%Y%m%d %H%M%S")
		content_new='编辑第一篇文章的内容 %s'  %time.strftime("%Y%m%d %H%M%S")

		#-----------------使用pageobject重构前--------------------------
		'''
		lib.common.login(self.dr,username,password)
		pid=lib.post_lib.create(self.dr)
		lib.post_lib.edit(self.dr,pid,title_new,content_new)

		self.dr.get(lib.common.get_domain()+'/wp-admin/edit.php')
		time.sleep(3)
		post_id='post-'+pid
		post=self.dr.find_element_by_id(post_id)
		title_check=post.find_element_by_css_selector('.row-title').text
		print(title_check)
		
		'''
		#------------------------使用pageobject重构----------------------------------
		login_page=LoginPage(self.dr)
		login_page.login(username,password)

		create_page=CreatePage(self.dr)
		create_page.create(None,None)
		pid=create_page.get_pid()
		
		edit_post_page=EditPostPage(self.dr,pid)
		edit_post_page.edit(title_new,content_new)

		home_page=HomePage(self.dr)
		title=home_page.get_post(pid).text
		print (title)
		
		
		self.assertTrue(title_new in title)
	


	def tearDown(self):
		print('End test')
		self.dr.quit()

if __name__=='__main__':
	unittest.main()