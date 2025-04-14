from abc import ABC, abstractmethod
from typing import Self


class ILoginPageUi(ABC):

    @abstractmethod
    def set_user_name(self, user_name: str) -> Self:
        pass

    @abstractmethod
    def set_password(self, password: str) -> Self:
        pass

    @abstractmethod
    def click_on_sign_in_btn(self) -> Self:
        pass