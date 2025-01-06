
import os
from pathlib import Path

# Path.cwd()
#print(dir)
# print(__file__)

# py_file_location=os.path.dirname(os.path.realpath(__file__))

# print(py_file_location)
py_file_location=os.path.dirname(os.path.realpath(__file__))
csv_file_name="match_analysis.csv"
csv_file_name_and_path=os.path.join(py_file_location, csv_file_name)


print(py_file_location)
print(csv_file_name)
print(csv_file_name_and_path)