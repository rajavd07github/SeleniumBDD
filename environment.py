from selenium  import webdriver

def before_all(context):
  """
  Setup actions to run before all tests.
  This might include starting the WebDriver and setting up test data.
  """
  context.browser = webdriver.Chrome()
  context.browser.implicitly_wait(10)  # Wait up to 10 seconds for elements to appear

def before_all(context):
    """
   Teardown actions to run after all tests.
   This might include closing the WebDriver and cleaning up test data.
   """
    context.browser.quit()

def before_scenario(context,scenario):
    """
    Setup actions to run before each scenario.
    You can use this function to reset states or prepare specific data for each scenario.
    """
    print (f" starting scenario: {scenario.name}")

def after_scenario(context,scenario):
    """
   Teardown actions to run after each scenario.
   You can use this function to log results or perform cleanup specific to each scenario.
   """
    if scenario.status=="failed":
        # take sceenshot in case of failure
        print(f"screenshots/{scenario.name}.png")

    print(f" ending scenario: {scenario.name}")


