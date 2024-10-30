from kazoo.client import KazooClient
'''
在zookeeper递归搜索某个目录下是否存在指定的字符串
'''
# 连接到 Zookeeper
zk = KazooClient(hosts='127.0.0.1:2181')
zk.start()

# 目标目录和要查找的字符串
target_path = "/my_directory"
search_string = "your_target_string"

# 递归搜索所有子节点
def search_in_znode(path):
    try:
        # 获取当前节点的值
        data, stat = zk.get(path)
        data_str = data.decode('utf-8')

        # 检查值是否包含目标字符串
        if search_string in data_str:
            print(f"Found in {path}: {data_str}")

        # 获取并遍历所有子节点
        children = zk.get_children(path)
        for child in children:
            child_path = f"{path}/{child}"
            search_in_znode(child_path)
    except Exception as e:
        print(f"Error accessing {path}: {e}")

# 开始搜索
search_in_znode(target_path)

# 关闭 Zookeeper 连接
zk.stop()
