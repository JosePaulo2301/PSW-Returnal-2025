# Lógica da aplicação

import __init__
from models.database import engine
from models.model import Payment, Subscription
from sqlmodel import Session, select
from datetime import date, datetime

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

    def delete(self, id):
        with Session(self.engine) as session:
            statement = select(Subscription).where(Subscription.id == id)
            result = session.exec(statement).one()
            session.delete(result)
            session.commit()

         #função privada/interna(dentro do escopo da classe)   
    def _has_pay(self, result):
        for res in result:
            if res.date.month == date.today().month:
                return True
        return False

    def pay(self, subscription: Subscription):
        with Session(self.engine) as session:
            
            statement = select(Payment).join(Subscription).where(Payment.subscription_id == subscription.id)
            res = session.exec(statement).all()

            if self._has_pay(res):
                question = input("Essa conta já foi paga esse mês,deseja paga-la novamente? Y ou N: ")
                if question.upper() != "Y":
                    return None

            pay = Payment(subscription_id=subscription.id, date=date.today())
            session.add(pay)
            session.commit()

    def total_value(self):
        with Session(self.engine) as session:
            statement = select(Subscription)
            res = session.exec(statement).all()
        

        total = 0
        for result in res:
            total+= result.valor
        return float(total)
    

    def _get_last_23_monats_native(self):
        today = datetime.now()
        year = today.year
        month = today.month
        last_12_month = []

        for _ in range(12):
            last_12_month.append((month, year))  
            month -= 1
            if month == 0:
                month = 12
                year -= 1

        return last_12_month[::-1]  


    def _get_values_for_months(self, last_12_months):
        with Session(self.engine) as session:
            statement = select(Payment).join(Subscription)
            result = session.exec(statement).all()
            value_for_months = []
            for i in last_12_months:
                value = 0
                for res in result:
                    if res.subscription and res.date.month == i[0] and res.date.year == i[1]:
                        value += float(res.subscription.valor)
                value_for_months.append(value)
            return value_for_months


    def gen_chart(self):
        last_12_months = self._get_last_23_monats_native()
        values_for_months = self._get_values_for_months(last_12_months)
        print(last_12_months)
        print(values_for_months)


        import matplotlib.pyplot as plt

        plt.plot([1,2], [5,5])
        plt.show()

ss = SubscribeService(engine)
print(ss.gen_chart())

