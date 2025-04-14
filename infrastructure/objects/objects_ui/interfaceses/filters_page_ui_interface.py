from abc import abstractmethod, ABC


class FiltersPageUiInterface(ABC):
    @abstractmethod
    def click_on_filter_by_type(self, filter_type):
        pass

    @abstractmethod
    def click_on_filter_by_name(self, filter_name):
        pass

    @abstractmethod
    def click_on_apply_filters_btn(self):
        pass