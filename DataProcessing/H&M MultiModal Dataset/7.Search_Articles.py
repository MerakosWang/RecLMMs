import pandas as pd

# 读取CSV文件，并确保 article_id 列是字符串类型
csv_file = 'articles.csv'
articles_df = pd.read_csv(csv_file, dtype={'article_id': str})

# 读取TXT文件并获取物品ID
txt_file = 'Articles_List.txt'
with open(txt_file, 'r') as file:
    item_ids = file.read().split()
    item_ids = [id.strip() for id in item_ids]

# 打印调试信息
print("Sample article IDs from CSV:")
print(articles_df['article_id'].head(10))  # 打印前10个ID

print("Sample item IDs from TXT:")
print(item_ids[:10])  # 打印前10个ID

print("Checking for matches:")
print(articles_df['article_id'].isin(item_ids).head(10))  # 检查前10个ID是否匹配

# 过滤CSV数据
filtered_df = articles_df[articles_df['article_id'].isin(item_ids)]

# 查看过滤后的数据
print(f"Number of rows after filtering: {len(filtered_df)}")
print(filtered_df.head())  # 显示前几行过滤后的数据

# 输出到新的CSV文件
output_file = 'articles_1000.csv'
filtered_df.to_csv(output_file, index=False)

print(f"Filtered data has been saved to {output_file}")
