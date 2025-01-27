import time

from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


@given('User is on the login page')
def step_user_on_login(context):
    print("@given stated")
    context.browser = webdriver.Chrome()
    context.browser.maximize_window()
    context.browser.get("https://www2.hm.com/en_in/index.html")
    # wait for the Accept all cookies to be clickable
    WebDriverWait(context.browser,5).until(
        EC.element_to_be_clickable((By.ID,"onetrust-accept-btn-handler"))).click()
    #To wait until URL is changes
    WebDriverWait(context.browser,10).until(
        EC.url_contains("https://www2.hm.com/en_in/index.html"))
    assert "https://www2.hm.com/en_in/index.html" in context.browser.current_url
    print("@given Ended")


@when('User enters valid credentials')
def steps_to_enter_credentials(context):
    print("when stated")
    # click on signin button
    context.browser.find_element(By.CSS_SELECTOR,".CGae.mYRh.vEfo.__5DXf.k0Zy").click()
    time.sleep(2)
    # Enter the username
    context.browser.find_element(By.CSS_SELECTOR,"#email").send_keys("raja.viknesh@outlook.com")
    # Enter the Password
    context.browser.find_element(By.CSS_SELECTOR,"#password").send_keys("Loveis@07")
    # Click on submit button
    context.browser.find_element(By.CSS_SELECTOR,"button[type='submit']").click()
    print("when Ended")


@then('User is redirected to the homepage')
def steps_to_redirect(context):
    try:
        print("@then stated")
        myaccount=WebDriverWait(context.browser,10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,".HcHv")))
        myaccount.click()
        WebDriverWait(context.browser,10).until(
            EC.url_contains("https://www2.hm.com/en_in/account"))
        assert "https://www2.hm.com/en_in/account" in context.browser.current_url
    except Exception as e:
        print (f" error is {e}")
    finally:
        context.browser.quit()
        print("@then stated")

