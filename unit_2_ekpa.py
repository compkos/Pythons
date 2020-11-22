import math
correct_type=True
a_value=0
b_value=0
c_value=0
d_value=0
while correct_type==True:
  a=input('Δώσε ένα ακέραιο αριθμό a διάφορο του 0 : ')
  try:
    a_value = int(a)
    if a_value==0:
      print(f'Η Τιμή για το a είναι ίση με 0, προσπάθησε ξανά')
    else:
      correct_type=False
  except ValueError:
    print(f'Η Τιμή {a} δεν είναι ακέραια τιμή, προσπάθησε ξανά')

correct_type=True
while correct_type==True:
  b=input('Δώσε ένα ακέραιο αριθμό b : ')

  try:
    b_value = int(b)
    correct_type=False
  except ValueError:
    print(f'Η Τιμή {b} δεν είναι ακέραια τιμή, προσπάθησε ξανά')

correct_type=True
while correct_type==True:
  c=input('Δώσε ένα ακέραιο αριθμό c : ')
  try:
    c_value = int(c)
    correct_type=False
  except ValueError:
    print(f'Η Τιμή {c} δεν είναι ακέραια τιμή, προσπάθησε ξανά')

print()
print(f"Δώσατε τους αριθμούς a={a_value}, b={b_value}, c={c_value}")
print()
d_value=(b_value**2)-4*(a_value*c_value)
if d_value>0:
  x_1_value=int((-1*b_value+math.sqrt(d_value))/2)
  x_2_value=int((-1*b_value-math.sqrt(d_value))/2)
  print(f"Οι 2 πραγματικές άνισες ρίζες της διακρίνουσας που έχει τιμή {d_value} άρα >0 είναι {x_1_value},{x_2_value}")
elif d_value==0:
  x_1_value=int((-1*b_value)/2*a_value)
  print(f"Η μία ρίζα της διακρίνουσας που έχει τιμή {d_value} άρα =0 είναι {x_1_value}")
else:
  print(f"Δεν υπάρχουν πραγματικές ρίζες γιατί η τιμή της διακρίνουσας είναι {d_value} άρα <0")