"""
Team Name: Slop Stoppers
Team Members:
- Joshua Fahlgren
- Mathew Rogers
"""

import random
import math
import sys
import os
from typing import List

sys.path.append(os.path.join(os.path.dirname(__file__), "MLForensics", "FAME-ML"))

import constants
import py_parser
import numpy as np
import statistics


def makeChunks(the_list, size_):
    for i in range(0, len(the_list), size_):
        yield the_list[i : i + size_]


def dumpContentIntoFile(strP, fileP):
    fileToWrite = open(fileP, "w")
    fileToWrite.write(strP)
    fileToWrite.close()
    return str(os.stat(fileP).st_size)


def getAllPythonFilesinRepo(path2dir):
    valid_list = []
    for root_, dirnames, filenames in os.walk(path2dir):
        for file_ in filenames:
            full_path_file = os.path.join(root_, file_)
            if os.path.exists(full_path_file):
                if file_.endswith(constants.PY_FILE_EXTENSION) and (
                    py_parser.checkIfParsablePython(full_path_file)
                ):
                    valid_list.append(full_path_file)
    valid_list = np.unique(valid_list)
    return valid_list


def Average(Mylist):
    return sum(Mylist) / len(Mylist)


def Median(Mylist):
    return statistics.median(Mylist)


def fuzzer():
    failure_count = 0
    error_messages = []

    for _ in range(100):
        try:
            test_list = random.choices(range(100), k=random.randint(0, 100))
            if random.choice([True, False]):
                test_list = []
            chunk_size = random.choice([1, 0, -1, 100, random.randint(1, 50)])
            list(makeChunks(test_list, chunk_size))
        except Exception as e:
            failure_count += 1
            error_msg = f"makeChunks failed with input {test_list}, {chunk_size}: {e}"
            error_messages.append(error_msg)
            print(error_msg)

    for _ in range(100):
        try:
            test_str = random.choice(
                [
                    "",
                    "".join(random.choices("abcdefghijklmnopqrstuvwxyz", k=1000)),
                    "".join(random.choices("!@#$%^&*()", k=random.randint(1, 100))),
                    "Test\nNew Line\n1234",
                ]
            )
            test_file = f"test_file_{random.randint(0, 1000)}.txt"
            dumpContentIntoFile(test_str, test_file)
            os.remove(test_file)
        except Exception as e:
            failure_count += 1
            error_msg = (
                f"dumpContentIntoFile failed with input {test_str}, {test_file}: {e}"
            )
            error_messages.append(error_msg)
            print(error_msg)

    for _ in range(100):
        try:
            test_dir = random.choice(
                [f"nonexistent_dir_{random.randint(0, 1000)}", ".", "/dev/null"]
            )
            getAllPythonFilesinRepo(test_dir)
        except Exception as e:
            failure_count += 1
            error_msg = f"getAllPythonFilesinRepo failed with input {test_dir}: {e}"
            error_messages.append(error_msg)
            print(error_msg)

    for _ in range(100):
        try:
            test_list = random.choice(
                [
                    [random.uniform(-1000, 1000) for _ in range(random.randint(1, 50))],
                    [0] * random.randint(1, 50),
                    [sys.float_info.max, -sys.float_info.max],
                    [random.uniform(1, 10)],
                ]
            )
            Average(test_list)
        except Exception as e:
            failure_count += 1
            error_msg = f"Average failed with input {test_list}: {e}"
            error_messages.append(error_msg)
            print(error_msg)

    for _ in range(100):
        try:
            test_list = random.choice(
                [
                    [random.uniform(-1000, 1000) for _ in range(random.randint(1, 50))],
                    [random.randint(1, 10)] * random.randint(1, 50),
                    [0],
                    [
                        random.randint(1, 10),
                        random.randint(1, 10),
                        random.randint(1, 10),
                    ],
                ]
            )
            Median(test_list)
        except Exception as e:
            failure_count += 1
            error_msg = f"Median failed with input {test_list}: {e}"
            error_messages.append(error_msg)
            print(error_msg)

    if failure_count > 0:
        print(f"Total failures: {failure_count}")
        with open("fuzz.log", "w") as log_file:
            log_file.write("\n".join(error_messages))


if __name__ == "__main__":
    fuzzer()
