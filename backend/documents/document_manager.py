from pathlib import Path

folder = Path('D:/Quiz Generator/backend/documents')
def file_paths():
    txt_files = list(folder.glob('*.txt'))
    return txt_files