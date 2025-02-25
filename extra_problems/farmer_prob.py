land_per_crop = 16

tomato_yield = (10 * 0.3 + 12 * 0.7) * land_per_crop
potato_yield = 10 * land_per_crop
cabbage_yield = 14 * land_per_crop
sunflower_yield = 0.7 * land_per_crop
sugarcane_yield = 45 * land_per_crop

tomato_price = 7
potato_price = 20
cabbage_price = 24
sunflower_price = 200
sugarcane_price = 4000

tomato_revenue = tomato_yield * tomato_price * 1000
potato_revenue = potato_yield * potato_price * 1000
cabbage_revenue = cabbage_yield * cabbage_price * 1000
sunflower_revenue = sunflower_yield * sunflower_price * 1000
sugarcane_revenue = sugarcane_yield * sugarcane_price * 1000

total_sales = tomato_revenue + potato_revenue + cabbage_revenue + sunflower_revenue + sugarcane_revenue

chemical_free_sales = total_sales - sugarcane_revenue

print("Total Sales: Rs.", total_sales)
print("Chemical-Free Sales after 11 months: Rs.", chemical_free_sales)
