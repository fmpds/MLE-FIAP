from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name:str):
    return {"message":f"Hello {name}"}


@app.get("/calculadora/soma")
async def sum(number1:int, number2:int):
    result = number1 + number2
    return int(result)

@app.get("/calculadora/subtrai")
async def sum(number1:int, number2:int):
    result = number1 - number2
    return int(result)


@app.get("/calculadora/multiplica")
async def sum(number1:int, number2:int):
    result = number1 * number2
    return int(result)

@app.get("/calculadora/divide")
async def sum(number1:int, number2:int):
    if number2 == 0:
        return {"Não pode ser feita divisão por zero."}
    else:
        result = number1 / number2
    
    return result

# boas praticas definir eventuais erros
# Tratamento de erro 404 - Rota não encontrada
@app.exception_handler(404)
async def not_found(request, exc):
    return {"error": "Rota não encontrada"}

# Tratamento de erro 422 - Validação de dados falhou
@app.exception_handler(422)
async def validation_error(request, exc):
    return {"error": "Erro de validação de dados"}

# Tratamento de erro 500 - Erro interno do servidor
@app.exception_handler(500)
async def internal_server_error(request, exc):
    return {"error": "Erro interno do servidor"}



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)