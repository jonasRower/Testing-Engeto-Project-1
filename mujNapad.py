import os
import datetime

class slozkySProjekty:

    def vytvorSlozkuSProjektem(self, nazevUkolu):
        tridaProjekt = cestyProjektu()
        nazevSlozky = tridaProjekt.vratCestuSlozkyUkolu(nazevUkolu)

        print(nazevSlozky)

        # Create the directory
        try:
            os.mkdir(nazevSlozky)
            print(f"Directory '{nazevSlozky}' created successfully.")
        except FileExistsError:
            print(f"Directory '{nazevSlozky}' already exists.")
        except PermissionError:
            print(f"Permission denied: Unable to create '{nazevSlozky}'.")
        except Exception as e:
            print(f"An error occurred: {e}")


    def vytvorSouborDescription(self, nazevUkolu):
        tridaProjekt = cestyProjektu()
        cestaDescriptionUkolu = tridaProjekt.vratCestuSoubDesciptionUkolu(nazevUkolu)

        with open(cestaDescriptionUkolu, "a") as f:
            f.write("")


    def detekujZdaExistujeSoub(self, nazevUkolu, nazevSouboru):
        tridaProjekt = slozkySProjekty()
        nazevAdresare = tridaProjekt.nazevAdresare
        celaCestaSouboru = nazevAdresare + "\\" + nazevUkolu + "\\" + nazevSouboru

        if celaCestaSouboru.exists():
            print("File exists")
        else:
            print("File does not exist")

        #a = Path(celaCestaSouboru)




class cestyProjektu:
    def __init__(self):
        self.nazevAdresare = "Testing Akademie - Projekt 1"

    def vratCestuSlozkyUkolu(self, nazevUkolu):
        cestaSlozkyUkolu = self.nazevAdresare + "\\" + nazevUkolu

        return(cestaSlozkyUkolu)

    def vratCestuSoubDesciptionUkolu(self, nazevUkolu):
        cestaSlozkyUkolu = self.vratCestuSlozkyUkolu(nazevUkolu)
        cestaDescriptionUkolu = cestaSlozkyUkolu + "\\description.txt"

        return(cestaDescriptionUkolu)


class textDoDescription:


    def vratAktualniCasProZapis(self):
        current_time = datetime.datetime.now()

        return(current_time)

    def vratTextPopisu(self, popisUkolu, status, deadline):
        current_time = self.vratAktualniCasProZapis()
        text = str(current_time) + " : \n\t Description: " + popisUkolu + "\n\t Status: " + status + "\n\t Deadline: " + deadline

        return(text)


    def zapisPopisUkolu(self, nazevUkolu, popisUkolu, status, deadLine):
        tridaProjekt = cestyProjektu()
        cestaDescriptionUkolu = tridaProjekt.vratCestuSoubDesciptionUkolu(nazevUkolu)
        text = self.vratTextPopisu(popisUkolu, status, deadLine)

        with open(cestaDescriptionUkolu, "a") as f:
            f.write("\n" + text)


# vytvori slozku, kam umisti ukol
tridaProjekt = slozkySProjekty()
tridaProjekt.vytvorSlozkuSProjektem("Ukol_1")
tridaProjekt.vytvorSouborDescription("Ukol_1")

tridaObsahDescription = textDoDescription()
tridaObsahDescription.zapisPopisUkolu("Ukol_1", "Udelej to tak, aby slo zadat vice ukolu", "Open", "16.8.2026")

