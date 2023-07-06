import time

import allure
import pytest

from pages.widgets.page_data_picker import PageDatePicker


@allure.epic("Ui tests")
@allure.feature("Widgets")
@allure.link(name="Date Picker", url="https://demoqa.com/menu")
@allure.title("Тест поля для ввода даты")
# @pytest.mark.parametrize("date_time, ec", [("November 23 2009 16:20", "November 23, 2009 4:20 PM"),
#                                            ("15/03/2012/16:20", "November 23, 2009 4:20 PM"),
#                                            ("afafaaffaafafaffafaafaf", ""),
#                                            ("???????????????????????????????????????????????", "")])
def test_data_picker(get_driver):
    _steps = PageDatePicker(get_driver)
    _steps.transition()
    _steps.input_date_and_time("November 23 2009 16:20", "June 2, 2023 2:49 PM")
    _steps.input_date_and_time("15/03/2012/16:20", "June 2, 2023 2:49 PM")
    _steps.input_date_and_time("afafaaffaafafaffafaafaf", "")
    _steps.input_date_and_time("???????????????????????????????????????????????", "")
