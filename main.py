import banwords as b
import sys
import os
import time
import LLM

def mod1():
    os.system("cls")
    choice=int(input("请敏感词类型：\n1.广告敏感词\n2.枪爆敏感词\n3.新闻禁用词\n4.返回\n5.退出程序\n请输入选项："))
    if choice==4:
        main()
    elif choice==5:
        exit(0)
    prompt=input("请输入需要替换敏感词的文本：")
    char=input("请输入替换后的字符：")
    if choice==1:
        print(f"替换结果为：{b.nobantext(prompt,sys.path[0]+'\广告敏感词.txt',char)}")
    elif choice==2:
        print(f"替换结果为：{b.nobantext(prompt,sys.path[0]+'\枪爆敏感词.txt',char)}")
    elif choice==3:
        print(f"替换结果为：{b.nobantext(prompt,sys.path[0]+'\新闻禁用词.txt',char)}")
    time.sleep(5)

def mod2():
    os.system("cls")
    LLM.AI("sk-UlpCmmpivAj7IumVaDcuJc2NSnuapuSsxPw6Cmi1RsjXZrNc","https://api.moonshot.cn/v1","moonshot-v1-8k")
    choice=input("是否继续检测?[Y/n]")
    if choice=="Y":
        mod2()
    elif choice=="n":
        main()
    time.sleep(5)

def main():
    while 1:
        os.system("cls")
        choice=int(input("1.敏感词库检测\n2.大模型检测\n3.退出程序\n请输入选项："))
        if choice==1:
            while 1:
                mod1()
        elif choice==2:
            mod2()
        elif choice==3:
            exit(0)


if __name__ == '__main__': 
    main()