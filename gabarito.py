# Cadastrar aluno (nome + 2 notas)
# Listar todos alunos cadastrados
# Mostrar estatísticas da turma (3.1- total de alunos, 3.2 - média, 3.3 - aprovados/reprovados)
# Sair do programa
#
# Crie 3 listas: nomes, notas1, notas2
#
# Funções:
# exibir_menu()
# cadastrar_aluno(nomes, notas1, notas2)
# calcular_media(n1,n2) (retorne uma lista com a média de cada aluno)
# situacao(media) (retorna uma lista se o aluno foi aprovado/reprovado)
# listar_alunos(nomes,notas1,notas2) (listar os alunos e nota de cada um deles)
# estatisticas_turma(nomes, notas1, notas2) (calcular quantos aprovados e reprovados)

nomes = []
n1 = []
n2 = []
m = []

def exibir_menu():
    print('Seja bem vindo ao sistema de notas da FIAP')
    print('Digite:')
    print('1 - Cadastrar aluno e as notas 1 e 2 do CP')
    print('2 - Listar alunos cadastrados e suas respectivas notas')
    print('3 - Mostrar total de alunos')
    print('4 - Mostrar a média de cada aluno')
    print('5 - Qtde de alunos aprovados e reprovados')
    print('6 - Para sair')
    print()
    print()

def cadastrar(nome_aluno, nota1, nota2):
    nomes.append(nome_aluno)
    n1.append(nota1)
    n2.append(nota2)

def listar_alunos(nomes, n1, n2):
    for j in range(len(nomes)):
        print(f'{nomes[j]}: 1){n1[j]:.1f}; 2){n2[j]:.1f};')

def media(nomes, n1, n2):
    for i in range(len(n1)):
        m.append( (n1[i] + n2[i])/2 )

    for j in range(len(nomes)):
        print(f'{nomes[j]}: {m[j]}')

def aprovados(n1, n2):
    aprovado = 0
    reprovado = 0
    for i in range(len(n1)):
        if (n1[i] + n2[i])/2 >= 6:
            aprovado += 1
        else:
            reprovado += 1
    return [aprovado, reprovado]



while True:
    exibir_menu()
    op = input('Digite a opção desejada: ')
    if op == '1':
        nome_aluno = input('Digite o nome do aluno:')
        nota1 = float(input('Digite a nota da CP1 do aluno:'))
        nota2 = float(input('Digite a nota da CP2 do aluno:'))
        cadastrar(nome_aluno, nota1, nota2)
    elif op == '2':
        listar_alunos(nomes,n1, n2)
    elif op == '3':
        print(f'O total de alunos é: {len(nomes)}.')
    elif op == '4':
        media(nomes, n1, n2)
    elif op == '5':
        a = aprovados(n1, n2)[0]
        r = aprovados(n1, n2)[1]
        print(f'Temos: {a} aprovados e {r} reprovados!')
    elif op == '6':
        break
    else:
        print('Opção inválida!')

