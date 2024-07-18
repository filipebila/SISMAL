#Estrutura principal do programa de planejamento e execução da logística de transporte de material universitário


#Importando as bibliotecas necessárias
import pandas as pd


#Listando as funções necessárias

#Cadastrando os locais de destino
def cadastro_omse():
    candidatos = int(input("Quantidade de Candidatos: "))
    salas = int(input("Quantidades de Salas/Setores: "))
                     
    print('ok')
    return candidatos, salas


#Cadastrando materiais
def cadastro_material():
    print('ok1')
    
#Calculando peso e volumes
def peso_volumes(candidatos, salas):
    print('ok2', candidatos, salas)
    
#Gerando guias de transporte
def gera_guia():
    print('ok3')
    
def main():
    candidatos, salas = cadastro_omse()
    cadastro_material()
    peso_volumes(candidatos, salas)
    gera_guia()
    
if __name__ == "__main__":
    main()