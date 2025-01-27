import time

from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common import by


@given('User is on the login page')
def step_user_on_login(context):
    context.browser = webdriver.Chrome()
    context.browser.get("https://www2.hm.com/en_in/index.html")
    assert "https://www2.hm.com/en_in/index.html" in context.browser.current_url
    time.sleep(5)


@when('User enters valid credentials')
def steps_to_enter_credentials(context):
    context.browser.find_element_by_cssselector("#email").sendkeys("hi@gmail.com")
    context.browser.find_element_by_name("Login/ Sign Up").sendkeys("raja.viknesh@gmail.com")

@then('User is redirected to the homepage')
def steps_to_redirect(context):
    assert "https://www.redbus.in/" in context.currenturl
    context.browser.quit()

