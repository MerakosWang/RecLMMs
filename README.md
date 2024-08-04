# RecLMMs

**West Lake University Artificial Intelligence Summer Program G3_Project** :rocket:

---

#### 模型选择

**[MiniCPM-Llama3-v-2_5][1] 是 MiniCPM-V 系列的最新型号。该模型基于 SigLip-400M 和 Llama3-8B-Instruct 构建，共有 8B 参数。与 MiniCPM-V 2.0 相比，它表现出显着的性能改进。**

**优势：**

- 强大的 OCR 能力
- 指令追踪与复杂推理能力
- 多语言支持
- 易于使用和微调

![MiniCPM性能表现](https://cdn-uploads.huggingface.co/production/uploads/64abc4aa6cadc7aca585dddf/v2KE3wqQgM05ZW3dH2wbx.png)

[1]: (https://huggingface.co/openbmb/MiniCPM-Llama3-V-2_5)

---

#### 数据集

**选择[H&M 个性化时尚数据集][3]**

- **images** - 每一个 article_id 的商品所对应的图片

- **articles** - 每一个 article_id 对应的商品具体的 Metadata

- **customers** - 每一个 customer_id 对应的顾客具体的 Metadata

- **transactions_train** - 历史购买记录

**原始图像过大(34G),缩放 128x128[数据集地址][5]**

[5]: https://www.kaggle.com/datasets/odins0n/handm-dataset-128x128?select=images_128_128
[3]: https://www.kaggle.com/competitions/h-and-m-personalized-fashion-recommendations/overview

**Amazon 数据集**

- **[benchmark][7]**
- **[数据介绍页][6]**

[7]: https://paperswithcode.com/dataset/amazon-review
[6]: https://nijianmo.github.io/amazon/index.html

---

#### 模型部署与运行

- **环境配置**

  - Pillow==10.1.0
    torch==2.1.2
    torchvision==0.16.2
    transformers==4.40.0
    sentencepiece==0.1.99

  - pip install flash_attn
  - pip install transformers==4.37.2 gradio==4.16.0 accelerate==0.26.1

- **模型运行**
  - python hf.py --model_path=../autodl-tmp/MiniCPM-Llama3-V-2_5 --torch_dtype=float32
- **运行网络隧穿**
  - 端口暴露和链接详见[教程][4]

[4]: https://www.autodl.com/docs/ssh_proxy/

---

#### 参考

[PALR: Personalization Aware LLMs for Recommendation][2]

[2]: https://arxiv.org/abs/2305.07622

- 推荐系统
  - 基于大模型的推荐
    - LLM+Prompt
  - 大模型增强的推荐
  - 大模型幻觉
    - 推荐一个不存在的地点/商品/理论

#### H&M 数据集格式

- **images**

  - 目录下是商品的图片，不是每个商品都有图片的，子目录的名字是商品 id 的前 3 个数字

- **articles.csv**
  - 商品相关信息，包含如下 25 个字段

| 字段                         | 说明                                                                          |
| ---------------------------- | ----------------------------------------------------------------------------- |
| article_id                   | 物品 id，10 位数字字符，如 0108775015                                         |
| product_code                 | 产品 code，7 位数字字符，如 0108775，是 article_id 的前 7 位                  |
| prod_name                    | 产品名，如 Strap top（系带上衣）                                              |
| product_type_no              | 产品类型 no，2 位或者 3 位数字，有 -1 值                                      |
| product_type_name            | 产品类型名。如 Vest top（背心）                                               |
| product_group_name           | 产品组名称，如 Garment Upper body（服装上身）                                 |
| graphical_appearance_no      | 图案外观 no，如 1010016                                                       |
| graphical_appearance_name    | 图案外观名，如 Solid（固体;立体图形）                                         |
| colour_group_code            | 颜色组 code，如 09，2 位数字                                                  |
| colour_group_name            | 颜色组名称，如 Black                                                          |
| perceived_colour_value_id    | 感知颜色值 id，-1，1，2，3，4，5，6，7，一共这几个值。                        |
| perceived_colour_value_name  | 感知颜色值名称，如 Dark（黑暗的），Dusty Light 等                             |
| perceived_colour_master_id   | 感知颜色主 id，1 位或者 2 位数字                                              |
| perceived_colour_master_name | 感知颜色主名称，如 Beige（浅褐色的）                                          |
| department_no                | 部门 no，4 位数字                                                             |
| department_name              | 部门名称，如 Outdoor/Blazers DS                                               |
| index_code                   | 索引 code，单个大写字母，如 A G F D 等                                        |
| index_name                   | 索引名，如 Lingeries/Tights（内衣/紧身裤）                                    |
| index_group_no               | 索引组 no，1 位或者 2 位数字                                                  |
| index_group_name             | 索引组名称，如 Ladieswear（女装）                                             |
| section_no                   | 部门 no，2 位数字                                                             |
| section_name                 | 部门名称，如 Womens Everyday Basics（女性日常基础知识）                       |
| garment_group_no             | 服装组 no，4 位数字                                                           |
| garment_group_name           | 服装组名称，如 Jersey Basic（泽西岛基本款）                                   |
| detail_desc                  | 细节的文本描述，如 Jersey top with narrow shoulder straps（窄肩带的泽西上衣） |

- **customers.csv**
  - 用户相关信息，包含如下 7 个字段：

| 字段                   | 说明                                                                                           |
| ---------------------- | ---------------------------------------------------------------------------------------------- |
| customer_id            | 用户 id，字符串，如：00000dbacae5abe5e23885899a1fa44253a17956c6d1c3d25f88aa139fdfc657          |
| FN                     | 35%有值，值为 1，65% 缺失                                                                      |
| Active                 | 34%值为 1，66% 无值                                                                            |
| club_member_status     | 俱乐部成员状态，93% ACTIVE，7% PRE-CREATE（预先创建）                                          |
| fashion_news_frequency | 时尚新闻频率，64% NONE，35% Regularly（有规律地），1% 其它值                                   |
| age                    | 年龄，有缺失值，1%缺失                                                                         |
| postal_code            | 邮政代码，很长的字符串。例如，52043ee2162cf5aa7ee79974281641c6f11a68d276429a91f8ca0d4b6efa8100 |

- **transactions_train.csv**
  - 用户行为数据，包含如下 5 个字段：
    | 字段 | 说明 |
    |-------------------|----------------------------------------------------------|
    | t_dat | 时间，就是商品的购买时间。如 2019-09-18，只精确到日。 |
    | customer_id | 用户 id |
    | article_id | 商品 id |
    | price | 价格 |
    | sales_channel_id | 销售渠道 id，值只有 1、2 两个，应该是线上、线下两个 |
