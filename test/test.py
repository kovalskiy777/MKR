import os
import pytest
from main import compare_files

@pytest.fixture
def setup_files():
    # Write contents to file1.txt
    with open("file1.txt", "w") as file:
        file.write("line1\n")
        file.write("line2\n")
        file.write("line3\n")

    # Write contents to file2.txt
    with open("file2.txt", "w") as file:
        file.write("line2\n")
        file.write("line3\n")
        file.write("line4\n")

    yield

    # Clean up files after tests
    os.remove("file1.txt")
    os.remove("file2.txt")
    os.remove("same.txt")
    os.remove("diff.txt")

def test_compare_files(setup_files):
    # Call function to compare files
    compare_files("file1.txt", "file2.txt", "same.txt", "diff.txt")

    # Read contents of same.txt
    with open("same.txt", "r") as file:
        same_content = file.readlines()

    # Read contents of diff.txt
    with open("diff.txt", "r") as file:
        diff_content = file.readlines()

    # Assert expected content in same.txt
    assert same_content == ["line2\n", "line3\n"]

    # Assert expected content in diff.txt
    assert diff_content == ["line1\n", "line4\n"]