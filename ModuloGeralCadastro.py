def AdicionarAluno(alunos):
    nome = input('Nome : ')
    matricula = input('Digite a matricula do aluno :')
    alunos[matricula]=nome.lower()

def removerAluno (alunos):
    matricula = input('Digite o número da matricula para excluir :')
    alunos.pop(matricula)

def AtualizarAluno(alunos):
    matricula = input("Digite o número de matrícula do aluno que deseja atualizar: ")
    if matricula in alunos:
        novo_nome = input("Digite o novo nome do aluno: ")
        alunos[matricula] = novo_nome
        print("Nome do aluno atualizado com sucesso!")
    else:
        print("Aluno não encontrado.")
def VerAlunos (alunos):
    print("Lista de alunos:")
    for matricula, nome in alunos.items():
        print(f'Matrícula: {matricula}\n '
              f'Nome: {nome}')
    
alunos = {}

while True:
    escolha = int(input('Escolha uma opção :\n'
                        '1 - Cadastrar novo aluno ?\n'
                        '2 - Visualizar dados dos alunos : \n'
                        '3 - Atualizar Cadastro : \n'
                        '4 - Apagar aluno cadastrado :\n'
                        '0 - Finalizar cadastros .\n'))
    match escolha:
        case 1 :
            AdicionarAluno(alunos)

        case 2 :
            VerAlunos(alunos)

        case 3 :
            AtualizarAluno (alunos)
        
        case 4 :
            removerAluno(alunos)

        case 0 :
            print('Cadastro de alunos finalizado !')
            break