

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    
    price_table = {
                    "A" : 50,
                    "B" : 30,
                    "C" : 20,
                    "D" : 15,
                  }
    


    sku_list = [unit for unit in skus]

    for unit in sku_list:
        if unit not in price_table:
            return -1
    
    sku_count = {}

    for unit in sku_list:
        sku_count[unit] = sku_count.get(unit, 0) + 1
    
    total_checkout_value = 0

    for unit in price_table.keys():
        print(unit)
        if unit == "A":
            discounted, non_discounted = divmod(sku_count[unit], 3)
            total_checkout_value += discounted * 130
            total_checkout_value += non_discounted * price_table[unit]
        elif unit == "B":
            discounted, non_discounted = divmod(sku_count[unit], 2)
            total_checkout_value += discounted * 45
            total_checkout_value += non_discounted * price_table[unit]
        else:
            total_checkout_value += price_table[unit] * sku_count[unit]
    
    return total_checkout_value


print(checkout("AAB"))
