from datetime import datetime
#from py.xml import html

import pytest
from py._xmlgen import html


@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    cells.insert(2, html.th('Description'))
    cells.insert(1, html.th('Time', class_='sortable time', col='time'))
    cells.insert(3,html.th("Test_nodeid"))
    cells.pop(3)

@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    cells.insert(2, html.td(report.description))
    cells.insert(1, html.td(datetime.utcnow(), class_='col-time'))
    cells.insert(3,html.td(report.nodeid))
    cells.pop(3)

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    report.description = str(item.function.__doc__)
    #report.nodeid = report.nodeid.encode