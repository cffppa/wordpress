from pages.base_page import BasePage 
from lib.common import get_domain
from selenium.webdriver.common.action_chains import ActionChains 
import time

class PostListPage(BasePage):

	def __init__(self,driver):
		super(PostListPage,self).__init__(driver)
		self.url=get_domain()+'/wp-admin/edit.php'
		self.navigate()

	def find_post(self,pid):
		post_id='post-'+str(pid)
		return self.by_id(post_id)

	def delete(self,pid):
		post_id='post-'+str(pid)
		post=self.by_id(post_id)
		ActionChains(self.driver).move_to_element(post).perform()
		time.sleep(2)
		post.find_element_by_css_selector('.trash').click()
		time.sleep(2)

	def is_post_exist(self,pid):
		post_id='post-'+str(pid)
		try:
			WebDriverWait(self.driver,10).until(expected_contidions.presence_of_element_located((By.ID,post_id)))
		except:
			return False
		return True

