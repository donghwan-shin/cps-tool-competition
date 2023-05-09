#
# import re
#
# # 读取日志文件
# with open('merged.log', 'r') as f:
#     lines = f.readlines()
#
# # 解析每一行为字典，并根据 pop_size 进行排序
# records = []
# for line in lines:
#     if not re.match(r'^pop_size=\d+, num_gens=\d+, cxpb=\d+\.\d+, mutpb=\d+\.\d+, best_individual=\[.*\], fitness=\(.*\),$',
#                     line.strip()):
#         # 如果行的格式不正确，则跳过该行
#         print(f"跳过行：{line.strip()}")
#         continue
#     record = {}
#     for item in line.strip().split(', '):
#         key, value = item.split('=')
#         record[key] = value
#     records.append(record)
# records.sort(key=lambda x: -int(x['pop_size']))
#
# # 将排序后的字典转换回字符串并写入文件中
# with open('merged.log', 'a') as f:
#     for record in records:
#         line = ', '.join([f"{k}={v}" for k, v in record.items()])
#         f.write(line + '\n')




        # import os
        # import json
        #
        # # 指定输入和输出文件路径
        # input_file = 'final_output.log'
        # output_file = 'GA_best_in.log'
        #
        # # 打开输入和输出文件
        # with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
        #     # 逐行读取输入文件内容
        #     for line in f_in:
        #         try:
        #             # 将每行内容转换为Python字典
        #             data = json.loads(line.strip())
        #
        #             # 从字典中获取所需的值并格式化输出
        #             pop_size = data['pop_size']
        #             num_gens = data['num_gens']
        #             cxpb = data['cxpb']
        #             mutpb = data['mutpb']
        #             best_individual = data['best_individual']
        #             fitness = data['fitness']
        #             output_line = f"pop_size={pop_size}, num_gens={num_gens}, cxpb={cxpb}, mutpb={mutpb}, best_individual={best_individual}, fitness={fitness}\n"
        #
        #             # 将格式化的输出写入输出文件中
        #             f_out.write(output_line)
        #         except json.JSONDecodeError:
        #             # 如果解析JSON时出错，跳过当前行并打印错误消息
        #             print(f"Error parsing line: {line}")
        #
        # # 输出处理完毕的消息
        # print(f"Finished processing {input_file} and writing to {output_file}")

#
# with open('GA_best_in.log', 'r') as f1, open('GA_best_individuals.log', 'r') as f2, open('merged.txt', 'w') as out:
#     out.write(f1.read())
#     out.write(f2.read())

#
# # 读取txt文件并将每行数据存储为元组的列表
# with open('data.txt', 'r') as file:
#     data = [tuple(line.strip().split(', ')) for line in file]
#
# # 根据pop_size值排序
# data_sorted = sorted(data, key=lambda x: int(x[0].split('=')[1]))
#
# # 将排序后的结果输出到新的txt文件中
# with open('data_sorted.txt', 'w') as file:
#     for line in data_sorted:
#         file.write(', '.join(line) + '\n')


# import re
#
# # 定义函数，将A文件中的每一行转换为B文件的格式
# def convert_to_b_format(line):
#     match = re.match(r'^pop_size=(\d+), num_gens=(\d+), mutation_rate=(\d+\.\d+), elite_rate=(\d+\.\d+), best_individual=\[(.*)\], best_fitness=(.*)$', line.strip())
#     if match:
#         return f"pop_size={match.group(1)}, num_gens={match.group(2)}, cxpb=0.9, mutpb={match.group(3)}, best_individual={match.group(5)}, fitness=({match.group(6)})"
#     else:
#         # 如果行的格式不正确，则返回空字符串，并打印错误信息
#         print(f"无法转换行：{line.strip()}")
#         return ''
# # 读取A文件中的所有行，并转换为B文件格式的行
# a_lines = []
# with open('GA_best_in.log', 'r') as f:
#     for line in f:
#         b_line = convert_to_b_format(line)
#         if b_line:
#             a_lines.append(b_line)
#
# # 读取B文件的所有行
# with open('GA_best_individuals.log', 'r') as f:
#     b_lines = f.readlines()
#
# # 将转换后的A文件内容和B文件内容合并到一个列表中
# merged_lines = a_lines + b_lines
#
# # 根据需要进行排序或者过滤
# merged_lines.sort(key=lambda x: -int(re.search(r'pop_size=(\d+)', x).group(1)))
#
# # 将结果写入到新的日志文件中
# with open('merged3.log', 'a') as f:
#     for line in merged_lines:
#         f.write(line.strip() + '\n')


