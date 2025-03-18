current_temperature = int(input("Current Temperature: "))
budget = float(input("Budget: "))
weatherCondition = str(input("Current Weather Condition: "))

if(current_temperature > 75) and (budget > 20) and (weatherCondition == "Sunny"):
    print('Go to the beach!')
elif(budget < 20) and (weatherCondition == "Sunny"):
    print('Have a picnic in the park.')

if(budget > 15) and (weatherCondition == "Rainy"):
    print('Visit a museum!')
elif(budget < 15) and (weatherCondition == "Rainy"):
    print('Stay in and watch a movie at home.')

if(current_temperature < 60) or (weatherCondition == "Cloudy"):
    print('Go to a coffee shop and enjoy a warm drink.')
