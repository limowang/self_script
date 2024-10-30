import json
from kazoo.client import KazooClient

# 连接到 Zookeeper 服务器
zk = KazooClient(hosts='127.0.0.1:2181')
zk.start()

# Zookeeper 节点路径
node_path = "/sensors_analytics/backpack/skv/skv_offline/apps/363"

# 获取当前节点的数据
data, stat = zk.get(node_path)
data_str = data.decode('utf-8')  # 将字节数据解码为字符串

# 将字符串数据解析为 Python 字典
json_data = json.loads(data_str)

# 修改 app_status 字段
json_data["status"] = "AS_DROPPED"

# 将修改后的字典转回 JSON 字符串
new_data_str = json.dumps(json_data)

# 将新数据写回 Zookeeper
zk.set(node_path, new_data_str.encode('utf-8'))

print(f"Successfully updated {node_path} with new status: {json_data['status']}")

# 关闭 Zookeeper 连接
zk.stop()
