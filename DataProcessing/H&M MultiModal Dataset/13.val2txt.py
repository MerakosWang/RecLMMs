import json

with open('HM_val_data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

if isinstance(data, list):
    with open('val.txt', 'w', encoding='utf-8') as file:
        for index, item in enumerate(data):
            if isinstance(item, dict):
                image_path = item.get('image', '')
                conversations = item.get('conversations', [])
                user_contents = []
                found_assistant = False

                for conversation in conversations:
                    if found_assistant:
                        break
                    if conversation['role'] == 'user':
                        # 去除<image>\n字段并替换换行符为\n
                        content = conversation['content'].replace('<image>\n', '').replace('\n', '\\n')
                        user_contents.append(content)
                    elif conversation['role'] == 'assistant':
                        found_assistant = True

                # 将所有内容拼接成一行
                content_text = '\\n'.join(user_contents)

                file.write(f'image: {image_path}\n')
                file.write(f'content: {content_text}\n\n')

else:
    print("JSON文件的根结构不是一个列表或字典。请检查文件格式。")
