# 对用户特征进行总结提炼
import csv


def summarize_customer_data(input_csv, output_txt):
    with open(input_csv, 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        with open(output_txt, 'w', encoding='utf-8') as txt_file:
            for row in csv_reader:
                customer_id = row['customer_id']
                fn = 'Subscribed' if row['FN'] == '1.0' else 'Not Subscribed'
                active = 'Active' if row['Active'] == '1.0' else 'Not Active'
                club_member_status = row['club_member_status']
                fashion_news_frequency = row['fashion_news_frequency']
                age = row['age']

                summary = (f"Customer ID: {customer_id}, Fashion News Subscription: {fn}, "
                           f"Active Status: {active}, Club Member Status: {club_member_status}, "
                           f"Fashion News Frequency: {fashion_news_frequency}, Age: {age} years.")

                txt_file.write(summary + '\n')


# 使用示例
input_csv = 'customers_1000.csv'  # 输入CSV文件路径
output_txt = 'customers_summary_1000.txt'  # 输出TXT文件路径

summarize_customer_data(input_csv, output_txt)
