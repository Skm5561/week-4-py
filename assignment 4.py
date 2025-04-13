def clean_log_file(content):
    # Remove all lines containing "DEBUG"
    lines = content.splitlines()
    cleaned_lines = [line for line in lines if "DEBUG" not in line]
    return "\n".join(cleaned_lines)

def process_log_file():
    try:
        filename = input("Enter the log file name to clean: ")

        with open(filename, "r") as infile:
            content = infile.read()

        cleaned_content = clean_log_file(content)

        output_filename = "cleaned_" + filename
        with open(output_filename, "w") as outfile:
            outfile.write(cleaned_content)

        print(f"✅ Cleaned log saved as '{output_filename}'")

    except FileNotFoundError:
        print("❌ File not found. Please check the filename.")
    except IOError:
        print("❌ Unable to read or write the file.")
    except Exception as e:
        print(f"⚠️ Something unexpected went wrong: {e}")

# Run the log cleaner
process_log_file()
