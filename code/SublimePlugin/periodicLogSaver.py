import threading
import time
import copy
import sublime
from datetime import datetime as dt


class PeriodicLogSaver(threading.Thread):

	def __init__(self, group=None, target=None, name=None,
				 args=(), kwargs=None, verbose=None):
		super(PeriodicLogSaver,self).__init__(group=group, target=target,name=name)
		self.args = args
		self.kwargs = kwargs
		return

	def run(self):
		while True:
			
			curr_file = sublime.active_window().active_view().file_name()
			curr_date = dt.now().strftime('%Y-%m-%d')
			inMemoryLogDeepCopy=copy.deepcopy(self.kwargs['inMemoryLog'])
			inMemoryLog=self.kwargs['inMemoryLog']
			inMemoryLog.clear()

			self.write_log_file(inMemoryLogDeepCopy)
			time.sleep(self.kwargs['timeout'])

	def write_log_file(self, file_times_dict):

		f = open(self.kwargs['LOG_FILE_PATH'], 'a')

		for key, val in file_times_dict.items():
			curr_date = key
			file_dict = val

			for file_name, times_list in file_dict.items():
				for time_start_end in times_list:
					f.write(curr_date + ',' + file_name + ',' + str(time_start_end[0]) + ',' + str(time_start_end[1]) + '\n')  # noqa: E501

		f.close()

		return True