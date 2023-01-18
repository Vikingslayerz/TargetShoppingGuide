import time
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_argument('--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1')
driver = webdriver.Chrome(options=chrome_options)
# driver.implicitly_wait(10)
driver.get("https://www.target.com")


# store_location_box = driver.find_element(By.ID, "web-store-id-msg-btn")
# store_location_box.click()

# select_a_store = driver.find_element(By.CLASS_NAME, "ReactModal__Content")
# search_div = select_a_store.find_element(By.CLASS_NAME, "sc-hHTYSt")

# zip_code_box = search_div.find_element(By.TAG_NAME, "input")
# zip_code_box.click()
# zip_code_box.send_keys("55126")
# look_up_button = search_div.find_element(By.TAG_NAME, "button")
# look_up_button.click()

# try:
#     shoreview_box = driver.find_elements(By.CLASS_NAME, "styles__SpacingWrapper-sc-ai1efk-1")[1]
#     shoreview_box_button_set_as_my_store = shoreview_box.find_elements(By.TAG_NAME, "button")[0]
# except:
#     time.sleep(5)
#     shoreview_box = driver.find_elements(By.CLASS_NAME, "styles__SpacingWrapper-sc-ai1efk-1")[1]
#     shoreview_box_button_set_as_my_store = shoreview_box.find_elements(By.TAG_NAME, "button")[0]

# shoreview_box_button_set_as_my_store.send_keys(Keys.RETURN)

search_box = driver.find_element(By.NAME, "searchTerm")
search_box.click()
search_box.send_keys("preworkout")
search_box.submit()

time.sleep(3)

results_section = driver.find_element(By.CLASS_NAME, "styles__StyledRowWrapper-sc-z8946b-1")
results_list = results_section.find_element(By.CLASS_NAME, "sc-hHTYSt")
results_list = results_list.find_elements(By.TAG_NAME, "div")
print(len(results_list))

product = None
for result in results_list:
    try:
        product = WebDriverWait(driver, 2).until(EC.element_to_be_clickable(result))
        break
    except:
        continue

for i, result in enumerate(results_list):
    if product == result:
        print(i)
        break

product.click()
time.sleep(120)
