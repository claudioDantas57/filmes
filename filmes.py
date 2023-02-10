import sqlalchemy as db
import pymysql
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, String, Numeric
from sqlalchemy.sql import functions


engine = db.create_engine("mysql+pymysql://root:@localhost:3306/filmes")
Base = declarative_base()

class Filmes(Base):
    __tablename__ = 'titulos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    genero = Column(String(60))
    quantidade = Column(Numeric)



Base.metadata.create_all(engine)

g1 = Filmes(genero = "drama", quantidade = 20)
g2 = Filmes(genero = "terror", quantidade  = 20)
g3 = Filmes(genero = "comedia", quantidade  = 20)
g4 = Filmes(genero = "aventura", quantidade  = 20)

Session = sessionmaker(bind=engine)
session = Session()



#session.add_all([g1, g2, g3, g4])
#session.commit()




def consultar():
    consulta = session.query(Filmes).all()
    for filme in consulta:
        print(filme.id,filme.genero, filme.quantidade)


def alterar():
    consultar()
    id_titulos = int(input("Digite o ID do gênero que terá a quantidade alterada: "))
    titulos = session.query(Filmes).filter(Filmes.id == id_titulos).one()
    quantidade = int(input("Informe a quantidade de titulos a ser alterada: "))
    titulos.quantidade = quantidade
    session.commit()


def deletar():
    consultar()
    id_titulos = int(input("Digite o ID do gênero que será deletado: "))
    titulos = session.query(Filmes).filter(Filmes.id == id_titulos).one()
    session.delete(titulos)
    session.commit()


def inserir():
    n_genero =input('digite o gênero a ser inserido: ')
    qdt_titulos= int(input('digite a quantidade de títulos: '))
    new_genero = Filmes(genero=n_genero, quantidade=qdt_titulos)
    session.add(new_genero)
    session.commit()




while True:
    print("MENU DE OPÇÕES:\n"
          "- Digite 1 para consultar a quantidade de filmes por gênero. \n"
          "- Digite 2 para alterar a quantidade. \n"
          "- Digite 3 para deletar a quantidade gênero. \n"
          "- Digite 4 para inserir  a quantidae gênero. \n"
          "- Digite 5 para sair.\n")

    opcao = int(input("Informe a opção desejada: "))

    if opcao == 1:
        print("Você quer ver o gênero e a quantide de títulos.")
        consultar()

    elif opcao == 2:
        print("Você quer alterar a quantidade de títulos por gênero.")
        alterar()
    elif opcao == 3:
        print("Você quer deletar um gênero.")
        deletar()
    elif opcao == 4:
        print("Você quer inserir um gênero.")
        inserir()
    elif opcao == 5:
        break
