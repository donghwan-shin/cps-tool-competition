import json
import os
import datetime


class BestIndividualSaver:
    def __init__(self, folder_path, subfolder_name):
        self.folder_path = os.path.join(folder_path, subfolder_name)

        # create folder(if not )
        if not os.path.exists(self.folder_path):
            os.makedirs(self.folder_path)

    def save_best_individual(self, best_individual):
        # generate the file name
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = f"result_{timestamp}.json"
        file_path = os.path.join(self.folder_path, file_name)

        # check the output file
        if os.path.exists(file_path):
            # if has read it
            with open(file_path, "r") as f:
                # read the file，JSON to Python
                data = json.load(f)
        else:
            # if folder exist , create  it
            data = []

        # add the data to ..
        if data == []:
            print("没有文件")
        data.append({"best_individual": str(best_individual), "fitness": str(best_individual.fitness)})
        print("有文件")

        # make the data to the folder
        with open(file_path, "w") as f:
            # change the data to JSON and wirte the folder
            json.dump(data, f)

