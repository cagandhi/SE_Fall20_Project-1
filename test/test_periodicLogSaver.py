import sublime
import sys
import os

from datetime import datetime as dt
from unittest import TestCase
from unittest.mock import Mock, patch


periodicLoSaver = sys.modules["SE_Fall20_Project-1.SublimePlugin.periodicLogSaver"]
version = sublime.version()

class TestPeriodicLogSaver(TestCase):