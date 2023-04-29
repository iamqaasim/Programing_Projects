'''
This programe computes the costs of sending a parcel based on the variables listed below

Variables:
  Fright type: air or land
  Insurance cover: full or limited
  Gift cover: yes or no
  Delivery type: priority or standard
  Parcel type: sleeve, box or create

User inputs are validated at run time before moving to the computational function
'''

#Costs
#Freight (per km)
air_freight = 0.36
land_freight = 0.25

#Insurance cover: 
full_insurance = 50.00
limited_insurance = 25.00

#Gift cover: 
gift_cover = 15.00
no_gift_cover = 0.00

#Delivery type: 
priority_delivery = 100.00 
standard_delivery = 20.00

#Parcel type:
postage_sleeve = 100
postage_box = 150
postage_crate = 400

#Validate user iinputs
#Freight:
#validate distance input
def validate_distance() -> int:
  distance = input("Distance (in km): ")
  try:
    int(distance)
  except ValueError:
    print("invalid input, please input a number ONLY")
    return validate_distance()
  else:
    if int(distance):
      valid_distance = True
    else:
      valid_distance = False
    if valid_distance:
      return int(distance)
    else:
      print("invalid input, please input a number ONLY")
      return validate_distance()

#validate freight input
def validate_freight() -> str:
  freight = input("Freight type (Air/Land): ")
  valid = ["air", "land"]
  if freight.lower() in valid:
    valid_freight = True
  else:
    valid_freight = False
  if valid_freight:
    return freight.lower()
  else:
    print("invalid input")
    return validate_freight()

#Insurance
#validate insurance input
def validate_insurance() -> str:
  insurance = input("Insurance cover (Full/Limited): ")
  valid = ["full", "limited"]
  if insurance.lower() in valid:
    valid_insurance = True
  else:
    valid_insurance = False
  if valid_insurance:
    return insurance.lower()
  else:
    print("invalid input")
    return validate_insurance()
  
#Gift: 
#validate gift input
def validate_gift() -> str:
  gift = input("Gift cover (Yes/No): ")
  valid = ["yes", "no"]
  if gift.lower() in valid:
    valid_gift = True
  else:
    valid_gift = False
  if valid_gift:
    return gift.lower()
  else:
    print("invalid input")
    return validate_gift()

#Delivery: 
#validate delivery input
def validate_delivery() -> str:
  delivery = input("Delivery type (Priority/Standard): ")
  valid = ["priority", "standard"]
  if delivery.lower() in valid:
    valid_delivery = True
  else:
    valid_delivery = False
  if valid_delivery:
    return delivery.lower()
  else:
    print("invalid input")
    return validate_delivery()

#Parcel:
#validate parcel input
def validate_parcel() -> str:
  parcel = input("Parcel type (Sleeve/Box/Crate): ")
  valid = ["sleeve", "box", "crate"]
  if parcel.lower() in valid:
    valid_parcel = True
  else:
    valid_parcel = False
  if valid_parcel:
    return parcel.lower()
  else:
    print("invalid input")
    return validate_parcel()

#computational function
def courier_calculation(distance: int, freight: str, insurance: str, gift: str, delivery: str, parcel: str) -> str:
  print("")
  print("List items:") 
  
  #calculate freight cost with distance
  if freight == "air":
    freight = int(distance*air_freight)
  if freight == "land":
    freight = int(distance*land_freight)
  print(f"Freight cost    = R{freight}")

  #Insurance type: 
  if insurance == "full":
    insurance = full_insurance
  if insurance == "limited":
    insurance = limited_insurance
  print(f"Insurance cost  = R{insurance}")

  #Gift cover: 
  if gift == "yes":
    gift = gift_cover
  if gift == "no":
    gift = no_gift_cover
  print(f"Gift cover cost = R{gift}")

  #Delivery type:
  if delivery == "priority":
    delivery = priority_delivery
  if delivery == "standard":
    delivery = standard_delivery
  print(f"Delivery cost   = R{delivery}")
  
  #Parcel type
  if parcel == "sleeve":
    parcel = postage_sleeve
  if parcel == "box":
    parcel = postage_box
  if parcel == "crate":
    parcel = postage_crate
  print(f"Parcel cost     = R{parcel}")

  #calculate total courier cost
  total_cost = int(freight) + int(insurance) + int(gift) + int(delivery) + int(parcel)
  print("") 
  print(f"Total courier cost = R{total_cost}")


if __name__ == '__main__': #run file in terminal using commad "python main.py"
  '''
  Test user inputs:
  distance  = validate_distance()
  freight   = validate_freight()
  insurance = validate_insurance()
  gift      = validate_gift()
  delivery  = validate_delivery()
  parcel    = validate_parcel()
  '''
  
  courier_calculation(validate_distance(), validate_freight(), validate_insurance(), validate_gift(), validate_delivery(), validate_parcel())