import threading
import time
import copy
import sublime
from datetime import datetime as dt
import sys


class PeriodicLogSaver(threading.Thread):

	def __init__(self, group=None, target=None, name=None,
				 args=(), kwargs=None, verbose=None):
		super(PeriodicLogSaver,self).__init__(group=group, target=target,name=name)
		self.args = args
		self.kwargs = kwargs
		return

	def run(self):
		while True:
			try:
				curr_file = sublime.active_window().active_view().file_name()
				curr_date = dt.now().strftime('%Y-%m-%d')

				if curr_file is not None:
					inMemoryLogDeepCopy=copy.deepcopy(self.kwargs['inMemoryLog'])
					inMemoryLog=self.kwargs['inMemoryLog']
					inMemoryLog.clear()

					if curr_date in inMemoryLogDeepCopy and curr_file in inMemoryLogDeepCopy[curr_date]:
						end_time=time.time()
						inMemoryLogDeepCopy[curr_date][curr_file][-1][1]=end_time

						if curr_date not in inMemoryLog:
							inMemoryLog[curr_date] = {}

						if curr_file not in inMemoryLog[curr_date]:
							inMemoryLog[curr_date][curr_file] = [[end_time, None]]
						# else: # do we need this?
						# 	inMemoryLog[curr_date][curr_file].append([start_time, end_time])

						self.write_log_file(inMemoryLogDeepCopy)
				time.sleep(self.kwargs['timeout'])
			except Exception as e:
				exc_type, exc_obj, exc_tb = sys.exc_info()
				print("periodicLogSaver:PeriodicLogSaver:run(): %s on line number: %s", str(e), str(exc_tb.tb_lineno))

	def write_log_file(self, file_times_dict):
		try:
			f = None
			f = open(self.kwargs['LOG_FILE_PATH'], 'a')

			for key, val in file_times_dict.items():
				curr_date = key
				file_dict = val

				for file_name, times_list in file_dict.items():
					for time_start_end in times_list:
						f.write(curr_date + ',' + file_name + ',' + str(time_start_end[0]) + ',' + str(time_start_end[1]) + '\n')  # noqa: E501

			f.close()
		except Exception as e:
			if f:
				f.close()
			exc_type, exc_obj, exc_tb = sys.exc_info()
			print("periodicLogSaver:PeriodicLogSaver():write_log_file(): %s on line number: %s", str(e), str(exc_tb.tb_lineno))

		return True
