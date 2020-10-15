def run(data):
    data = list(data)
    original = ['A', 'T', 'C', 'G']
    complement = ['T', 'A', 'G', 'C']

    for i in range(len(data)):
        data[i] = complement[original.index(data[i])]

    data.reverse()
    return ''.join(item for item in data)
