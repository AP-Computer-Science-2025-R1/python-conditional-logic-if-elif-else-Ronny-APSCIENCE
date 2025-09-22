print("Ronny Joel Illicachi")

score = 85
if score>= 90:
   print("Grade A")

elif score >=80:
     print("Grade B")

elif score > 82:
     print("Honors B")

else:
    print("Grade:C or lower")
    
age = 20
has_fake_id = True

if age >= 21:
    print("Welcome. Please come in.")

elif has_fake_id == True:
    print("Your ID looks fake. Get Out.")
    
else:
    print("Sorry, you are too young to enter")
    
username = "AdminUser"
password = "Password123"

if username == "AdminUser" == password == "SuperSecret":
    print("Full system access granted")

elif username == "Guest" or password == "Password123":
    print("Guest access granted")

else:
    print("Access Denied")
    
temp = 45

if temp < 0:
    print("Danger: Freezing. Pipes may burst.")
    
if temp < 32:
    print("Warning: Below freezing.")
    
elif temp > 90 or temp < 100:
    print("Danger: Heat advisory")
    
elif temp >= 110:
    print("Danger: Extreme heat")
    
else:
    print("Temperature is normal")
    
purchase_total = 75

if purchase_total > 50:
    print("You get free shipping!")
    
if purchase_total == 0:
    print("You get free shipping!")
    
else:
    print("Standard shipping cost: $5.00")
    
username = "admin"
password_length = 12

if username == "admin" and password_length < 10 :
    print("Login Successful.")
    
if username == "user" and password_length<=6:
    print("Admin password incorrect")
    
else:
    print("User password must be 6+")
