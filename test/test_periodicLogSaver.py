import sublime
import sys
import os

# from datetime import datetime as dt
from unittest import TestCase
from unittest.mock import patch

version = sublime.version()

periodicLogSaver = sys.modules["CodeTime.code.SublimePlugin.periodicLogSaver"]


def mock_requests_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    if args[0] == 'http://someurl.com/test.json':
        return MockResponse({"key1": "value1"}, 200)
    elif args[0] == 'http://someotherurl.com/anothertest.json':
        return MockResponse({"key2": "value2"}, 200)

    return MockResponse(None, 404)


class TestPeriodicLogSaver(TestCase):

    def test_write_log_file(self):
        BASE_PATH = os.path.join(os.path.expanduser('~'), '.codeTime')
        FILE_PATH = os.path.join(BASE_PATH, '.temp_logs')
        logger = periodicLogSaver.PeriodicLogSaver(kwargs={'LOG_FILE_PATH': FILE_PATH, 'API_TOKEN': 'abcdsedjk', 'REQUEST_URL': 'http://local/codetime'})
        try:
            d = {'2020-09-19': {'temp1.py': [[1000, 2000], [3000, 3200]]},
                 '2020-09-20': {'temp2.py': [[5000, 6000]]}}  # noqa: E128, E501

            with patch('urllib.request.urlopen') as mock_request:
                _ = logger.write_log_file(d)  # noqa: F841
                mock_request.return_value.status_code = 200
                arr = []
                for local_date, file_dict in d.items():
                    for filenm, times_arr in file_dict.items():
                        for ele in times_arr:
                            str1 = local_date + ',' + filenm + ',' + str(ele[0]) + ',' + str(ele[1]) + '\n'  # noqa: E501
                            arr.append(str1)

                with open(FILE_PATH, 'r') as f:
                    lines = f.readlines()
                    self.assertEqual(lines, arr)
        finally:
            os.remove(FILE_PATH)
