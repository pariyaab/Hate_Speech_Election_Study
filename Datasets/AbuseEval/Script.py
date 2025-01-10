import csv


input_file_path = "keywords_offenseval_test.txt"
output_file_path = "keywords_offenseval_test.csv"

off_class_keywords = []
not_class_keywords = []

# Read the file
with open(input_file_path, "r") as file:
    lines = file.readlines()

# Process the lines to extract keywords
current_class = None
for line in lines:
    # Skip empty lines and headings
    if line.strip() == "OFF class - Top 50":
        current_class = "OFF"
    elif line.strip() == "NOT class - Top 50":
        current_class = "NOT"
    elif line.strip():
        # Split each line into word and value, we only care about the word (keyword)
        word, _ = line.split()

        # Append keywords based on the current class
        if current_class == "OFF":
            off_class_keywords.append(word)
        elif current_class == "NOT":
            not_class_keywords.append(word)

# Write keywords to CSV
with open(output_file_path, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Class", "Keyword"])  # Header row
    # Write the OFF class keywords
    for keyword in off_class_keywords:
        writer.writerow(["OFF", keyword])
    # Write the NOT class keywords
    for keyword in not_class_keywords:
        writer.writerow(["NOT", keyword])

# Confirm the CSV file has been created
print(f"Keywords have been saved to '{output_file_path}'.")
