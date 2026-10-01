import json
import re

def process_jsonl(file_path):
    """
    读取JSONL文件，将test_list中的前两个测试用例添加到prompt中
    
    Args:
        file_path: JSONL文件路径
    """
    # 读取所有数据
    data_list = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            if line.strip():  # 跳过空行
                data_list.append(json.loads(line))
    
    # 处理每条数据
    for data in data_list:
        if 'test_list' in data and 'prompt' in data:
            # 获取前两个测试用例
            test_cases = data['test_list'][:2]
            
            # 移除assert语句，提取测试用例内容
            examples = []
            for test in test_cases:
                # 使用正则表达式移除assert语句
                # 匹配 assert function_name(...) == expected_result
                match = re.match(r'assert\s+(\w+)\((.*?)\)\s*==\s*(.+)', test)
                if match:
                    func_name = match.group(1)
                    args = match.group(2)
                    expected = match.group(3)
                    examples.append(f"{func_name}({args}) == {expected}")
            
            # 将测试用例添加到prompt中
            if examples:
                prompt = data['prompt']
                # 添加示例部分
                prompt += "\n\nExamples:\n"
                for example in examples:
                    prompt += f"- {example}\n"
                
                # 更新prompt
                data['prompt'] = prompt.rstrip()
    
    # 写回文件
    with open(file_path, 'w', encoding='utf-8') as f:
        for data in data_list:
            f.write(json.dumps(data, ensure_ascii=False) + '\n')
    
    print(f"处理完成！共处理 {len(data_list)} 条数据")
    print(f"结果已保存到: {file_path}")

# 使用示例
if __name__ == "__main__":
    # 替换为你的文件路径
    file_path = "/home/zlyuaj/Causal/MetaGPT/data/mbpp_sanitized_ET.jsonl"
    
    try:
        process_jsonl(file_path)
    except FileNotFoundError:
        print(f"错误: 找不到文件 '{file_path}'")
    except json.JSONDecodeError as e:
        print(f"错误: JSON解析失败 - {e}")
    except Exception as e:
        print(f"错误: {e}")