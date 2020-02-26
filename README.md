# daoink API接口

## 一：获取手机验证码

* url:  `api/phone_verification_code/`
* 方法：`GET`

**请求：**

| 请求参数     | 类型   | 含义     |
| ------------ | ------ | -------- |
| phone_number | string | 手机号码 |

例子：

```
/api/phone_verification_code/?phone_number=17782813941
```

**响应：**

| 返回参数 | 类型          | 含义         |
| -------- | ------------- | ------------ |
| success  | true 或 false | 是否发送成功 |
| message  | string        | 提示信息     |

例子：

```
{
    "success": true,
    "message": "send msg success"
}
```



## 二:  注册

* url:  `api/register/`
* 方法：`POST`

**请求：**

| 请求参数     | 类型   | 含义          |
| ------------ | ------ | ------------- |
| phone_number | string | 手机号码      |
| verify_code  | string | 6位手机验证码 |
| password     | string | 密码          |

例子：

```
{
    'phone_number': '17712341234',
    'verify_code': '123456',
    'password': '123456'
}
```

**响应：**

| 请求参数 | 类型          | 含义            |
| -------- | ------------- | --------------- |
| success  | true 或 false | 是否注册成功    |
| token    | string        | 返回的Token令牌 |
| message  | dict          | 提示信息        |

例子：

```
{
    "success": false,
    "message": {
        "phone_number": [
            "手机号码格式错误"
        ],
        "verify_code": [
            "验证码错误"
        ]
    },
    "token": null
}
```



## 三：登录  

* urI:  `api/login/`
* 方法：`POST`

**请求：**

| 请求参数 | 类型   | 含义   |
| -------- | ------ | ------ |
| username | string | 用户名 |
| password | string | 密码   |

例子：

```
{
    'username': '17712341234',
    'password': '1234456'
}
```

**响应：**

| 返回参数 | 类型                | 含义         |
| -------- | ------------------- | ------------ |
| success  | 布尔值, true或false | 登录是否成功 |
| token    | string 或 null      | 登录令牌     |
| username | string 或 null      | 用户名       |
| user_id  | string 或 null      | 用户id       |

例子：

* 登录成功

```
{"success":false,"token":null,"username":null,"user_id":null}
```
* 登录失败 
```
{"success":true,"token":"8s2d95585b34a24520833ca7b45ba099338f15c8","username":"admin","user_id":1}
```

