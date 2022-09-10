class Storage:
    storage_list = []
    #class atribute e storage_list toest vsi4ki metodi mogat da go polzvat

    def __init__(self, capacity: int):
        self.capacity = capacity

    def add_product(self, product: str):
        if self.capacity > 0:
            Storage.storage_list.append(product)
            self.capacity -= 1

    def get_products(self):
        return Storage.storage_list

storage = Storage(4)
storage.add_product("apple")
storage.add_product("banana")
storage.add_product("potato")
storage.add_product("tomato")
storage.add_product("bread")
print(storage.get_products())