from models import Pessoas

# Insere dados na tabela Pessoa
def insere_pessoas():
    pessoa = Pessoas(nome='IASpok', idade=12)
    print(pessoa)
    pessoa.save()

# Consulta dados na tabela Pesoa
def consulta():
    pessoas = Pessoas.query.all()
    print(pessoas)
    #for i in pessoa:
    #    print(i.id)
    pessoa = Pessoas.query.filter_by(nome='IASpok').first()
    print(pessoa.id)


# Altera dados na tabela Pessoa
def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Rafael').first()
    pessoa.idade = 21
    pessoa.save()


# Exclui dados na tabela Pessoa
def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='IASpok').first()
    pessoa.delete()


if __name__ == '__main__':
# insere_pessoas()
    #exclui_pessoa()
    consulta()
    #altera_pessoa()
