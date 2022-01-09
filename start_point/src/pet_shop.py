def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(cash):
    return cash["admin"]["total_cash"]

def add_or_remove_cash(num1, num2):
    num1["admin"]["total_cash"] += num2
    return num1["admin"]["total_cash"]

def add_or_remove_cash(num1, num2):
    num1["admin"]["total_cash"] += num2
    return num1["admin"]["total_cash"]

def get_pets_sold(pets_sold):
    return pets_sold["admin"]["pets_sold"]

def increase_pets_sold(num1, num2):
    num1["admin"]["pets_sold"] += num2
    return num1["admin"]["pets_sold"]

def get_stock_count(stock_num):
    return len(stock_num["pets"])


def get_pets_by_breed(pet_shop, breed):
    list = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed:
             list.append(pet)
    return list

def get_pets_by_breed(pet_shop, breed):
    list = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed:
             list.append(pet)
    return list

def find_pet_by_name(pet_shop, pet_name):
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            return pet

def find_pet_by_name(pet_shop, pet_name):
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            return pet

def remove_pet_by_name(pet_shop, pet_name):
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            pet_shop["pets"].remove(pet)

def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)
    return pet_shop

def get_customer_cash(pet_shop):
    return pet_shop["cash"]

def remove_customer_cash(cash, cash_deducted):
    cash["cash"] -= cash_deducted
    return cash["cash"]

def get_customer_pet_count(customer):
    return len(customer["pets"])

def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)
    return customer


