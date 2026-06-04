def load_file(path):
    with open(path, encoding='utf-8',mode='r') as f:
        content = f.read()
        return content
    

