图书馆
----

### 检索图书

`GET /library/search/<string:keyword>/page/<int:page>`

#### Parameters

name|description
:--:|:---:
keyword | 关键字
page    |  页码

**Response**

```json
[
    {
        "press_time": "2015.1", # 出版时间
        "num": "1", # 序号
        "index_num": "TP312JA/H97ah",  # 索取号
        "name": "写给大忙人看的Java SE 8＝Java SE 8 for the really impatient",# 名称
        "author": "(美)Cay S. Horstmann著；张若飞译",# 作者
        "press": "电子工业出版社", # 出版社
        "total": "3", # 馆藏
        "ctrlno": "572952", # 图书馆系统控制号(在图书馆的唯一编号)
        "left": "2"  # 剩余
    },
    .......
]
```

### 查看图书借阅状态

`GET /library/book/<int:ctrlno>`

#### Parameters

name|description
:--:|:---:
ctrlno | 图书唯一编号

**Response**

```json
{
    "status_list": [
        {
            "status": "可供出借",    # 状态
            "login_num": "A1369744", # 登录号
            "volume": "",  # 卷期
            "index_num": "TP312JA/H97ah",# 索取号
            "location": "电工电子计算机馆",  # 馆藏地
            "year": "", # 年代
            "type": "普通图书"  # 借阅类型
        },
        {
            "status": "可供出借",
            "login_num": "A1369745",
            "volume": "",
            "index_num": "TP312JA/H97ah",
            "location": "电工电子计算机馆",
            "year": "",
            "type": "普通图书"
        }
    ],
    "isbn": "978-7-121-22728-8"
}
```