#
# with open('data_sorted2.txt', 'r') as f:
#     lines = f.readlines()
#
# results = []
# for line in lines:
#     data = line.strip().split(',')
#     result = {}
#     result['pop_size'] = int(data[0].split('=')[1])
#     result['num_gens'] = int(data[1].split('=')[1])
#     result['cxpb'] = float(data[2].split('=')[1])
#     result['mutpb'] = float(data[3].split('=')[1])
#     result['best_individual'] = eval(data[4].split('=')[1])
#     result['fitness'] = float(data[5].split('=')[1].strip('()'))
#     results.append(result)
#
# sorted_results = sorted(results, key=lambda x: (x['pop_size'], x['num_gens'], x['cxpb'], x['mutpb']))
#
# with open('sorted_results.txt', 'w') as f:
#     for result in sorted_results:
#         f.write(f"pop_size={result['pop_size']}, num_gens={result['num_gens']}, cxpb={result['cxpb']}, mutpb={result['mutpb']}, best_individual={result['best_individual']}, fitness=({result['fitness']})\n")
#
#
# with open('data_sorted2.txt', 'r') as file:
#     for line in file:
#         data = line.strip().split(', ')
#         if len(data) != 6:
#             print(f"Error: Incorrect number of elements in line '{line}'")
#             continue
#
#         try:
#             pop_size = int(data[0].split('=')[1])
#             num_gens = int(data[1].split('=')[1])
#             cxpb = float(data[2].split('=')[1])
#             mutpb = float(data[3].split('=')[1])
#             best_individual = eval(data[4].split('=')[1])
#             fitness = float(data[5].split('=')[1].strip('()'))
#         except:
#             print(f"Error: Incorrect data format in line '{line}'")
#             continue
#
#         if not isinstance(pop_size, int) or not isinstance(num_gens, int) or not isinstance(cxpb,
#                                                                                             float) or not isinstance(
#                 mutpb, float) or not isinstance(best_individual, list) or not isinstance(fitness, float):
#             print(f"Error: Incorrect data types in line '{line}'")
#             continue
#
#         for individual in best_individual:
#             if not isinstance(individual, tuple) or len(individual) != 2 or not all(
#                     isinstance(x, int) for x in individual):
#                 print(f"Error: Incorrect data format in line '{line}'")
#                 continue
#
#         print(f"Line '{line.strip()}' is correctly formatted.")
# 打开txt文件并读取所有行
# with open('newfile.txt', 'r') as f:
#     lines = f.readlines()
#
# data_list = []
# for line in lines:
#     try:
#         data = line.strip().split(', ')
#         data_dict = {}
#         for item in data:
#             key, value = item.split('=')
#             data_dict[key.strip()] = eval(value.strip())
#         data_list.append(data_dict)
#     except Exception as e:
#         print(f"Error: {e}")
#         print(f"Line: {line}")
#         continue
#
# sorted_data = sorted(data_list, key=lambda x: (x['pop_size'], x['num_gens'], x['cxpb'], x['mutpb']))


#
# import json
#
# # 从.log文件中读取数据
# with open('GA_best_individuals.log', 'r') as f:
#     lines = f.readlines()
#
# # 解析每一行数据并将其转换为字典
# data_list = []
# for line in lines:
#     data = line.strip().split(', ')
#     data_dict = {}
#     for item in data:
#         key, value = item.split('=')
#         data_dict[key.strip()] = eval(value.strip())
#     data_list.append(data_dict)
#
# # 从.json文件中读取数据
# with open('merged.log', 'r') as f:
#     json_data = json.load(f)
#
# # 将json数据中的每个字典添加到data_list中
# for item in json_data:
#     data_list.append(item)
#
# # 根据pop_size, num_gens, cxpb, mutpb排序
# sorted_data = sorted(data_list, key=lambda x: (x['pop_size'], x['num_gens'], x['cxpb'], x['mutpb']))
#
# # 将排序后的数据写入新的文件
# with open('11newfile.txt', 'w') as f:
#     for data in sorted_data:
# #         f.write(str(data)+'\n')
# import json
#
# data = []
#
#
#
# with open('data_sorted2.txt', 'r') as f:
#     lines = f.readlines()
#
# for line in lines:
#     parts = line.strip().split(', ')
#     try:
#         pop_size = int(parts[0].split('=')[1])
#         num_gens = int(parts[1].split('=')[1])
#         cxpb = float(parts[2].split('=')[1])
#         mutpb = float(parts[3].split('=')[1])
#         best_individual = json.loads(parts[4].split('=')[1])
#         fitness = float(parts[5].split('=')[1].strip('(),'))
#         d = {
#             'pop_size': pop_size,
#             'num_gens': num_gens,
#             'cxpb': cxpb,
#             'mutpb': mutpb,
#             'best_individual': best_individual,
#             'fitness': fitness
#         }
#         data.append(d)
#     except json.decoder.JSONDecodeError as e:
#         print("Error: Could not decode JSON on line {}: {}".format(line, e))
#


