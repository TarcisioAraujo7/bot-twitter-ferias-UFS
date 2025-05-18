# Bot de Férias UFS 🐦🎓

Um bot em Python que publica automaticamente, todos os dias às 08:00 UTC, mensagens de contagem regressiva para os períodos de férias e recessos da Universidade Federal de Sergipe (UFS). Utiliza a API v2 do Twitter via Tweepy e é orquestrado pelo GitHub Actions.

[Bot Férias da UFS](https://twitter.com/UFS_ferias)

## 📋 Sumário

1. [Funcionalidades](#-funcionalidades)  
2. [Tecnologias](#-tecnologias)  
3. [GitHub Actions](#-github-actions)  
4. [Contribuições](#-contribuições)  


## 🔍 Funcionalidades

- **Detecção automática**: identifica se hoje está em período letivo ou de férias/recesso.  
- **Contagem regressiva**: calcula quantos dias faltam para o próximo início ou término de cada período.  
- **Mensagens personalizadas**: gera frases de celebração e alerta conforme o número de dias restante.  
- **Publicação no Twitter**: usa o endpoint v2 (`client.create_tweet`) do Tweepy para postar automaticamente.  
- **Agendamento via CI/CD**: roda diariamente às 08:00 UTC através de GitHub Actions.  


## ⚙️ Tecnologias

- **Linguagem**: Python 3.8+  
- **Biblioteca Twitter**: Tweepy (Client v2)  
- **Automação**: GitHub Actions  


## 🛠️ GitHub Actions
O workflow .github/workflows/tweet.yml executa:

1. **Checkout** do código  
2. **Setup** do Python 3.x  
3. **Instalação** das dependências (`tweepy`, `python-dotenv`)  
4. **Execução** de `bot_ferias.py` diariamente às 08:00 UTC


## 🤝 Contribuições

1. Abra uma **issue** descrevendo sua sugestão ou bug.  
2. Faça um **fork** e crie uma **branch** com sua melhoria.  
3. Envie um **pull request** detalhando as alterações.  