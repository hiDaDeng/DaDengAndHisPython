尽管已经有很多方法可用于关键字生成（例如，Rake、YAKE!、TF-IDF 等），但我想创建一个非常基本但功能强大的方法来提取关键字和关键短语。这就是 KeyBERT 的用武之地！它使用 **BERT 嵌入** 和 **简单余弦相似度** 来查找文档中与文档本身最相似的短语。

KeyBERT步骤

1. 首先使用 BERT 提取文档嵌入以获得**文档级向量表示**。
2. 随后，为 N-gram 词/短语提取**词向量**。
3. 然后，我们使用余弦相似度来找到与文档最相似的单词/短语。
4. 最后可以将最相似的词识别为最能描述整个文档的词。

<br>

## 安装


```python
!pip3 install keybert
```

<br>

## 初始化模型

KeyBERT库需要安装配置spacy语言模型

具体参考**公众号：大邓和他的Python** 2021-10-29 的推文 查看spacy配置方法


初始化模型


```python
from keybert import KeyBERT
import spacy
import jieba


zh_model = spacy.load("zh_core_web_sm")
bertModel = KeyBERT(model=zh_model)
```

<br>

## 准备数据

中文测试数据需要先分词，而后构造成类英文的语言结构(用空格间隔的文本)


```python
# 测试数据
doc =  """时值10月25日抗美援朝纪念日，《长津湖》片方发布了“纪念中国人民志愿军抗美援朝出国作战71周年特别短片”，再次向伟大的志愿军致敬！
　　电影《长津湖》全情全景地还原了71年前抗美援朝战场上那场史诗战役，志愿军奋不顾身的英勇精神令观众感叹：“岁月峥嵘英雄不灭，丹心铁骨军魂永存！”影片上映以来票房屡创新高，目前突破53亿元，暂列中国影史票房总榜第三名。
　　值得一提的是，这部影片的很多主创或有军人的血脉，或有当兵的经历，或者家人是军人。提起这些他们也充满自豪，影片总监制黄建新称：“当兵以后会有一种特别能坚持的劲儿。”饰演雷公的胡军透露：“我父亲曾经参加过抗美援朝，还得了一个三等功。”影片历史顾问王树增表示：“我当了五十多年的兵，我的老部队就是上甘岭上下来的，那些老兵都是我的偶像。”
　　“身先士卒卫华夏家国，血战无畏护山河无恙。”片中饰演七连连长伍千里的吴京感叹：“要永远记住这些先烈们，他们给我们带来今天的和平。感谢他们的付出，才让我们有今天的幸福生活。”饰演新兵伍万里的易烊千玺表示：“战争的残酷、碾压式的伤害，其实我们现在的年轻人几乎很难能体会到，希望大家看完电影后能明白，是那些先辈们的牺牲奉献，换来了我们的现在。”
　　影片对战争群像的恢弘呈现，对个体命运的深切关怀，令许多观众无法控制自己的眼泪，观众称：“当看到影片中的惊险战斗场面，看到英雄们壮怀激烈的拼杀，为国捐躯的英勇无畏和无悔付出，我明白了为什么说今天的幸福生活来之不易。”（记者 王金跃）
        """


doc = ' '.join(jieba.lcut(doc))


# 关键词提取
keywords = bertModel.extract_keywords(doc, 
                                      keyphrase_ngram_range=(1, 1),
                                      stop_words=None,
                                      top_n=10)
keywords
```




    [('铁骨', 0.5028),
     ('纪念日', 0.495),
     ('丹心', 0.4894),
     ('战役', 0.4869),
     ('影史', 0.473),
     ('父亲', 0.4576),
     ('票房', 0.4571),
     ('偶像', 0.4497),
     ('精神', 0.4436),
     ('家国', 0.4373)]


<br>

## 常用extract_keywords参数

**bertModel.extract_keywords(docs, keyphrase_ngram_range, stop_words, top_n)**

- **docs** 文档字符串（空格间隔词语的字符串）
- **keyphrase_ngram_range** 设置ngram，默认(1, 1)
- **stop_words** 停用词列表
- **top_n** 显示前n个关键词，默认5
- **highlight** 可视化标亮关键词，默认False
- use_maxsum: 默认False;是否使用Max Sum Similarity作为关键词提取标准，
- use_mmr: 默认False;是否使用Maximal Marginal Relevance (MMR) 作为关键词提取标准
- diversity 如果use_mmr=True，可以设置该参数。参数取值范围从0到1

<br>

对于**keyphrase_ngram_range**参数， 

- (1, 1) 只单个词， 如"抗美援朝", "纪念日"是孤立的两个词
- (2, 2) 考虑词组， 如出现有意义的词组 "抗美援朝 纪念日"
- (1, 2) 同时考虑以上两者情况


<br>

```python
# 关键词提取
keywords = bertModel.extract_keywords(doc, 
                                      keyphrase_ngram_range=(2, 2),
                                      stop_words=None,
                                      diversity=0.7, 
                                      top_n=10)
keywords
```




    [('影片 总监制', 0.5412),
     ('丹心 铁骨', 0.5339),
     ('抗美援朝 纪念日', 0.5295),
     ('长津湖 片方', 0.5252),
     ('志愿军 致敬', 0.5207),
     ('老兵 偶像', 0.5192),
     ('票房 创新', 0.5108),
     ('军人 血脉', 0.5084),
     ('家国 血战', 0.4946),
     ('家人 军人', 0.4885)]


