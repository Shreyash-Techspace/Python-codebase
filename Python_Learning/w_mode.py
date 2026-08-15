# w Mode - open the file for writing. Overwrites the file
# creates a new file if the file does not exist


fh = open("file1.txt", 'wt')
fh.write("This file is created using w mode in Python.\n")
fh.write("This is the first line.\n")
fh.write("This is the second line.\n")
fh.close()
