# 将商品信息进行行总结
import csv

def summarize_item(row):
    return f"Article ID: {row['article_id']} - {row['prod_name']}, {row['product_type_name']}, " \
           f"{row['product_group_name']}, {row['graphical_appearance_name']} ({row['colour_group_name']})," \
           f" {row['perceived_colour_value_name']}, {row['department_name']}, {row['index_name']}," \
           f" {row['section_name']}, {row['detail_desc']}."

def convert_file(input_file, output_file):
    with open(input_file, mode='r', encoding='utf-8') as infile, open(output_file, mode='w', encoding='utf-8') as outfile:
        reader = csv.DictReader(infile)
        for row in reader:
            summary = summarize_item(row)
            outfile.write(summary + '\n')


input_file = 'articles_1000.csv'  # Replace with the path to your input file
output_file = 'articles_summary_1000.txt'  # Replace with the desired output file path
convert_file(input_file, output_file)
