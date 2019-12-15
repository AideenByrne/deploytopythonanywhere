import mysql.connector
import dbconfig as cfg

class VinylDAO:
    db=""
    def __init__(self):
        self.db = mysql.connector.connect(
        host=cfg.mysql['host'],
        user=cfg.mysql['username'],
        password=cfg.mysql['password'],
        database=cfg.mysql['database']
 )

    def create(self, values):
        cursor = self.db.cursor()
        sql="insert into vinyl (artist, title, label, price) values (%s,%s, %s, %s)"
        cursor.execute(sql, values)
        self.db.commit()
        return cursor.lastrowid

    def getAll(self):
        cursor = self.db.cursor()
        sql="select * from vinyl"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        for result in results:
            returnArray.append(self.converttoDictionary(result))
        return results

    def findByID(self, id):
        cursor = self.db.cursor()
        sql="select * from vinyl where id = %s"
        values = (id,)
        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.converttoDictionary(result)

    def update(self, values):
        cursor = self.db.cursor()
        sql="update vinyl set artist=%s, title=%s, label=%s, price=%s where id = %s"
        cursor.execute(sql, values)
        self.db.commit()

    def delete(self, id):
        cursor = self.db.cursor()
        sql="delete from vinyl where id = %s"
        values = (id,)
        cursor.execute(sql, values)
        self.db.commit()
        print("delete done")
    
    def converttoDictionary(self, result):
        colnames=['id', 'Artist', 'Title', 'Label', 'Price']
        item = {}
        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                item[colName] = value
        return item 

vinylDAO = VinylDAO()