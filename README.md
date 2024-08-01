# RecLMMs

**West Lake University Artificial Intelligence Summer Program G3_Project** :rocket:

#### 模型选择

**[MiniCPM-Llama3-v-2_5][1] 是 MiniCPM-V 系列的最新型号。该模型基于 SigLip-400M 和 Llama3-8B-Instruct 构建，共有 8B 参数。与 MiniCPM-V 2.0 相比，它表现出显着的性能改进。**

**优势：**

- 强大的 OCR 能力
- 指令追踪与复杂推理能力
- 多语言支持
- 易于使用和微调

![MiniCPM性能表现](https://cdn-uploads.huggingface.co/production/uploads/64abc4aa6cadc7aca585dddf/v2KE3wqQgM05ZW3dH2wbx.png)

[1]: (https://huggingface.co/openbmb/MiniCPM-Llama3-V-2_5)

#### 数据集

**选择[H&M 个性化时尚数据集][3]**

- **images** - 每一个 article_id 的商品所对应的图片

- **articles** - 每一个 article_id 对应的商品具体的 Metadata

- **customers** - 每一个 customer_id 对应的顾客具体的 Metadata

- **transactions_train** - 历史购买记录

[3]: https://www.kaggle.com/competitions/h-and-m-personalized-fashion-recommendations/overview

#### 模型部署与运行

- **环境配置**

  - pip install flash_attn
  - pip install transformers==4.37.2 gradio==4.16.0 accelerate==0.26.1

- **模型运行**
  - python hf.py --model_path=../autodl-tmp/MiniCPM-Llama3-V-2_5 --torch_dtype=float32

#### 参考

[PALR: Personalization Aware LLMs for Recommendation][2]

[2]: https://arxiv.org/abs/2305.07622
