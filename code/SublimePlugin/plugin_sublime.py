import sublime
import sublime_plugin

import time

file_times_dict = {}
file_ext_lang_mapping = {}


def when_activated(view):
	window = view.window()
	if window is not None:
		file_name = view.file_name()

		if file_name is not None:
			project = window.project_data()
			folders = window.folders()

			start_time = time.time()
			end_time = None

			if file_name not in file_times_dict:
				file_times_dict[file_name] = [[start_time, end_time]]
			else:
				file_times_dict[file_name].append([start_time, end_time])

			print("File_name: ", file_name)
			print("Project: ", project)
			print("Folders: ", folders)
			print("\n ----- \n")


def when_deactivated(view):
	window = view.window()
	if window is not None:
		file_name = view.file_name()

		if file_name is not None:
			end_time = time.time()
			file_times_dict[file_name][-1][1] = end_time


class CustomEventListener(sublime_plugin.EventListener):
	def on_load(self, view):
		print(view.file_name(), "just got loaded")

	def on_pre_save(self, view):
		print(view.file_name(), "is about to be saved")

	def on_post_save(self, view):
		print(view.file_name(), "just got saved")

	def on_new(self, view):
		print("new file")

	'''
	def on_modified(self, view):
		print("\n ----- \n")
		print(view.file_name(), "modified")
		when_activated(view)

	def on_modified_async(self, view):
		when_activated(view)
	'''

	def on_activated(self, view):
		print(view.file_name(), "is now the active view")
		when_activated(view)

	def on_deactivated(self, view):
		print(view.file_name(), "is deactivated view")
		when_deactivated(view)

	def on_close(self, view):
		print(view.file_name(), "is no more")
		f = open("/Users/miteshgandhi/Desktop/sublime_logs.txt", "a")
		f.write("Closing some file: " + str(view.file_name()) + " at time: " + str(time.time()) + "\n\n")  # noqa: E501
		f.close()


class ExampleCommand(sublime_plugin.TextCommand):
	def run(self, edit):

		print(file_times_dict)

		display_list = []

		for file_name, times_list in file_times_dict.items():
			sum_seconds = 0
			for time_start_end in times_list:
				sum_seconds += time_start_end[1] - time_start_end[0]

			display_list.append([file_name, sum_seconds])

		print(display_list)
