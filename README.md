TimeIt
======

This is a Python 3 script to which utilizes the POSIX `time` utility to over several runs to derive averages for `real`, `user`, and `sys` times. The output in seconds only. Minutes are converted to seconds when present.


Rational
--------

As part of my creation of <https://github.com/runeimp/hello> I wanted to include averaged values for multiple runs of

```bash
$ time ./hello_str
Hello, world!

real    0m0.003s
user    0m0.001s
sys     0m0.001s

$ time ./hello_arg 'Command Line'
Hello, Command Line!

real    0m0.003s
user    0m0.001s
sys     0m0.001s
```

This was fairly time consuming to do by hand once I got more than 5 languanges in the repo. Something may already exist but I couldn't find it so I created `timeit` to handle this for me.


Usage
-----

```bash
$ timeit "time ./hello_str" "time ./hello_arg 'Command Line'"

time time ./hello_str
   real:  |  user:  |  sys:
  0.00360 | 0.00100 | 0.00100

time time ./hello_arg 'Command Line'
   real:  |  user:  |  sys:
  0.00740 | 0.00200 | 0.00200
```

If you would like it to loop more or less then specify `-l #`, `--loop #`, or `/loop #` where `#` is the number of loops to make. Use `-h`, `--help`, or `/help` for more info.  O:-)


Installation
------------

This installation example assumes you have a directory off of your home directory named `repos`, a local `bin` directory that already exists in your `PATH` and you have already installed Python 3. Adjust appropriately if you have a different location for your cloned repositories or intend to link the script to another executable path.

Installing in the following fashion will allow for easy updating of the repo while maintaining an extensionless executable reference.


### Linux, UNIX, etc.

First install Python 3 if it's not already present. I recommend your local package manager `apt-get`, et. al. Or download and install manually from [ActivePython 3 from ActiveState][] or [Download Python for Other Platforms | Python.org][].

```bash
$ cd ~/repos
$ git clone git@github.com:runeimp/timeit.git
$ cd ~/bin
$ ln -s ../repos/timeit/timeit.py timeit
```


### macOS/Darwin

First you must install Python 3 via a package manager such as [Fink][], [Homebrew][], or [The MacPorts Project][]. Or download and install manually from [ActivePython 3 from ActiveState][] or [Python Releases for Mac OS X | Python.org][]. I use Homebrew personally.


#### Homebrew

```bash
$ brew update
...
$ brew install python3
...
```


#### Install

```bash
$ cd ~/repos
$ git clone git@github.com:runeimp/timeit.git
$ cd ~/bin
$ ln -s ../repos/timeit/timeit.py timeit
```


### Windows

Windows support needs to involve testing for the OS and use one of the recommendations from [batch file - How to measure execution time of command in windows command line? - Stack Overflow][] and other sources I've yet to investigate.


ToDo:
-----

* [ ] Add Windows support



[ActivePython 3 from ActiveState]: http://www.activestate.com/activepython-3
[batch file - How to measure execution time of command in windows command line? - Stack Overflow]: http://stackoverflow.com/questions/673523/how-to-measure-execution-time-of-command-in-windows-command-line
[Download Python for Other Platforms | Python.org]: https://www.python.org/download/other/
[Fink]: http://www.finkproject.org/
[Homebrew]: http://brew.sh/
[Python Releases for Mac OS X | Python.org]: https://www.python.org/downloads/mac-osx/
[Python Releases for Windows | Python.org]: https://www.python.org/downloads/windows/
[The MacPorts Project]: https://www.macports.org/
