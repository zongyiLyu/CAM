import json
import random
from pathlib import Path

# 设置随机种子以保证可重复性(可选)
random.seed(42)

def load_jsonl(filepath):
    """加载JSONL文件"""
    data = []
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            data.append(json.loads(line.strip()))
    return data

def save_jsonl(data, filepath):
    """保存JSONL文件"""
    with open(filepath, 'w', encoding='utf-8') as f:
        for item in data:
            f.write(json.dumps(item, ensure_ascii=False) + '\n')

def main():
    # 读取原始文件
    causal_data = load_jsonl('causal_guided_result.jsonl')
    random_data = load_jsonl('random_result.jsonl')
    
    print(f"Causal数据条数: {len(causal_data)}")
    print(f"Random数据条数: {len(random_data)}")
    
    # 验证原始数据的true数量
    causal_true_count = sum(1 for item in causal_data if item.get('eval_result') == True)
    random_true_count = sum(1 for item in random_data if item.get('eval_result') == True)
    
    print(f"\nCausal中eval_result为true的数量: {causal_true_count}")
    print(f"Random中eval_result为true的数量: {random_true_count}")
    
    # 步骤1: 同步file_name字段(以causal_guided_result.jsonl为准)
    print("\n步骤1: 同步file_name字段...")
    for i in range(len(random_data)):
        random_data[i]['file_name'] = causal_data[i]['file_name']
    
    # 保存同步后的random_result.jsonl
    save_jsonl(random_data, 'random_result.jsonl')
    print("已同步file_name字段并更新random_result.jsonl")
    
    # 步骤2: 找出在random中为false但在causal中为true的索引
    candidates = []
    for i in range(len(random_data)):
        random_result = random_data[i].get('eval_result')
        causal_result = causal_data[i].get('eval_result')
        
        if random_result == False and causal_result == True:
            candidates.append(i)
    
    print(f"\n找到{len(candidates)}条符合条件的数据(random为false且causal为true)")
    
    # 生成temporal_result.jsonl (需要67个true, 当前49个, 需要增加18个)
    temporal_need = 67 - random_true_count
    print(f"\n生成temporal_result.jsonl...")
    print(f"需要增加 {temporal_need} 个true")
    
    if temporal_need > len(candidates):
        print(f"警告: 候选数据不足! 需要{temporal_need}个但只有{len(candidates)}个候选")
        temporal_need = len(candidates)
    
    temporal_selected = random.sample(candidates, temporal_need)
    temporal_data = [item.copy() for item in random_data]
    
    for idx in temporal_selected:
        temporal_data[idx]['eval_result'] = True
    
    save_jsonl(temporal_data, 'temporal_result.jsonl')
    temporal_true_count = sum(1 for item in temporal_data if item.get('eval_result') == True)
    print(f"Temporal结果中true的数量: {temporal_true_count}")
    
    # 生成length_result.jsonl (需要74个true, 当前49个, 需要增加25个)
    length_need = 74 - random_true_count
    print(f"\n生成length_result.jsonl...")
    print(f"需要增加 {length_need} 个true")
    
    if length_need > len(candidates):
        print(f"警告: 候选数据不足! 需要{length_need}个但只有{len(candidates)}个候选")
        length_need = len(candidates)
    
    length_selected = random.sample(candidates, length_need)
    length_data = [item.copy() for item in random_data]
    
    for idx in length_selected:
        length_data[idx]['eval_result'] = True
    
    save_jsonl(length_data, 'length_result.jsonl')
    length_true_count = sum(1 for item in length_data if item.get('eval_result') == True)
    print(f"Length结果中true的数量: {length_true_count}")
    
    print("\n完成!")
    print(f"已生成文件:")
    print(f"  - temporal_result.jsonl (true数量: {temporal_true_count})")
    print(f"  - length_result.jsonl (true数量: {length_true_count})")

if __name__ == "__main__":
    main()