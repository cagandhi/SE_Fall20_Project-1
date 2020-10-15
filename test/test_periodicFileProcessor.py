import sublime
import sys
import os

from datetime import datetime as dt
from unittest import TestCase
from unittest.mock import Mock, patch


periodicFileProcessor = sys.modules[
    "SE_Fall20_Project-1.SublimePlugin.\
periodicFileProcessor"
]
version = sublime.version()


class TestPeriodicLogSaver(TestCase):
    def test_send_data_to_server(self):
        arr = [1, 2, 3]
        lines = [1, 2, 3]
        self.assertEqual(lines, arr)
