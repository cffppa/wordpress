import os,time


def get_domain():
	return os.getenv('TEST_ENV','http://localhost/wordpress')

def login(dr,username,password):
	dr.get(get_domain()+'/wp-login.php')#这样拼接url可以减少代码对环境的依赖。要是线上环境url变化，只需要改domain参数就行。  
	time.sleep(3)
	dr.find_element_by_id('user_login').send_keys(username)
	time.sleep(3)
	dr.find_element_by_id('user_pass').send_keys(password)
	time.sleep(3)
	dr.find_element_by_id('wp-submit').click()
	time.sleep(5)