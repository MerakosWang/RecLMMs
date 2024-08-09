import json
import random


def read_item_ids(file_path):
    item_ids = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.strip().split()
            user_id = parts[0]
            items = parts[1:]
            item_ids[user_id] = items
    return item_ids


def format_image_path(image_id):
    if len(image_id) >= 3:
        return f"./images_128_128/{image_id[:3]}/{image_id}.jpg"
    else:
        return ""


def parse_txt(user_file, item_file):
    item_ids = read_item_ids(item_file)

    with open(user_file, 'r', encoding='utf-8') as file:
        data = file.read().strip()

    users_data = data.split('\n\n')
    parsed_data = []

    for idx, user_data in enumerate(users_data):
        user_dict = {}
        lines = user_data.split('\n')

        user_id = lines[0].split(': ')[1].strip()
        user_dict['id'] = str(idx)

        # Retrieve item IDs for the current user
        user_item_ids = item_ids.get(user_id, [])
        if len(user_item_ids) >= 20:
            image_id = user_item_ids[15]  # 16th item in 0-indexed list
            user_dict['image'] = format_image_path(image_id)
        else:
            user_dict['image'] = ""  # Default if less than 20 items

        user_features = ""
        purchase_history = []
        feature_flag = True

        for line in lines[1:]:
            line = line.strip()
            if line.startswith("Purchase History:"):
                feature_flag = False
                continue

            if feature_flag:
                user_features += line + " "
            else:
                if line:  # Ensure line is not empty
                    purchase_history.append(line.split('. ')[1].strip())

        user_features = user_features.strip()

        # Number the first 15 items of purchase history
        numbered_purchase_history = [f"{i + 1}. {item}" for i, item in enumerate(purchase_history[:15])]

        # Shuffle the last 5 items (recommendations)
        recommendations = purchase_history[15:20]
        shuffled_recommendations = recommendations[:]
        random.shuffle(shuffled_recommendations)
        numbered_recommendations = [f"{i + 1}. {item}" for i, item in enumerate(shuffled_recommendations)]

        # Determine the index of the first recommendation item in the shuffled recommendations list
        first_recommendation = recommendations[0]
        recommendation_index = shuffled_recommendations.index(first_recommendation) + 1

        conversations = [
            {
                "role": "user",
                "content": "Based on the user's characteristics and their recent purchase of 15 items, choose the most suitable item from the 5 candidate recommendations that the user is most likely to be interested in, and output the recommended item's ID."
            },
            {
                "role": "user",
                "content": f"User Features: {user_features}"
            },
            {
                "role": "user",
                "content": "Purchase History:\n" + "\n".join(numbered_purchase_history)
            },
            {
                "role": "user",
                "content": "From the 5 candidate recommendation items, choose the one that the user is most likely to purchase, and output only the index of that item："
            },
            {
                "role": "user",
                "content": "\n".join(numbered_recommendations)
            },
            {
                "role": "assistant",
                "content": str(recommendation_index)
            },
            {
                "role": "user",
                "content": f"<image>\nThe actual product purchased by the user:{recommendation_index}"
            }
        ]

        user_dict['conversations'] = conversations
        parsed_data.append(user_dict)

    return parsed_data


def save_json(parsed_data, output_path):
    with open(output_path, 'w', encoding='utf-8') as json_file:
        json.dump(parsed_data, json_file, indent=4, ensure_ascii=False)

# Update these file paths as needed
user_file = 'Interaction_1000.txt'
item_file = 'Regulation_1000.txt'
output_file = 'HM_Dataset_1000.json'

parsed_data = parse_txt(user_file, item_file)
save_json(parsed_data, output_file)
