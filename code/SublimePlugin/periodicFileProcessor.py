import sys
import threading
import time
import requests
from datetime import datetime as dt


class PeriodicFileProcessor(threading.Thread):
    def __init__(
        self,
        group=None,
        target=None,
        name=None,
        args=(),
        kwargs=None,
        verbose=None,
    ):
        super(PeriodicFileProcessor, self).__init__(
            group=group, target=target, name=name
        )
        self.args = args
        self.kwargs = kwargs
        return

    def run(self):
        while True:
            try:
                self.send_data_to_server()
                time.sleep(self.kwargs["timeout"])
            except Exception as e:
                exc_type, exc_obj, exc_tb = sys.exc_info()
                line_no = str(exc_tb.tb_lineno)
                print(
                    "periodicLogSaver:PeriodicLogSaver:run(): {error} on line \
                    number: {lno}".format(
                        error=str(e), lno=line_no
                    )
                )

    def send_data_to_server(self):
        f = open(
            "/Users/prithvirajchaudhuri/Desktop/CSC510/"
            + "Project/CodeTime/demofile2.txt",
            "a",
        )
        api_token = "74815790-d740-4344-b9c3-a505514edf88VHSda13oJOr5Iba4"
        obj = [
            {
                "file_name": "test.java",
                "file_extension": "java",
                "detected_language": "java",
                "log_date": "2020-10-01",
                "log_timestamp": "160000290",
                "api_token": api_token,
            },
            {
                "file_name": "test.py",
                "file_extension": "py",
                "detected_language": "python",
                "log_date": "2020-10-01",
                "log_timestamp": "160000290",
                "api_token": api_token,
            },
        ]

        response = requests.post(
            "http://localhost:8000/codetime/timelog/", json=obj
        )

        f.write(response.json())
        f.close()
