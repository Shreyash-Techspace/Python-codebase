# 'a' mode => Append mode (add elements at the end)
# if the file does not exist , a mode create the file

fh = open("file1.txt", 'at')
fh.write("\nThis content has been written using 'a' mode.\n")
fh.write("'a' mode is used to add new content at the end of the file.\n")
fh.write("Good bye!")
fh.close()
