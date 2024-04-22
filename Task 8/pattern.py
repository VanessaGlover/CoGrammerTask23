max_rows = 10
for row in range (1,10):
    if row <=5:
        stars = "*" * row
        print(stars)
    
    else:
        bottom_rows = max_rows-row
        stars="*" * bottom_rows
        print(stars)