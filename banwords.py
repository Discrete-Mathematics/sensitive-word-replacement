def has_banwords(text,path):#将text中的禁词返回为words
    banwords=getbanwords(path)
    words=[]
    for word in banwords:
        if word in text:
            words.append(word)
    return words

def getbanwords(path):#从banwords（路径）中读取禁词列表。
    f=open(path, mode='r', encoding='utf-8')
    lines=f.readlines()
    txtdata=[]
    for line in lines:
        line=line.strip('\n')
        line=line.strip(" ")
        txtdata.append(line)
    #print(txtdata)
    return txtdata

def replace_banword(banwords,text,char):#将出现在banwords里的text中的词替换为星号
    for word in banwords:
        if word in text:
            text=text.replace(word,char*len(word))
    return text

def nobantext(text,path,char):
    return replace_banword(has_banwords(text,path),text,char)
