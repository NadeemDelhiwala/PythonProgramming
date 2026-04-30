# fibonacci series
# 0 1 1 2 3 5 8 13 21 34 55
 # a=0
 # b=1
 # res=0+1=1 (a+b)
 # a=b ,a=1 gets stored now
 # b=res =1
 
 # res =1+1=2 (a+b)
 # a=1
 # b=2
 
 # res =1+2 =3 (a+b)
 # a=b a=2
 # b=3
 
 # res =2 +3 =5 (a+b)
 # a =b  , a=3
 # b=5
 
 # res =3+ 5 (a+b)
 # a=b , a=5
# b=5
 
# user input
# 1 --> 0
# 2 --> 0 1
# 3 --> 0 1 1
# 4 --> 0 1 1 2

# for i in range(1, 11):
#   print(i, end=" ")
#   # print(i, end=" ,")


def fibonacci_series(n):
  first_no = 0  # first number =0
  second_no = 1  # second_number =1
  if n == 1:
    print(first_no)
  elif n == 2:
    print(second_no)
  else:
    print(first_no, second_no, end=" ")
    for i in range(n - 2):
      third_no = first_no + second_no  # 0 + 1 =1 third_no=1
      first_no = second_no
      second_no = third_no
      print(second_no, end=" ")
    

fibonacci_series(8)
    
