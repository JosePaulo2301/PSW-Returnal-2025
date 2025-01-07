# Lógica da aplicação
import __init__
from models.database import engine
from models.model import Subscrition
from sqlmodel import Session, select
from datetime import date

class SubscribeService:
    def __init__(self, engine):
        self.engine = engine

    def create(self, subscription: Subscrition):
        with Session(self.engine) as session:
            session.add(subscription)
            session.commit()
            return subscription
    
    def list_all(self):
        with Session(self.engine) as session:
            ...

ss = SubscribeService(engine)
subscription = Subscrition(empresa='netflix', site='netflix.com.br', data_assinatura=date.today(), valor=23)
ss.create(subscription)