from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, insert, delete, update
from secrets import *

# Cria Engine
engine = create_engine(
    f'mysql+pymysql://{user}:{password}@localhost/mercado')


class CrudProducts():
    def __init__(self):
        # Cria Base praparada a refletir o que já existe no banco de dados
        Base = automap_base()
        Base.prepare(engine, reflect=True)

        self.session = Session(engine)
        self.connection = engine.connect()

        # Obtem tabelas do banco de dados
        self.Product = Base.classes.produto
        # self.Cart = Base.classes.carrinho
        # self.CartProduct = Base.classes.carrinho_produto

    def query2object(self, query_records):
        result_object = []
        for row in query_records:
            d = {}
            for column in row.__table__.columns:
                d[column.name] = str(getattr(row, column.name))
            result_object.append(d)

        return result_object

    def create(self, creation_object):
        stmt = (
            insert(self.Product).
            values(nome=creation_object["nome"], preco=creation_object["preco"], categoria=creation_object["categoria"],
                   marca=creation_object["marca"], descricao=creation_object["descricao"], desconto=creation_object["desconto"])
        )

        with engine.connect() as conn:
            result = conn.execute(stmt)

        return result

    def get_all(self):
        records = self.session.query(self.Product).all()
        return self.query2object(records)

    def get_by_id(self, id_produto):
        record = self.session.query(
            self.Product).filter_by(id_produto=id_produto)
        return self.query2object(record)[0]

    def update_by_id(self, id_produto, update_object):
        record = self.get_by_id(id_produto)

        for key, value in update_object.items():
            record[key] = value

        stmt = (
            update(self.Product).
            where(self.Product.id_produto == id_produto).
            values(nome=record["nome"], preco=record["preco"], categoria=record["categoria"],
                   marca=record["marca"], descricao=record["descricao"], desconto=record["desconto"])
        )

        with engine.connect() as conn:
            result = conn.execute(stmt)
        
        return result

    def delete_by_id(self, id_produto):
        stmt = (
            delete(self.Product).
            where(self.Product.id_produto == id_produto)
        )
        with engine.connect() as conn:
            result = conn.execute(stmt)

        return result
