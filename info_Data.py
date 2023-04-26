import csv 
    
def info_stock():

    symbol = []

    with open('stocks.csv') as csvfile:
        info_get = csv.reader(csvfile)
        for row in info_get:
            symbol.append(row[0])
            
            return symbol