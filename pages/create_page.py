from pages.base_page import BasePage 
import time
from selenium.webdriver.common.keys import Keys 
from lib.common import get_domain

class CreatePage(BasePage):

	def __init__(self,driver):
		super(CreatePage,self).__init__(driver)
		self.url=get_domain()+'/wp-admin/post-new.php'
		self.navigate()

	def title_text_field(self):
		return self.by_id('post-title-0')

	def content_text_field(self):
		return self.by_css('p[class="block-editor-rich-text__editable editor-rich-text__editable wp-block-paragraph"]')

	def submit_1_button(self):
		return self.by_css('button[class="components-button editor-post-publish-panel__toggle is-button is-primary"]')

	def submit_2_button(self):
		return self.by_css('button[class="components-button editor-post-publish-button is-button is-default is-primary is-large"]')

	def create(self,title,content):
		if title is None:title='第一篇文章的第一个标题 %s' %time.strftime("%Y%m%d %H%M%S")
		if content is None:content='这是第一篇文章的内容 %s'  %time.strftime("%Y%m%d %H%M%S")

		self.title_text_field().send_keys(title)
		self.title_text_field().send_keys(Keys.ENTER)
		time.sleep(2)
		self.content_text_field().send_keys(content)
		time.sleep(1)
		self.submit_1_button().click()
		time.sleep(1)
		self.submit_2_button().click()
		time.sleep(1)

	def get_pid(self):
		pid=self.current_url().split('&')[0].split('=')[-1]
		return int(pid)

	def view_post(self):
		return self.by_css('[class="components-button is-button is-default"]')



