import sys
import time
from time import sleep

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from infrastructure.infra.dal.data_reposetory.data_rep import DataRep
from infrastructure.infra.dal.web_driver_extension.web_driver_extension import DriverEX
from infrastructure.objects.objects_ui.filters_page_ui import FiltersPageUi
from infrastructure.objects.objects_ui.interfaceses.activity_logs_page_ui_interface import ActivityLogsPageInterface


class ActivityLogsPageUi(ActivityLogsPageInterface):
    def __init__(self, driver: WebDriver) -> None:
        self.__driver = driver
        self.__activity_log_page_url = F"{DataRep.cymulate_url}cym/activity_logs"

    # locators
        self.__filter_btn_ext = By.CSS_SELECTOR, "div[class*='FilterBar'] button[class*='cymulate-icon-button']"
        self.__assessment_id_ext = By.CSS_SELECTOR, "div[test-data-id='assessmentID']"

    def navigate_to_activity_log_page(self):
        self.__driver.get(self.__activity_log_page_url)
        return self

    def click_on_filter_btn(self) -> FiltersPageUi:
        DriverEX.force_click(driver=self.__driver, by=self.__filter_btn_ext)
        return FiltersPageUi(self.__driver)

    def print_assessment_ids_by_num_of_rows(self, num_of_rows: int):
        elements = DriverEX.search_elements(driver=self.__driver, by=self.__assessment_id_ext)

        for _ in range(5):  # Try up to 5 times
            if elements:
                break
            time.sleep(0.3)
            elements = DriverEX.search_elements(driver=self.__driver, by=self.__assessment_id_ext)

        for element in elements[:num_of_rows]:
            sys.stdout.write(element.text.strip() + "\n")

        return self

