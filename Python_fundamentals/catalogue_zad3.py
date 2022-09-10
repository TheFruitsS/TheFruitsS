class Catalogue:

    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product_name: str):
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        return [product for product in self.products if product.startswith(first_letter)]
        #startswith() tarsi s kakvo zapochva stringa v lista moje da se zamesti i taka product[0] == first_letter

    def __repr__(self):
        string_in_product = f"Items in the {self.name} catalogue:\n"
        string_in_product += '\n'.join(sorted(self.products))
        return string_in_product

catalogue = Catalogue("Furniture")
catalogue.add_product("SofaBed")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)