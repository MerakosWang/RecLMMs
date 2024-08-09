import json
import os

def main(json_file_path):
    with open(json_file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    for item in data:
        image_path = item.get("image", "")
        if not os.path.isfile(image_path):
            print(f"Image file does not exist: {image_path}")

if __name__ == "__main__":
    json_file_path = 'HM_train_data.json'  # Replace with your actual JSON file path
    main(json_file_path)
