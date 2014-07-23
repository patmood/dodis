#!/usr/bin/env python
import optparse

def main():
  p = optparse.OptionParser()
  p.add_option('--title', '-t', default="")
  p.add_option('--item', '-i', default="")
  options, arguments = p.parse_args()
  filename = 'newfile.txt'

  if options.item:
    write_file(filename, options.item)
  elif options.title:
    write_title(filename, options.title)
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

def write_file(filename, text):
  file = open(filename, "a")
  file.write("- %s\n" % text)
  file.close()
  read_file(filename)

if __name__ == '__main__':
  main()
