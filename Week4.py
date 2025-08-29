def modify_content(content):
    return content


def main():
    try:
        # Ask user for the input filename
        input_filename = input("Enter the name of the file to read: ").strip()

        # Try to open and read the file
        with open(input_filename, "r", encoding="utf-8") as infile:
            content = infile.read()

        # Modify the content
        modified_content = modify_content(content)

        # Create an output filename
        output_filename = "modified_" + input_filename

        # Write modified content to new file
        with open(output_filename, "w", encoding="utf-8") as outfile:
            outfile.write(modified_content)

        print(f"Modified file has been saved as: {output_filename}")

    except FileNotFoundError:
        print("Error: The file does not exist.")
    except PermissionError:
        print("Error: You don’t have permission to read this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()