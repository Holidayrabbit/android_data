import os
import ast
import shutil

def process_files():
    # 1. 合并train.txt和test.txt
    combined_data = []
    
    # 读取train.txt
    try:
        with open('train.txt', 'r') as f:
            train_content = f.read()
            train_data = ast.literal_eval(train_content)
            combined_data.extend(train_data)
    except FileNotFoundError:
        print("找不到train.txt文件")
        return
    
    # 读取test.txt
    try:
        with open('test.txt', 'r') as f:
            test_content = f.read()
            test_data = ast.literal_eval(test_content)
            combined_data.extend(test_data)
    except FileNotFoundError:
        print("找不到test.txt文件")
        return
    
    # 2. 修改路径格式并删除恶意样本
    new_data = []
    deleted_files = []
    
    for item in combined_data:
        old_path, label = item
        
        # 提取年份和文件名
        parts = old_path.split('\\')
        year = parts[-2]  # 年份
        filename = parts[-1]  # 文件名
        
        # 构建新路径
        new_path = f"../allapk/{year}/{year}/{filename}"
        new_data.append([new_path, label])
        
        # 3. 如果标签为1（恶意），删除对应的文件
        if label == 1:
            full_path = f"../allapk/{year}/{year}/{filename}.apk"
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    deleted_files.append(full_path)
                except Exception as e:
                    print(f"删除文件 {full_path} 时出错: {e}")
            else:
                print(f"警告: 文件不存在 {full_path}")
    
    # 将新数据写入合并后的文件
    with open('combined_data.txt', 'w') as f:
        f.write(str(new_data))
    
    print(f"处理完成。合并了 {len(combined_data)} 条数据，删除了 {len(deleted_files)} 个恶意样本文件。")
    print(f"新数据已保存到 combined_data.txt")

def format_combined_data():
    try:
        # 读取combined_data.txt
        with open('combined_data.txt', 'r') as f:
            content = f.read()
            data = ast.literal_eval(content)
        
        # 过滤掉标签为1的样本
        benign_data = [item for item in data if item[1] == 0]
        
        # 格式化输出，每个样本一行
        with open('combined_data.txt', 'w') as f:
            for item in benign_data:
                f.write(str(item) + '\n')
        
        print(f"格式化完成。保留了 {len(benign_data)} 个良性样本，删除了 {len(data) - len(benign_data)} 个恶意样本的路径。")
        print(f"新数据已保存到 combined_data.txt，每个样本占一行。")
    
    except Exception as e:
        print(f"格式化数据时出错: {e}")
    

if __name__ == "__main__":
    process_files()
    format_combined_data()
