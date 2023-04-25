from pages.page_base import BasePage


class PageDroppable(BasePage):
    def step_1_transition(self):
        self._all_transition("", "")

