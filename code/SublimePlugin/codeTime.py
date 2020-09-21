import sublime_plugin
import time
import platform
import os
from datetime import datetime as dt
import threading
import sys

from .periodicLogSaver import PeriodicLogSaver

# create data folder based on OS
if platform.system() == 'Windows':
	DATA_FOLDER_PATH = os.path.join(os.getenv('APPDATA'), '.codeTime')
else:
	DATA_FOLDER_PATH = os.path.join(os.path.expanduser('~'), '.codeTime')

if not os.path.exists(DATA_FOLDER_PATH):
	os.makedirs(DATA_FOLDER_PATH)

# define log file path
LOG_FILE_PATH = os.path.join(DATA_FOLDER_PATH, '.sublime_logs')

# define local variables
file_times_dict = {}
periodic_log_save_timeout = 300 #seconds
periodic_log_save_on = True

# remove this function
def write_log_file(file_times_dict, file_path=LOG_FILE_PATH):

	f = open(file_path, 'a')

	for key, val in file_times_dict.items():
		curr_date = key
		file_dict = val

		for file_name, times_list in file_dict.items():
			for time_start_end in times_list:
				f.write(curr_date + ',' + file_name + ',' + str(time_start_end[0]) + ',' + str(time_start_end[1]) + '\n')  # noqa: E501

	f.close()

	return True


def when_activated(view):
	try:
		window = view.window()
		if window is not None:
			file_name = view.file_name()

			if file_name is not None:
				start_time = time.time()
				end_time = None

				curr_date = dt.now().strftime('%Y-%m-%d')

				if curr_date not in file_times_dict:
					file_times_dict[curr_date] = {}

				if file_name not in file_times_dict[curr_date]:
					file_times_dict[curr_date][file_name] = [[start_time, end_time]]  # noqa: E501
				else:
					file_times_dict[curr_date][file_name].append([start_time, end_time])  # noqa: E501

				print('File_name: ', file_name)
				print('\n ----- \n')
	except Excepion as e:
		exc_type, exc_obj, exc_tb = sys.exc_info()
		print("codeTime:when_activated(): %s on line number: %s", str(e), str(exc_tb.tb_lineno))


def when_deactivated(view):
	try:
		window = view.window()
		if window is not None:
			file_name = view.file_name()

			if file_name is not None:
				end_time = time.time()

				curr_date = dt.now().strftime('%Y-%m-%d')

				file_times_dict[curr_date][file_name][-1][1] = end_time

				print('File_name: ', file_name)
				print('\n ----- \n')
	except Excepion as e:
		exc_type, exc_obj, exc_tb = sys.exc_info()
		print("codeTime:when_deactivated(): %s on line number: %s", str(e), str(exc_tb.tb_lineno))



class CustomEventListener(sublime_plugin.EventListener):
	def on_post_save(self, view):
		print(view.file_name(), 'just got saved')

	def on_activated(self, view):
		try:
			print(view.file_name(), 'is now the active view')
			when_activated(view)
		except Excepion as e:
			exc_type, exc_obj, exc_tb = sys.exc_info()
			print("codeTime:CustomEventListener():on_activated() %s on line number: %s", str(e), str(exc_tb.tb_lineno))


	def on_deactivated(self, view):
		try:
			print(view.file_name(), 'is deactivated view')
			when_deactivated(view)
		except Excepion as e:
			exc_type, exc_obj, exc_tb = sys.exc_info()
			print("codeTime:CustomEventListener():on_deactivated() %s on line number: %s", str(e), str(exc_tb.tb_lineno))


	def on_close(self, view):
		try:
			print(view.file_name(), 'is no more')

			file_name = view.file_name()
			curr_date = dt.now().strftime('%Y-%m-%d')
			print(file_name)
			print(file_times_dict)
			if file_name is not None and file_name in file_times_dict[curr_date]:
				end_time = time.time()

				last_time_list = file_times_dict[curr_date][file_name][-1]

				if last_time_list[1] is None:
					last_time_list[1] = end_time

				with open(LOG_FILE_PATH, 'a') as f:
					f.write(curr_date + ',' + file_name + ',' + str(last_time_list[0]) + ',' + str(last_time_list[1]) + '\n')  # noqa: E501
		except Excepion as e:
			exc_type, exc_obj, exc_tb = sys.exc_info()
			print("codeTime:CustomEventListener():on_close() %s on line number: %s", str(e), str(exc_tb.tb_lineno))


# view.run_command('dashboard')
class DashboardCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		try:
			for key, val in file_times_dict.items():
				curr_date = key
				file_dict = val

				for file_name, times_list in file_dict.items():
					for time_start_end in times_list:
						print(curr_date + ' -||- ' + file_name + ' -||- ' + str(time_start_end[0]) + ' -||- ' + str(time_start_end[1]) + '\n')  # noqa: E501
		except Excepion as e:
			exc_type, exc_obj, exc_tb = sys.exc_info()
			print("codeTime:DashboardCommand():run() %s on line number: %s", str(e), str(exc_tb.tb_lineno))



def plugin_loaded():
	try:
		if periodic_log_save_on:
			periodcLogSaver = PeriodicLogSaver(kwargs={'inMemoryLog':file_times_dict, 'timeout':periodic_log_save_timeout, 'LOG_FILE_PATH': LOG_FILE_PATH})
			periodcLogSaver.start()
	except Excepion as e:
		exc_type, exc_obj, exc_tb = sys.exc_info()
		print("codeTime:plugin_loaded() %s on line number: %s", str(e), str(exc_tb.tb_lineno))
