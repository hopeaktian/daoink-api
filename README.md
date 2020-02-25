# daoink API接口
## 一：登录  

* urI: `api/login/`
* 方法：POST

| 请求参数 | 类型   | 含义   |
| -------- | ------ | ------ |
| username | string | 用户名 |
| password | string | 密码   |

| 返回参数 | 类型                | 含义         |
| -------- | ------------------- | ------------ |
| success  | 布尔值, true或false | 登录是否成功 |
| token    | string 或 null      | 登录令牌     |
| username | string 或 null      | 用户名       |
| user_id  | string 或 null      | 用户id       |

