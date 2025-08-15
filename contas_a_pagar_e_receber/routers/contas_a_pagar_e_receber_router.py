from fastapi import APIRouter
from pydantic import BaseModel
from typing import List


# criação da rota |contas-a-pagar-e-receber|
router = APIRouter(prefix="/contas-a-pagar-e-receber")

# DTO  para a função
class ContasPagarReceberResponse(BaseModel):
    id:int
    descricao:str
    valor:float
    tipo:str

# rota base da rota |contas-a-pagar-e-receber|
@router.get("/", response_model=List[ContasPagarReceberResponse])
def listar_contas():
    return [
        ContasPagarReceberResponse(
            id=1,
            descricao="conta 1",
            valor=1000.50,
            tipo="Pagar"
        ),
        ContasPagarReceberResponse(
            id=2,
            descricao="conta 2",
            valor=5000.50,
            tipo="Receber"
        )
    ]