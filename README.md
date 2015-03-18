ETips-api
---------

校园接口(非官方版)，用于解救水深火热的ETips

### 安装依赖

```shell
virtualenv env
source env/bin/activate
pip install -r requirements.txt
```

### 本地测试

```shell
gunicorn wsgi:app
```