import mysql.connector
import dbconfig as cfg

class VinylDAO:
    db=""
    def connectToDB(self):
        self.db = mysql.connector.connect(
        host=cfg.mysql['host'],
        user=cfg.mysql['username'],
        password=cfg.mysql['password'],
        database=cfg.mysql['database']
 )

    def __init__(self):
        self.connectToDB()

    def getCursor(self):
        if not self.db.is_connected():
            self.connectToDB()
        return self.db.cursor()

    def create(self, values):
        cursor = self.getCursor()
        sql="insert into vinyl (artist, title, label, price) values (%s,%s, %s, %s)"
        cursor.execute(sql, values)

        self.db.commit()
        lastRowId=cursor.lastrowid  
        cursor.close()
        return lastRowId

    def getAll(self):
        cursor = self.getCursor()
        sql="select * from vinyl"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        for result in results:
            print(result)
            returnArray.append(self.converttoDictionary(result))
        cursor.close()
        return returnArray

    def findByID(self, id):
        cursor = self.getCursor()
        sql="select * from vinyl where id = %s"
        values = (id,)
        cursor.execute(sql, values)
        result = cursor.fetchone()
        vinyl= self.converttoDictionary(result)
        cursor.close()
        return vinyl

    def update(self, values):
        cursor = self.getCursor()
        sql="update vinyl set artist=%s, title=%s, label=%s, price=%s where id = %s"
        cursor.execute(sql, values)
        self.db.commit()
        cursor.close()

    def delete(self, id):
        cursor = self.getCursor()
        sql="delete from vinyl where id = %s"
        values = (id,)
        cursor.execute(sql, values)
        self.db.commit()
        cursor.close()
    
    def converttoDictionary(self, result):
        colnames=['id', 'Artist', 'Title', 'Label', 'Price']
        item = {}
        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                item[colName] = value
        return item 

vinylDAO = VinylDAO()