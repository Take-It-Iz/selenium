from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import (
    Keys,
)  # allows to send keyboard keys input (ENTER, ESC etc.)
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

chrome_driver_path = "C:\Files"  # path to browser driver
chrome_driver = webdriver.Chrome(chrome_driver_path)
chrome_driver.maximize_window()
chrome_driver.get("https://realpython.com/")

file_path = "C:\Projects\python\\automation\selenium\\tutorial"
file_name = os.path.join(file_path, "articles_1.txt")

search_field = chrome_driver.find_element(By.NAME, "q")
search_field.clear()
search_field.send_keys("Selenium")
search_field.send_keys(Keys.RETURN)  # ENTER button

try:
    # retieve data from search result and write it to file
    results = WebDriverWait(chrome_driver, 10).until(
        EC.presence_of_element_located((By.ID, "resultsArea"))
    )
    description = results.find_elements(By.CLASS_NAME, "text-muted")

    file = open(file_name, "w")
    for d in description:
        file.write(d.text + "\n")
    file.close()

    time.sleep(5)

    # write article titles and links to these articles to another file
    article_titles = chrome_driver.find_elements(By.XPATH, "//h2[@class='my-0 h5']")
    article_links = chrome_driver.find_elements(
        By.XPATH, "//a[@class='stretched-link']"
    )

    file_name = os.path.join(file_path, "articles_2.txt")
    file = open(file_name, "w")
    for (t, l) in zip(article_titles, article_links):
        file.write(t.text + "\n" + l.get_attribute("href") + "\n\n")
    file.close()
finally:
    time.sleep(10)
