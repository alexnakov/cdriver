from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException
import time

class CDriver(Chrome):
    def __init__(self):
        super().__init__()

    def query_selector_all(self, css_selector, timeout=10, retries=5):
        for attempt in range(retries):
            try:
                elements = WebDriverWait(self, timeout).until(
                    EC.presence_of_all_elements_located((By.CSS_SELECTOR, css_selector))
                )
                return elements
            except (NoSuchElementException, StaleElementReferenceException, TimeoutException):
                if attempt < retries - 1:
                    time.sleep(1)
                else:
                    raise

    def find_element_by_text(self, inner_text, timeout=10, retries=5):
        for attempt in range(retries):
            try:
                elements = WebDriverWait(self, timeout).until(
                    EC.presence_of_all_elements_located((By.XPATH, f"//*[contains(text(), '{inner_text}')]"))
                )
                return elements[0]
            except (NoSuchElementException, StaleElementReferenceException, TimeoutException):
                if attempt < retries - 1:
                    time.sleep(1)
                else:
                    raise