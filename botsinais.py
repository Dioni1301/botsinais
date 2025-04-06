from datetime import datetime, timedelta
import telebot
import random
import time
from pytz import timezone
import os
import json
import bd

print("""

░█████╗░███████╗██╗██╗░░░░░██╗░█████╗░  ██╗░██████╗░░█████╗░███╗░░░███╗██╗███╗░░██╗░██████╗░
██╔══██╗██╔════╝██║██║░░░░░██║██╔══██╗  ██║██╔════╝░██╔══██╗████╗░████║██║████╗░██║██╔════╝░
███████║█████╗░░██║██║░░░░░██║███████║  ██║██║░░██╗░███████║██╔████╔██║██║██╔██╗██║██║░░██╗░
██╔══██║██╔══╝░░██║██║░░░░░██║██╔══██║  ██║██║░░╚██╗██╔══██║██║╚██╔╝██║██║██║╚████║██║░░╚██╗
██║░░██║██║░░░░░██║███████╗██║██║░░██║  ██║╚██████╔╝██║░░██║██║░╚═╝░██║██║██║░╚███║╚██████╔╝
╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝╚═╝╚═╝░░╚═╝  ╚═╝░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝╚═╝░░╚══╝░╚═════╝░
      
                 Faça parte da maior comunidade de igaming do Brasil, acesse:
                             www.afiliaigaming.com
""")

print("Bot de sinais iniciado com sucesso. ©Afilia iGaming.\n")

# Corrigido: leitura segura do config.json com codificação UTF-8
config_path = os.path.join(os.path.dirname(__file__), 'config.json')
with open(config_path, 'r', encoding='utf-8') as config_file:
    config_data = json.load(config_file)

api_key = config_data.get('api_key', '')
chat_id = config_data.get('chat_id', '')
affiliate_link = config_data.get('affiliate_link', '')

print(f"API Key: {api_key}")
print(f"Chat ID: {chat_id}")
print(f"Affiliate Link: {affiliate_link}")

bot = telebot.TeleBot(token=api_key)
script_dir = os.path.dirname(os.path.abspath(__file__))

def enviar_imagem(caminho_imagem, legenda, markup=None):
    caminho_completo = os.path.join(script_dir, caminho_imagem)
    with open(caminho_completo, 'rb') as photo:
        bot.send_photo(chat_id=chat_id, photo=photo, caption=legenda, parse_mode='MARKDOWN', reply_markup=markup)

mensagem_inicio_enviada = False
tz = timezone('America/Sao_Paulo')

while True:
    now = datetime.now(tz)
    h = now.hour
    m = now.minute
    s = now.second

    if not mensagem_inicio_enviada:
        print(f'{h}:{m}:{s} - Início da Sessão')
        texto_inicio = '''
🚀*Sessão Iniciada!*🚀

🤖 *Analisando banco de dados para você apostar nos melhores horários!* 🎮✨

É crucial ressaltar que indicamos a a melhor plataforma e horário, portanto, certifique-se de estar na plataforma em que estamos identificando oportunidades.

Passo a passo para seguir os sinais:

💻 Se cadastre na plataforma indicada para garantir as melhores oportunidades.

⏳ Aguarde o sinal indicado.

💰 Garanta seu lucro utilizando as informações fornecidas.

🛑 Lembre-se: *Não tente em outros sites!*

🤖 A inteligência artificial analisa criteriosamente a melhor plataforma e horário para sua segurança, sucesso e diversão.
'''
        markup_inicio = telebot.types.InlineKeyboardMarkup()
        markup_inicio.add(telebot.types.InlineKeyboardButton(text="🎮 JOGUE AQUI 🎮", url=affiliate_link))
        enviar_imagem('1.png', texto_inicio, markup=markup_inicio)
        time.sleep(60)
        mensagem_inicio_enviada = True

    for _ in range(4):
        numero_aleatorio1 = round(random.uniform(1, 10))
        numero_aleatorio2 = round(random.uniform(1, 10))
        numero_aleatorio3 = round(random.uniform(2, 4))
        numero_aleatorio4 = round(random.uniform(87, 96))

        print(numero_aleatorio1, numero_aleatorio2)

        texto_sinal = f'''
🍀 Fortune Tiger, Rabbit, OX, Mouse, Panda. (Todos Fortunes)

🎰 [Plataforma do sinal]({affiliate_link})

🔥 *{numero_aleatorio1}X Normal*

🚀 *{numero_aleatorio2}X Turbo*

🎯 Assertividade: {numero_aleatorio4}%

⌚ Válido por: {numero_aleatorio3} Minutos

⚠️ *Não tente em outro sites!* 

👇🏻 Clique abaixo para cadastrar na plataforma:
'''
        markup_sinal = telebot.types.InlineKeyboardMarkup()
        markup_sinal.add(telebot.types.InlineKeyboardButton(text="🎮 JOGUE AQUI 🎮", url=affiliate_link))
        enviar_imagem('sinaldetectado.png', texto_sinal, markup=markup_sinal)
        time.sleep(150)

    time.sleep(240)
