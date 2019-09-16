from pages.base_page import BasePage 
import time
from lib.common import get_domain

class EditPostPage(BasePage):

	def __init__(self,driver,pid):
		super(EditPostPage,self).__init__(driver)		
		self.url=get_domain()+'/wp-admin/post.php?post=%d&action=edit' %pid
		self.navigate()

	def edit_title_text_field(self):
		return self.by_id('post-title-0')

	def edit_content_text_field(self):
		return self.by_css('.components-autocomplete p')

	def submit_button(self):
		return self.by_css('[class~="editor-post-publish-button"]')

	def view_post(self):
		return self.by_css('[class="components-button is-button is-default"]')

	def edit(self,title,content):
		self.edit_title_text_field().send_keys(title)
		time.sleep(2)
		self.edit_content_text_field().send_keys(content)
		time.sleep(2)
		self.submit_button().click()
		time.sleep(3)

