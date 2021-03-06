# Do Dis
## A command line todo list in python

Do Dis is an extremely simple todo list manager for the commanline.

## Installation

1. Clone this repo `git clone https://github.com/patmood/dodis.git`
2. Simply run `python dodis.py` to get started
3. For regular use and fast execution, add an alias in your shell profile (eg `~/.bashrc` for bash, or `~/.config/fish/config.fish` for fish shell). Add the line:

`alias do="python ~/path/to/dodis/dodis.py"`

This allows you to quickly add items from anywhere by running `do`

## Usage

### Add and item

```
$ do Buy milk

# TODO

  [0] - Buy milk

```

### Remove an item

```
$ do -d 0

# TODO

```

### Change the title

```
$ do -t DO THESE THINGS:

# DO THESE THINGS

  [0] - Buy milk

```

### Use a custom list file

The default list file is `TODO.md` located in the same directory as the script. You can use a custom list and switch between them using the `-f` option.

`$ do -f mylist.md`

### Reset a list

`$ do -r TODO.md`

### Options

Usage:

`python dodis.py [options]`

Options:

```
-h, --help        show all options
-t, --title       change the list title
-d, --delete      delete a list item
-r, --reset       reset a list
```

## Credit

Dodis was inspired by Steve Tosh's "t" http://stevelosh.com/projects/t/. An awesome project that I wanted to attempt myself while learning python.
