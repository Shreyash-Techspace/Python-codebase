# x mode => create a file

fh = open("file1.txt", 'xt')

# Writing into a file => write(content)
fh.write("This file is created using the 'x' mode in Python.\n")
fh.write("Next line.")

# Close the file
fh.close()
