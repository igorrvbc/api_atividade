from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
# Para criar conexão com o banco, abrir sessão
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.orm import declarative_base

# 'convert_unicode' para lidar com a acentuação no bd.
engine = create_engine('sqlite:///atividades.db')

# AUTOCOMMIT para commit sozinho, BINDS para referenciar o bd para abrir a sessão.
db_session = scoped_session(sessionmaker(autocommit=False, bind=engine))

# Default para criar o bd de sqlite e para alterar/consultar.
Base = declarative_base()
Base.query = db_session.query_property()


# Criando a Tabela Pessoas:
class Pessoas(Base):
    __tablename__ = 'pessoas'
    id = Column(Integer, primary_key=True)
    nome = Column(String(40), index=True)
    idade = Column(Integer)

    def __repr__(self):
        return '<Pessoa {}>'.format(self.nome)

# Inserir dados no BD. (obs: Lembra o Git)
    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()


# Criando a tabela Atividades
class Atividades(Base):
    __tablename__ = 'atividades'
    id = Column(Integer, primary_key=True)
    nome = Column(String(80))
    pessoa_id = Column(Integer, ForeignKey('pessoas.id'))
    pessoa = relationship("Pessoas")

    def __repr__(self):
        return '<Atividades {}>'.format(self.nome)

    # Inserir dados no BD. (obs: Lembra o Git)
    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

def init_db():
    Base.metadata.create_all(engine)


if __name__ == '__main__':
    init_db()
