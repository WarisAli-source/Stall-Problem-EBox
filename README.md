# Stall-Problem-EBox
Ebox Internship Problem
STALL
Stall
Now let's try out another simple concept of calculating the Stall amount in our application. For this, we can take our example of Class Stall, and its child classes GoldStall and PlatinumStall.
     
Create a parent class Stall with the following attributes.

Attribute	Datatype
name	str
detail	str
contact	int
owner_name	str
basic_price	int
Use the __init__() method to initialize the attributes.

Method	Description
display()	This method is used to display the details of the Stall.
 

Create Two other child classes(GoldStall, PlatinumStall) with the following attributes and method

Attribute	Datatype
extra_amount	int
Use the __init__() method to initialize the attributes.

Method	Description
display()	This method is used to calculate the total price and display the details of the  Stall.
 
Note : Use super().display() to call parent class display details in child class
 Refer to sample input/output for further details and format of the output.

[All Texts in bold corresponds to the input and rest are output]

Sample Input and Output 1:
Menu
1.Gold stall
2.PlatinumStall
 
Enter customer choice
1
Enter Stall name
chandan Express
Enter Stall Details
Express of life
Enter contact number
9876543210
Enter Owner name
Chandan
Enter Basic price
1200
Enter the Extra amount for GoldStall
750
Name: chandan Express
Details: Express of life
Contact Number: 9876543210
Owner Name: Chandan
Stall price per day: 1950

Sample Input and Output 2:
Menu
1.Gold stall
2.PlatinumStall
 
Enter customer choice
2
Enter Stall name
victory Stalls
Enter Stall Details
Products to win
Enter contact number
7896543210
Enter Owner name
sabar subash
Enter Basic price
1234
Enter the Extra amount for GoldStall
523
Name: victory Stalls
Details: Products to win
Contact Number: 7896543210
Owner Name: sabar subash
Stall price per day: 1757
 
