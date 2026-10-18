

todos = []
while True:
    print("1.添加待办")
    print("2.查看待办")
    print("3.删除待办")
    print("4.退出")
    choice=input("请选择:")
    if choice=="1":
        item = input("请输入待办")
        todos.append(item)
        print("已添加",item)

    elif choice=="2":
            if len(todos)==0: #len(todos)表示todos的长度
             print("暂无待办")
            else:
             print("当前待办")
            for i in range(len(todos)):#表示i在todos长度中取值如果todos长度为2那么i依次取0，1，2
             print(i+1,".",todos[i])
    elif choice=="3":
        if len(todos)==0:
             print("没有可以删除的待办")
        else:
            for i in range(len(todos)):
             print(i+1,".",todos[i])
            num = input("请输入你要删除的编号:")
            if num.isdigit():
                 index = int(num) - 1
                 if 0 <= index < len(todos):
                     remove = todos.pop(index)
                     print("已删除",remove)
                 else:
                     print("不存在该条待办")
    elif choice=="4":
        print("已退出")
        break
    else:
        print("输入无效")




