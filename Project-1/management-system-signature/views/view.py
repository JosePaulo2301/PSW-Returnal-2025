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

         #função privada/interna(dentro do escopo da classe)   
    def _has_pay(self, result):
        for res in result:
            if res.date.month == date.today().month:
                return True
        return False

    def pay(self, subscription: Subscription):
        with Session(self.engine) as session:
            # Filtra por "subscription_id"
            statement = select(Payment).join(Subscription).where(Payment.subscription_id == subscription.id)
            res = session.exec(statement).all()

            if self._has_pay(res):
                question = input("Essa conta já foi paga esse mês,deseja paga-la novamente? Y ou N: ")
                if question.upper() != "Y":
                    return None

            # Cria um novo pagamento
            pay = Payment(subscription_id=subscription.id, date=date.today())
            session.add(pay)
            session.commit()



ss = SubscribeService(engine)
subscription = Subscription(empresa='globo.play', site='goboplay.com.br', data_assinatura=date.today(), valor=75.44)
#ss.create(subscription)

assinaturas = ss.list_all()
for chave, valor in enumerate(assinaturas):
    print(f'[{chave} -> {valor.empresa}]')

x = int(input())
ss.pay(assinaturas[x])