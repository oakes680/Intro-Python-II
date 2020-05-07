from item import Item
# Implement a class to hold room information. This should have name and
# description attributes.

class Room(): 
    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items = items

    def __str__(self):
        return_string = "-----"
        return_string += "\n"
        return_string += self.name
        return_string += "\n"
        return_string += self.description
        return_string += "\n"
        return_string += f"items available {self.available_items()}"
        return_string += "\n"
        return_string += f"possible moves{self.get_exits_string()}"
        return return_string


    def get_exits_string(self):
        exits = []
        if self.n_to is not None:
            exits.append("n")
        if self.s_to is not None:
            exits.append("s")
        if self.e_to is not None:
            exits.append("e")
        if self.w_to is not None:
            exits.append("w")
        return exits

    # def available_items(self):
    #     return self.items[0].name

    def available_items(self):
        itm = []
        for item in self.items:
            itm.append(item.name)
        return itm
        
