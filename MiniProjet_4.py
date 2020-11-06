import sqlite3

conn = sqlite3.connect('Miniprojet4.db')
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS REPER(id INT,nom TEXT ,prenom TEXT , téléphone INT ,email TEXT ,qualité TEXT)")
conn.commit()

choix = 6
while choix == 6 :
    print("Dans la base de données annuraire")
    print("1 - Insertion")
    print("2 - Suppression")
    print("3 - Modification")
    print("4 - Recherche")
    print("5 - Fin du programme")
    print("Quel est votre choix ?")
    
    choix = int(input("choisis un programme :"))

while choix is not 0 :


    if choix == 1 :
        nom = input("insérer le nom :")
        prenom = input("insérer le prénom :")
        telephone = int(input("insérer le numéro de téléphone :"))
        email = input("insérer l'email :")
        qualité = input("insérer la qualité :")
        data = (nom, prenom, telephone, email, qualité)
        cur.execute("INSERT INTO REPER(nom,prenom,téléphone,email,qualité) VALUES(?, ?, ?, ?, ?)", data)
        choix = 0
        conn.commit()

        
    elif choix == 2 :
        telephone = int(input("Numéro de téléphone de la personne a supprimer :"))
        suppr = (telephone,)
        cur.execute("DELETE FROM REPER WHERE téléphone = ?", suppr)
        choix = 0
        conn.commit()

        
    elif choix == 3 :
        print("modification du numero d'une personne")
        nom = input("insérer le nom :")
        telephone = int(input("insérer le nouveau numéro de téléphone :"))
        modif = (telephone,nom)
        cur.execute('UPDATE REPER SET téléphone = ? WHERE nom = ?', modif)
        choix = 0
        conn.commit()
        
    elif choix == 4 :
        
        cur.execute('SELECT nom FROM REPER WHERE qualité = "amis"')
        liste = cur.fetchall()
        choix = 0
        conn.commit()
        

cur.close()
conn.close()