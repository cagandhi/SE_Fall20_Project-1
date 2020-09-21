import sublime
import sys
import os

from datetime import datetime as dt
from unittest import TestCase
from unittest.mock import Mock, patch

version = sublime.version()
codeTime = sys.modules["SE_Fall20_Project-1.codeTime"]


class TestFunctions(TestCase):

	@patch('time.time', return_value=100)
	def test_when_activated(self, mock_time):
		view = Mock()
		view.filename.return_value = "sample.txt"
		datetime = Mock()
		codeTime.when_activated(view)
		view.window.assert_called_once()
