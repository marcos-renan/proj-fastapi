import uvicorn
from fastapi import FastAPI

# importaçao da rota |contas-a-pagar-e-receber|
from contas_a_pagar_e_receber.routers import contas_a_pagar_e_receber_router

# declaração do app
app = FastAPI()

# rota base de toda app
@app.get("/")
def helloworld()->str:
    return "Hello World"

# inclusao da rotas nas rotas do app
app.include_router(contas_a_pagar_e_receber_router.router)

# se rodar no main.py executar servidor uvicorn
if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)