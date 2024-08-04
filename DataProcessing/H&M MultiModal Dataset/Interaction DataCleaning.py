# 对交互数小于20的用户进行剔除

from tqdm import tqdm

# 定义输入和输出文件路径
input_txt = 'user_purchases.txt'
output_txt = 'filtered_user_purchases.txt'


filtered_data = []

with open(input_txt, 'r') as infile:
    lines = infile.readlines()
    for line in tqdm(lines, desc="Filtering"):
        parts = line.strip().split()
        customer_id = parts[0]
        article_ids = parts[1:]
        if len(article_ids) >= 20:
            filtered_data.append(line)


with open(output_txt, 'w') as outfile:
    for line in tqdm(filtered_data, desc="Writing"):
        outfile.write(line)

print(f"过滤后的用户购买记录已成功写入到 {output_txt} 文件中。")
