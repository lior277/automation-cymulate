from infrastructure.infra.dal.data_reposetory.data_rep import DataRep
from infrastructure.infra.utils.enums.filter_type import FilterType
from infrastructure.objects.objects_ui.activity_logs_page_ui import ActivityLogsPageUi
from infrastructure.objects.objects_ui.login_page_ui import LoginPageUi
from tests.test_suit_Base import TestSuitBase

class TestPrintFirstThreeAssessmentIdsUi(TestSuitBase):
    @classmethod
    def setup_class(cls):
        # This runs once for the class
        cls.__driver = cls.get_driver()
        cls.__driver.get(f"{DataRep.cymulate_url}login")

        # Initialize page objects
        cls.login_page_ui = LoginPageUi(cls.__driver)

        # Perform login
        cls.login_page_ui \
            .set_user_name(DataRep.user_name) \
            .set_password(DataRep.password) \
            .click_on_sign_in_btn()

    @classmethod
    def teardown_class(cls):
        if cls.__driver:
            cls.driver_dispose(driver=cls.__driver)

    def test_print_first_three_assessment_ids_ui(self):
        activities_page = ActivityLogsPageUi(self.__driver)

        # filter page
        filters_page = activities_page \
            .navigate_to_activity_log_page() \
            .click_on_filter_btn()

        # choose the filter and get_assessment_ids
        filters_page \
            .click_on_filter_by_type(FilterType.TYPE) \
            .click_on_filter_by_name("advanced-scenarios") \
            .click_on_apply_filters_btn() \
            .print_assessment_ids_by_num_of_rows(3)



