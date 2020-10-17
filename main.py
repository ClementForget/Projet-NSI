#Imports
import fonctions
#Déclaration Var
classe = []

#programme
print("Bonjours, ")
print("Vous êtes dans le programmes de gestions dico")
print("Pour le moment, votre base de donner ne contient personne")
print("Pour ajouter des gens faites 1")

menu_ok = False
while(menu_ok != True):
  try:
    menu = int(input("Quelle option choisez vous ? "))
  except:
    print("Vous n'avez pas choisi un nombre !")
    continue
  if(menu == 1):
    menu_ok = True
    print("\n")
    print("Bienvenur dans l'assistant d'ajout")
    classe.append(fonctions.add_infos(input("Choisisez un Prenom : "), input("Choisisez un Nom : "), input("Choisisez une Classe :"), input("Choisisez un Age : ")))

  else:
    print("\n")
    print("Votre entez n'est pas valide !")
    continue
