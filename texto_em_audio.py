#pinheirocfc@gmail.com
#Instrucoes em https://youtu.be/BtwHAvsNaA8

import pyttsx3 #pip instal pyttsx3

#le o texto que esta guardado em um arquivo .txt
f = open('C:/Users/pinheiro/Google Drive/Projetos Python/Modelos/Temporarios/Hino Plameiras.txt', 'r', encoding="utf8")
texto = f.read()

speaker = pyttsx3.init() #inicia serviço biblioteca
voices = speaker.getProperty('voices') #metodo de voz

#ver as vozes instaladas na maquina
for voice in voices:
    print(voice, voice.id) #traz os idiomas de voz instalados em sua maquina
    
speaker.setProperty('voice', voices[2].id) #define a voz padrao, no meu caso o portugues era o[2] (iniciando do zero)
rate = speaker.getProperty('rate')
speaker.setProperty('rate', rate-25) #muda velocidade da leitura, quando menor mais lento

print(texto) #escreve o texto na tela
speaker.say(texto) #define o texto que será lido
speaker.runAndWait() #le o texto
f.close() #fecha o modo deleitura do arquivo txt
