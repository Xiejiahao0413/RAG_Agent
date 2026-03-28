import json

d = {
    "name":"小米",
    "age":11,
    "gender":"男"
}
print(str(d)) #{'name': '小米', 'age': 11, 'gender': '男'}
s = json.dumps(d)  #{"name": "\u5c0f\u7c73", "age": 11, "gender": "\u7537"}
s1 = json.dumps(d,ensure_ascii=False)     #{"name": "小米", "age": 11, "gender": "男"}
print(s)
print(s1)   

l= [
    {
        "name":"周杰轮",
        "age": 11,
        "gender":"男"
    },
    {
        "name":"蔡依临",
        "age": 12,
        "gender": "k"
    },
    {
        "name":"小明",
        "age": 16,
        "gender":"男"
    }
]

print(json.dumps(l,ensure_ascii=False))  
#[{"name": "周杰轮", "age": 11, "gender": "男"}, {"name": "蔡依临", "age": 12, "gender": "k"}, {"name": "小明", "age": 16, "gender": "男"}]

json_str = '{"name": "周杰轮", "age": 11,"gender": "男"}'
json_arrary_str = '[{"name": "周杰轮", "age": 11, "gender": "男"}, {"name": "蔡依临", "age": 12, "gender": "k"}, {"name": "小明", "age": 16, "gender": "男"}]'

s3 = json.loads(json_str)
print(s3,type(s3))    #import json

d = {
    "name":"小米",
    "age":11,
    "gender":"男"
}
print(str(d)) #{'name': '小米', 'age': 11, 'gender': '男'}
s = json.dumps(d)  #{"name": "\u5c0f\u7c73", "age": 11, "gender": "\u7537"}
s1 = json.dumps(d,ensure_ascii=False)     #{"name": "小米", "age": 11, "gender": "男"}
print(s)
print(s1)   

l= [
    {
        "name":"周杰轮",
        "age": 11,
        "gender":"男"
    },
    {
        "name":"蔡依临",
        "age": 12,
        "gender": "k"
    },
    {
        "name":"小明",
        "age": 16,
        "gender":"男"
    }
]

print(json.dumps(l,ensure_ascii=False))  
#[{"name": "周杰轮", "age": 11, "gender": "男"}, {"name": "蔡依临", "age": 12, "gender": "k"}, {"name": "小明", "age": 16, "gender": "男"}]

json_str = '{"name": "周杰轮", "age": 11,"gender": "男"}'
json_arrary_str = '[{"name": "周杰轮", "age": 11, "gender": "男"}, {"name": "蔡依临", "age": 12, "gender": "k"}, {"name": "小明", "age": 16, "gender": "男"}]'

s3 = json.loads(json_str)
print(s3,type(s3))  #{'name': '周杰轮', 'age': 11, 'gender': '男'} <class 'dict'>

res_list = json.loads(json_arrary_str)
print(res_list,type(res_list))  
#[{'name': '周杰轮', 'age': 11, 'gender': '男'}, {'name': '蔡依临', 'age': 12, 'gender': 'k'}, {'name': '小明', 'age': 16, 'gender': '男'}] <class 'list'>
