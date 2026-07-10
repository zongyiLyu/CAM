import json
from scipy.stats import kendalltau
import numpy as np

def load_jsonl(file_path):
    """加载 JSONL 文件"""
    data = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            data.append(json.loads(line.strip()))
    return data

def get_rank_positions(rank_list):
    """将排名列表转换为位置字典"""
    return {item: idx for idx, item in enumerate(rank_list)}

def calculate_kendall_tau(list1, list2):
    """
    计算两个排名列表的 Kendall's Tau
    处理不同长度的列表，只考虑共同元素
    """
    # 获取共同元素
    common_items = set(list1) & set(list2)
    
    if len(common_items) < 2:
        return None
    
    # 获取位置映射
    pos1 = get_rank_positions(list1)
    pos2 = get_rank_positions(list2)
    
    # 提取共同元素的排名
    ranks1 = [pos1[item] for item in common_items]
    ranks2 = [pos2[item] for item in common_items]
    
    # 计算 Kendall's Tau
    tau, p_value = kendalltau(ranks1, ranks2)
    return tau

def calculate_top_k_kendall(list1, list2, k=5):
    """计算 Top-K 的 Kendall's Tau"""
    top_k_1 = list1[:k]
    top_k_2 = list2[:k]
    return calculate_kendall_tau(top_k_1, top_k_2)

def filter_rank_list(rank_list, features_to_remove):
    """从 rank_list 中删除指定的 feature"""
    return [item for item in rank_list if item not in features_to_remove]

def main():
    # 加载两个文件
    original_data = load_jsonl('./causal_analysis.jsonl')
    human_data = load_jsonl('./human_annotate.jsonl')
    
    # 创建映射以便比较相同的 setting
    original_dict = {(item['dataset'], item['model']): item['rank_list'] 
                     for item in original_data}
    human_dict = {(item['dataset'], item['model']): item['rank_list'] 
                  for item in human_data}

    # 过滤 rank_list 并处理长度不匹配
    # for key in original_dict:
    #     original_dict[key] = filter_rank_list(original_dict[key], features_to_remove)
    
    # for key in human_dict:
    #     human_dict[key] = filter_rank_list(human_dict[key], features_to_remove)
    
    # 处理长度不匹配：截取到较短的长度
    for key in original_dict:
        if key in human_dict:
            len1 = len(original_dict[key])
            len2 = len(human_dict[key])
            min_len = min(len1, len2)
            original_dict[key] = original_dict[key][:min_len]
            human_dict[key] = human_dict[key][:min_len]

    print("=" * 80)
    print("Kendall's Tau correlation")
    print("=" * 80)
    
    # 存储所有的相关性值
    all_full_taus = []
    print(f"{'Dataset':<15} {'Model':<20} {'Full List':<15}")
    print("-" * 80)
    
    for key in sorted(original_dict.keys()):
        if key in human_dict:
            dataset, model = key
            original_rank = original_dict[key]
            human_rank = human_dict[key]
            
            # 计算完整列表的 Kendall's Tau
            full_tau = calculate_kendall_tau(original_rank, human_rank)

            if full_tau is not None:
                all_full_taus.append(full_tau)
            
            full_tau_str = f"{full_tau:.4f}" if full_tau is not None else "N/A"
            
            print(f"{dataset:<15} {model:<20} {full_tau_str:<15}")
    
    print("-" * 80)

    if all_full_taus:
        mean_full = np.mean(all_full_taus)
        print(f"  Avg. Kendall's Tau: {mean_full:.4f}")
    
    print("-" * 80)
    print()



if __name__ == "__main__":
    main()