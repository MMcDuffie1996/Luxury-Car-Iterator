#Miles McDuffie
#The following is the input of car types, its features, and brands (regular and luxury)
regular_car_brands = ['nissan', 'subaru', 'dodge', 'toyota', 'mazda', 'buick', 'jeep', 'kia', 'hyundai' ,'ford', 'fisker', 'chystler', 'chevy', 'honda', 'fiat']
#Telling the difference between both luxury and regular car brands
luxury_car_brands = ['bmw', 'alfa romero', 'audi', 'genesis', 'rolls royce', 'tesla', 'bentley', 'lexus', 'porsche', 'ferrari', 'jaguar', 'cadillac', 'maserati']
#See if you can backslash a list
# car_types = ['minivan', 'suv', 'hatchback', 'station wagon', 'convertible', 'sedan', 'truck', 'ford mustang', 'limousine', 'coupe', 'sports car', 'cross over', 'hybrid']
#line 6 may not be needed
luxury_safety_features = ['adaptive cruise control', 'park assist', 'driver attention monitor', 'electronic stability control system', 'lane tracing assist', 'assisted braking system']

#get some space between lines so you won't confuse yourself
#problem: python is reading the input first, but not the greeting



user_car = input("Please tell me, what is your car brand: ").lower()
# follow_up_question = input("what is your car type: ")

for car in regular_car_brands:#this loop iterates between all the regular car brands
    if user_car == car:#if the user car matches within the regular car brands it will print and end the program
        print("This is a regular car brand.")
for car in luxury_car_brands:#this loop iterates through luxury car brands
    if user_car == car:
        user_safety_feature = input("What are your car safety features: ").lower()
        safety_feature_found = 0 # flag to indicate whether safety feature is luxury
        for feature in luxury_safety_features:#this is where I use nested for loops to see if the safety feature matches in Luxury_safety_features
            if user_safety_feature == feature:
                print("Yes! this is a luxury car brand.")
                safety_feature_found = 1 # safety feature IS luxury, set flag to 1 indicating it is found
        if safety_feature_found == 0: # if the luxury feature is NOT found, say it is not a luxury car
            print("this is not a luxury car brand, please refer back to list.")        
