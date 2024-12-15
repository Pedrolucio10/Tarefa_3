import os
from datetime import datetime

def obter_resposta(texto: str) -> str:
    comando: str = texto.lower()

    respostas = {
        ('olá', 'boa tarde', 'bom dia'): 'Olá tudo bem!',
        'como estás': 'Estou bem, obrigado!',
        'como te chamas': 'O meu nome é: Bot :)',
        'tempo': 'Está um dia de sol!',
        ('bye', 'adeus', 'tchau'): 'Gostei de falar contigo! Até breve...',
        'horas': lambda: f'São: {datetime.now():%H:%M} horas',
        'data': lambda: f'Hoje é dia: {datetime.now():%d-%m-%Y}',
        'qual o teu trabalho?': 'Sou um chatbot, programado para ajudar!',
        'qual é o teu humor?': 'Estou sempre bem! 😊',
        'quem é o presidente de portugal?': 'O presidente de Portugal é o Marcelo Rebelo de Sousa.',
        'quantos anos tens?': 'Eu não tenho idade, sou um programa!',
        'onde vives?': 'Eu vivo na nuvem, na internet!'
    }

    for chave, resposta in respostas.items():
        if isinstance(chave, tuple):
            if comando in chave:
                return resposta
        elif chave in comando:
            # Verifica se a resposta é uma função (lambda) e a executa
            if callable(resposta):
                return resposta()
            return resposta

    return f'Desculpa, não entendi a questão! {texto}'

    for chave, resposta in respostas.items():
        if isinstance(chave, tuple):
            if comando in chave:
                return resposta
        elif chave in comando:
            return resposta

    if 'horas' in comando:
        return f'São: {datetime.now():%H:%M} horas'

    if 'data' in comando:
        return f'Hoje é dia: {datetime.now():%d-%m-%Y}'

    return f'Desculpa, não entendi a questão! {texto}'


def chat() -> None:
    print('Bem-vindo ao ChatBot!')
    print('Escreva "bye" para sair do chat')
    name: str = input('Bot: Como te chamas? ')
    print(f'Bot: Olá, {name}! \n Como te posso ajudar?')

    while True:
        user_input: str = input('Tu: ')
        resposta: str = obter_resposta(user_input)
        print(f'Bot: {resposta}')

        if resposta == 'Gostei de falar contigo! Até breve...':
            break

    print('Chat acabou')
    print()


def main() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')
    chat()


if __name__ == '__main__':
    main()
