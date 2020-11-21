from selenium import webdriver
from time import sleep
from pw import *

# registration
def main(username):
    driver = webdriver.Chrome()
    driver.get("https://www.instagram.com/")
    sleep(2)
    driver.find_element_by_xpath("//input[@name=\"username\"]")\
        .send_keys("imvngvli")
    driver.find_element_by_xpath("//input[@name=\"password\"]")\
        .send_keys(pw)
    driver.find_element_by_xpath('//button[@type="submit"]')\
        .click()
    sleep(4)
    driver.find_element_by_xpath("//*[@id=\"react-root\"]/section/main/div/div/div/div/button")\
        .click()
    sleep(2)
    driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]")\
        .click()
    sleep(7)

def concat_flw():
    print("lol")

if __name__ == "__main__":
    main("imvgvli")