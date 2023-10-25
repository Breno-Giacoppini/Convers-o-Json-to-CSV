import pandas as pd
import json


# Dados JSON
dados_json =[
    {
        "Registro 1": {
        "Veiculo": "Volvo VNL 860",
        "Nome do Cliente": "Ana Silva",
        "Ano do Carro": "2020",
        "Cliente": "Sim",
        "Tipo de Problema": "Problema no sistema de suspensao",
        "eixos": "6",
        "peso": "12.500 kg",
        "altura": "3.90 metros",
        "comprimento": "6.90 metros"
        }
    },
    {
        "Registro 2": {
            "Veiculo": "Kenworth W900",
            "Nome do Cliente": "Maria Souza",
            "Ano do Carro": "2020",
            "Cliente": "Sim",
            "Tipo de Problema": "Problema na transmissao",
            "eixos": "4",
            "peso": "10 toneladas",
            "altura": "3 metros",
            "comprimento": "7 metros"
        }
    },
    {
        "Registro 3": {
            "Veiculo": "Peterbilt 379",
            "Nome do Cliente": "Antonio Silva",
            "Ano do Carro": "2018",
            "Cliente": "Sim",
            "Tipo de Problema": "Problema no sistema eletrico",
            "eixos": "4",
            "peso": "12 toneladas",
            "altura": "3.2 metros",
            "comprimento": "7.5 metros"
        }
    },
    {
        "Registro 4": {
            "Veiculo": "Mack Anthem",
            "Nome do Cliente": "Ana Santos",
            "Ano do Carro": "2021",
            "Cliente": "Sim",
            "Tipo de Problema": "Problema no sistema de freio",
            "eixos": "4",
            "peso": "11 toneladas",
            "altura": "3.1 metros",
            "comprimento": "7.3 metros"
        }
    },
    {
        "Registro 5": {
            "Veiculo": "International LoneStar",
            "Nome do Cliente": "Luiz Pereira",
            "Ano do Carro": "2019",
            "Cliente": "Sim",
            "Tipo de Problema": "Problema no sistema de direcao",
            "eixos": "2",
            "peso": "8 toneladas",
            "altura": "2.8 metros",
            "comprimento": "6.5 metros"
        }
    },
    {
        "Registro 6": {
            "Veiculo": "Freightliner Cascadia",
            "Nome do Cliente": "Eduardo Costa",
            "Ano do Carro": "2020",
            "Cliente": "Sim",
            "Tipo de Problema": "Problema no sistema de ar condicionado",
            "eixos": "2",
            "peso": "9 toneladas",
            "altura": "2.7 metros",
            "comprimento": "6.2 metros"
        }
    },
    {
        "Registro 7": {
            "Veiculo": "Paccar MX-13",
            "Nome do Cliente": "Rosa Ferreira",
            "Ano do Carro": "2018",
            "Cliente": "Sim",
            "Tipo de Problema": "Problema no sistema de suspensao",
            "eixos": "2",
            "peso": "8.5 toneladas",
            "altura": "2.6 metros",
            "comprimento": "6 metros"
        }
    },
    {
        "Registro 8": {
            "Veiculo": "MAN TGX",
            "Nome do Cliente": "Paulo Lima",
            "Ano do Carro": "2021",
            "Cliente": "Sim",
            "Tipo de Problema": "Problema no sistema de transmissao",
            "eixos": "2",
            "peso": "8.2 toneladas",
            "altura": "2.5 metros",
            "comprimento": "5.8 metros"
        }
    },
    {
        "Registro 9": {
            "Veiculo": "DAF XF",
            "Nome do Cliente": "Cristina Alves",
            "Ano do Carro": "2019",
            "Cliente": "Sim",
            "Tipo de Problema": "Problema no sistema de escape",
            "eixos": "2",
            "peso": "7.8 toneladas",
            "altura": "2.4 metros",
            "comprimento": "5.5 metros"
        }
    },
    {
        "Registro 10": {
            "Veiculo": "Komatsu WA900-8",
            "Nome do Cliente": "Jose Oliveira",
            "Ano do Carro": "2018",
            "Cliente": "Sim",
            "Tipo de Problema": "Problema no sistema hidraulico",
            "eixos": "2",
            "peso": "7.5 toneladas",
            "altura": "2.3 metros",
            "comprimento": "5 metros"
        }
    }
]

# Crie um DataFrame do pandas a partir dos dados JSON
dados_formatados = []

for registro in dados_json:
    registro_numero = list(registro.keys())[0]
    dados = registro[registro_numero]
    linha = [registro_numero, dados["Veiculo"], dados["Nome do Cliente"], dados["Ano do Carro"], dados["Cliente"], dados["Tipo de Problema"], dados["eixos"], dados["peso"], dados["altura"], dados["comprimento"]]
    dados_formatados.append(linha)

df = pd.DataFrame(dados_formatados, columns=["Registro", "Veiculo", "Nome do Cliente", "Ano do Carro", "Cliente", "Tipo de Problema", "eixos", "peso", "altura", "comprimento"])

# Salve o DataFrame em um arquivo CSV
df.to_csv('seuarquivo10.csv', index=False)

print("Conversão concluída com sucesso!")
