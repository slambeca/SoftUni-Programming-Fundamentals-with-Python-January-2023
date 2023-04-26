class Catalogue:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def get_by_letter(self, first_letter):
        filtered = []
        for product in self.products:
            if product[0] == first_letter:
                filtered.append(product)
        # or return [product for product in self.products if product[0] == first_letter]
        # list comprehension is faster and here it is better to use it than a for loop

        return filtered
    # keep the predefined methods last

    def __repr__(self):
        result = f"Items in the {self.name} catalogue:"    # static header of our string

        for product in sorted(self.products):
            result += "\n" + product

        return result


catalogue = Catalogue("Furniture")

catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")

print(catalogue.get_by_letter("C"))
print(catalogue)