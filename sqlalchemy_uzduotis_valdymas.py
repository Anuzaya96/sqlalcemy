from sqlalchemy_uzduotis import engine, Darbuotojai, Base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

session = sessionmaker(bind=engine)()

def print_employess_info():
    print("Darbuotojai")
    print("(#, Vardas, pavarde, gimimo data, pareigos, atlyginimas)")
    darbuotojai = session.query(Darbuotojai).all()
    for darbuotojas in darbuotojai:
        print(darbuotojas)

def new_employee():
    print("Naujas darbuotojas")
    try:
        vardas = input("Vardas: ")
        pavarde = input("Pavarde: ")
        gimimo_data = input("Gimimo data: ")
        paregos = input("Pareigos: ")
        atlyginimas = input("Atlyginimas: ")
    except ValueError:
        print("Klaida: atlyginmas turi būti skaičius")
        return
    else:
        darbuotojas = Darbuotojai(vardas, pavarde, gimimo_data, paregos, atlyginimas)
        session.add(darbuotojas)
        session.commit()
        print(f"Darbuotojas {darbuotojas} įvestas sėkmingai")


def input_employee():
    print_employess_info()
    try:
        darbuotojo_id = int(input("Iveskite trinamo darbuotojo ID: "))
    except ValueError:
        print("KLAIDA: ID turi buti skaicius")
        return None
    else:
        if darbuotojo_id:
            darbuotojas = session.query(Darbuotojai).get(darbuotojo_id)
            if darbuotojas:
                return darbuotojas
            else:
                print(f"KLAIDA: Projektas su ID: {darbuotojo_id} neegzistuoja.")
                return None


def update_employee():
    darbuotojas = input_employee()
    if darbuotojas:
        try:
            vardas = input(f"Vardas ({darbuotojas.vardas}): ")
            pavarde = input(f"Pavarde ({darbuotojas.pavarde}): ")
            gimimo_data = input(f"Gimimo data ({darbuotojas.gimimo_data}): ")
            pareigos = input(f"Pareigos ({darbuotojas.pareigos}): ")
            atlyginimas = float(input(f"Atlyginimas ({darbuotojas.atlyginimas}): ") or 0)
        except ValueError:
            print("KLAIDA: atlyginimas turi buti skaicius.")
            return
        else:
            if len(vardas) > 0:
                darbuotojas.vardas = vardas
            if len(pavarde) > 0:
                darbuotojas.pavarde = pavarde
            if gimimo_data > 0:
                darbuotojas.gimimo_data = gimimo_data
            if len(pareigos) > 0:
                darbuotojas.pareigos = pareigos
            if atlyginimas > 0:
                darbuotojas.atlyginimas = atlyginimas
            session.commit()
            print(f"Darbuotojo {darbuotojas} duomenys atnaujinti sėkmingai")


def delete_employee():
    trinamas = input_employee()
    if trinamas:
        session.delete(trinamas)
        session.commit()
        print(f"Darbuotojas {trinamas} istrintas sekmingai")


while True:
    print("=== Darbuotojų valdymo duomenų bazė ===")
    print("Pasirinkite: ")
    print("- q: iseiti")
    print("- r: rodyti visus darbuotojus")
    print("- n: naujas darbuotojas")
    print("- u: pakeisti darbuotojo duomenis")
    print("- d: trinti darbuotoją")
    pasirinkimas = input("Pasirinkite: ").casefold()

    if pasirinkimas == "q":
        print("Viso gero!")
        break
    elif pasirinkimas == "r":
        print_employess_info()
    elif pasirinkimas == "n":
        new_employee()
    elif pasirinkimas == "u":
        update_employee()
    elif pasirinkimas == "d":
        delete_employee()
    else:
        print("Klaida: Blogas pasirinkimas, rinkites is naujo")