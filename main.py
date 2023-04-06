import mysql.connector

def conn():
    mydb = mysql.connector.connect(  
    host = "localhost",
    user = "root",
    password = "Mostwanted13?")
    return mydb


cursor = conn().cursor()

# create database
cursor.execute("CREATE DATABASE IF NOT EXISTS boutique")

# create table categorie
cursor.execute("""
CREATE TABLE IF NOT EXISTS categories (
    id PRIMARY KEY INT AUTO_INCREMENT,
    nom VARCHAR(255))
    """)

# create the produit table
cursor.execute("""
CREATE TABLE IF NOT EXISTS produits (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(255),
    description TEXT,
    prix INT,
    quantite INT,
    id_categorie INT,
    FOREIGN KEY (id_categorie) REFERENCES categorie(id)
)
""")

class produits :
    def __init__(self) -> None:
        self.mydb = mysql.connector.connect(  
            host = "localhost",
            user = "root",
            password = "Mostwanted13?")
        self.cursor = self.mydb.cursor()

    def create(self, nom, description, prix, quantité, id_categorie):
        sql = "INSERT INTO produits (nom, description, prix, quantité, id_categorie) VALUES (%s, %s, %s, %s,%s)"
        val = (nom, description, prix, quantité, id_categorie)
        self.cursor.execute(sql, val)
        self.mydb.commit()
        return self.cursor.lastrowid

    def read(self, id):
        sql = "SELECT * FROM produits"
        val = (id,)
        self.cursor.execute(sql, val)
        result = self.cursor.fetchone()
        if result is None:
            return None
        else:
            return {'id': result[0], 'nom': result[1], 'description': result[2], 'prix': result[3], 'quantité': result[4],'id_categorie':result[5]}
        
    def update(self, id, nom=None, description=None, prix=None, quantité=None, id_categorie=None):
        produit = self.read(id)
        if produit is None:
            return False
        else:
            if nom is not None:
                produit['nom'] = nom
            if description is not None:
                produit['description'] = description
            if prix is not None:
                produit['prix'] = prix
            if quantité is not None:
                produit['quantité'] = quantité
            if id_categorie is not None:
                produit['id_categorie'] = id_categorie
            sql = "UPDATE produits SET nom = %s, d = %s, prix = %s, quantité = %s, id_categorie = %s WHERE id = %s"
            val = (produit['nom'], produit['description'], produit['prix'], produit['quantité'], produit['id_categorie'])
            self.cursor.execute(sql, val)
            self.mydb.commit()
            return True
        
    def delete(self, id):
        sql = "DELETE FROM produits WHERE id = %s"
        val = (id,)
        self.cursor.execute(sql, val)
        self.mydb.commit()
        return self.cursor.rowcount

    def close(self):
        self.cursor.close()
        self.mydb.close()

class categories :
    def __init__(self) -> None:
        self.mydb = mysql.connector.connect(  
            host = "localhost",
            user = "root",
            password = "Mostwanted13?")
        self.cursor = self.mydb.cursor()
    
    def create(self, nom):
        sql = "INSERT INTO categories (nom) VALUES (%s)"
        val = (nom)
        self.cursor.execute(sql, val)
        self.mydb.commit()
        return self.cursor.lastrowid

    def read(self, id):
        sql = "SELECT * FROM categories"
        val = (id,)
        self.cursor.execute(sql, val)
        result = self.cursor.fetchone()
        if result is None:
            return None
        else:
            return {'id': result[0], 'nom': result[1]} 
    
    def update(self, id, nom=None):
        categorie = self.read(id)
        if categorie is None:
            return False
        else:
            if nom is not None:
                categorie['nom'] = nom
            sql = "UPDATE categories SET nom = %s"
            val = categorie['nom']
            self.cursor.execute(sql, val)
            self.mydb.commit()
            return True
        