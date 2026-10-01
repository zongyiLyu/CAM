import os
import json
import re
from pathlib import Path
from collections import defaultdict

def extract_folder_info(folder_name):
    """
    从文件夹名提取setting和prune的feature个数
    例如: results-humaneval_gpt-4o-mini-ca_original_dataset_prune_5
    返回: (setting, prune_count)
    """
    # 使用正则表达式匹配最后的 _数字 模式
    match = re.match(r'(.+)_(\d+)$', folder_name)
    if match:
        prefix = match.group(1)  # xx部分
        prune_count = int(match.group(2))  # yy部分
        
        # 从prefix中提取setting
        # 假设格式为 results-{setting}_original_dataset_prune
        # 可以根据实际情况调整这个逻辑
        setting_match = re.search(r'results-(.+?)_original_dataset_prune', prefix)
        if setting_match:
            setting = setting_match.group(1)
        else:
            # 如果没有匹配到，使用整个prefix作为setting
            setting = prefix
        
        return setting, prune_count
    return None, None

def count_pass_results(jsonl_file):
    """
    统计JSONL文件中"pass_results": [true]的个数
    """
    count = 0
    try:
        with open(jsonl_file, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    data = json.loads(line)
                    # 检查是否有pass_results字段且值为[true]
                    if 'pass_results' in data:
                        if data['pass_results'] == [True] or data['pass_results'] == [True]:
                            count += 1
                    elif  'pass' in data:
                        if data['pass'] == True:
                            count += 1
                except json.JSONDecodeError:
                    continue
    except Exception as e:
        print(f"读取文件 {jsonl_file} 时出错: {e}")
    return count

def process_directory(root_dir):
    """
    处理指定目录下的所有文件夹
    """
    # 存储结果: {prune_count: total_pass_count}
    results = defaultdict(int)
    
    # 存储每个setting和prune_count的详细信息（用于调试）
    detailed_results = defaultdict(lambda: defaultdict(int))
    
    root_path = Path(root_dir)
    
    # 遍历所有子文件夹
    for folder in root_path.iterdir():
        if not folder.is_dir():
            continue
        
        folder_name = folder.name
        setting, prune_count = extract_folder_info(folder_name)
        
        if setting is None or prune_count is None:
            print(f"跳过文件夹 {folder_name}: 无法提取信息")
            continue
        
        print(f"处理文件夹: {folder_name} (setting: {setting}, prune_count: {prune_count})")
        
        # 遍历文件夹中的所有JSONL文件
        jsonl_files = list(folder.glob('**/*.jsonl'))
        
        if not jsonl_files:
            print(f"  警告: 未找到JSONL文件")
            continue
        
        folder_pass_count = 0
        for jsonl_file in jsonl_files:
            pass_count = count_pass_results(jsonl_file)
            folder_pass_count += pass_count
            print(f"  文件 {jsonl_file.name}: {pass_count} 个通过")
        
        # 累加到总结果
        results[prune_count] += folder_pass_count
        detailed_results[setting][prune_count] = folder_pass_count
        
        print(f"  总计: {folder_pass_count} 个通过\n")
    
    return results, detailed_results

def main():
    # 指定要处理的目录
    root_dir = '.'
    
    if not os.path.exists(root_dir):
        print(f"错误: 目录 {root_dir} 不存在")
        return
    
    print(f"\n开始处理目录: {root_dir}\n")
    print("=" * 60)
    
    # 处理目录
    results, detailed_results = process_directory(root_dir)
    
    # 为每个setting（xx）输出单独的JSON文件
    output_dir = 'prune_results'
    os.makedirs(output_dir, exist_ok=True)
    
    print("\n" + "=" * 60)
    print("统计结果:")
    print("=" * 60)
    
    for setting, prune_data in detailed_results.items():
        # 按prune_count排序
        sorted_prune_data = dict(sorted(prune_data.items()))
        
        # 生成输出文件名，使用setting作为文件名
        output_file = os.path.join(output_dir, f'{setting}_statistics.json')
        
        # 保存到JSON文件
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(sorted_prune_data, f, indent=2, ensure_ascii=False)
        
        print(f"\nSetting: {setting}")
        for prune_count, pass_count in sorted_prune_data.items():
            print(f"  Prune {prune_count} features: {pass_count} 个通过")
        print(f"  已保存到: {output_file}")
    
    # 同时保存一个汇总文件
    summary_file = os.path.join(output_dir, 'all_statistics_summary.json')
    summary_data = {
        'summary_by_prune_count': dict(sorted(results.items())),
        'by_setting': {k: dict(sorted(v.items())) for k, v in detailed_results.items()}
    }
    
    with open(summary_file, 'w', encoding='utf-8') as f:
        json.dump(summary_data, f, indent=2, ensure_ascii=False)
    
    print("\n" + "=" * 60)
    print(f"所有结果已保存到目录: {output_dir}/")
    print(f"- 每个setting有独立的JSON文件")
    print(f"- 汇总文件: {summary_file}")

if __name__ == '__main__':
    main()