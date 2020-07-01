"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"
import os


path_name = os.getcwd()
file_name = '/src/foo.txt'
full_path = path_name + file_name
with open(full_path) as f:
    read_data = f.read()
print(read_data)

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

path_name = os.getcwd()
file_name = '/src/bar.txt'
full_path = path_name + file_name
with open(full_path, 'w') as f:
    f.write('Hello world!\n')
    f.write('This is line 2\n')
    f.write('This is line 3')

with open(full_path) as f:
    read_data = f.read()
print(read_data)
