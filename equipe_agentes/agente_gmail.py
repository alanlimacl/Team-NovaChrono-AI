import os
from agno.agent import Agent
from agno.tools.google.gmail import GmailTools


DIRETORIO_ATUAL = os.path.dirname(os.path.abspath(__file__))
DIRETORIO_RAIZ = os.path.dirname(DIRETORIO_ATUAL)
CAMINHO_CREDENCIAIS = os.path.join(DIRETORIO_RAIZ, 'credentials.json')
CAMINHO_TOKEN = os.path.join(DIRETORIO_RAIZ, 'token_gmail.json')

ferramenta_gmail = GmailTools(credentials_path=CAMINHO_CREDENCIAIS, token_path=CAMINHO_TOKEN, port=8080)

def funcao_agente_gmail():
    agente = Agent(
        name='Agente Gmail',
        tools=[ferramenta_gmail],
        description="Este agente TEM ACESSO e ESTÁ CONFIGURADO para buscar, ler e enviar e-mails do usuário. Transfira qualquer solicitação sobre e-mails para este agente.",
        instructions="""Você é responsável por utilizar a função Gmail.
        Regras INEGOCIÁVEIS:
        1. Limite a busca EXATAMENTE à quantidade solicitada.
        2. É PROIBIDO retornar links, URLs ou códigos HTML. Se remover um link, REMOVA também os parênteses vazios como ( ) ou [ ] que sobrarem.
        3. NÃO COPIE o corpo original do email. Você deve LER o email e escrever um RESUMO de no máximo 2 frases curtas.
        4. Use ESTRITAMENTE este formato e nada mais:
        - De: [Apenas o Nome do Remetente]
        - Data: [Data formato DD/MM/AAAA]
        - Assunto: [Assunto]
        - Resumo: [Seu resumo de 2 frases curtas]"""
    )
    return agente

