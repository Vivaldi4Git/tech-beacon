---
layout: post
title: "预训练数据获取流程"
date: 2025-05-31
categories: [AI, LLM]
tags: [预训练, 数据准备]
---


![预训练数据获取流程](/images/ai-learning/how-to-get-pretraining-data.png)

## 数据从哪里来?

目前主要有两种方式:

1. **自己去采集**
    - 比如 [OpenAI](https://platform.openai.com/docs/bots)、[Anthropic](https://darkvisitors.com/agents/claudebot) 这样的大公司,都有自己的数据采集团队
    - 他们会写程序去互联网上收集各种文章、网页

2. **用现成的数据库**
   - 最有名的是 CommonCrawl(简称 CC)
   - 这是一个公益组织,从2007年开始就在收集网页
   - 每隔1-2个月,他们就会发布新收集的数据
   - 最新一次(2024年4月)收集了27亿个网页

## 具体怎么收集数据?

这个过程分为两大阶段:

### 第一阶段：收集原始数据

就拿 CommonCrawl 来说,他们是这样工作的:

1. **写一个网络爬虫程序**
   - 先找一些知名网站作为起点
   - 程序会自动点击页面上的链接
   - 通过链接发现更多的网页
   - 就像蜘蛛结网一样,慢慢把网页都收集起来

### 第二阶段：筛选有用的内容

1. **筛选有用的网站(URL Filtering)**
   - 并不是所有网站都适合用来训练AI
   - 要把垃圾网站、广告站都过滤掉
   - 要把带病毒的、违法的网站都剔除
   - 用一个黑名单来记录这些不要的网站域名

2. **提取网页文本(Text Extraction)**
   - 网页里面除了文章内容,还有很多其他东西
   - 比如导航栏、广告、按钮等等
   - 我们要把真正有用的文本内容提取出来
   - 就像从一本书里面把正文内容摘出来一样

3. **语言过滤(Language Filtering)**
   - 用语言检测器判断每个网页是什么语言
   - 按照需要保留特定语言的内容
   - 比如 Fine-web 只保留英语占比超过 65% 的网页
   - 不同公司有不同的语言选择策略:
     - 有的公司只要英语内容
     - 有的公司希望模型能懂多种语言
     - 比如删掉所有西班牙语内容,模型就学不会西班牙语

4. **去重和隐私保护(Deduplication & PII Removal)**
   - 去重：删除重复出现的内容
     - 网络上有很多复制粘贴的内容
     - 重复内容会影响模型的训练效果
   - 隐私保护：删除个人信息
     - 比如地址、社保号等个人信息
     - 保护用户隐私

这样经过层层过滤,我们最终得到了质量较高的训练数据。

相关资源：
- [HuggingFace Fine-web](https://huggingface.co/spaces/HuggingFaceFW/blogpost-fineweb-v1)
- [Common Crawl](https://commoncrawl.org/)