from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import bs4
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup as soup
import time
import imdb


class WhatsAppBot:

	def __init__(self):
		self.driver = webdriver.Chrome("./chromedriver.exe")



	def start(self):
		self.driver.get("https://web.whatsapp.com/")
		self.wait = WebDriverWait(self.driver, 600)
		

	def auto_respond(self):
		
		try:
			new_message = self.driver.find_elements_by_class_name('_31gEB')
			print('found')
			
			current_url = self.driver.page_source
			
			page_soup = soup(current_url, 'html.parser')
			latest_messages = page_soup.findAll("div", {"class":"_3tBW6"})
			
			name_of_movie = str(latest_messages[0].text)
			
			ac = ActionChains(self.driver)
			ac.move_to_element(new_message[0]).move_by_offset(-10, 0).click().perform()
			
			ia = imdb.IMDb()
			
			try:
				search = ia.search_movie(name_of_movie)
				id_of_movie = search[0].movieID
				movie = ia.get_movie(id_of_movie)
				cst = movie['cast']
				ac1 = cst[0]
				ac2 = cst[1]
				ac3 = cst[2]
				ac4 = cst[3]
				ac5 = cst[4]
				ac6 = cst[5]
				ac7 = cst[6]
				ac8 = cst[7]
				ac9 = cst[8]
				send_ready_message = f"{ac1}, {ac2}, {ac3}, {ac4}, {ac5}, {ac6}, {ac7}, {ac8}, {ac9}"
			except:
				send_ready_message = 'Cannot find Any Movie Please Check Again'
			
			message = self.driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]
			message.send_keys(send_ready_message)
			sendbutton = self.driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')[0]
			sendbutton.click()
			new_message = None
			current_url = None
			page_soup = None
			latest_messages = None
			name_of_movie = None
			ac = None
			ia = None
			search = None
			id_of_movie = None
			movie = None
			cst = None
			ac1 = None
			ac2 = None
			ac3 = None
			ac4 = None
			ac5 = None
			print(send_ready_message)
			send_ready_message = None
			self.auto_respond()

		except:
			new_message = None
			current_url = None
			page_soup = None
			latest_messages = None
			name_of_movie = None
			ac = None
			ia = None
			search = None
			id_of_movie = None
			movie = None
			cst = None
			ac1 = None
			ac2 = None
			ac3 = None
			ac4 = None
			time.sleep(1)
			self.auto_respond()

	def send_message(self):
		target = ''
		messtobesend= "Namastey!!"
		x_arg = '//span[contains(@title,' + target + ')]'
		group_title = self.wait.until(EC.presence_of_element_located((
			By.XPATH, x_arg)))
		group_title.click()
		for i in range(100):
			message = self.driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]
			message.send_keys(messtobesend)
			sendbutton = self.driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')[0]
			sendbutton.click()

if __name__ == '__main__':
	bot = WhatsAppBot()
	bot.start()
	bot.auto_respond()

