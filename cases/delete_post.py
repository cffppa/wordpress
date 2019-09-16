import time,lib.common,lib.post_lib
import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from pages.login_page import LoginPage 
from pages.create_page import CreatePage 
from pages.post_list_page import PostListPage 


class DeleteCase(unittest.TestCase):

	domain=''
	dr=None


	def setUp(self):
		print('start test')
		self.dr=webdriver.Chrome()
		lib.common.get_domain()

	'''
	def is_post_exists(self,post_id):
		try:
			WebDriverWait(self.dr,10).until(expected_conditions.presence_of_element_located((By.ID,post_id)))
		except:
			return False
		return True
	'''

	def test_delete(self):
		#登录
		username='chenff'
		password='Cisco_123456'
		title='第一篇文章的第一个标题 %s' %time.strftime("%Y%m%d %H%M%S")

		#-----------------使用pageobject重构前--------------------------
		'''
		lib.common.login(self.dr,username,password)
		#创建一篇新文章。
		post_id='post-'+lib.post_lib.create(self.dr,title,None)
		self.dr.get(lib.common.get_domain()+'/wp-admin/edit.php')
		time.sleep(5)

		post=self.dr.find_element_by_id(post_id)
		ActionChains(self.dr).move_to_element(post).perform()
		time.sleep(2)
		xpath='//tr[@id="'+post_id+'"]/td/div[3]/span[3]/a'    #拼接“移动至回收站”的xpath
		self.dr.find_element_by_xpath(xpath).click()
		self.assertFalse(self.is_post_exists(post_id))     #断言元素不存在
		'''
		#------------------------使用pageobject重构----------------------------------
		login_page=LoginPage(self.dr)
		login_page.login(username,password)

		create_page=CreatePage(self.dr)
		create_page.create(title,None)
		pid=create_page.get_pid()

		post_list_page=PostListPage(self.dr)
		post_list_page.delete(pid)

		self.assertFalse(post_list_page.is_post_exist(pid))     #断言元素不存在
	


	def tearDown(self):
		print('End test')
		self.dr.quit()

if __name__=='__main__':
	unittest.main()