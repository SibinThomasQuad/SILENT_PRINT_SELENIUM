from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import os

options = FirefoxOptions()
options.add_argument("--headless")
profile = webdriver.FirefoxProfile()
profile.set_preference("print.always_print_silent", True)
profile.set_preference("print.print_bgimages", True)
profile.set_preference("print.print_unwriteable_margin_bottom", 0)
profile.set_preference("print.print_unwriteable_margin_left", 0)
profile.set_preference("print.print_unwriteable_margin_right", 0)
profile.set_preference("print.print_unwriteable_margin_top", 0)
driver = webdriver.Firefox(firefox_profile=profile,options=options)
html_file = os.getcwd() + "//" + "web.html"
driver.get("file:///" + html_file)
driver.execute_script("window.print();")
