#Imports
import fonctions
#Déclaration Var
classe = []
finish = False

#programme
print("Bonjours, ")
print("Vous êtes dans le programmes de gestions dico")
print("Pour le moment, votre base de donner ne contient personne")

while(finish != True):
  menu_ok = False
  while(menu_ok != True):
    
    print(f"Vous avez pour le moment {len(classe)} entrée dans votre table ")
    print("\n")
    print("Pour ajouter des gens faites 1")
    print("Pour afficher vos données faites 2")
    print("Pour suprimer un element du tableau 3")
    try:
      menu = int(input("Quelle option choisez vous ? "))
    except:
      print("Vous n'avez pas choisi un nombre !")
      continue
    if(menu == 1):
    #Debut ajout
      menu_ok = True
      print("\n")
      print("Bienvenur dans l'assistant d'ajout")
      classe.append(fonctions.add_infos(input("Choisisez un Prenom : "), input("Choisisez un Nom : "), input("Choisisez une Classe :"), input("Choisisez un Age : ")))
  #Affichage table
      print("\n")
      print('Vos données : ')
      print("\n")
      print(fonctions.aff_data(classe))
      print("\n")
    
    elif(menu == 2):
      #Affichage table
      if (len(classe)== 0):
        print(" La classe est vide ")
        continue
      print("\n")
      print('Vos données : ')
      print("\n")
      print(fonctions.aff_data(classe))
      print("\n")

    elif(menu == 3):
      if(len(classe) == 0):
        print("Vous ne pouvez pas supprimer quelqu'un, il n'y a personne dans votre liste ! ")
        continue
      else:
        print("\n")
        print('Vos données : ')
        print("\n")
        print(fonctions.aff_data(classe))
        print("\n")
        classe = fonctions.dell_data(classe)
        print("\n")
        print('Vos données : ')
        print("\n")
        print(fonctions.aff_data(classe))
        print("\n")
      

    else:
      print("\n")
      print("Votre entez n'est pas valide !")
      continue
