# Activities & Practices

# 01 What would be the output of the following code:
# for i in range(3):
#   print(i)
# output: 0 1 2  

# 02 What would be the output of the following code:
# numbers = [2, 4, 6, 8]
# for number in numbers:
#   print("hello!")
# output: hello! hello! hello! hello!

# 03 What would be the output of the following code:
# numbers = [1, 1, 2, 3]
# for number in numbers:
#   if number % 2 == 0:
#     continue
#   print(number)
# output: 1 1 3

# 04 Fill in the blank with the appropriate while condition in order to print the numbers 1 through 10 in order:
# i = 1
# while i < 10:
#     print(i)
#     i += 1
# output: 1 2 3 4 5 6 7 8 9 10


# 05 Which of these list comprehensions will create a list equal to desired_list?
# my_list = [5, 10, -2, 8, 20]
# desired_list = [10, 8, 20]
# my_list = [i for i in my_list if i > 5]
# print(my_list)
# output: [10, 8, 20]

# 06 What would be the output of the following code:
# drink_choices = ["coffee", "tea", "water", "juice", "soda"]
# for drink in drink_choices:
#   print(drink)
# output: coffee tea water juice soda

# 07 What would be the output of the following code:
# for i in range(3):
#   print(5)
# output: 5 5 5

# 08 What would be the output of the following code:
# numbers = [1, 1, 2, 3]
# for number in numbers:
#   if number % 2 == 0:
#     break
#   print(number)
# output: 1 1

# 09 Which of these list comprehensions will create a list equal to desired_list?
#desired_list = [-1, 0, 1, 2, 3]
# desired_list = [i-1 for i in range(5)]
# print(desired_list)
# output: [-1, 0, 1, 2, 3]

# 10 Fill in the code to loop over the list grouped_topics and print every element in the list.
# grouped_topics = [["Algorithms", "Data Structures", "AI"], ["Linear Regression", "SQL"]]
# for sublist in grouped_topics:
#     for sublist_element in sublist:
#         print(sublist_element)
# output: Algorithms Data Structures AI Linear Regression SQL


# print("-----------------------------------------------------")
# print("-----------------------------------------------------")


# "Carly's Clippers" Activity 
# I didn't fully grasp from step 7 - 13 _ [01/23/2022]
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
prices = [30, 25, 40, 20, 20, 35, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0
for price in prices:
  total_price = total_price + price

average_price ="Average Haircut Price: " + str(total_price / len(prices))
print(average_price)
print("----------------------------")
new_prices = [price - 5 for price in prices]
print(new_prices)  
print("----------------------------")
total_revenue = 0
for i in range(len(hairstyles)):
  total_revenue = total_revenue + prices[i] * last_week[i]
print("Total Revenue: "+str(total_revenue))
print("----------------------------")
average_daily_revenue = total_revenue / 7
print("Average daily revenue: "+str(average_daily_revenue))
print("----------------------------")
cuts_under_30 = [
  hairstyles[i]
  for i in range(len(hairstyles))
  if new_prices[i] < 30
]
print(cuts_under_30)              