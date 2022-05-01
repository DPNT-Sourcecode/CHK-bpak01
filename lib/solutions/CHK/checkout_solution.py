

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    
    price_table = {
                    "A" : 50,
                    "B" : 30,
                    "C" : 20,
                    "D" : 15,
                    "E" : 40,
                  }
    


    sku_list = [unit for unit in skus]

    for unit in sku_list:
        if unit not in price_table:
            return -1
    
    sku_count = {}

    for unit in sku_list:
        sku_count[unit] = sku_count.get(unit, 0) + 1
    
    # ADD a B for every two E's
    if "B" in sku_count.keys() and "E" in sku_count.keys():
        additions, _ = divmod(sku_count["E"], 2)
        sku_count["B"] -= additions
        if sku_count["B"] < 1:
            del sku_count["B"]

    
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




