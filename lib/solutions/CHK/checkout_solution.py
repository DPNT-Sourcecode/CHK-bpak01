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
    
    buy_x_get_y = [(2, "E", 1, "B"), (2, "F", 1, "F"), (3, "N", 1, "M"), (3, "R", 1, "Q"), (3, "U", 1, "U") ]

    x_for_y = {"A" : [(5, 200), (3, 130)], 
               "B" : [(2, 45)], 
               "H" : [(10, 80), (5, 45)], 
               "K" : [(2, 150)], 
               "P" : [(5, 200)], 
               "Q" : [(3, 80)], 
               "V" : [(3, 130), (2, 90)],
              }

    sku_list = [unit for unit in skus]
    for unit in sku_list:
        if unit not in price_table:
            return -1
    

    sku_count = {}
    for unit in sku_list:
        sku_count[unit] = sku_count.get(unit, 0) + 1

    for offer in buy_x_get_y:
        if offer[1] == offer[3]:
            if offer[1] in sku_count.keys() and sku_count[offer[3]] > offer[0]:
                sku_count[offer[1]] = math.ceil(sku_count[offer[1]] * (offer[0]/(offer[0]+offer[2])))
        else:
            if offer[1] in sku_count.keys() and offer[3] in sku_count.keys() and sku_count[offer[1]] >= offer[0]:
                sku_count[offer[3]] -= math.ceil(sku_count[offer[1]] * (offer[2]/offer[0]))
                if sku_count[offer[3]] <= 0:
                    del sku_count[offer[3]]
    
    print(sku_count)
    total_checkout_value = 0
    for unit in sku_count.keys():
        if unit in x_for_y:
            sku_num = sku_count[unit]

            for offer in x_for_y[unit]:
                discounted, sku_num = divmod(sku_num, offer[0])
                total_checkout_value += discounted * offer[1]
            total_checkout_value += sku_num * price_table[unit]

    
        else:
            total_checkout_value += price_table[unit] * sku_count[unit]

    
    
    return total_checkout_value


print(checkout("ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"))
# - {"method":"checkout","params":["ABCDEFGHIJKLMNOPQRSTUVWXYZ"],"id":"CHK_R4_033"}, expected: 965, got: 890
# - {"method":"checkout","params":["ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"],"id":"CHK_R4_139"}, expected: 1880, got: 1760
# - {"method":"checkout","params":["LGCKAQXFOSKZGIWHNRNDITVBUUEOZXPYAVFDEPTBMQLYJRSMJCWH"],"id":"CHK_R4_140"}, expected: 1880, got: 1760

