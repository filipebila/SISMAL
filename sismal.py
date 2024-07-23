#Estrutura principal do programa de planejamento e execução da logística de transporte de material universitário


#Importando as bibliotecas necessárias
import pandas as pd
import csv

#Listando as funções necessárias
    #Cadastrando os locais de destino
def cadastro_omse():
    omse = {}
    omse['Número da OMSE'] = int(input('Número da OMSE: '))
    omse['Organização Militar'] = input('Organização Militar: ')
    omse['Quantidade de Candidatos'] = int(input('Quantidade de Candidatos: '))
    omse['Endereço da OM'] = input('Endereço da OM: ')
    omse['Local de prova'] = input('Endereço do local de prova: ')
    omse['Quantidade de setores de prova'] = int(input('Quantidade de setores: '))
    
    omse['Quantidade de Setores ate 12'] = int(input('Quantidade de setores até 12: '))
    omse['Quantidade de Setores ate 22'] = int(input('Quantidade de setores até 22: '))
    omse['Quantidade de Setores ate 27'] = int(input('Quantidade de setores até 27: '))
    omse['Quantidade de Setores ate 33'] = int(input('Quantidade de setores até 33: '))
    omse['Quantidade de Setores ate 39'] = int(input('Quantidade de setores até 39: '))
    omse['Quantidade de Setores ate 45'] = int(input('Quantidade de setores até 45: '))
    omse['Quantidade de Setores ate 99'] = int(input('Quantidade de setores até 99: '))   
       
    print(omse)
    
    return omse

    
    
   # with open(arquivo_csv, mode='a', newline='') as file:
    #    writer = csv.DictWriter(file, fieldnames=omse.keys())
     #   writer.writeheader()
      #  writer.writerow(omse)
          
   
    

    #Cadastrando materiais
#def cadastro_material():
    #print('ok1')
    
    #Calculando peso e volumes
#def peso_volumes(candidatos, salas):
    #print('ok2', candidatos, salas)
    
    #Gerando guias de transporte
#def gera_guia():
    #print('ok3')
    
def main():
    #candidatos, salas = cadastro_omse()
    omse = cadastro_omse()
    omse_df = pd.DataFrame(omse, index= [omse['Número da OMSE']])
    
    omse_df.to_csv('omse.csv')
    
    print('Dados salvos')
    #peso_volumes(candidatos, salas)
    #gera_guia()
    
if __name__ == "__main__":
    main()