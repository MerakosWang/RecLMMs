import pandas as pd

# 读取txt文件中的用户ID（每行第一个字符串）
with open('Regulation_1000.txt', 'r') as f:
    user_ids = [line.split()[0] for line in f]

# 打印读取到的用户ID以进行调试
print("User IDs from txt file:", user_ids)

# 读取csv文件
df = pd.read_csv('customers.csv')

# 打印csv文件的列名以进行调试
print("CSV columns:", df.columns)

# 确保列名没有前后空格
df.columns = df.columns.str.strip()

# 去除csv文件中用户ID的前后空格
df['customer_id'] = df['customer_id'].str.strip()

# 过滤出在txt文件中的用户ID对应的记录
filtered_df = df[df['customer_id'].isin(user_ids)]

# 打印过滤后的数据框以进行调试
print("Filtered DataFrame:", filtered_df)

# 将结果保存到另一个csv文件
filtered_df.to_csv('customers_1000.csv', index=False)

print("Filtered data has been saved to 'filtered_data.csv'")
