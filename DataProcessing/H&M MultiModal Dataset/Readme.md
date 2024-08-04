### HM 数据集处理流程

#### 用户交互数据生成

- **Gen_InteractionList.py**

  - 用于生成用户所有交互历史，按照时间顺序进行排序

- **根据 transactions_train.csv 中记录的用户购买物品历史，生成交互数据，格式为：<user_id><item_id><item_ud>...<item_id>**
