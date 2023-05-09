import json
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
best_individual_path = os.path.join(current_dir, "best_individual")
output_file_path = os.path.join(current_dir, "output.json")

result = []
for folder_name in os.listdir(best_individual_path):
    folder_path = os.path.join(best_individual_path, folder_name)
    if not os.path.isdir(folder_path):
        continue
    json_files = [f for f in os.listdir(folder_path) if f.endswith(".json")]
    for file_name in json_files:
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, "r") as f:
            data = json.load(f)
            for item in data:
                best_individual = eval(item["best_individual"])
                fitness = eval(item["fitness"])
                result.append({
                    "pop_size": 5,
                    "num_gens": 5,
                    "cxpb": 0.1,
                    "mutpb": 0.1,
                    "best_individual": best_individual,
                    "fitness": fitness
                })

with open(output_file_path, "w") as f:
    json.dump(result, f)
