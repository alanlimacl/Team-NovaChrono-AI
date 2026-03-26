import os
from agno.models.openrouter import OpenRouter
from agno.team import Team
from agno.db.sqlite import SqliteDb
from dotenv import load_dotenv

from equipe_agentes.agente_hack_news import funcao_agente_hackernews
from equipe_agentes.agente_agenda import funcao_agente_agenda
from equipe_agentes.agente_gmail import funcao_agente_gmail
from equipe_agentes.agente_financeiro import funcao_agente_fianceiro

load_dotenv()

BASE_OPEN_ROUTER = os.getenv("OPENROUTER_BASE_URL")
OPEN_ROUTER_KEY = os.getenv("OPENROUTER_API_KEY")
MODELO = os.getenv('MODELO')

armazenamento_equipe = SqliteDb(db_file='banco_dados/memoria_agente.db')


equipe_agentes = Team(
    name='Equipe NovaChrono',
    members=[funcao_agente_hackernews(), funcao_agente_agenda(), funcao_agente_gmail(), funcao_agente_fianceiro()],
    model=OpenRouter(
        id=MODELO,
        api_key=OPEN_ROUTER_KEY,
    ),
    db=armazenamento_equipe,
    add_history_to_context=True,
    num_history_messages=5,
    instructions="""Você é o orquestrador (líder) da equipe.
    Sua ÚNICA função é delegar a pergunta do usuário para o membro correto.
    REGRAS OBRIGATÓRIAS:
    1. NUNCA tente responder perguntas sobre e-mails, agenda ou notícias sozinho.
    2. O Agente Gmail ESTÁ configurado. Transfira a tarefa para ele.
    3. Quando o subordinado devolver a resposta, APENAS REPASSE EXATAMENTE O QUE ELE DISSE para o usuário. Não adicione introduções, não tente formatar novamente e não faça resumos extras.""",
    debug_mode=True)


def perguntar_agente(pergunta):
    resposta = equipe_agentes.run(pergunta)
    
    return resposta.content


