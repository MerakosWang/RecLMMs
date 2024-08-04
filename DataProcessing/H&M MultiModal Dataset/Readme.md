### HM 数据集处理流程

#### 用户交互数据生成

- **Gen_InteractionList.py**

  - 用于生成用户所有交互历史，按照时间顺序进行排序

    - **根据 transactions_train.csv 中记录的用户购买物品历史，生成交互数据，格式为：<user_id><item_id><item_ud>...<item_id>**

- **Interaction DataCleaning.py**

  - 对交互数小于 20 的用户进行剔除,保证每位用户具有更完备的购买特征
    - **对生成的交互 txt 文件进行二次处理**

- **Data Cutting.py**
  - 小样本数据集制作
    - 这里先制作 1000 位用户的多模态交互数据集
