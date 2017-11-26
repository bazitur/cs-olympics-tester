#!/usr/bin/env python3

# Copyright (c) 2017 Basil Miturich
# distributed under MIT License, see LICENSE.md for the full license

from glob import glob
from subprocess import run, PIPE, TimeoutExpired
import argparse
from os.path import splitext, join as join_path, exists as path_exists
from os import getcwd
from warnings import warn
from sys import exit

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="solution to be tested")
    parser.add_argument("-p", "--problem", help="problem ID", default=None)
    parser.add_argument(
        "-a", "--archive",
        help="relative path to archive of problems",
        default="./"
    )
    parser.add_argument(
        "-i", "--interpreter",
        help="program interpreter. Default: guessed from file extension",
        default=None
    )
    parser.add_argument(
        "-t", "--time-limit",
        help="time limit for each test. Default: 1.0",
        default=1.0,
        type=float
    )
    args = parser.parse_args()
    path_to_archive = join_path(getcwd(), args.archive)
    path_to_problem = join_path(getcwd(), args.filename)
    if not path_exists(path_to_problem):
        print("Unable to find solution file.")
        return 1
    elif not path_exists(path_to_archive):
        print("Unable to find test folder.")
        return 1
    filename = args.filename
    if args.problem:
        problem_no = args.problem
    else:
        problem_no = splitext(filename)[0]

    if args.interpreter:
        prefix = args.interpreter
    else:
        file_format = splitext(filename)[1][1:]
        prefix = {
            "py": "python",
            "rb": "ruby"
        }.get(file_format)
        if prefix is None:
            warn("Unable to guess interpreter. Running without prefix...")
            prefix = ""
    problem_folder = join_path(path_to_archive, problem_no, "tests")
    tests = glob(join_path(problem_folder, "??"))
    answers = glob(join_path(problem_folder, "??.a"))
    if not tests:
        print("Unable to find tests in folder `{}`.".format(problem_folder))
        return 1
    cnt = 0
    for idx, (test, answer) in enumerate(zip(sorted(tests), sorted(answers))):
        with open(test) as test_file, open(answer) as answer_file:
            try:
                proc = run(
                    [prefix, path_to_problem],
                    input=str.encode(test_file.read()),
                    stdout=PIPE,
                    timeout=args.time_limit
                )
                result = proc.stdout.decode()
                if result.strip() == answer_file.read().strip():
                    print("#{:<2} OK".format(idx))
                    cnt += 1
                else:
                    print("#{:<2} ERROR".format(idx))
            except TimeoutExpired:
                print("#{:<2} TIMEOUT".format(idx))
    print("\nPassed {0} tests out of {1} ({2:.1f}%)".format(
        cnt, len(answers), cnt / len(answers) * 100
    ))


if __name__ == "__main__":
    exit(main())
