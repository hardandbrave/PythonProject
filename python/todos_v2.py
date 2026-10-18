import json
import os


FILE="todos.json"

def load_todos():
    if not(os.path.exists(FILE)):
        return []
    with open (FILE,"r",encoding="utf-8") as f:
        return json.load(f)



def save_todos(todos):
    with open (FILE,"w",encoding="utf-8") as f:
        json.dump(todos,f,ensure_ascii=False,indent=4)



def show_todos(todos):
    if len(todos)==0:
      print("暂无待办")
      return
    for i in range(len(todos)):
     if todos[i]["done"]:
         status="√"
     else:
         status=""
     print(i+1,".",f"[{status}]",todos[i]["title"])



def add_todos(todos):
    title = input("请输入代办内容")
    todos.append({"title":title,"done":False})
    save_todos(todos)



def delect_todos(todos):
    if len(todos)==0:
        print("暂无待办")
        return
    show_todos(todos)
    num = input("请选择需要删除的序号：")
    if num.isdigit():
     index=int(num) - 1
     if index>=0 and index<len(todos):
       removed = todos.pop(index)
       save_todos(removed)
       print("已删除序号",removed["title"])
     else:
      print("序号不存在")
    else:
      print("请输入数字")




def toggle_todos(todos):
    if len(todos)==0:
     print("暂无待办")
     return
    show_todos(todos)
    num = input("请选择要切换的序号")
    if num.isdigit():
        index=int(num) - 1
        if index>=0 and index<len(todos):
            todos[index]["done"] = not todos[index]["done"]
            save_todos(todos)
            print("已更新")
        else:
         print("序号不存在")
    else:
        print("请输入数字")



def main():
 todos=load_todos()

 while True:
    print("\n-------待办清单-------")
    print("1.添加待办:")
    print("2.查看待办:")
    print("3.删除待办:")
    print("4.切换完成状态:")
    print("5.退出:")


    choice = input("请选择：")
    if choice == "1":
        add_todos(todos)
    elif choice == "2":
        show_todos(todos)
    elif choice == "3":
        delect_todos(todos)
    elif choice == "4":
        toggle_todos(todos)
    elif choice == "5":
        print("退出程序")
        break
    else:
        print("输入无效")


main()