<br>

```python
#可视化
keywords = bertModel.extract_keywords(doc, 
                                      keyphrase_ngram_range=(2, 2),
                                      stop_words=None,
                                      highlight=True,
                                      top_n=10)
```


<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">时值 10 月 25 日 <span style="color: #000000; text-decoration-color: #000000; background-color: #ffff00">抗美援朝 纪念日</span> 《 长津湖 》 片方 发布 了 “ 纪念 中国人民志愿军 抗美援朝 
出国 作战 71 周年 特别 短片 ” ， 再次 向 伟大 的 <span style="color: #000000; text-decoration-color: #000000; background-color: #ffff00">志愿军 致敬</span> 　 　 电影 《 长津湖 》 全情 
全景 地 还原 了 71 年前 抗美援朝 战场 上 那场 史诗 战役 ， 志愿军 奋不顾身 的 英勇 精神 令 
观众 感叹 ： “ 岁月峥嵘 英雄 不 灭 ， <span style="color: #000000; text-decoration-color: #000000; background-color: #ffff00">丹心 铁骨</span> 永存 ！ ” 影片 上映 以来 票房 屡 创新 高 ， 
目前 突破 53 亿元 ， 暂列 中国 影史 票房 总榜 第三名 。 　 　 值得一提的是 ， 这部 影片 的 
很多 主创 或 有 军人 的 血脉 ， 或 有 当兵 的 经历 ， 或者 家人 是 军人 。 提起 这些 他们 也 
充满 自豪 ， <span style="color: #000000; text-decoration-color: #000000; background-color: #ffff00">影片 总监制</span> 建新 称 ： “ 当兵 以后 会 有 一种 特别 能 坚持 的 劲儿 。 ” 饰演 
雷公 的 胡军 透露 ： “ 我 父亲 曾经 参加 过 抗美援朝 ， 还 得 了 一个 三等功 。 ” 影片 历史 
顾问 王树增 表示 ： “ 我 当 了 五十多年 的 兵 ， 我 的 老 部队 就是 上甘岭 上 下来 的 ， 那些
老兵 都 是 我 的 偶像 。 ” 　 　 “ 身先士卒 卫 华夏 家国 ， 血战 无畏 护 山河 无恙 。 ” 片中 
饰演 七 连连 长伍 千里 的 吴京 感叹 ： “ 要 永远 记住 这些 先烈 们 ， 他们 给 我们 带来 今天 
的 和平 。 感谢 他们 的 付出 ， 才 让 我们 有 今天 的 幸福生活 。 ” 饰演 新兵 伍 万里 的 易 
烊 千玺 表示 ： “ 战争 的 残酷 、 碾压 式 的 伤害 ， 其实 我们 现在 的 年轻人 几乎 很 难能 
体会 到 ， 希望 大家 看 完 电影 后能 明白 ， 是 那些 先辈 们 的 牺牲 奉献 ， 换来 了 我们 的 
现在 。 ” 　 　 影片 对 战争 群像 的 恢弘 呈现 ， 对 个体 命运 的 深切关怀 ， 令 许多 观众 
无法控制 自己 的 眼泪 ， 观众 称 ： “ 当 看到 影片 中 的 惊险 战斗 场面 ， 看到 英雄 们 
壮怀激烈 的 拼杀 ， 为国捐躯 的 英勇无畏 和 无悔 付出 ， 我 明白 了 为什么 说 今天 的 
幸福生活 来之不易 。 ” （ 记者 王金跃 ）
</pre>


<br>


```python
# 关键词提取
keywords = bertModel.extract_keywords(doc, 
                                      keyphrase_ngram_range=(2, 2),
                                      stop_words=None,
                                      use_mmr=True, diversity=0.05, 
                                      top_n=10)

keywords
```




    [('影片 总监制', 0.5412),
     ('长津湖 片方', 0.5252),
     ('抗美援朝 纪念日', 0.5295),
     ('丹心 铁骨', 0.5339),
     ('志愿军 致敬', 0.5207),
     ('老兵 偶像', 0.5192),
     ('票房 创新', 0.5108),
     ('军人 血脉', 0.5084),
     ('家国 血战', 0.4946),
     ('家人 军人', 0.4885)]


<br>

## 英文KeyBERT

同样需要配置spacy，参考**公众号：大邓和他的Python** 2021-10-29 的推文 查看spacy配置方法


```python
from keybert import KeyBERT
import spacy

en_model = spacy.load("en_core_web_sm")

doc = """
         Supervised learning is the machine learning task of learning a function that
         maps an input to an output based on example input-output pairs. It infers a
         function from labeled training data consisting of a set of training examples.
         In supervised learning, each example is a pair consisting of an input object
         (typically a vector) and a desired output value (also called the supervisory signal). 
         A supervised learning algorithm analyzes the training data and produces an inferred function, 
         which can be used for mapping new examples. An optimal scenario will allow for the 
         algorithm to correctly determine the class labels for unseen instances. This requires 
         the learning algorithm to generalize from the training data to unseen situations in a 
         'reasonable' way (see inductive bias).
      """
kw_model = KeyBERT()
keywords = kw_model.extract_keywords(doc, keyphrase_ngram_range=(1, 2))
keywords
```

Run

    [('supervised learning', 0.6779),
     ('supervised', 0.6676),
     ('signal supervised', 0.6152),
     ('examples supervised', 0.6112),
     ('labeled training', 0.6013)]
