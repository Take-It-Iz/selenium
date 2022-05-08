from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_driver_path = "C:\Projects\python\\automation\selenium\\tutorial"
chrome_driver = webdriver.Chrome(chrome_driver_path)
chrome_driver.maximize_window()
chrome_driver.get("https://realpython.com/")


try:
    learn_dropdown = WebDriverWait(chrome_driver, 10).until(
        EC.presence_of_element_located((By.ID, "navbarDropdownLibrary"))
    )
    learn_dropdown.click()  # click on dropdown menu

    learning_paths = WebDriverWait(chrome_driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[@class='dropdown-item'][4]"))
    )
    learning_paths.click()  # click on 'Learning Paths'
    chrome_driver.back()  # step back
    chrome_driver.forward()

finally:
    chrome_driver.quit()
