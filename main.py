def write_to_file(filename):
    try:
        with open(filename, 'w') as file:
            file.write("This is line 1\n")
            file.write("12345\n")
            file.write("Another line with some text and numbers: 9876\n")
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error occurred while writing to file: {e}")
    else:
        print("File created and written successfully.")

def read_from_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("Contents of my_file.txt:")
            print(content)
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error occurred while reading file: {e}")

def append_to_file(filename):
    try:
        with open(filename, 'a') as file:
            file.write("This is line 4, appended.\n")
            file.write("54321\n")
            file.write("Appending another line with some text and numbers: 1234\n")
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error occurred while appending to file: {e}")
    else:
        print("Content appended to file successfully.")

if __name__ == "__main__":
    filename = "my_file.txt"
    write_to_file(filename)
    read_from_file(filename)
    append_to_file(filename)
    read_from_file(filename)



