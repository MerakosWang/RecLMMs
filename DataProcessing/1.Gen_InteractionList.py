# 用于生成用户所有交互历史，按照时间顺序进行排序，采取留一策略

import csv
from collections import defaultdict
from tqdm import tqdm

# 输入和输出文件路径
input_csv = 'transactions_train.csv'
output_txt = 'user_purchases.txt'
user_purchases = defaultdict(list)

with open(input_csv, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    total_rows = sum(1 for row in reader)
    csvfile.seek(0)
    next(reader)

    for row in tqdm(reader, total=total_rows - 1, desc="Processing"):
        customer_id = row['customer_id']
        article_id = row['article_id']
        user_purchases[customer_id].append(article_id)


with open(output_txt, 'w') as txtfile:
    for customer_id, article_ids in user_purchases.items():
        line = f"{customer_id} " + " ".join(article_ids) + "\n"
        txtfile.write(line)

print(f"成功写入 {output_txt} 文件中。")
