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
                    "K" : 70,
                    "L" : 90,
                    "M" : 15,
                    "N" : 40,
                    "O" : 10,
                    "P" : 50,
                    "Q" : 30,
                    "R" : 50,
                    "S" : 20,
                    "T" : 20,
                    "U" : 40,
                    "V" : 50,
                    "W" : 20,
                    "X" : 17,
                    "Y" : 20,
                    "Z" : 21,
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
    
    bundle_offer = ["S", "T", "X", "Y", "Z"]

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
    
 

    total_checkout_value = 0
    for unit in sku_count.keys():
        if unit in bundle_offer:
            continue

        if unit in x_for_y:
            sku_num = sku_count[unit]

            for offer in x_for_y[unit]:
                discounted, sku_num = divmod(sku_num, offer[0])
                total_checkout_value += discounted * offer[1]
            total_checkout_value += sku_num * price_table[unit]
            del sku_count[unit]

        else:
            total_checkout_value += price_table[unit] * sku_count[unit]
            del sku_count[unit]



    bundle_skus = sorted(sku_count.items(), key=lambda x: price_table[x[0]], reverse=True)
    print(bundle_skus)
    bundle_list = []
    for unit in bundle_skus:
        counter = unit[1]
        while counter != 0:
            bundle_list.append(unit[0])
            counter -= 1
    print(bundle_list)
    if len(bundle_list) % 3 == 0:
        bundles_num, _ = divmod(len(bundle_list), 3)
        total_checkout_value += bundles_num * 45
    elif len(bundle_list) > 3:
        bundles_num, remainder = divmod(len(bundle_list), 3)
        total_checkout_value += bundles_num * 45
        print(total_checkout_value)
        
        for unit in bundle_list[-remainder:]:
            print(unit)
            total_checkout_value += price_table[unit]
    else:
        for unit in bundle_list[remainder:]:
            total_checkout_value += price_table[unit]


    return total_checkout_value

print(checkout("STYXZZZ"))





