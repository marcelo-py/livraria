#by: Marcelo dos Santos
class Livraria:
    def __init__(self, arq):
        self.arq = arq
        self.arquivoexiste = False
        self.livros = dict()

    def arquivo_existe(self):
        try:
            a = open(self.arq, 'rt')
            a.close()
        except FileNotFoundError:
            print('Aruivo não existe!')
        else:
            self.arquivoexiste = True


    def criar_arquivo(self):
        if not self.arquivoexiste:
            try:
                a = open(self.arq, 'wt+')
                a.close()

            except:
                print('Erro ao criar o arquivo {}'.format(self.arq))
            else:
                print('Arquivo criado com sucesso!')

    def add_livros(self, nome, autor, tipo='<desconhecido>'):
        try:
            a = open(self.arq, 'at')
        except:
            print('Erro ao adcionar livro')
        else:
            try:
                a.write('{}; {}; {}\n'.format(nome, autor, tipo))
            except:
                print('Erro ao adcionar livro e autor')
            else:
                print('Livro adcionado com sucesso ao banco de dados!')


    def livros_disponiveis(self):
        print('{:^66}'.format('Lista de livros disponiveis'))
        print('='*66)
        #esse for vai ficar aqui ate eu pensar em um lugar melhor pra colocar ele, mas n deve ficar aqui
        for c in open(self.arq):
            c = c.strip().split(';')
            c[2] = c[2].replace('\n', '')
            self.livros[c[0]] = c[1].strip().lower(), c[2].strip().lower()
        for livro in self.livros.items():
            print('Titulo: {}; Autor(a): {}; Tipo: {}'.format(livro[0], livro[1][0], livro[1][1]))

    def procurar(self, op):
        # aqui é uma das referencias das pesquisas
        titulo = ''.replace(' ', '').strip().lower()
        autor = ''.replace(' ', '').strip().lower()
        tipo = ''.replace(' ', '').strip().lower()

        #jogando o que deve ser titulo para variavel titulo
        for v in self.livros.keys():
            titulo += v.lower().strip().replace(' ', '') #concatenando e preparando para pesquisas no metodo

        #jogando os valores que pertencem aos titulos o que deve ser autor e tipo de livro(ambos se encontram em uma tupla dentro do atributo self.livros
        for v in self.livros.values():
            autor+= v[0].strip().lower() #concatenando e preparando para pesquisas
            tipo+= v[1].lower().lower()

        #se o usuario digitar o que se parece um titulo de livo irá buscar livro por titulo
        if op in titulo and op not in autor and tipo:
            print('-'*50)
            print('Parce que vc tentou procurar um livro pelo titulo!')
            print('resultado da pesquisa:')
            for livros in self.livros.keys():
                if livros == op:
                    print('\033[1;32mtitulo:', livros, '\033[mautor: {}; tipo: {}'.format(*self.livros[livros]))

        #se tentar buscar livro pelo o que se parece ser um autor
        elif op in autor and op not in tipo and op not in titulo:
            print('Parece que você tentou  procurar por autor')
            print('resultado da pesquisa:')
            for l in self.livros:
                if self.livros[l][0] == op:
                    print('titulo: {}; \033[1;33mautor: {}\033[m; tipo: {}'.format(l, self.livros[l][0], self.livros[l][1]))

        #se tentar buscar livro pelo que se parece um tipo de livro
        elif op in tipo and op not in titulo and op not in autor:
            print('Parece que você tentou procurar por tipo de filme!')
            print('resultado da pesquisa:')
            for i in self.livros:
                if self.livros[i][1].lower() == op.lower():
                    print('titulo: {}; autor: {}; \033[1;33mtipo: {}\033[m'.format(i, self.livros[i][0], self.livros[i][1]))

        #se nenhuma especificação do livro não se encontrar no "bando de dados"
        else:
            print('Nenhum resultado encontrado!')

#programa principal
l = Livraria('livraria.txt')
l.arquivo_existe()
l.criar_arquivo()
l.livros_disponiveis()
while True:
    print('{:^60}'.format('Livraria'))
    print('-'*60)
    opç = int(input('''    1 - Ver livro disponiveis
    2 - Adicionar livro 
    3 - Procurar livro
    0 - Sair
    =>'''))
    if opç == 1:
        if len(l.livros) == 0:
            sn = input('Não há livros disponiveis na biblieoteca, deseja adicionar? Sim<S/N>Não')[0].upper()
            if sn == 'S':
                titulo = input('Digite o titulo do livro')
                autor = input('Digite o nome do autor do livro')
                tipo = input('Digite o tipo do livro')
                l.add_livros(titulo, autor, tipo)

        l.livros_disponiveis()
    elif opç == 2:
        titulo = input('Digite o titulo do livro')
        autor = input('Digite o nome do autor do livro')
        tipo = input('Digite o tipo do livro')
        if len(autor) == 0:
            autor = 'desconhecido'
        l.add_livros(titulo.strip(), autor.strip(), tipo.strip())
    elif opç == 3:
        proc = input('Digite um titulo, autor ou tipo de livro ').lower()
        l.procurar(proc)
    elif opç == 0:
        break
    else:
        print('Digite uma opção correta!')
