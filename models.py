from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///Atribuicao.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         bind=engine,))
Base = declarative_base()
Base.query = db_session.query_property()

class Contrato(Base):
    __tablename__ = 'ATRIBUICAO'
    __table_args__ = {'extend_existing': True} 
    id = Column(Integer, primary_key = True)
    contrato = Column(String(250), nullable=False)
    horas_habeis = Column(Integer, nullable=False)

class Disciplina(Base):
    __tablename__ = 'ATRIBUICAO'
    __table_args__ = {'extend_existing': True} 
    id = Column(Integer, primary_key = True)
    cod_jupiter = Column(String(250), nullable=False)
    disciplina = Column(String(250), nullable=False)
    contrato = Column(String(250), nullable=False)

class Atribuicao(Base):
    __tablename__ = 'NOVA_ATRIBUICAO'    
    cod_jupiter = Column(String(250), primary_key = True)
    disciplina = Column(String(250), nullable=False)
    contrato = Column(String(250), nullable=False)
    def save(self):
        db_session.add(self)
        db_session.commit()


def init_db():
    Base.metadata.create_all(bind=engine)
 
if __name__ == '__main__':
    init_db()
