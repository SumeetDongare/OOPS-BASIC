input_file = "input.txt"
output_file = "output.txt"
with open(input_file, "r") as file:
    lines = file.readlines()
line_count = len(lines)
print(f"Total number of lines: {line_count}")
first_two_lines = lines[:2]
with open(output_file, "w") as file:
    file.writelines(first_two_lines)
print(f"First {len(first_two_lines)} line(s) written to '{output_file}'.")
"""
Input.txt
Apple
Banana
Cherry
Orange
Mango
"""

"""
Output:-
Apple
Banana
"""