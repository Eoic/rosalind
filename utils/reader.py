import os


class Reader:
    @staticmethod
    def read_data(id, is_sample):
        file_name = os.path.join(id, f"{id}{'-sample' if is_sample else ''}.txt")

        if os.path.isfile(file_name):
            with open(file_name) as file:
                return file.read()

    @staticmethod
    def write_data(id, data):
        file_name = os.path.join(id, f"{id}-result.txt")

        with open(file_name, 'w') as file:
            file.write(data)
