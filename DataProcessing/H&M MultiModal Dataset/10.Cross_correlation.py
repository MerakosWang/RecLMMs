import re

# 用户产品交互历史
def read_purchase_file(purchase_file):
    purchases = {}
    with open(purchase_file, 'r', encoding='utf-8', errors='ignore') as file:
        for line in file:
            parts = line.strip().split()
            user_id = parts[0]
            product_ids = parts[1:]
            purchases[user_id] = product_ids
    return purchases

# 用户特征读取
def read_user_features_file(user_features_file):
    user_features = {}
    with open(user_features_file, 'r', encoding='utf-8', errors='ignore') as file:
        for line in file:
            match = re.match(r'Customer ID: (.*?), Fashion News Subscription: (.*?), Active Status: (.*?), Club Member Status: (.*?), Fashion News Frequency: (.*?), Age: (.*?) years\.', line.strip())
            if match:
                user_id = match.group(1)
                features = {
                    'Fashion News Subscription': match.group(2),
                    'Active Status': match.group(3),
                    'Club Member Status': match.group(4),
                    'Fashion News Frequency': match.group(5),
                    'Age': match.group(6)
                }
                user_features[user_id] = features
    return user_features

# 产品特征
def read_product_features_file(product_features_file):
    product_features = {}
    with open(product_features_file, 'r', encoding='utf-8', errors='ignore') as file:
        for line in file:
            match = re.match(r'Article ID: (.*?) - (.*)', line.strip())
            if match:
                product_id = match.group(1)
                description = match.group(2)
                product_features[product_id] = description
    return product_features


def write_output(purchases, user_features, product_features, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        for user_id, product_ids in purchases.items():
            file.write(f'User ID: {user_id}\n')
            if user_id in user_features:
                features = user_features[user_id]
                file.write(
                    f'User Features: Fashion News Subscription: {features["Fashion News Subscription"]}, Active Status: {features["Active Status"]}, Club Member Status: {features["Club Member Status"]}, Fashion News Frequency: {features["Fashion News Frequency"]}, Age: {features["Age"]} years.\n')
            else:
                file.write('User Features: Information Missing\n')

            file.write('Purchase History:\n')
            for index, pid in enumerate(product_ids, start=1):
                description = product_features.get(pid, 'Unknown Product')
                file.write(f'{index}. {description}\n')
            file.write('\n')


# 文件路径
purchase_file = 'Regulation_1000.txt'
user_features_file = 'customers_summary_1000.txt'
product_features_file = 'articles_summary_1000.txt'
output_file = 'Interaction_1000.txt'

# 读取数据
purchases = read_purchase_file(purchase_file)
user_features = read_user_features_file(user_features_file)
product_features = read_product_features_file(product_features_file)

# 写入结果
write_output(purchases, user_features, product_features, output_file)
