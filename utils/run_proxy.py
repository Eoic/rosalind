from utils.reader import Reader


class RunProxy:
    @staticmethod
    def run(id, sample, file_output, callback):
        data = Reader.read_data(id, sample)

        if file_output:
            Reader.write_data(id, callback(data))
        else:
            return callback(data)
