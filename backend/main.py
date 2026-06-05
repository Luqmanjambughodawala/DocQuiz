from fastapi import FastAPI
from documents import document_manager as dc
from schema.schema import Question,Quiz
app = FastAPI()

@app.get('/get_files')
def search_files():
    print("DEBUG file_paths:", dc.file_paths)
    path = dc.file_paths()
    return path