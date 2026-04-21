import requests

# 你的 QQ 号
qq = "3062616330"

# 三个免费项目
tasks = [
    {"tid": "4044", "name": "QQ名片赞"},
    {"tid": "4045", "name": "空间访客"},
    {"tid": "4046", "name": "空间说说赞"}
]

headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0",
    "Referer": "https://qq.gmw1.cn/"
}

for task in tasks:
    url = "https://qq.gmw1.cn/ajax.php"
    params = {
        "act": "gettool",
        "cid": "58",
        "tid": task["tid"],
        "input": qq  # 这里就是提交你的QQ号
    }

    try:
        res = requests.get(url, params=params, headers=headers, timeout=10)
        print(f"【{task['name']}】返回结果：")
        print(res.text)
        print("-" * 50)
    except Exception as e:
        print(f"{task['name']} 请求失败：{e}")