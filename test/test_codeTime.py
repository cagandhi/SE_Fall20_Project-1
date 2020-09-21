import sublime
import sys
import os

from datetime import datetime as dt
from unittest import TestCase
from unittest.mock import Mock, patch

version = sublime.version()
codeTime = sys.modules["SE_Fall20_Project-1.codeTime"]


class TestFunctions(TestCase):

	def test_write_log_file(self):
		pass
