class CategoryRepository:
    def __init__(self,cursor):
        self.cursor = cursor

    def get(self, category):
        self.cursor.execute("select * from CATEGORY where CATEGORY_ID = " + category.id)
        for(id,name,minAge,maxAge):
            return category.Category(id,name,minAge,maxAge)