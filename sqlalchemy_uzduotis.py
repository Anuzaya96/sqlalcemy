#Sukurti programą, kuri:
#
#Leistų įvesti darbuotojus: vardą, pavardę, gimimo datą, pareigas, atlyginimą, nuo kada dirba 
# (data būtų nustatoma automatiškai, pagal dabartinę datą).

#Duomenys būtų saugomi duomenų bazėję, panaudojant SQLAlchemy ORM (be SQL užklausų)
#Vartotojas galėtų įrašyti, peržiūrėti, ištrinti ir atnaujinti darbuotojus.



import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///data/employees.db')
Base = declarative_base() 

class Darbuotojai(Base):
    __tablename__ = 'Employees'
    id = Column(Integer, primary_key=True)
    vardas = Column("Vardas", String)
    pavarde = Column("Pavarde", String)
    gimimo_data = Column("Gimimo data", DateTime)
    pareigos = Column("Pareigos", String)
    atlyginimas = Column("Atlyginimas", Float)
    dirba_nuo = Column("Dirba nuo", DateTime, default=datetime.datetime.utcnow)

    def __init__(self, vardas, pavarde, gimimo_data, pareigos, atlyginimas):
        self.vardas = vardas
        self.pavarde = pavarde
        self.gimimo_data = datetime.datetime.strptime(gimimo_data, "%Y-%m-%d")
        self.pareigos = pareigos
        self.atlyginimas = atlyginimas
    
    def __repr__(self):
        return f"{self.id},{self.vardas},{self.pavarde},{self.gimimo_data},{self.pareigos},{self.dirba_nuo}"


if __name__ == "__main__":
    Base.metadata.create_all(engine)
