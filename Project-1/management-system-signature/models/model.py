from sqlmodel import Field, SQLModel, create_engine

from typing import Optional
from datetime import date
from decimal import Decimal


class Subscrition(SQLModel, table=True):
    Id: int = Field(primary_key=True)
    empresa: str
    site: Optional[str] = None
    data_assinatura: date
    valor: Decimal


sqlite_file_name = 'database.db'
sqlite_url = f'sqlite:///{sqlite_file_name}'
engine = create_engine(sqlite_url, echo=True)

if __name__ == '__main__':
    SQLModel.metadata.create_all(engine)

