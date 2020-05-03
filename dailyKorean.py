import random, logging, pyperclip, pyautogui, time, webbrowser, re

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

logging.basicConfig(level=logging.INFO,
                    format='%(message)s')
#logging.disable(logging.CRITICAL)

pyautogui.PAUSE = 0.5
waitTime = 30

# randint generate lesson number
lessonNum = random.randint(13, 145)

# Regex to find page link
regex = re.compile(f"(/lesson-{lessonNum})(/)?(-)?(/d)*(/)?")

# selenium open website
url = 'https://www.howtostudykorean.com/?s=' + 'Lesson + ' + str(lessonNum)
logging.info(f"Searching page for lesson {lessonNum}...")

browser = webdriver.Chrome()
browser.get(url)
logging.info(f"{'-' * 100}")

# Find link for lesson page
linkElems = browser.find_elements_by_partial_link_text(f"Lesson {lessonNum}:")

# Links found
links = []

# Append links found
for elem in linkElems:
    links.append(elem.get_attribute('href'))

for link in links:
    match = regex.search(str(link))
    if match != None:
        index = links.index(link)
        logging.info("Match found.")
        logging.info(f"Link: {linkElems[index].get_attribute('href')}")

# Click on link for that lesson in English
linkElem = linkElems[index]
logging.info(f"Entering page for lesson {lessonNum}...")
linkElem.click()

# Get top left corner coordinate
window = pyautogui.getActiveWindow()
topLeftCoord = window.topleft
addressBarCoord = (topLeftCoord[0] + 620, topLeftCoord[1] + 60)

# Click on address bar
pyautogui.click(addressBarCoord)

# Select address and copy to clipboard
pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('ctrl', 'c')

# Open Chrome browser
mainURL = ('https://www.howtostudykorean.com/')
webbrowser.open(mainURL)

# Wait for browser to load
time.sleep(3)

# Chrome browser address bar coordinate
chromeAddressCoord = (600, 50)

# Enter address in clipboard
logging.debug(f"Clicking {chromeAddressCoord}")
pyautogui.click(chromeAddressCoord)

logging.debug("Pasting address")
pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('ctrl', 'v')

logging.debug("Entering page")
pyautogui.press('enter')

# Close selenium browser
browser.quit()
