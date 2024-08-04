### HM 数据集处理流程

| 用户数 | 商品数 | 交互数 |
| ------ | ------ | ------ |
| 1000   | 10683  | 20000  |

#### 用户交互数据生成

- **Gen_InteractionList.py**

  - 用于生成用户所有交互历史，按照时间顺序进行排序

    - **根据 transactions_train.csv 中记录的用户购买物品历史，生成交互数据，格式为：<user_id><item_id><item_ud>...<item_id>**

- **Interaction_DataCleaning.py**

  - 对交互数小于 20 的用户进行剔除,保证每位用户具有更完备的购买特征
    - **对生成的交互 txt 文件进行二次处理**

- **Data_Cutting.py**

  - 小样本数据集制作
    - 这里先制作 1000 位用户的多模态交互数据集

- **Interaction_Cutting.py**

  - 担心过多商品类目，LLM 无法记忆，先使每个用户只保留 20 个商品类目，18 个用于训练，第 19 用于验证，第 20 用于测试

- **Search_Customers.py**

  - 从 customers.csv 中找出那 1000 条用户 id 所在的用户属性信息

- **Articles_Retrieval_and_Removal.py**

  - 挑出所有商品 id，去重统计

- **Search Articles**
  - 从 articles.csv 中找到所有满足交互的商品 id
