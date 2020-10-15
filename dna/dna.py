def run(data):
    result = [data.count(target) for target in ['A', 'C', 'G', 'T']]
    return " ".join(repr(item) for item in result)
