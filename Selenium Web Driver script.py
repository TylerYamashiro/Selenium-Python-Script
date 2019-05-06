##Tyler Yamashiro##
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(executable_path=r"C:\Users\Tyler\Desktop\HwSelen\Chromedriver.exe")
driver.get("http://localhost:59052/")
assert "Roster - AttendanceStar" in driver.title

assert driver.find_element_by_id("AvatarBox")
person = driver.find_element_by_id("AvatarBox")
person.click()
assert "Student Portal - AttendanceStar" in driver.title

assert driver.find_element_by_id("HomeLinkNavBar")
student = driver.find_element_by_id("HomeLinkNavBar")
student.click()
assert "Roster - AttendanceStar" in driver.title

assert driver.find_element_by_id("KioskModeLinkNavBar")
kiosk = driver.find_element_by_id("KioskModeLinkNavBar")
kiosk.click()
assert "Kiosk - AttendanceStar" in driver.title

assert driver.find_element_by_id("AvatarAttendanceLinkNavBar")
avatar = driver.find_element_by_id("AvatarAttendanceLinkNavBar")
avatar.click()
assert "Welcome - AttendanceStar" in driver.title

assert driver.find_element_by_id("BodyBackgroundColorId")
driver.close()


