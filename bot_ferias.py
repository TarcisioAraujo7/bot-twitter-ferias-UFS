import tweepy
import os
from datetime import date, timedelta
from typing import List, NamedTuple

class Ferias(NamedTuple):
    nome: str
    inicio: date
    fim: date

FERIAS: List[Ferias] = [
    Ferias("Recesso Set/2025", date(2025, 9, 13), date(2025, 10, 5)),
    Ferias("Férias Fim de Ano 2025", date(2025, 12, 20), date(2026, 1, 11)),
    Ferias("Recesso Mar/2026", date(2026, 2, 28), date(2026, 3, 22)),
    Ferias("Recesso Jul/Ago 2026", date(2026, 7, 25), date(2026, 8, 16)),
    Ferias("Recesso de Final de Ano 2026", date(2026, 12, 19), date(2026, 12, 31)),
]

# --- AUTENTICAÇÃO TWITTER ---
BEARER_TOKEN         = os.getenv('BEARER_TOKEN')
API_KEY              = os.getenv('API_KEY')
API_KEY_SECRET       = os.getenv('API_KEY_SECRET')
ACCESS_TOKEN         = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET  = os.getenv('ACCESS_TOKEN_SECRET')

client = tweepy.Client(
    bearer_token=BEARER_TOKEN,
    consumer_key=API_KEY,
    consumer_secret=API_KEY_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET,
    wait_on_rate_limit=True
)

hoje = date.today()

def encontra_ferias_atual(data: date) -> Ferias:
    for p in FERIAS:
        if p.inicio <= data <= p.fim:
            return p
    return None

def encontra_proximas_ferias(data: date) -> Ferias:
    futuros = [p for p in FERIAS if p.inicio > data]
    return min(futuros, key=lambda p: p.inicio) if futuros else None

def formata_mensagem(dias: int, contexto: str) -> str:
    if contexto == 'antes':
        if dias > 15:
            return f'As férias começam em {dias} dias.'
        if 5 < dias <= 15:
            return f'Reta final! Faltam apenas {dias} dias para as férias.'
        if 1 < dias <= 5:
            return f'Contagem regressiva! Restam {dias} dias para as férias.'
        if dias == 1:
            return 'É amanhã! Finalmente começam as férias. 🎉'
    else:  # durante as férias
        if dias > 15:
            return f'As férias irão terminar em {dias} dias.'
        if 5 < dias <= 15:
            return f'Faltam apenas {dias} dias para acabar as férias.'
        if 1 < dias <= 5:
            return f'Contagem regressiva! Restam {dias} dias de férias.'
        if dias == 1:
            return 'Acaba amanhã! Só mais 1 dia de férias. Aproveite! 😎'
    return ''

def tuitar_dias():
    atual = encontra_ferias_atual(hoje)
    if atual:
        dias_restantes = (atual.fim - hoje).days
        mensagem = formata_mensagem(dias_restantes, 'durante')
    else:
        proximo = encontra_proximas_ferias(hoje)
        if not proximo:
            print("Nenhum período de férias futuro cadastrado.")
            return
        dias_restantes = (proximo.inicio - hoje).days
        mensagem = formata_mensagem(dias_restantes, 'antes')

    if mensagem:
        client.create_tweet(text=mensagem)
        print("Tweet enviado:", mensagem)
    else:
        print("Nenhuma condição de mensagem satisfeita.")

tuitar_dias()
