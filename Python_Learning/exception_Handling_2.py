import io

try:
    fh = open("file10.txt", 'wt')
    fh.write("Hello World")
except FileNotFoundError as file_err:  # if user wants to see what error is happen and the message while exception
    print("File not found error")
    print(file_err)
except io.UnsupportedOperation as io_err:
    print(io_err)
else:  # else = will execute when there is no error in try block
    print("else block")
finally:  # finally => will execute in both the cases
    print("finally block")
    fh.close()
