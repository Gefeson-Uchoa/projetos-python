'''
app transforma texto em audio, voce pode escolher a linguagem que sera reproduzida o audio
'''

from gtts import gTTS
from playsound import playsound

audio = 'audio.mp3'
linguagem = 'pt-br'
texto = 'sejam bem vindos ao meu repositorio no Github, me chamo Gefeson'  # aqui voce escreve a mensagem

sp = gTTS(
    text=texto,
    lang=linguagem
)

sp.save(audio)
playsound(audio)