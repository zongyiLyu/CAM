import os
import json
from pathlib import Path
from typing import Dict, Any, Optional


def read_file_content(file_path: Path) -> Optional[str]:
    """读取文件内容，如果文件不存在则返回None"""
    try:
        if file_path.exists():
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read()
    except Exception as e:
        print(f"读取文件 {file_path} 时出错: {e}")
    return None


def read_json_file(file_path: Path) -> Optional[Dict]:
    """读取JSON文件内容"""
    try:
        if file_path.exists():
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
    except Exception as e:
        print(f"读取JSON文件 {file_path} 时出错: {e}")
    return None


def find_first_file_in_dir(directory: Path, extension: str = None) -> Optional[Path]:
    """在目录中查找第一个文件（可指定扩展名）"""
    try:
        if directory.exists() and directory.is_dir():
            files = list(directory.iterdir())
            if extension:
                files = [f for f in files if f.is_file() and f.suffix == extension]
            else:
                files = [f for f in files if f.is_file()]

            if files:
                return files[0]
    except Exception as e:
        print(f"查找文件时出错 {directory}: {e}")
    return None


def find_python_file_in_code_dir(base_dir: Path, folder_name: str) -> Optional[str]:
    """在 folder_name/folder_name 目录下查找Python文件"""
    code_dir = base_dir / folder_name
    if code_dir.exists() and code_dir.is_dir():
        # 查找所有Python文件
        py_files = list(code_dir.glob('*.py'))
        if py_files:
            # 优先返回main.py，否则返回第一个
            main_py = code_dir / 'main.py'
            if main_py.exists():
                return read_file_content(main_py)
            else:
                return read_file_content(py_files[0])
    return None


def process_folder(folder_path: Path) -> Dict[str, Any]:
    """处理单个文件夹，提取所需信息"""
    folder_name = folder_path.name
    result = {
        "file_name": folder_name,
        "requirements": None,
        "code": None,
        "prd": None,
        "system_design": None,
        "task": None
    }

    # 读取 requirements.txt
    requirements_file = folder_path / "requirements.txt"
    result["requirements"] = read_file_content(requirements_file)

    eval_res = folder_path / "eval_result.txt"
    eval_result = read_file_content(eval_res)

    if eval_result:
        result["eval_result"] = bool(read_file_content(eval_res)[:-1])
    else:
        result["eval_result"] = None

    # 读取代码文件（在 folder_name/folder_name 目录下）
    result["code"] = find_python_file_in_code_dir(folder_path, folder_name)

    # 读取 docs 目录下的 JSON 文件
    docs_dir = folder_path / "docs"

    # 读取 prd JSON
    prd_dir = docs_dir / "prd"
    if prd_dir.exists():
        prd_file = find_first_file_in_dir(prd_dir, '.json')
        if prd_file:
            result["prd"] = read_json_file(prd_file)

    # 读取 system_design JSON
    system_design_dir = docs_dir / "system_design"
    if system_design_dir.exists():
        sd_file = find_first_file_in_dir(system_design_dir, '.json')
        if sd_file:
            result["system_design"] = read_json_file(sd_file)

    # 读取 task JSON
    task_dir = docs_dir / "task"
    if task_dir.exists():
        task_file = find_first_file_in_dir(task_dir, '.json')
        if task_file:
            result["task"] = read_json_file(task_file)

    return result


def process_directory(root_dir: str, output_file: str = None):
    """处理指定目录下的所有文件夹并输出到JSONL文件"""
    root_path = Path(root_dir)

    if not root_path.exists():
        print(f"错误: 目录 {root_dir} 不存在")
        return

    # 如果没有指定输出文件名，使用目录名
    if output_file is None:
        output_file = f"{root_path.name}.jsonl"

    # 获取所有子文件夹
    folders = [f for f in root_path.iterdir() if f.is_dir()]

    print(f"找到 {len(folders)} 个文件夹")

    # 处理每个文件夹并写入JSONL文件
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for folder in folders:
            print(f"处理文件夹: {folder.name}")
            folder_data = process_folder(folder)

            # 写入JSONL格式（每行一个JSON对象）
            json_line = json.dumps(folder_data, ensure_ascii=False)
            outfile.write(json_line + '\n')

    print(f"处理完成！结果已保存到: {output_file}")


def find_workspace_directories(base_dir: str) -> list:
    """在指定目录下查找所有以workspace开头的文件夹"""
    base_path = Path(base_dir)
    
    if not base_path.exists():
        print(f"错误: 目录 {base_dir} 不存在")
        return []
    
    # 查找所有以workspace开头的文件夹
    workspace_dirs = [d for d in base_path.iterdir() 
                      if d.is_dir() and d.name.startswith('workspace')]
    
    return workspace_dirs


if __name__ == "__main__":
    # 使用示例
    # 指定基础目录路径
    base_directory = "."  # 修改为你的基础目录路径，默认为当前目录
    
    # 查找所有以workspace开头的文件夹
    workspace_dirs = find_workspace_directories(base_directory)
    
    if not workspace_dirs:
        print("未找到以'workspace'开头的文件夹")
    else:
        print(f"找到 {len(workspace_dirs)} 个workspace文件夹")
        
        # 处理每个workspace目录
        for workspace_dir in workspace_dirs:
            print(f"\n处理workspace目录: {workspace_dir.name}")
            process_directory(str(workspace_dir))