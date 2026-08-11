nomes = []
notas1 = []
notas2 = []

def exibir_menu():
    print("===== MENU =====")
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Estatísticas da turma")
    print("4 - Sair")


def cadastrar_aluno(nomes, notas1, notas2):
    nome=input("Digite o nome do aluno: ")
    nota1=int(input("Digite a primeira nota do aluno: "))
    nota2=int(input("Digite a segunda nota do aluno: "))
    nomes.append(nome)
    notas1.append(nota1)
    notas2.append(nota2)

def calcular_media(nota1, nota2):
    media = (nota1 + nota2) / 2
    return media

def situacao(media):
    if media >= 6:
        situacao = "Passou"
    else: situacao = "Reprovou"
    return situacao

def listar_alunos(nomes):
    return print(f"Lista de alunos:{nomes}")

def estatisticas_turma(nomes, notas1, notas2):
    total_alunos = len(nomes)

    soma_medias = 0
    aprovados = 0
    reprovados = 0

    for i in range(len(nomes)):
        media = calcular_media(notas1[i], notas2[i])

        soma_medias += media

        if media >= 6:
            aprovados += 1
        else:
            reprovados += 1

    media_turma = soma_medias / total_alunos

    return f"As estatísticas da turma são: total de alunos = {total_alunos}; Média da turma = {media_turma:.2f}; Aprovados = {aprovados}; Reprovados = {reprovados}"

while True:
    exibir_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_aluno(nomes, notas1, notas2)
    elif opcao == "2":
        listar_alunos(nomes)
    elif opcao == "3":
        print(estatisticas_turma(nomes, notas1, notas2))
    elif opcao == "4":
        break
