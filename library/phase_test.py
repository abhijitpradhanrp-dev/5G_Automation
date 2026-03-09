import sys
sys.path.append("./variablefiles")
import var_file
import json
from tabulate import tabulate
from robot.api import logger
from robot.libraries.BuiltIn import BuiltIn
import matplotlib.pyplot as plt


class phase_test():

    ROBOT_LIBRARY_SCOPE = 'GLOBAL'  # setting library scope as global

    def __init__(self):
        pass

    def lscpu_log(self):
        config_file_handle = open(var_file.config_file_path, "r")
        platform_handle = open(var_file.log_file_path, "r")
        output_handle = open(var_file.output_txt_path, "w+")
        for elemi in config_file_handle:
            datai = elemi.rstrip("\n")
            platform_handle.seek(0,0)
            for elemj in platform_handle:
                dataj = elemj.split(":")

                if datai in dataj:
                    output_handle.write(elemj)

    def get_lscpu(self):
        my_dict = {}
        fob = open(var_file.output_txt_path, "r")
        foc = open(var_file.output_json_path, "w+")

        for elem in fob:
            data = elem.split(":")
            my_dict[data[0]] = data[-1].strip("\n").strip()


        output = json.dumps(my_dict)
        foc.write(output)
        fob.close()
        return output

    def lscpu_table(self):
        with open(var_file.output_json_path) as jsonfile:
            data = json.load(jsonfile)       
            headers = ['item', 'value']
        data1 = sorted([(k, v) for k, v in data.items()])  # flip the code and name and sort
        with open(var_file.table_output_path, 'w', encoding="utf-8") as f:
            f.write(tabulate(data1, headers=headers, tablefmt="fancy_grid"))
        print(tabulate(data1, headers=headers, tablefmt="fancy_grid"))
    
    def lscpu_tableplot(self):
        with open(var_file.output_json_path,encoding="utf-8") as jsonfile:
            data = json.load(jsonfile)
            print(data)

        # Convert dictionary into sorted list of tuples
        data1 = sorted(data.items())

        # Separate keys and values
        items = [i[0] for i in data1]
        values = [i[1] for i in data1]

        # Create figure
        fig, ax = plt.subplots()

        # Remove axes
        ax.axis('off')

        # Create table
        table_data = [[items[i], values[i]] for i in range(len(items))]

        table = ax.table(
            cellText=table_data,
            colLabels=["Item", "Value"],
            loc='center'
        )
        # Adjust table size
        table.auto_set_font_size(False)
        table.set_fontsize(10)
        table.scale(1, 1.5)

        # Save graphical output as image
        plt.savefig(var_file.table_output_path)

         # Show graphical table
        plt.show()
    
obj = phase_test()
obj.lscpu_log()
obj.get_lscpu()
obj.lscpu_table()
obj.lscpu_tableplot()

