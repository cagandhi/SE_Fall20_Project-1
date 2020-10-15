import threading
import time
import copy
import sublime
from datetime import datetime as dt
import sys


class PeriodicFileProcessor(threading.Thread):

    def __init__(self, group=None, target=None, name=None,
					args=(), kwargs=None, verbose=None):
		super(PeriodicFileProcessor, self).__init__(group=group, target=target, name=name)
		self.args = args
		self.kwargs = kwargs
		return

    def run(self):
		while True:
			try:
                #Add things here
				time.sleep(self.kwargs['timeout'])
			except Exception as e:
				exc_type, exc_obj, exc_tb = sys.exc_info()
				print("periodicLogSaver:PeriodicLogSaver:run(): {error} on line number: {lno}".format(error=str(e), lno=str(exc_tb.tb_lineno)))  # noqa: E501