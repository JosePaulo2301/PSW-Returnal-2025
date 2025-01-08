# Lógica da aplicação
import __init__
from models.database import engine
from models.model import Payment, Subscription
from sqlmodel import Session, select
from datetime import date

class SubscribeService:
    def __init__(self, engine):
        self.engine = engine

    def create(self, subscription: Subscription):
        with Session(self.engine) as session:
            session.add(subscription)
            session.commit()
            return subscription
    
    def list_all(self):
        with Session(self.engine) as session:
            statement = select(Subscription)
            result = session.exec(statement).all()
            return result
            
    def pay(self, subscription: Subscription):
        with Session(self.engine) as session:
            statement = select(Payment).where(Subscription.empresa == subscription.empresa)
            result = session.exec(statement).all()

            pago = False
            for res in result:
                print(res.date)


ss = SubscribeService(engine)
#subscription = Subscription(empresa='Youtube', site='youtube.com.br', data_assinatura=date.today(), valor=49.90)
#ss.create(subscription)
#print(ss.list_all())
ss.pay(Subscription)