#!/usr/bin/env python
import optparse

def main():
  p = optparse.OptionParser()
  p.add_option("--title", "-t", default="")
  p.add_option("--item", "-i", default="")
  p.add_option("--delete", "-d", default="")
  options, arguments = p.parse_args()
  filename = 'newfile.md'

  if options.item:
    write_item(filename, options.item)
  elif options.title:
    write_title(filename, options.title)
  elif options.delete:
    delete_item(filename, options.delete)
  else:
    read_file(filename)

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

if __name__ == "__main__":
  main()
