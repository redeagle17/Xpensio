def cat():
    to = 'zomato'
    amount = 500

    food = ['zomato','swiggy','eatsure','eatclub','dominos','pizzahut','ovenstory','mcdonalds','burger king','mojo pizza','fasoos','kaggis','kfc']
    travel = ['makemytrip','goibibo','easemytrip','indigo','airasia','spicejet','airindia','gofirst','ola','uber','rapido']
    ecommerce = ['dunzo','amazon','flipkart','myntra','bigbasket','dmart','bookmyshow']

    sumf=0
    sumt=0
    sume=0
    sumo=0
    if to.lower() in food:
        sumf += amount
    elif to.lower() in travel:
        sumt += amount
    elif to.lower() in ecommerce:
        sume += amount
    else:
        sumo += amount
        
    return {"category1":sumf,"category2":sumt,"category3":sume,"category4":sumo}