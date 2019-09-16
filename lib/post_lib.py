import time
import lib.common
from selenium.webdriver.common.keys import Keys

def create(dr,title=None,content=None):
	if title is None:title='第一篇文章的第一个标题 %s' %time.strftime("%Y%m%d %H%M%S")
	if content is None:content='这是第一篇文章的内容 %s'  %time.strftime("%Y%m%d %H%M%S")
	dr.get(lib.common.get_domain()+'/wp-admin/post-new.php')
	time.sleep(3)

	dr.find_element_by_id('post-title-0').send_keys(title)
	dr.find_element_by_id('post-title-0').send_keys(Keys.ENTER)
	time.sleep(5)
	content_ele=dr.find_element_by_css_selector('p[class="block-editor-rich-text__editable editor-rich-text__editable wp-block-paragraph"]')
	content_ele.send_keys(content)
	time.sleep(5)

	submint_ele=dr.find_element_by_css_selector('button[class="components-button editor-post-publish-panel__toggle is-button is-primary"]')
	submint_ele.click()
	time.sleep(3)
	submit_2=dr.find_element_by_css_selector('button[class="components-button editor-post-publish-button is-button is-default is-primary is-large"]')
	submit_2.click()
	time.sleep(3)
	url=dr.current_url
	post_id=url.split('&')[0].split('=')[-1]
	return post_id


def edit(dr,post_id,title,content):
	url=lib.common.get_domain()+'/wp-admin/post.php?post='+post_id+'&action=edit' 
	print(url)
	dr.get(url)
		
	if title is None:title='编辑第一篇文章的第一个标题 %s' %time.strftime("%Y%m%d %H%M%S")
	if content is None:content='编辑第一篇文章的内容 %s'  %time.strftime("%Y%m%d %H%M%S")
	title_ele=dr.find_element_by_css_selector('textarea[class="editor-post-title__input"]')
	title_ele.send_keys(title)
	time.sleep(2)
	content_ele=dr.find_element_by_css_selector('.components-autocomplete p')
	content_ele.send_keys(content)
	time.sleep(2)

	submit_ele=dr.find_element_by_css_selector('[class~="editor-post-publish-button"]')
	submit_ele.click()
	time.sleep(3)