from StringIO import StringIO
from mock import MagicMock
import unittest
import dodis
import os
import sys

class Test(unittest.TestCase):
  def setUp(self):
    self.file_path = os.path.dirname(os.path.realpath(__file__)) + "/test_list.md"
    self.test_file = open(self.file_path, "w")
    self.test_file.write("#TODO\n- rustle jimmies\n")
    self.test_file.close()

  def test_main(self):
    pass

  def test_read_file(self):
    output = StringIO()
    saved_stdout = sys.stdout
    sys.stdout = output

    dodis.read_file(self.file_path)

    actual = output.getvalue()
    self.assertEqual(actual, "\n#TODO\n\n  [0] - rustle jimmies\n\n")
    output.close()
    sys.stdout = saved_stdout

  def test_write_title(self):
    dodis.read_file = MagicMock()
    dodis.write_title(self.file_path, "test title")
    actual = open(self.file_path, "r").readline()
    dodis.read_file.assert_called_with(self.file_path)
    self.assertEqual(actual, " # test title\n")

  def test_write_item(self):
    dodis.write_item(self.file_path, "do the thing")
    actual = "".join(open(self.file_path, "r").readlines())
    self.assertEqual(actual, "#TODO\n- rustle jimmies\n- do the thing\n")
