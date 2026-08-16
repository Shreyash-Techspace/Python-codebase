# incorrect file name , error in opening the file => FileNotFoundError: [Errno 2] No such file or directory: 'practie.txt'

fh = open("practice00.txt", 'rt')
content = fh.read()
fh.close()
print(content)

# mismatch the mode and operatons performs => io.UnsupportedOperation: not writable/readable
fh = open("practice.txt", 'rt')
fh.write("some content")
fh.close()
