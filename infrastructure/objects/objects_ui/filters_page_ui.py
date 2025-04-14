from typing import TYPE_CHECKING

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

if TYPE_CHECKING:
    from infrastructure.objects.objects_ui.activity_logs_page_ui import ActivityLogsPageUi

from infrastructure.infra.dal.web_driver_extension.web_driver_extension import DriverEX
from infrastructure.infra.utils.enums.filter_type import FilterType
from infrastructure.objects.objects_ui.interfaceses.filters_page_ui_interface import FiltersPageUiInterface


class FiltersPageUi(FiltersPageUiInterface):
    def __init__(self, driver: WebDriver) -> None:
        self.__driver = driver
        self.__choose_filter = "//div[contains(@class,'StyledFiltersListItem') and .//span[text()='{name}']]"
        self.__filter_name = "button[test-id='{name}']"

    # locators
        self.__apply_filters_btn_ext = (By.CSS_SELECTOR, "button[test-id='apply-filters']")

    def click_on_filter_by_type(self, filter_type: FilterType):
        filter_type_ext = (By.XPATH, self.__choose_filter.format(name=filter_type.value))
        DriverEX.force_click(driver=self.__driver, by=filter_type_ext)
        return self

    def click_on_filter_by_name(self, filter_name: str):
        filter_name_ext = (By.CSS_SELECTOR, self.__filter_name.format(name=filter_name))
        DriverEX.force_click(driver=self.__driver, by=filter_name_ext)
        return self

    def click_on_apply_filters_btn(self)-> "ActivityLogsPageUi":
        from infrastructure.objects.objects_ui.activity_logs_page_ui import ActivityLogsPageUi
        DriverEX.force_click(driver=self.__driver, by=self.__apply_filters_btn_ext)
        return ActivityLogsPageUi(self.__driver)
