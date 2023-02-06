import requests

player_id = 10030
server_ip = "192.168.1.21:5000"

data = {"stuffList": []}
url = "http://{}/api/{}/stuff".format(server_ip, player_id)

data["stuffList"].append({"itemID": 1104000007, "number": 1000})  # itemID为1104000007的物品，数量1000
data["stuffList"].append({"itemID": 1104000008, "number": 1000})
data["stuffList"].append({"itemID": 1104000009, "number": 1000})
data["stuffList"].append({"itemID": 1104000010, "number": 1000})
data["stuffList"].append({"itemID": 1104000011, "number": 1000})
data["stuffList"].append({"itemID": 1104000012, "number": 1000})

requests.post(url, json=data, timeout=5)    # 添加道具
# requests.delete(url, json=data, timeout=5)   # 删除道具