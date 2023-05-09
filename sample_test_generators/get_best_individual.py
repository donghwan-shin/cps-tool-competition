# import json
# import os
#
# from sample_test_generators.s2net import best_individual
#
# # 定义输出文件名
# output_file = "best_individual.json"
#
# # 检查输出文件是否存在
# if os.path.exists(output_file):
#     # 如果存在，直接打开文件，将数据写入
#     with open(output_file, "a") as f:
#         # 读取文件内容，将JSON格式的数据转换为Python对象
#         data = json.load(f)
#
#         # 将需要输出的数据添加到列表中
#         data.append({"best_individual": str(best_individual), "fitness": str(best_individual.fitness)})
#
#         # 将数据转换为JSON格式并输出到文件
#         json.dump(data, f)
# else:
#     # 如果文件不存在，创建一个新文件，将数据写入
#     with open(output_file, "w") as f:
#         # 创建一个空的列表，用于存储输出的数据
#         data = [{"best_individual": str(best_individual), "fitness": str(best_individual.fitness)}]
#
#         # 将数据转换为JSON格式并输出到文件
#         json.dump(data, f)



