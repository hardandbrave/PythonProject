import json#不要忘记定义json
todos=[
       {"title":"学python","done":False},
       {"title":"写代码","done":True},
      ]
for t in todos:print(t["title"],t["done"])#索引是todos[t]所以要改为todos[t][title]而不是todos[title]
with open("todos.json","w",encoding="utf-8") as f:#encoding=“utf—8”为了防止中文乱码
    json.dump(todos,f,ensure_ascii=False,indent=4)#indent=4缩进4个单位更美观
    print("保存成功")
with open("todos.json","r",encoding="utf-8") as f:
    data=json.load(f)
    print(data)
for t in todos:print(t["title"],t["done"])