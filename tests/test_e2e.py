import time
import smtplib
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def send_email(user, pwd, recipient, subject, body):
    FROM = user
    TO = recipient if isinstance(recipient, list) else [recipient]
    SUBJECT = subject
    TEXT = body

    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(user, pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print('successfully sent the mail')
    except:
        print("failed to send mail")


driver = webdriver.Chrome(executable_path="C:\SeleniumDrivers\chromedriver.exe")
driver.get("https://test.kommunicate.io")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
wait = WebDriverWait(driver, 30)
print("Waiting for the iframe to display")
wait.until(expected_conditions.presence_of_element_located(
    (By.XPATH, "//iframe[@class='kommunicate-custom-iframe chat-popup-widget-vertical']")))
print("iframe located")
element_to_hover_over = driver.find_element_by_xpath(
    "//iframe[@class='kommunicate-custom-iframe chat-popup-widget-vertical']")
hover = ActionChains(driver).move_to_element(element_to_hover_over)
hover.perform()
print("Hover overed on iframe")
driver.switch_to.frame("kommunicate-widget-iframe")
time.sleep(3)
dismiss = driver.find_element_by_xpath("//div[@id='chat-popup-widget-container']//div//div")
if dismiss.is_displayed():
    dismiss.click()
else:send_email("Sharaththippeshappa@gmail.com", "Sharu@1234", "Sharaththippeshappa@gmail.com", "Failed: Close button not displayed")
driver.find_element_by_xpath("//div[@id='launcher-svg-container']").click()
print("Clicked on chat icon")
wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//div[text()='Online']")))
print("Waiting for FAQ button to display")
driver.find_element_by_xpath("//button[@id='km-faq']").click()
print("Clicked on FAQ icon")
faqcount = len(driver.find_elements_by_class_name("km-faq-list"))
print("FAQ Count is: "+str(faqcount))
if faqcount > 20:
    send_email("Sharaththippeshappa@gmail.com", "Sharu@1234", "Sharaththippeshappa@gmail.com", "FAQcoun",
               "FAQcount is :" + str(faqcount))
