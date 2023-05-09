import json
import os

# 获取当前脚本所在目录
current_dir = os.path.dirname(os.path.abspath(__file__))
# 获取best_individual目录下的所有子目录
best_individual_path = os.path.join(current_dir, "best_individual")
sub_folders = os.listdir(best_individual_path)

# 第二个子目录的名称
target_folder_name = sub_folders[9]

# 遍历best_individual目录下的所有子目录
for folder_name in sub_folders:
    folder_path = os.path.join(best_individual_path, folder_name)
    # 如果不是目录，跳过
    if not os.path.isdir(folder_path):
        continue
    # 如果不是第二个子目录的名称，跳过
    if folder_name != target_folder_name:
        continue
    # 获取该子目录中的所有JSON文件
    json_files = [f for f in os.listdir(folder_path) if f.endswith(".json")]
    # 转换JSON文件
    result = []
    for file_name in json_files:
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, "r") as f:
            data = json.load(f)
            for item in data:
                best_individual = item["best_individual"]
                fitness = item["fitness"]
                result.append({
                    "pop_size": 5,
                    "num_gens": 5,
                    "cxpb": 0.9,
                    "mutpb": 0.9,
                    "best_individual": best_individual,
                    "fitness": fitness
                })
    # 输出转换结果到output.json文件

    output_file_path = os.path.join(current_dir, "output_result.log")

    with open(output_file_path, "a") as f:
        # 将每个元素转化为字符串，并每个元素占一行
        f.write("\n".join([json.dumps(item, ensure_ascii=False) for item in result]))

    print("finsished")
