from abc import ABC, abstractmethod


class ActivityLogsPageInterface(ABC):
    @abstractmethod
    def navigate_to_activity_log_page(self):
        pass

    @abstractmethod
    def click_on_filter_btn(self):
        pass

    @abstractmethod
    def print_assessment_ids_by_num_of_rows(self, num_of_rows):
        pass