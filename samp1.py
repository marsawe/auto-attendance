import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.options import Options
option1=Options()
option1.add_argument("--disable-notifications")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=option1)
driver.get("https://teams.microsoft.com/_#/school/teams-grid/General?ctx=teamsGrid")
time.sleep(3)
elem=driver.find_element(By.ID,"i0116")
elem.send_keys("Insert email id"+Keys.ENTER)
elem2=driver.find_element(By.ID,"i0118")
elem2.send_keys("Insert password"+Keys.ENTER)
time.sleep(5)
driver.find_element(By.ID,"idSIButton9").click()
time.sleep(10)
#You need to access the channel twice because teams is weird. The third one is because I was having issues, don't think it's needed
driver.get("Link to the channel the meet is in")
time.sleep(15)
driver.get("Channel the meet is in")
time.sleep(10)
driver.get("Channel the meet is in")
time.sleep(10)
driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[2]/div[1]/teams-grid/div/div/middle-messages-stripe/div/messages-header/div[2]/div/message-pane/div/div[1]/div/div/calling-persistent-indicator/div/div/div/ul/li/calling-persistent-indicator-item/div/div/calling-join-button/button").click()
time.sleep(10)
driver.find_element(By.XPATH,"/html/body/div[7]/div[2]/div/div/div/div[1]/div/div/div[2]/div/button").click()
time.sleep(10)
driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[2]/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div[2]/div/div/section/div[1]/div/div/button").click()

time.sleep(10)
driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[2]/div[1]/div/calling-screen/div/div[2]/calling-unified-bar/section/div/div/div[3]/items-group/div/item-widget[1]/push-button/div/button").click()
time.sleep(10)
driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[2]/div[1]/div/calling-screen/div/div[2]/meeting-panel-components/calling-chat/div/context-message-pane/div[2]/new-message/div/div[2]/form/div[3]/div[1]/div[2]/div/div/div[2]/div/div/div/div").send_keys("I am present"+Keys.ENTER)
time.sleep(5)
driver.close()