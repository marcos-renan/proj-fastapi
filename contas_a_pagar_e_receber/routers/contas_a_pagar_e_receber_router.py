from decimal import Decimal

from fastapi import APIRouter
from pydantic import BaseModel


# criação da rota |contas-a-pagar-e-receber|
router = APIRouter(prefix="/contas-a-pagar-e-receber")

# DTO  para a função
class ContasPagarReceberResponse(BaseModel):
    id:int
    descricao:str
    valor:Decimal
    tipo:str

# rota base da rota |contas-a-pagar-e-receber|
@router.get("/")
def listar_contas():
    return [
        {"contas1" : "contas1"},
        {"contas2" : "contas2"}
    ]