import time
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
# chrome_options.add_argument('--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1')
driver = webdriver.Chrome(options=chrome_options)
driver.set_window_size(400, 450)
driver.implicitly_wait(10)
driver.get("https://www.target.com")

# Set local zip code (55126)
store_location_box = driver.find_element(By.ID, "web-store-id-msg-btn")
store_location_box.click()

select_a_store = driver.find_element(By.CLASS_NAME, "ReactModal__Content")
search_div = select_a_store.find_elements(By.TAG_NAME, "div")[14]

zip_code_box = search_div.find_element(By.TAG_NAME, "input")
zip_code_box.click()
zip_code_box.send_keys("55126")
look_up_button = search_div.find_element(By.TAG_NAME, "button")
look_up_button.click()

try:
    shoreview_box = driver.find_elements(By.CLASS_NAME, "styles__SpacingWrapper-sc-ai1efk-1")[1]
    shoreview_box_button_set_as_my_store = shoreview_box.find_elements(By.TAG_NAME, "button")[0]
except:
    time.sleep(5)
    shoreview_box = driver.find_elements(By.CLASS_NAME, "styles__SpacingWrapper-sc-ai1efk-1")[1]
    shoreview_box_button_set_as_my_store = shoreview_box.find_elements(By.TAG_NAME, "button")[0]

shoreview_box_button_set_as_my_store.send_keys(Keys.RETURN)


# Search for item
search_box = driver.find_elements(By.TAG_NAME, "input")[1]
search_box.click()

time.sleep(3)
search_box = driver.find_elements(By.TAG_NAME, "input")[-1]
# search_box = WebDriverWait(driver, 15).until(EC.element_to_be_clickable(driver.find_element(By.NAME, "searchTerm")))
search_box.send_keys("preworkout")

search_box.submit()

time.sleep(10)

# Select top result available in store
results_section = driver.find_element(By.CLASS_NAME, "styles__StyledRowWrapper-sc-z8946b-1")
results_list = results_section.find_elements(By.TAG_NAME, "div")[0]
# Each panel has the class in the main div and one more internal, need to remove the internal ones
results_list = results_list.find_elements(By.XPATH, "./*")
print(len(results_list))
results_list = [result for result in results_list if "sponsored" not in result.get_attribute("innerHTML")]

print(len(results_list))

print(results_list)

product = [result for result in results_list if "In stock" in result.get_attribute("innerHTML")]

print(product)
product = product[0]

# product = None
# for result in results_list:
#     try:
#         product = WebDriverWait(driver, 2).until(EC.element_to_be_clickable(result))
#         break
#     except:
#         continue

# for i, result in enumerate(results_list):
#     if product == result:
#         print(i + 6)
#         print(product.get_attribute("innerHTML"))
#         break

product.click()
time.sleep(10)
driver.refresh()
time.sleep(10)
aisle_location = driver.find_element(By.CLASS_NAME, "styles__StyledAvailabilitySneakPeekAndAisleInfoDiv-sc-2vujr8-1")
print(aisle_location.get_attribute("innerHTML"))

time.sleep(120)
