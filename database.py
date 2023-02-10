from sqlalchemy import Column, Integer, String, create_engine, text, UniqueConstraint, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///vocab.db')
Base = declarative_base()

class Vocab(Base):
    __tablename__ = "vocab"
    id = Column(Integer, primary_key=True)
    unit_id = Column(Integer, ForeignKey('unit.id'))
    english = Column(String, unique=True)
    german = Column(String, unique=True)
    __table_args__ = (UniqueConstraint(
        'english', name='uq_english'), UniqueConstraint('german', name='uq_german'))

class Unit(Base):
    __tablename__ = "unit"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    __table_args__ = (UniqueConstraint('name', name='uq_name'), )


# Create the vocabulary table in the database
Base.metadata.create_all(bind=engine)

# Start a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

session = Session()

def add_vocabs():
    session.add(Unit(name='UNIT 1'))
    session.add(Unit(name='UNIT 2'))
    session.add(Unit(name='UNIT 3'))
    session.add(Unit(name='UNIT 4'))
    session.add(Unit(name='UNIT 5'))
    
    session.add(Vocab(english='time', german='Zeit', unit_id=1))
    session.add(Vocab(english='water', german='Wasser', unit_id=1))
    session.add(Vocab(english='book', german='Buch', unit_id=5))
    session.add(Vocab(english='house', german='Haus', unit_id=2))
    session.add(Vocab(english='dog', german='Hund', unit_id=5))
    session.add(Vocab(english='cat', german='Katze', unit_id=4))
    session.add(Vocab(english='car', german='Auto', unit_id=5))
    session.add(Vocab(english='sun', german='Sonne', unit_id=1))
    session.add(Vocab(english='moon', german='Mond', unit_id=5))
    session.add(Vocab(english='tree', german='Baum', unit_id=2))
    session.add(Vocab(english='flower', german='Blume', unit_id=5))
    session.add(Vocab(english='chair', german='Stuhl', unit_id=1))
    session.add(Vocab(english='table', german='Tisch', unit_id=5))
    session.add(Vocab(english='computer', german='Computer', unit_id=2))
    session.add(Vocab(english='phone', german='Telefon', unit_id=5))
    session.add(Vocab(english='television', german='Fernseher', unit_id=3))
    session.add(Vocab(english='music', german='Musik', unit_id=5))
    session.add(Vocab(english='movie', german='Film', unit_id=4))
    session.add(Vocab(english='food', german='Essen', unit_id=2))
    session.add(Vocab(english='drink', german='Getränk', unit_id=1))
    session.add(Vocab(english='country', german='Land', unit_id=4))
    session.add(Vocab(english='mountain', german='Berg', unit_id=3))
    session.add(Vocab(english='river', german='Fluss', unit_id=5))
    session.add(Vocab(english='ocean', german='Ozean', unit_id=4))
    session.add(Vocab(english='beach', german='Strand', unit_id=5))
    session.add(Vocab(english='sky', german='Himmel', unit_id=2))
    session.add(Vocab(english='earth', german='Erde', unit_id=1))
    session.add(Vocab(english='person', german='Person', unit_id=5))
    session.add(Vocab(english='animal', german='Tier', unit_id=2))
    session.add(Vocab(english='example', german='Beispiel', unit_id=3))
    session.add(Vocab(english='year', german='Jahr', unit_id=1))
    session.add(Vocab(english='city', german='Stadt', unit_id=2))
    session.add(Vocab(english='state', german='Staat', unit_id=3))
    session.add(Vocab(english='we', german='wir', unit_id=4))
    session.add(Vocab(english='long', german='lang', unit_id=1))
    session.add(Vocab(english='other', german='andere', unit_id=3))
    session.add(Vocab(english='plumber', german='Klemtner', unit_id=3))
    session.add(Vocab(english='church', german='Kirche', unit_id=3))
    session.add(Vocab(english='soccer', german='Fußball', unit_id=4))
    session.add(Vocab(english='badmington', german='Federball', unit_id=4))
    
    

    
if __name__ == "__main__":
    add_vocabs()
    session.commit()
    session.close()