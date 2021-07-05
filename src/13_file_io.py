"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE
import os 
data = os.path.abspath("C:/Users/loki/desktop/lambda/Intro-Python-I/src/foo.txt")
"C:/Users/loki/desktop/lambda/Intro-Python-I/src/foo.txt"
def reader():
  the_reader = open(data, 'r')
  print_contents = the_reader.read()
  print(print_contents)
  the_reader.close()

reader()
# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE

def writer():
  the_writer = open("bar.txt", "w")
  write_contents = the_writer.write("python is clean\r\n python is fast\r\n python is nice\r\n")
  the_writer.close()

new_data = os.path.abspath("C:/Users/loki/desktop/lambda/Intro-Python-I/bar.txt")
"C:/Users/loki/desktop/lambda/Intro-Python-I/src/bar.txt"

def new_reader():
  the_new_reader =  open(new_data, 'r')
  print_new_contents = the_new_reader.read()
  print(print_new_contents)
  the_new_reader.close()