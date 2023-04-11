import time

import allure
import pytest

from pages.widgets.page_data_picker import PageDatePicker


@allure.step("")
@pytest.mark.parametrize("date_time, ec", [("November 23 2009 16:20", "November 23, 2009 4:20 PM"),
                                           ("15/03/2012/16:20", "November 23, 2009 4:20 PM"),
                                           ("afafaaffaafafaffafaafaf", ""),
                                           ("???????????????????????????????????????????????", "")])
def test_data_picker(get_driver, date_time: str, ec: str):
    _steps = PageDatePicker(get_driver)
    _steps.step_1_transition()
    _steps.step_2_input_date_and_time(date_time, ec)
