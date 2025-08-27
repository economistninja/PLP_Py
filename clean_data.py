try:
    with open('input.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("Error: The file 'input.txt' was not found. Please create the file and try again.")
    exit()

cleaned_content = content.strip().upper()
word_count = len(cleaned_content.split())

with open('output.txt', 'w') as file:
    file.write(f"Word Count: {word_count}\n\n")
    file.write(cleaned_content)
print("Success! The cleaned data has been written to 'output.txt'.")