import json

with open("output.txt", "r") as text_file, open("output.json", "w") as json_file:
    data = text_file.readlines()
    # Process the text data into a JSON-compatible format (e.g., list of dictionaries)
    json_data = [...]  # Replace with your processing logic
    json.dump(json_data, json_file, indent=4)