# # 读取txt文件并将每行数据存储为元组的列表
# with open('data_sorted2.txt', 'r') as file:
#     data = [tuple(line.strip().split(', ')) for line in file]
#
# # 根据pop_size、num_gens、cxpb和mutpb值排序
# data_sorted = sorted(data, key=lambda x: (
#     int(x[0].split('=')[1]) == 5,    # pop_size=5是否为True，True会被当作1来排序
#     int(x[1].split('=')[1]) == 5,    # num_gens=5是否为True，True会被当作1来排序
#     float(x[2].split('=')[1]),       # cxpb的值，越小越靠前
#     float(x[3].split('=')[1]),       # mutpb的值，越小越靠前
# ))
#
# # 将排序后的结果输出到新的txt文件中
# with open('data_sorted44444.txt', 'w') as file:
#     for line in data_sorted:
#         file.write(', '.join(line) + '\n')
#
# with open('data_sorted2.txt', 'r') as file:
#     data = [tuple(line.strip().split(', ')) for line in file]
#
# data_sorted = sorted(data, key=lambda x: (
#     int(x[0].split('=')[1]) != 5,   # 如果pop_size不是5，则排在后面
#     -int(x[0].split('=')[1]),       # 如果pop_size是5，倒序排列，即5在前
#     int(x[1].split('=')[1]),        # num_gens的值，越小越靠前
#     float(x[2].split('=')[1]),      # cxpb的值，越小越靠前
#     float(x[3].split('=')[1]),      # mutpb的值，越小越靠前
# ))
#
# with open('datdwwwww.txt', 'w') as file:
#     for line in data_sorted:
#         file.write(', '.join(line) + '\n')


# with open('result_data.txt', 'r') as file:
#     data = [tuple(line.strip().split(', ')) for line in file]
#
# data_sorted = sorted(data, key=lambda x: (
#     int(x[0].split('=')[1]),        # pop_size的值，越小越靠前
#     int(x[1].split('=')[1]),        # num_gens的值，越小越靠前
#     float(x[2].split('=')[1]),      # cxpb的值，越小越靠前
#     float(x[3].split('=')[1]),      # mutpb的值，越小越靠前
# ))
#
# data_sorted = sorted(data_sorted, key=lambda x: (
#     int(x[0].split('=')[1]) != 5,   # 如果pop_size不是5，则排在后面
#     int(x[1].split('=')[1]) != 5,   # 如果num_gens不是5，则排在后面
#     float(x[2].split('=')[1]),      # cxpb的值，越小越靠前
#     float(x[3].split('=')[1]),      # mutpb的值，越小越靠前
# ))
#
# with open('result_data2.txt', 'w') as file:
#     for line in data_sorted:
#         file.write(', '.join(line) + '\n')




with open('result_data.txt', 'r') as file:
    data = [tuple(line.strip().split(', ')) for line in file]

data_sorted = sorted(data, key=lambda x: (
    int(x[0].split('=')[1]),        # pop_size的值，越小越靠前
    int(x[1].split('=')[1]),        # num_gens的值，越小越靠前
    float(x[2].split('=')[1]),      # cxpb的值，越小越靠前
    float(x[3].split('=')[1]),      # mutpb的值，越小越靠前
))

try:
    data_sorted = sorted(data_sorted, key=lambda x: (
        int(x[0].split('=')[1]) != 5,   # 如果pop_size不是5，则排在后面
        int(x[1].split('=')[1]) != 5,   # 如果num_gens不是5，则排在后面
        float(x[2].split('=')[1]),      # cxpb的值，越小越靠前
        float(x[3].split('=')[1]),      # mutpb的值，越小越靠前
    ))
except:
    import traceback
    print("An error occurred in the following lines:")
    for tb in traceback.format_exc().splitlines():
        if "line" in tb:
            print(tb)

with open('result_data3.txt', 'w') as file:
    for line in data_sorted:
        file.write(', '.join(line) + '\n')
