init python: 

    class Inventory():
        def __init__(self, items, num_items):
            self.items = items
            self.num_items = num_items

        def add_item(self, item):
            self.items.append(item)
            self.num_items += 1

        def remove_item(self, item):
            self.items.remove(item)
            self.num_items -= 1

        def list_items(self):
            if len(self.items) < 1:
                blake ("В дневнике нету записей")
            else:
                for item in self.items:
                    blake(f"{item.name}, {item.description}")


    class InventoryItem():
        def __init__(self, name, description, path):
            self.name = name
            self.description = description
            self.path = path
# define - can't change 
# default - can change
