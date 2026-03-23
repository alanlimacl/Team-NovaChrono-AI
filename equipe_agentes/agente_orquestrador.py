import os
from agno.team import Team
from dotenv import load_dotenv
from agno.models.openrouter import OpenRouter

from equipe_agentes.agente_hack_news import agente_hnew
from equipe_agentes.prompt import INSTRUCAO_ORQUESTRADOR
from equipe_agentes.agente_agenda import agente_agnd

load_dotenv()

BASE_OPEN_ROUTER = os.getenv("OPENROUTER_BASE_URL")
OPEN_ROUTER_KEY = os.getenv("OPENROUTER_API_KEY")
MODELO = os.getenv('MODELO')


equipe_agentes = Team(
    name='Equipe NovaChrono',
    members=[agente_hnew(), agente_agnd()],
    model=OpenRouter(
        id=MODELO,
        api_key=OPEN_ROUTER_KEY,
    ),
    debug_mode=True

)

resposta = equipe_agentes.print_response('qual meu compromisso para amanha', stream=True)
