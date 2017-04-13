from domain.category import *


class CategoryRepository:
    def __init__(self,cnx):
        self.cnx = cnx

    def get(self, category):
        cursor = self.cnx.cursor()
        query = "select * from CATEGORY"

        fields = []
        if category.categoryId:
            fields.append("CATEGORY_ID=" + str(category.categoryId))
        if category.name:
            fields.append("NAME=\"" + str(category.name) + "\"")
        if category.minAge:
            fields.append("MIN_AGE=" + str(category.minAge))
        if category.maxAge:
            fields.append("MAX_AGE=" + str(category.maxAge))

        if len(fields) > 0:
            query += " where "
        query += " and ".join(fields) + ";"
        print(query)
        cursor.execute(query)
        result = []
        for (categoryId, name, minAge, maxAge) in cursor:
            result.append(Category(categoryId, name, minAge, maxAge))
        return result

    def add(self, category):
        cursor = self.cnx.cursor()
        query = "insert into CATEGORY ("
        fields = []
        values = []
        if category.categoryId:
            fields.append("CATEGORY_ID")
            values.append(str(category.categoryId))
        if category.name:
            fields.append("NAME")
            values.append("\"" + str(category.name) + "\"")
        if category.minAge:
            fields.append("MIN_AGE")
            values.append(str(category.minAge))
        if category.maxAge:
            fields.append("MAX_AGE")
            values.append(str(category.maxAge))

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
            fields.append("MIN_AGE=" + str(category.minAge) + "")
        if category.maxAge:
            fields.append("MAX_AGE=" + str(category.maxAge) + "")

        query += ", ".join(fields)

        query += " where CATEGORY_ID=" + str(category.categoryId) + ";"

        print(query)
        cursor.execute(query)

    def remove(self, category):
        cursor = self.cnx.cursor()
        query = "delete from CATEGORY where CATEGORY_ID=" + str(category.categoryId)
        print(query)
        cursor.execute(query)