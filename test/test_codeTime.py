import sublime
import sys
import os

from unittest import TestCase

version = sublime.version()
codeTime = sys.modules["SE_Fall20_Project-1.codeTime"]


class TestFunctions(TestCase):

	def test_write_log_file(self):

		try:
			d = {'2020-09-19': {'temp1.py': [[1000, 2000], [3000, 3200]]},
				'2020-09-20': {'temp2.py': [[5000, 6000]]}}  # noqa: E128, E501

			BASE_PATH = os.path.abspath(os.path.dirname(__file__))
			FILE_PATH = BASE_PATH + '/.temp_logs'

			_ = codeTime.write_log_file(d, FILE_PATH)

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


	def test_sample(self):
		pass
