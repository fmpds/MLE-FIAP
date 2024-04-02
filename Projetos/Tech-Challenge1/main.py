from fastapi import FastAPI
from pydantic import BaseModel

# Criar uma instância do FastAPI
app = FastAPI()

# Modelagem dos dados do livro usando Pydantic
class Book(BaseModel):
    title: str
    author: str
    pages: int

# Lista de livros (simulando um banco de dados simples)
books = []

# Rota para adicionar um novo livro
@app.post("/books/")
async def add_book(book: Book):
    books.append(book)
    return {"message": "Livro adicionado com sucesso"}

# Rota para obter todos os livros
@app.get("/books/")
async def get_books():
    return books

# Rota para obter um livro por seu índice na lista
@app.get("/books/{book_id}")
async def get_book(book_id: int):
    if book_id < len(books):
        return books[book_id]
    else:
        return {"error": "Livro não encontrado"}

# Rodar o servidor usando Uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
