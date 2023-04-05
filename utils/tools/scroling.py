class Scrolling:
    def __init__(self, driver):
        self._driver = driver

    def scroll_to(self, x=0, y=0):
        self._driver.execute_script(f"window.scrollTo({x},{y})")
