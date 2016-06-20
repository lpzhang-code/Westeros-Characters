from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, Items, Users

engine = create_engine(*args)
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# Add categories
names = ['Lannister', 'Stark', 'Baratheon', 'Tully', 'Targaryen', 'Bolton', 'Martell', 'Tyrell']

for house in names:
    name = Category(name = house)
    session.add(name)
    session.commit()

# Add items
ned = Items(name = 'Ned',
            image = 'http://vignette4.wikia.nocookie.net/gameofthrones/images/5/5c/Eddard_1x01.jpg/revision/latest?cb=20120511213934',
            description = 'Ned Stark is an honourable hero who is unfortunately decapitated for treason \
            after discovering the secret of incest between the Lannister siblings.',
            cat_name='Stark')

session.add(ned)

tyrion = Items(name = 'Tyrion',
               image = 'http://1.bp.blogspot.com/-Op9Hfd1qq7o/T5f06bDHG7I/AAAAAAAAAFQ/5qaxh3JswqM/s1600/Tyrion+Lannister.jpg',
               description = 'Tyrion is a dwarf but super-intelligent and able to outwit everybody else \
               his birth lead to the death of his mother and this is one of the reasons that he is despised by his father and sister.',
               cat_name='Lannister')

session.add(tyrion)

robert = Items(name = 'Robert',
               image ='http://vignette1.wikia.nocookie.net/hieloyfuego/images/e/ee/Robert_Baratheon_HBO.JPG/revision/latest?cb=20120124224134',
               description = 'Robert was a great warrior who defeated Rhaegar but then turned out to be a drunken oaf of a king. \
               He was skilled in battle but proved to be an incompetent ruler who was primarily interested in drinking and whoring',
               cat_name='Baratheon')

session.add(robert)

session.commit()
