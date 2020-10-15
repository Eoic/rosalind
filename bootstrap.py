import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--id')
arguments = parser.parse_args()

if arguments.id is not None:
    id = arguments.id
    sample_data = f"{id}/{id}-sample.txt"
    source = f"{id}/{id}.py"
    data = f"{id}/{id}.txt"

    if not os.path.exists(id):
        os.mkdir(id)

    for file_name in [sample_data, data]:
        with open(file_name, 'w') as data_file:
            pass

    with open(source, 'w') as source_file:
        source_file.write('def run(data):\n')
        source_file.write('    pass\n')
