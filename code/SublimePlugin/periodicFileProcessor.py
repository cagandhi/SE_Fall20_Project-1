import copy
import sys
import threading
import time
from datetime import datetime as dt

import sublime


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
        f.write("Now the file has more content!")
        f.close()
