# cs-olympics-tester
Simple script to test cs olympics solutions

## Usage
```bash
~$ ./tester.py --help
usage: tester.py [-h] [-p PROBLEM] [-a ARCHIVE] [-i INTERPRETER]
                 [-t TIME_LIMIT]
                 filename

positional arguments:
  filename              solution to be tested

optional arguments:
  -h, --help            show this help message and exit
  -p PROBLEM, --problem PROBLEM
                        problem ID
  -a ARCHIVE, --archive ARCHIVE
                        relative path to archive of problems
  -i INTERPRETER, --interpreter INTERPRETER
                        program interpreter. Default: guessed from file
                        extension
  -t TIME_LIMIT, --time-limit TIME_LIMIT
                        time limit for each test. Default: 1.0
```

## License
This script is distributed under MIT License. See LICENSE.md for more.

## TODO:
  - [ ] add compiled languages support