def fact_line_rec_proc(n):
   if n == 0 or n == 1:
       return 1
   else:
       return n * fact_line_rec_proc(n - 1)
number = int(input("введите число которое хотите возвести в факториал"))
print(fact_line_rec_proc(number))