###se importan las librerias (SpeechRecognition keyboard pyaudio)  ###
import speech_recognition as sr 
# se elige que archivo se va a transcribir (este siempre tiene que se wav)
filename = "PRIMERA CLASE/prueba de transcripcion/audio1.wav"
# y como va a lllamarse el texto donde quedara escrito
outfile = "transcripcion.txt"
r= sr.Recognizer()

try:
    #se usa el archivo que se va a transcribir
    with sr.AudioFile(filename) as source:
        #y alargar la duracion de este mismo 
        duration= int (source.DURATION)
        full_transcription= ""
        print ("procesando audio")
        for i in range(0, duration, 10):
            try: 
                #se elige formato y el tipo de idiama al que traducir  
                audio_data= r.record(source,duration=10)
                text= r.recognize_google(audio_data, language="es-ES")
                full_transcription += text + "\n"
                print (f"fragmento {i // 10+1}: {text}")
                
                #se escriben los errores que pueden ocurrir
            except sr.UnknownValueError:
                print (f"Fragmento {i // 10+1}: No se pudo entender el audio")
                full_transcription += "[No se pudo entender el audio]\n"
            except sr.RequestError as e:
                print (f"Error al comunicarse con google {e}")
                break
            # la finalizacion del archivo 
        with open(outfile, 'w', encoding="utf-8") as f:
            f.write(full_transcription)
        print ("Transcripción completada y guardada en", outfile)
        # y por si no se encuentra el archivo
except FileNotFoundError:
    print (f"El archivo {filename} no se encuentra, asegurarse que el archivo este bien ubicado")
except ValueError:
    print ("El formato de audio no es compatible con google speech recognition")
except Exception:
    print ("Error desconocido")
    