from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from infrastructure.infra.dal.web_driver_extension.web_driver_extension import DriverEX
from infrastructure.objects.objects_ui.interfaceses.login_page_ui_interface import ILoginPageUi


class LoginPageUi(ILoginPageUi):
    def __init__(self, driver: WebDriver) -> None:
        self.__driver = driver

        # locators
        self.__user_name_ext = (By.CSS_SELECTOR, "input[test-id='email']")
        self.__password_ext = (By.CSS_SELECTOR, "input[test-id='password']")
        self.__login_btn_ext = (By.CSS_SELECTOR, "button[test-id='sign-in']")

    def set_user_name(self, user_name: str):
        DriverEX.send_keys_auto(self.__driver, self.__user_name_ext, user_name)
        return self

    def set_password(self, password: str):
        DriverEX.send_keys_auto(self.__driver, self.__password_ext, password)
        return self

    def click_on_sign_in_btn(self):
        DriverEX.force_click(self.__driver, self.__login_btn_ext)
        return self