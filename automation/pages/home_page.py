from automation.pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)


def hello(*args, name: str):
    print(args, name)

hello("miew", "whoof", name="king")
