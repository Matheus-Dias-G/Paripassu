import sys
from datetime import date
from unidecode import unidecode

today = date.today()
today = today.strftime('%d/%m/%y')

providers = {'Antônio Marcos': '91.391.397/0001-45', 'Água de Coco':'91.393.397/0001-46'}


top = 'documento elo erigem;data;nome produto;quantidade'
def main():
    if len(sys.argv) < 2:
        print('Uso: python paripassu.py <text>')
        sys.exit(1)

    text = sys.argv[1]
    text = text.split("\n")
    index_list = range(0, len(text))
    for n in index_list:
        text[n] = text[n].split(', ')
        #print(text[n][0])

        for provider in providers.keys():
            if unidecode(text[n][0].lower()) == unidecode(provider.lower()):
                #text[n][0] =  providers[provider]
                print(providers[provider])
if __name__ == "__main__":
    main()
