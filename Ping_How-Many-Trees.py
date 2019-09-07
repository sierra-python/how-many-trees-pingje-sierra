sac = 100.11 # Sq. Mi in Sacramento

# 5 sample areas, 200' x 200'
area1 = 7
area2 = 10
area3 = 20
area4 = 30
area5 = 27

# Average trees for our samples
avg_trees = (area1 + area2 + area3 + area4 + area5) / 5

# Get size of sample are in square feet
sample = 200 * 200

# convert 1 sq mi to sq ft
convert_mi = 5280 * 5280

# sample area in sq mi
sample_mi = sample / convert_mi

# trees per sample area multipled by area of Sacramento
answer = (avg_trees / sample_mi) * sac

print('{:,}'.format(int(answer)))
