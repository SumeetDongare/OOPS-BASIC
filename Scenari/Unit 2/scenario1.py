class Mobile:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def get_category(self):
        if self.price >= 50000:
            return "Premium"
        elif self.price >= 20000:
            return "Mid-range"
        else:
            return "Budget"


class Store:
    def __init__(self):
        self.mobiles = []

    def add_mobile(self, mobile):
        self.mobiles.append(mobile)

    def display_mobiles(self):
        print("\n--- Mobile Store ---")

        for mobile in self.mobiles:
            print("Brand   :", mobile.brand)
            print("Model   :", mobile.model)
            print("Price   :", mobile.price)
            print("Category:", mobile.get_category())
            print("--------------------")


# Creating store
store = Store()

# Adding mobiles
store.add_mobile(Mobile("Apple", "iPhone 15", 70000))
store.add_mobile(Mobile("Samsung", "Galaxy A55", 35000))
store.add_mobile(Mobile("Redmi", "Note 13", 15000))
store.add_mobile(Mobile("OnePlus", "12R", 45000))

# Displaying all mobiles
store.display_mobiles()

"""
--- Mobile Store ---
Brand   : Apple
Model   : iPhone 15
Price   : 70000
Category: Premium
--------------------
Brand   : Samsung
Model   : Galaxy A55
Price   : 35000
Category: Mid-range
--------------------
Brand   : Redmi
Model   : Note 13
Price   : 15000
Category: Budget
--------------------
Brand   : OnePlus
Model   : 12R
Price   : 45000
Category: Mid-range
--------------------
"""






