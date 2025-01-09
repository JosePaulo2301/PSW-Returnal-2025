import __init__  # Assuming this import is required
from views.view import SubscribeService
from datetime import datetime
from decimal import Decimal
from models.model import Subscription
from models.database import engine


class UI:
    def __init__(self):
        self.subscription_service = SubscribeService(engine)

    def start(self):
        while True:
            print('''
                [1] -> Adicionar assinatura
                [2] -> Remover assinatura
                [3] -> Valor total
                [4] -> Gastos últimos 12 meses
                [5] -> Sair
            ''')
            try:
                choice = int(input('Escolha uma opção: '))
            except ValueError:
                print("Por favor, insira um número válido.")
                continue

            if choice == 1:
                self.add_subscription()
            elif choice == 2:
                self.delete_subscription()
            elif choice == 3:
                self.total_value()
            elif choice == 4:
                self.last_12_months_spent()
            elif choice == 5:
                print("Saindo do programa...")
                break
            else:
                print("Opção inválida. Tente novamente.")

    def add_subscription(self):
        try:
            empresa = input('Empresa: ')
            site = input('Site: ')
            data_assinatura = datetime.strptime(input('Data de assinatura (dd/mm/aaaa): '), '%d/%m/%Y')
            valor = Decimal(input('Valor: '))
            subscription = Subscription(
                empresa=empresa, site=site, data_assinatura=data_assinatura, valor=valor
            )
            self.subscription_service.create(subscription)
            print("Assinatura adicionada com sucesso!")
        except ValueError:
            print("Erro ao adicionar assinatura. Verifique os dados inseridos.")

    def delete_subscription(self):
        subscriptions = self.subscription_service.list_all()
        if not subscriptions:
            print("Nenhuma assinatura encontrada.")
            return

        print("Escolha qual assinatura deseja excluir:")
        for sub in subscriptions:
            print(f'[{sub.id}] -> {sub.empresa}')

        try:
            choice = int(input('Escolha a assinatura: '))
            self.subscription_service.delete(choice)
            print("Assinatura excluída com sucesso!")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido.")
        except Exception as e:
            print(f"Erro ao excluir assinatura: {e}")

    def total_value(self):
        try:
            total = self.subscription_service.total_value()
            print(f"Seu valor total mensal em assinaturas é: R${total:.2f}")
        except Exception as e:
            print(f"Erro ao calcular o valor total: {e}")

    def last_12_months_spent(self):
        try:
            self.subscription_service.gen_chart()
            print("Gráfico de gastos dos últimos 12 meses gerado com sucesso!")
        except Exception as e:
            print(f"Erro ao gerar gráfico: {e}")


# Executa o programa
if __name__ == "__main__":
    ui = UI()
    ui.start()