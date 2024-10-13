import os
import json

def list_files(startpath):
    """
    递归列出指定路径下的所有文件和文件夹，并返回一个字典表示的树形结构。
    
    :param startpath: 起始路径
    :return: 字典表示的树形结构
    """
    tree = {}
    for root, dirs, files in os.walk(startpath):
        relative_path = os.path.relpath(root, startpath)
        if relative_path == '.':
            relative_path = ''
        
        tree[relative_path] = {
            "dirs": [os.path.join(relative_path, d) for d in dirs],
            "files": [os.path.join(relative_path, f) for f in files]
        }
        
    return tree

def save_to_json(tree, output_file):
    """
    将树形结构保存到 JSON 文件中。
    
    :param tree: 字典表示的树形结构
    :param output_file: 输出文件路径
    """
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(tree, file, ensure_ascii=False, indent=4)

def main():
    # 指定需要扫描的文件夹路径
    folder_path = input("请输入文件夹路径: ")
    if not os.path.exists(folder_path):
        print("路径不存在，请检查后重新输入！")
        return
    
    # 指定输出文件路径
    output_file = input("请输入输出文件路径: ")
    
    print("\n正在生成文件目录...")
    tree = list_files(folder_path)
    
    save_to_json(tree, output_file)
    
    print(f"文件目录已成功保存到 {output_file}")

if __name__ == "__main__":
    main()