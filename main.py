
# Selenium imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as WS

# os import
import os

# Colors
WHITE = "\033[0;37m"
CYAN = "\033[1;36m"
GREEN = "\033[0;32m"
ORANGE = "\033[0;33m"
PINK = "\033[1;31m"
BLUE = "\033[0;34m"
PURPLE = '\033[95m'
DARKCYAN = '\033[36m'
YELLOW = '\033[93m'
RED = '\033[91m'

# Extras
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
END = '\033[0m'

#Clear screen function
clear = lambda: os.system('clear')


# Print Statement
print(YELLOW + BOLD + UNDERLINE + "Welcome to this web-browser..." + END)

ask = input(ORANGE + "1. Do you wanna paste just a link?\nor\n2. Just put a link name?\n: " + END)
ask = ask.lower()

# Input statement
if ask == '1' or ask == 'link':
  input1 = input("Enter the site link you wanna proceed to:- ")
  input1 = input1.lower()


  # Driver get
  driver = webdriver.Firefox()
  driver.get("{}".format(input1))

# CSS.
  CSS = WebDriverWait(driver, 60).until(
    WS.presence_of_element_located((By.CSS_SELECTOR, ".run-icon-svg"))
)

elif ask == '2' or ask == 'name':
  input1 = input("Enter the site name you wanna proceed to:- ")
  input1 = input1.lower()


  # Driver get
  driver = webdriver.Firefox()
  driver.get("https://{}.com".format(input1))

# CSS.
  CSS = WebDriverWait(driver, 60).until(
    WS.presence_of_element_located((By.CSS_SELECTOR, ".run-icon-svg")) 
)

else:
  print(RED + "Not really found!!" + END)

# Making the run clickable
CSS.click()

# Printing the end if it breaks
print("Over!")

