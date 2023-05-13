import googletrans

import io
import csv

traductor = googletrans.Translator()
idiomas = googletrans.LANGUAGES
texto = input()


headers = ['idioma', 'texto']

with open(f'{texto}.csv','w',newline='') as file:
    writer = csv.writer(file)
    writer.writerow( headers)

    for shortName,longName in idiomas.items():
        traduccion = traductor.translate(text=texto,src='es',dest=shortName)    
        idioma = [longName,traduccion.text]
        
        try:
            writer.writerow(idioma)
        except Exception as e:
            print(f"{idioma[0]} : {idioma[1]}")
print('listo')