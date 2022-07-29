import tweepy
from datetime import date

auth = tweepy.OAuthHandler('Sua autenticação', 'Sua autenticação')
auth.set_access_token('Seu token de acesso',
                      'Seu token de acesso')
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

hoje = date.today()
data_ferias: date = date(2022, 11, 25) # É necessario alterar as datas ao decorrer da mudança dos periodos
data_aulas: date = date(2022, 7, 4)

if hoje < data_aulas < data_ferias or data_ferias <= hoje < data_aulas:
    ferias = True
else:
    ferias = False


def tuitar_dias():
    if ferias:
        faltam = (data_aulas - hoje).days
        if 5 < faltam < 45:
            api.update_status(f'Faltam {faltam} dias para acabar as férias da UFS.')

        if 5 >= faltam > 1:
            api.update_status(f'Contagem regressiva! Restam apenas {faltam} dias de férias.')

        if faltam == 1:
            api.update_status('Acabou!!! Temos apenas mais 1 dia de férias, aproveitem bem. :)')

    else:
        faltam = (data_ferias - hoje).days
        if faltam > 15:
            api.update_status(f'As férias da UFS começam em {faltam} dias.')

        if 15 >= faltam > 1:
            api.update_status(f'Reta final! faltam apenas {faltam} dias para as férias da UFS.')

        if faltam == 1:
            api.update_status(
                f'É amanhã!!! finalmente as férias da UFS começam em {faltam} dia, aproveitem e descansem '
                f'bastante. :)')


tuitar_dias()
