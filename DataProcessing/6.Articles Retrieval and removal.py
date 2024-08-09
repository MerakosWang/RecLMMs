# 1000条数据商品id去重
def extract_unique_item_ids(input_file, output_file):
    unique_item_ids = set()

    # 读取文件并提取物品ID
    with open(input_file, 'r') as file:
        for line in file:
            parts = line.strip().split()
            item_ids = parts[1:]  # 排除第一个用户ID，只保留物品ID
            unique_item_ids.update(item_ids)

    # 将去重后的物品ID写入新的文件
    with open(output_file, 'w') as file:
        file.write(' '.join(sorted(unique_item_ids)))

    print(f'Unique item ID count: {len(unique_item_ids)}')


# 使用函数
input_file = 'Regulation_1000.txt'
output_file = 'Articles_List.txt'
extract_unique_item_ids(input_file, output_file)
