class CategoryRepository:
    def __init__(self,cnx):
        self.cnx = cnx

    def get(self, category):
        cursor = self.cnx.cursor()
        cursor.execute("select * from CATEGORY where CATEGORY_ID = " + category.id)
        for(id,name,minAge,maxAge) in cursor:
            return category.Category(id,name,minAge,maxAge)