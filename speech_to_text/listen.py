import speech_recognition as sr


def listen_microfone():
    #Habilita o microfone para ouvir o usuario
    microfone = sr.Recognizer()
    frase = ""
    with sr.Microphone() as source:
        #Chama a funcao de reducao de ruido disponivel na speech_recognition
        microfone.adjust_for_ambient_noise(source)
        print("Diga alguma coisa: ")
        audio = microfone.listen(source)
    try:
        frase = microfone.recognize_google(audio,language='pt-BR')
    except Exception as e:
        print("Não entendi")
    
    return frase

if __name__ == "__main__":
    result = ""
    while result != "sair":
        result = listen_microfone()
        print(result)