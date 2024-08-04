# 单纯从大数据集中，剪切一部分数据

def copy_lines(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as infile:
            lines = infile.readlines()

        # 取前1000行
        first_1000_lines = lines[:1000]
        with open(output_file, 'w', encoding='utf-8') as outfile:
            outfile.writelines(first_1000_lines)

        print(f"前1000行数据已成功拷贝到 {output_file}")

    except Exception as e:
        print(f"发生错误: {e}")


input_file = 'filtered_user_purchases.txt'  # 输入文件的路径
output_file = 'filtered_user_purchases_1000.txt'  # 输出文件的路径
copy_lines(input_file, output_file)
