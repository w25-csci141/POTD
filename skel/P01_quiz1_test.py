#POTD 1 test
import pytest
import subprocess
import sys
import re

basename = "P01_quiz1"


def test_quiz1():
    process = subprocess.Popen(
        [sys.executable, "P01_quiz1.py"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    #When prompted for input, enter newline
    stdout, stderr = process.communicate(input="\n")

    #define the pattern of the text string
    pattern = r"^What is \d+\s*\*\s*\d+"

    #verify that the input prompt matches the requirement
    assert re.match(pattern,stdout)

pytest.main(["P01_quiz1_test.py",  "-vv", "--showlocals", "-p", "no:faulthandler"])
