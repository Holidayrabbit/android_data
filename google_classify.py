# 导入必要的库
from google_play_scraper import app  # 用于从Google Play获取应用信息的库
import json  # 用于处理JSON数据
from tqdm import tqdm  # 用于显示进度条
from collections import Counter  # 用于计数
import os  # 用于操作文件系统
import re  # 用于正则表达式处理

# 读取良性应用数据集
with open(r"D:\lab-projects\piggyback\code\data\bengin_data_per10_uk.json") as f:
    bengin_data = json.load(f)  # 加载包含良性应用SHA256哈希值的JSON文件

# 读取应用元数据集
with open(r"D:\lab-projects\piggyback\code\data\apg-meta_new.json") as f:
    dataset = json.load(f)  # 加载包含应用详细信息的JSON文件

# 设置输出文件路径
json_name = r"D:\lab-projects\piggyback\code\data\category.json"

# 初始化结果列表
json_list = []

# 遍历所有良性应用
for sha in tqdm(bengin_data):  # 使用tqdm显示进度条
    # 在元数据集中查找匹配的SHA256哈希值
    item = [element for element in dataset if 'sha256' in element and element['sha256'] == sha]
    
    # 如果找到匹配项并且包含包名信息
    if 'pkg_name' in item[0]:
        app_id = item[0]['pkg_name']  # 获取应用的包名
        try:
            # 使用google_play_scraper获取应用信息
            app_info = app(app_id)
            
            # 创建包含SHA256、应用名称和分类的字典
            json_data = {
                "sha256": str(sha),  # 应用的SHA256哈希值
                "App Name": str(app_info['title']),  # 应用名称
                "category": str(app_info['genre'])  # 应用分类
            }
            
            # 将结果添加到列表中
            json_list.append(json_data)
        except Exception as e:
            # 如果获取应用信息失败，则跳过该应用
            pass

# 打印成功获取分类信息的应用数量
print(len(json_list))

# 将结果保存为JSON文件
with open(json_name, 'w') as file:
    json.dump(json_list, file, indent=4)  # 使用4个空格缩进格式化JSON