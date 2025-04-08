def read_and_modify_file(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

        modified_lines = [line.upper() for line in lines]

        new_filename = "modified_" + filename
        with open(new_filename, 'w') as new_file:
            new_file.writelines(modified_lines)

        print(f"File has been successfully modified and saved as '{new_filename}'.")

    except FileNotFoundError:
        print(" Error: The file you entered does not exist.")
    except IOError:
        print(" Error: The file could not be read or written.")

user_filename = input("Enter the filename you want to read and modify: ")
read_and_modify_file(user_filename)