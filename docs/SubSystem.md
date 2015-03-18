学生子系统
-----

**base_url=**`/news`

### 获得用户课表

`POST /timetable`

#### Parameters

name|description
:--:|:---:
userid | 用户名
psw    |  密码

**Response**

课表返回顺序是课表矩阵按行排列顺序
```json
[
    {
        "teacher": "",
        "address": "",
        "name": "",
        "day": 1,
        "time": 1
    },
     .....

    {
        "teacher": "尚小华",
        "address": "北主楼402",
        "name": "马克思主义基本原理",
        "day": 3, //周几 （周1-7）
        "time": 4  //第几节课时(共5)
    },
      ....... //有可能同一课时有多节课 如:
    {
        "teacher": "吕永超",
        "address": "北主楼805",
        "name": "毛泽东思想和中国特色社会主义理论体系概论(2)",
        "day": 1,
        "time": 5
    },
    {
        "teacher": "尚小华",
        "address": "北主楼801",
        "name": "科技伦理简论",
        "day": 1,
        "time": 5
    },

    .....
]
```


### 获取用户的成绩列表

`GET /score`

#### Parameters

name|description
:--:|:---:
userid | 用户名
psw    |  密码

**Return**

```json
[
    {
        "score_list": [
             ........
            {
                "remark": "", //备注
                "name": "体育（1）",//名称
                "score": "92",//成绩
                "xuefen": "1",// 学分
                "type": "必修",// 课程类型
                "id": "1500011"// 课程代号
            }
            ......
        ],
        "year": 1  //第几个学年
    },
    .......
]

```
