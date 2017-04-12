from domain.category import *


class CategoryRepository:
    def __init__(self,cnx):
        self.cnx = cnx

    def get_all(self):
        cursor = self.cnx.cursor()
        query = "select * from CATEGORY;"
        print(query)
        cursor.execute(query)
        result = []
        for (id, name, minAge, maxAge) in cursor:
            result.append(Category(id, name, minAge, maxAge))
        return result

    def get(self, category):
        cursor = self.cnx.cursor()
        query = "select * from CATEGORY where CATEGORY_ID = " + category.id
        print(query)
        cursor.execute(query)
        for (id, name, minAge, maxAge) in cursor:
            return Category(id, name, minAge, maxAge)

    def add(self, category):
        cursor = self.cnx.cursor()
        query = "insert into CATEGORY ("
        fields = []
        values = []
        if category.name:
            fields.append("NAME")
            values.append("\"" + str(category.name) + "\"")
        if category.minAge:
            fields.append("MIN_AGE")
            values.append("\"" + str(category.minAge) + "\"")
        if category.maxAge:
            fields.append("MAX_AGE")
            values.append("\"" + str(category.maxAge) + "\"")

        query += ", ".join(fields)
        query += ") values ("
        query += ", ".join(values)
        query += ");"

        print(query)

        cursor.execute(query)

    def update(self, category):
        cursor = self.cnx.cursor()
        query = "update CATEGORY set "

        fields = []

        if category.name:
            fields.append("NAME=\"" + str(category.name) + "\"")
        if category.minAge:
            fields.append("MIN_AGE=\"" + str(category.minAge) + "\"")
        if category.maxAge:
            fields.append("MAX_AGE=\"" + str(category.maxAge) + "\"")

        query += ", ".join(fields)

        query += " where CATEGORY_ID=" + str(category.categoryId) + ";"

        print(query)
        cursor.execute(query)

    def remove(self, category):
        cursor = self.cnx.cursor()
        query = "delete from CATEGORY where CATEGORY_ID=" + str(category.categoryId)
        print(query)
        cursor.execute(query)