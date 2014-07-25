import unittest
import dodis
import os

class Test(unittest.TestCase):
  def setUp(self):
    self.file_path = os.path.dirname(os.path.realpath(__file__)) + "/test_list.md"
    self.test_file = open(self.file_path, "w")
    self.test_file.close()

  def test_main(self):
    self.assertEqual(1,1)


  def test_read_file(self):
    pass

  def test_write_title(self):
    dodis.write_title(self.file_path, "test title")
    actual = open(self.file_path, "r").readline()
    self.assertEqual(actual, " # test title\n")

  def test_write_item(self):
    dodis.write_item(self.file_path, "do the thing")
    actual = open(self.file_path, "r").readline()
    self.assertEqual(actual, "- do the thing\n")
