from time import sleep

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

chromeDriver = webdriver.Chrome("C:/Users/cparloaga/Documents/chromedriverWin32/chromedriver")
chromeDriver.get("https://www.python.org")
print(chromeDriver.title)

action = ActionChains(chromeDriver)

downloadsMenu = chromeDriver.find_element_by_id("downloads")
action.move_to_element(downloadsMenu).perform()

# allReleasesMenu = chromeDriver.find_element_by_xpath(".//*[@id=\"downloads\"]/ul/li[1]")
allReleasesMenu = chromeDriver.find_element_by_xpath(".//li[@id='downloads']/ul[@class='subnav menu']/li[@class='tier-2 element-1']")
action.move_to_element(allReleasesMenu).perform()
allReleasesMenu.click()

print(chromeDriver.current_url)

releasesSection = chromeDriver.find_element_by_xpath(".//div[@class='row active-release-list-widget']/ol[@class='list-row-container menu']")
releasesVersions = releasesSection.find_elements_by_class_name("release-version")

# versionsList = []
# for item in releasesVersions:
#     versionsList.append(item.text)
#
# versionsList.sort(reverse=True)
# print("Latest version is: " + versionsList[0])

# for item in releasesVersions:
#     print(item.text)
print("Latest version is: " + releasesVersions[0].text)

sleep(5)
chromeDriver.close()