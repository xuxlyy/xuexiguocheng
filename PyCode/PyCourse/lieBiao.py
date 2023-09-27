shopping_list = []
shopping_list.append("xianshiqi")
shopping_list.append("jianpan")
shopping_list.remove("jianpan")
shopping_list.append("jianmao")
print(len(shopping_list))
shopping_list[1] = "yingpan"

price = [799,1000,200,800]
max_price=max(price)
min_price=min(price)
sorted_price = sorted(price)