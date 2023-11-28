import csv
import sys
from datetime import date
from unidecode import unidecode

today = date.today()
today = today.strftime('%d/%m/%y')

providers = {'fornecedor1': '91.391.397/0001-45', 'fornecedor2':'91.393.397/0001-46'}


top = ['Documento elo origem', 'Data', 'Nome produto', 'Embalagem', 'Capacidade embalagem', 'Unidade Embalagem', 'Quantidade']
def main():
    if len(sys.argv) < 2:
        print('Uso: python paripassu.py <text>')
        sys.exit(1)

    text = sys.argv[1]
    #make the separation between products
    text = text.split("\n")
    index_list = range(0, len(text))
    for n in index_list:
        text[n] = text[n].split(', ')
        #adding data on text
        text[n][1] = today
        
        for provider in providers.keys():
            if unidecode(text[n][0].lower()) == unidecode(provider.lower()):
                text[n][0] =  providers[provider]
 
    with open('<seu diretorio>', 'w') as f:
        write = csv.writer(f)
        print(top)
        write.writerow(top)
        for product in text:
            write.writerow(product)
        f.close()
        print('Arquivo tabela.csv criado no diretorio:<seu diretorio>')
if __name__ == "__main__":
    main()
