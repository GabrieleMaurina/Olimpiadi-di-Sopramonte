class Category:
    def __init__(self, category_id="", name="", min_age="", max_age=""):
        self.categoryId = category_id
        self.name = name
        self.minAge = min_age
        self.maxAge = max_age

    def __str__(self):
        return "Category:[categoryId=" + self.categoryId + ", name=" + self.name + ", minAge=" + self.minAge + ", maxAge=" + self.maxAge + "]"
