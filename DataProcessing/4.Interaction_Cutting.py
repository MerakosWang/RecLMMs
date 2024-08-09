#由于某些用户交互历史过于冗长，为了前期测试便捷，所有用户的交互信息只保留20条

def process_file(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as infile:
            lines = infile.readlines()

        processed_lines = []
        for line in lines:
            parts = line.strip().split(' ')
            user_id = parts[0]
            item_ids = parts[1:21]  # 取前20个物品id
            new_line = ' '.join([user_id] + item_ids)
            processed_lines.append(new_line)

        with open(output_file, 'w', encoding='utf-8') as outfile:
            for line in processed_lines:
                outfile.write(line + '\n')

        print(f"处理完成，结果已输出到 {output_file}")

    except Exception as e:
        print(f"发生错误: {e}")

# 示例用法
input_file = 'filtered_user_purchases_1000.txt'  # 输入文件的路径
output_file = 'Regulation_1000.txt'  # 输出文件的路径
process_file(input_file, output_file)
