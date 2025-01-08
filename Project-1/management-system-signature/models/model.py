from sqlmodel import Field, SQLModel, Relationship

from typing import Optional
from datetime import date
from decimal import Decimal


class Subscription(SQLModel, table=True):
    id: int = Field(primary_key=True)
    empresa: str
    site: Optional[str] = None
    data_assinatura: date
    valor: Decimal

class Payment(SQLModel, table=True):
    id: int = Field(primary_key=True)  # Deve ser "id" e não "Id"
    subscription_id: int = Field(foreign_key="subscription.id")  # Certifique-se de que o nome e a chave estrangeira estão corretos
    subscription: Subscription = Relationship()
    date: date



