from behave import *
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from webdriver_manager.chrome import ChromeDriverManager
#driver = webdriver.Chrome(ChromeDriverManager().install())

opt=Options()
opt.add_argument("--headless")

driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=opt)

@given(u'Launch chrome browser')
def step_impl(context):
    try:
        context.driver = driver
    except NameError:
        print("Chrome browser did not open")
    else:
        print("Chrome browser open successfully")


@when(u'open Orange hrm homepage')
def step_impl(context):
    context.driver.get("https://www.orangehrm.com/")
    time.sleep(1)
    context.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div/div/h3").is_displayed()


@when(u'close browser')
def step_impl(context):
    raise NotImplementedError(u'STEP: When close browser')