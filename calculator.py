keepProgramRunning = True
import math
import cmath
print("what type of operation would you like to do? ")
m=raw_input("Type one->add/subtract/multiply/divide/exponent/trigonometry(trig)/none: ")

#strings--------
add="add"
subtract="subtract"
multiply="multiply"
divide="divide"
exponent="exponent"
trig="trig"
none="none"
cosine="cosine"
sine="sine"
tangent="tangent"
radians="radians"
degrees="degrees"
#strings--------

m=m.lower()

if m==add:
   add_a=raw_input("what is your first number: ")
   if add_a.isdigit():
      add_b=raw_input("what do want to add that to:")
      if add_b.isdigit():
         print("%s + %s = %s") % (add_a,add_b,int(add_a)+int(add_b))
      else:
         print("Enter a valid number")
   else:
      print("Enter a valid number")
elif m==subtract:
   sub_a=raw_input("what is your first number: ")
   if sub_a.isdigit():
      sub_b=raw_input("what do you want to subtract that by: ")
      if sub_b.isdigit():
         print("%s - %s = %s") % (sub_a,sub_b,int(sub_a)-int(sub_b))
   else:
      print("Enter a valid number")
elif m==multiply:
   mult_a=raw_input("what is your first number: ")
   if mult_a.isdigit():
      mult_b=raw_input("what do want to multiply that by: ")
      if mult_b.isdigit():
         print("%s * %s = %s") % (mult_a,mult_b,int(mult_a)*int(mult_b))
      else:
         print("Enter a valid number")
   else:
      print("Enter a valid number")
elif m==divide:
   div_a=raw_input("what is your first number: ")
   if div_a.isdigit():
      div_b=raw_input("what do you want to divide that by: ")
      if div_b.isdigit():
         print("%s / %s = %s") % (div_a,div_b,int(div_a)/int(div_b))
      else:
         print("Enter a valid number")
   else:
      print("Enter a valid number")
elif m==exponent:
   exp_a=raw_input("what is your base number: ")
   if exp_a.isdigit():
      exp_b=raw_input("To the power of:")
      if exp_b.isdigit():
         print ("%s^%s = %s") % (exp_a,exp_b,int(exp_a)**int(exp_b))
      else:
         print("Enter a valid numberw")
   else:
      print("Enter a valid number")
elif m==trig:
   print("which operation would you like to do?")
   T=raw_input("cosine/sine/tangent: ")
   if T==cosine:
      cos_a=raw_input("what is the angle: ")
      if cos_a.isdigit():
         cos_b=raw_input("would you like that in radians or degrees: ")
         if cos_b==radians:
            print("cos(%s) = %s") % (cos_a,math.cos(int(cos_a)))
         elif cos_b==degrees:
            cos_c=math.radians(int(cos_a))
            print("cos(%s) = %s") % (cos_a,math.cos(int(cos_c)))
         else:
            print("Enter a valid operation")
      else:
         print("Enter a valid number")
   elif T==sine:
      sin_a=raw_input("what is the angle: ")
      if sin_a.isdigit():
         sin_b=raw_input("would you like that in radians or degrees: ")
         if sin_b==radians:
            print("sin(%s) = %s") % (sin_a,math.sin(int(sin_a)))
         elif sin_b==degrees:
            sin_c=math.radians(int(sin_a)) 
            print("sin(%s) = %s") % (sin_a,math.sin(int(sin_c)))
         else:
            print("Enter a valid operation")       
      else:
         print("Enter a valid number")
   elif T==tangent:
      tan_a=raw_input("what is the angle: ")
      if tan_a.isdigit():
         tan_b=raw_input("would you like that in radians or degrees: ")
         if tan_b==radians:
            print("tan(%s) = %s") % (tan_a,math.tan(int(tan_a)))
         elif tan_b==degrees:
            tan_c=math.radians(int(tan_a))
            print("tan(%s) = %s") % (tan_a,math.tan(int(tan_c)))
         else:
            print("Enter a valid operation")
      else:
         print("Enter a valid number")
   else:
      print("Enter a valid operation")
elif m==none:
   print("Too bad, bye :)")
   keepProgramRunning = False
else:
  print("Enter a valid operation")   
