import math

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    
    price_table = {
                    "A" : 50,
                    "B" : 30,
                    "C" : 20,
                    "D" : 15,
                    "E" : 40,
                    "F" : 10,
                    "G" : 20,
                    "H" : 10,
                    "I" : 35,
                    "J" : 60,
                    "K" : 80,
                    "L" : 90,
                    "M" : 15,
                    "N" : 40,
                    "O" : 10,
                    "P" : 50,
                    "Q" : 30,
                    "R" : 50,
                    "S" : 30,
                    "T" : 20,
                    "U" : 40,
                    "V" : 50,
                    "W" : 20,
                    "X" : 90,
                    "Y" : 10,
                    "Z" : 50,
                  }
    
    buy_x_get_y =[(2, "E", 1, "B"), (2, "F", 1, "F"), (3, "N", 1, "M"), (3, "R", 1, "Q"), (3, "U", 1, "U") ]

    x_for_y = [[(5, "A", 200), (3, "A", 130)], [(2, "B", 45)], [(10, "H", 80)], [(5, "H", 45)], [(2, "K", 150)], [(5, "P", 200)], [(3, "Q", 80)], [(3, "V", 130), (2, "V", 90)]]

    sku_list = [unit for unit in skus]
    for unit in sku_list:
        if unit not in price_table:
            return -1
    

    sku_count = {}
    for unit in sku_list:
        sku_count[unit] = sku_count.get(unit, 0) + 1


    sku_count = buy_x_get_y_free("E", "B", 2, 1, sku_count)
    sku_count = buy_x_get_y_free("F", "F", 2, 1, sku_count)
    # ADD a B for every two E's
    #if "B" in sku_count.keys() and "E" in sku_count.keys():
    #    additions, _ = divmod(sku_count["E"], 2)
    #    sku_count["B"] -= additions
    #    if sku_count["B"] < 1:
    #        del sku_count["B"]
    
    # ADD an F for every 2 F's
    #if "F" in sku_count.keys() and sku_count["F"] > 2:
    #    sku_count["F"] = math.ceil(sku_count["F"] * (2/3))


    
    total_checkout_value = 0

    for unit in sku_count.keys():

        if unit == "A":
            discounted, non_discounted = divmod(sku_count[unit], 5)
            total_checkout_value += discounted * 200

            discounted, non_discounted = divmod(non_discounted, 3)
            total_checkout_value += discounted * 130
            total_checkout_value += non_discounted * price_table[unit]
        elif unit == "B":
            discounted, non_discounted = divmod(sku_count[unit], 2)
            total_checkout_value += discounted * 45
            total_checkout_value += non_discounted * price_table[unit]
        else:
            total_checkout_value += price_table[unit] * sku_count[unit]
    
    return total_checkout_value


def buy_x_get_y_free(sku_bought, sku_promoted, sku_offer, skus_gifted, sku_dict):
    
    if sku_bought == sku_promoted:
        if sku_bought in sku_dict.keys() and sku_dict[sku_bought] > sku_offer:
            sku_dict[sku_bought] = math.ceil(sku_dict[sku_bought] * (sku_offer/(sku_offer+skus_gifted)))
            return sku_dict
    
    else:
        if sku_bought in sku_dict.keys() and sku_promoted in sku_dict.keys():
            additions, _ = divmod(sku_dict[sku_bought], sku_offer)
            sku_dict[sku_promoted] -= additions
            if sku_dict[sku_promoted] < 1:
                del sku_dict[sku_promoted]
            
            return sku_dict





