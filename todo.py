#!/usr/bin/env python
import optparse
import os

def main():
  p = optparse.OptionParser()
  p.add_option("--file", "-f", default="TODO.md")
  p.add_option("--title", "-t", default="")
  p.add_option("--add", "-a", default="")
  p.add_option("--delete", "-d", default="")
  p.add_option("--reset", "-r", default="")
  options, arguments = p.parse_args()

  if not os.path.exists(options.file):
    open(options.file, "a+").close()


  if options.add:
    write_item(options.file, options.add)
  elif options.title:
    write_title(options.file, options.title)
  elif options.delete:
    delete_item(options.file, options.delete)
  elif options.reset:
    reset_list(options.file)
  else:
    read_file(options.file)

def read_file(filename):
  print
  file = open(filename, "r")
  i = 0
  print(file.readline())
  for line in file:
    print("  [{0}] {1}".format(i, line)),
    i = i + 1
  file.close()
  print

def write_title(filename, title):
  file = open(filename, "r+")
  file.readline()
  contents = file.read()
  file.close()

  file = open(filename, "w")
  file.write(" # %s\n" % title)
  file.write(contents)
  file.close()
  read_file(filename)

def write_item(filename, text):
  file = open(filename, "a")
  file.write("- %s\n" % text)
  file.close()
  read_file(filename)

def delete_item(filename, item_num):
  file = open(filename, "r")
  lines = file.readlines()
  file.close()

  file = open(filename, "w")
  i = -1
  for line in lines:
    if str(i) != item_num:
      file.write(line)
    i = i + 1
  file.close()
  read_file(filename)

def reset_list(filename):
  file = open(filename, "w")
  file.write("# TODO\n")
  file.close()
  read_file(filename)

if __name__ == "__main__":
  main()
