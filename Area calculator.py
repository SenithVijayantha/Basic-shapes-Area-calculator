def Rectangle():
	w= int(input("Enter the width:- "))
	l = int(input("Enter the length:- "))
	print("Area = "+ str(area))
	area = (w * l)
#Rectangle()

def Circle():
	r = int(input("Enter radius:- "))
	area = (3.14 * r * r)
	print("Area = "+ str(area))
#Circle()

def Triangle():
	b = int(input("Enter base length:- "))
	h = int(input("Enter the height:- "))
	area = (1/2 * b * h)
	print("Area = "+ str(area))
#Triangle()

def Trapezoid():
	tl = int(input("Enter the top length:- "))
	bl = int(input("Enter the bottom length:- "))
	h = int(input("Enter the height:- "))
	area = (((tl + bl)/2) * h )
#Trapezoid()

def Parallelogram():
	b = int(input("Enter the base length:- "))
	h = int(input("Enter the height:- "))
	area = (b * h)
	print("Area = "+ str(area))
#Parallelogram()

Introduction = ("Welcome\n Using this software you can calculate area of following shapes.\n 1.Rectangle\n 2.Circle\n 3.Triangle\n 4.Trapezoid\n 5.Parallelogram")
print(Introduction)
Choice = str(input("Enter the number relevent to your choice:- "))

if (Choice == "1"):
	Rectangle()
elif (Choice == "2"):
	Circle()
elif (Choice == "3"):
	Triangle()
elif (Choice == "4"):
	Trapezoid()
else:
	Parallelogram()
