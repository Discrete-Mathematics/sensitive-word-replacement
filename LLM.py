from openai import OpenAI

def AI(api_key,base_url,model):
    # 初始化大模型服务
    client = OpenAI(
        api_key = api_key,
        base_url = base_url
    )

    prompt = '''
    # 评论内容审核指令

    ## 任务描述
    对用户提交的评论内容进行合规性评估，判断其是否适合在中国境内网络平台发布

    ## 评估维度
    1. **政治敏感性**
    - 是否包含不当政治表述
    - 是否涉及敏感政治人物/事件

    2. **宗教文化适配**
    - 是否含有宗教歧视内容
    - 是否符合社会主义核心价值观

    3. **法律合规性**
    - 是否违反网络安全法
    - 是否包含违法信息

    4. **社会文化规范**
    - 是否存在地域/民族歧视
    - 是否使用侮辱性语言
    - 是否包含低俗内容

    ## 替换规则
    将所有识别到的敏感词中的每个字替换为星号（*），例如“密码”会被替换为“**”,除此之外不做任何修改。  

    ## 保持语法

    在替换完成后，请确保文本的语法结构和上下文仍然通顺，不影响阅读体验。  

    ## 完全替换
    所有敏感词必须完全替换，不得遗漏。  

    ## 自动化处理
    无需手动干预，全部过程需要自动完成。 

    ## 兼容性
    适用于所有类型的文本内容，包括但不限于聊天对话、文章、评论等。  

    ## 用法示例1
    输入:"我今天打了人"
    输出:"我今天***"

    ## 用法示例2
    输入:"我喜欢你"
    输出:"我喜欢你"
    '''

    user_input=input("请输入需要替换敏感词的文本：")

    # 定义消息列表
    messages = [
        {
            "role": "system",
            "content": prompt
        },
        {
            "role": "user",
            "content": user_input  # 问问题。可以改改试试
        },
    ]

    # 调用大模型
    chat_completion = client.chat.completions.create(
        model=model,
        messages=messages,
    )

    # 输出回复
    print(f"替换结果为：{chat_completion.choices[0].message.content}")