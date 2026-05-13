# dictionary comprehension with if else condition
# d ={1:'odd',2:'even'}

even_odd_dict = {i:('even' if i % 2 == 0 else "odd") for i in range(1, 11) }
print(even_odd_dict)

voting_dict = {i:('Eligible' if i > 18 else "InEligible") for i in range(15, 21) }
print(voting_dict)
