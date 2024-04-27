import csv
import time

def registrar_tarefa(hora_atual, tarefa, titulo, nome, funcoes_outros, tempo_minutos, arquivo_csv):
    with open(arquivo_csv, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([hora_atual, tarefa, titulo, nome, funcoes_outros, tempo_minutos])

def main():
    # Nome do arquivo CSV para armazenar os dados
    arquivo_csv = 'registro_produtividade.csv'
    
    # Obter informações sobre cada tarefa
    tarefas = []
    while True:
        tarefa = input("Digite o nome da tarefa (ou digite 'fim' para parar): ")
        if tarefa.lower() == 'fim':
            break
        titulo = input("Digite o título relacionado à tarefa: ")
        nome = input("Digite o nome relacionado à tarefa: ")
        funcoes_outros = input("Digite outras informações (funções, etc.): ")
        tempo_minutos = int(input("Digite o tempo gasto na tarefa (em minutos): "))
        tarefas.append((tarefa, titulo, nome, funcoes_outros, tempo_minutos))
    
    # Registrar as tarefas
    hora_atual = time.strftime("%Y-%m-%d %H:%M:%S")
    for tarefa, titulo, nome, funcoes_outros, tempo_minutos in tarefas:
        registrar_tarefa(hora_atual, tarefa, titulo, nome, funcoes_outros, tempo_minutos, arquivo_csv)
        print(f"Tarefa '{tarefa}' registrada com sucesso.")
    
    print("Produtividade registrada no arquivo CSV com sucesso.")

if __name__ == "__main__":
    main()
