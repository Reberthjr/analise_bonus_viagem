import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC9cb4edaf41094786f5d761a489e39b65"
# Your Auth Token from twilio.com/console
auth_token = "0311f4d7a86cfda9d0be40df00c58184"
client = Client(account_sid, auth_token)

lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']
for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas ['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas ['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas ['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'no mês de {mes}  alguem bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        message = client.messages.create(
                to="+5531983277164",
            #VOCÊ SO PODE ENVIAR MENSAGENS PARA O SEU PRÓPRIO NUMERO!!
                from_="+15165186838",
                body=f'no mês de {mes}  alguem bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')

        print(message.sid)

# se for maior que 55.0000 enviamos um sms com o nome e o mes e as vendas do vendedor

""