import pandas as pd
import io
import plotly.graph_objects as go
import plotly.offline as pyo


print('-' * 60)
print('-' * 60)
nome_sistema = (input("Digite o nome do sistema para o Relatório: ")).upper()
print('-' * 60)
print('-' * 60)

tabela = pd.read_excel('funcoes.xlsx', skiprows=range(0, 5))

comercial = tabela['Menu'] == 'Comercial'
somaComercial = (tabela[comercial].sum())['Quantidade Acessos']

operacional = tabela['Menu'] == 'Operacional'
somaOperacional = (tabela[operacional].sum())['Quantidade Acessos']

tracking = tabela['Menu'] == 'Tracking'
somaTracking = (tabela[tracking].sum())['Quantidade Acessos']

frota = tabela['Menu'] == 'Frota'
somaFrota = (tabela[frota].sum())['Quantidade Acessos']

faturamento = tabela['Menu'] == 'Faturamento'
somaFaturamento = (tabela[faturamento].sum())['Quantidade Acessos']

financeiro = tabela['Menu'] == 'Financeiro'
somaFinanceiro = (tabela[financeiro].sum())['Quantidade Acessos']

infra_estrutura = tabela['Menu'] == 'Infra-Estrutura'
somaInfra_estrutura = (tabela[infra_estrutura].sum())['Quantidade Acessos']

relatorios = tabela['Menu'] == 'Relatórios'
somaRelatorios = (tabela[relatorios].sum())['Quantidade Acessos']

usuarios = tabela['Menu'] == 'Ger. Usuários'
somaUsuarios = (tabela[usuarios].sum())['Quantidade Acessos']

estoque = tabela['Menu'] == 'Estoque'
somaEstoque = (tabela[estoque].sum())['Quantidade Acessos']

container = tabela['Menu'] == 'Container'
somaContainer = (tabela[container].sum())['Quantidade Acessos']

edi = tabela['Menu'] == 'EDI'
somaEDI = (tabela[edi].sum())['Quantidade Acessos']

mobile = tabela['Menu'] == 'Mobile'
somaMobile = (tabela[mobile].sum())['Quantidade Acessos']

categorias = ['Comercial', 'Operacional', 'Tracking', 'Frota', 'Faturamento', 'Financeiro', 'Infra-Estrutura',
              'Relatórios', 'Ger. Usuários', 'Estoque', 'Container', 'EDI', 'Mobile']
categorias = [*categorias, categorias[0]]

sistema = [somaComercial, somaOperacional, somaTracking, somaFrota, somaFaturamento, somaFinanceiro,
           somaInfra_estrutura, somaRelatorios, somaUsuarios, somaEstoque, somaContainer, somaEDI, somaMobile]
sistema = [*sistema, sistema[0]]

fig = go.Figure(
    data=[
        go.Scatterpolar(r=sistema, theta=categorias, fill='toself', name=f"{nome_sistema}"),
    ],
    layout=go.Layout(
        title=go.layout.Title(text='Acesso por Menus de Funções ({})'.format(nome_sistema)),
        polar={'radialaxis': {'visible': True}},
        showlegend=True
    )
)

pyo.plot(fig)