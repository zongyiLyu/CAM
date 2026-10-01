import json

# 指定你的.jsonl文件路径
input_file = '/home/zlyuaj/Causal/MetaGPT/data/CodeContest_Test.jsonl'
output_file = '/home/zlyuaj/Causal/MetaGPT/data/CodeContest_Test_changed.jsonl'

# 用于存储处理后的数据
processed_data = []

# 读取.jsonl文件
with open(input_file, 'r', encoding='utf-8') as f:
    for task_id, line in enumerate(f):
        # 解析每一行的JSON数据
        data = json.loads(line)

        # 添加task_id
        data['task_id'] = task_id

        # 替换key名字
        if 'description' in data:
            data['prompt'] = data.pop('description')

        # 将处理后的数据加入列表
        processed_data.append(data)

# 将处理后的数据写入新的.jsonl文件
with open(output_file, 'w', encoding='utf-8') as f:
    for item in processed_data:
        f.write(json.dumps(item, ensure_ascii=False) + '\n')

print("数据处理完成，结果已保存到", output_file)