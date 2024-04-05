def read_file(file_path):
    with open(file_path, 'r') as file:
        return set(file.readlines())

def write_to_file(file_path, lines):
    with open(file_path, 'w') as file:
        file.writelines(lines)

def compare_files(file1, file2, same_file, diff_file):
    # Read contents of both files
    file1_lines = read_file(file1)
    file2_lines = read_file(file2)

    # Find common lines
    common_lines = file1_lines.intersection(file2_lines)

    # Write common lines to 'same.txt'
    write_to_file(same_file, sorted(common_lines))

    # Find different lines
    different_lines = file1_lines.symmetric_difference(file2_lines)

    # Write different lines to 'diff.txt'
    write_to_file(diff_file, sorted(different_lines))

if __name__ == "__main__":
    file1_path = "file1.txt"
    file2_path = "file2.txt"
    same_file_path = "same.txt"
    diff_file_path = "diff.txt"

    compare_files(file1_path, file2_path, same_file_path, diff_file_path)
