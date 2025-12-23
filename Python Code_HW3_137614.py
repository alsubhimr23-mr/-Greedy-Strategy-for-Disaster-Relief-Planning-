
"""
Name: Manar Alsubhi
ID  : 137614
==============================================

1. Determine Storage Capacity: 
    z = last two digits of my university ID = 14
    the warehouse storage capacity 
    C=max(z∗3,60) = max(14*3,60)= max(42,60) = 60
    
    
2. Customize the Supply List:  
- Each supply type has:
    1-initial quantity
    2-impact per unit
    3-total impact = quantity × impact per unit
    
    supply type     initial quantity   impact per unit   total impact
    --------------------------------------------------------------------
    Food Packs        20                5                100=20*5
    Water Bottles     30                3                90=30*3
    Medical Kits      10                12               120=10*12
    Blankets          15                6                90=15*6
    Hygiene Kits      8                 10               80=8*10
    
    
        
- Adjust the initial quantity of each supply type based on my (ID). 
    
    sum of odd digits of my UID = 1+3+7+1 = 12
    w = max (5, 12) = 12 
    qadjusted = qinitial * w 
    
    
    supply type     Adjusted Quantity   impact per unit   total impact
    --------------------------------------------------------------------
    Food Packs        20 * 12 = 240        5             5  * 240 = 1200
    Water Bottles     30 * 12 = 360        3             3  * 360 = 1080  
    Medical Kits      10 * 12 = 120        12            12 * 120 = 1440         
    Blankets          15 * 12 = 180        6             6  * 180 = 1080  
    Hygiene Kits      8  * 12 = 96         10            10 * 96  = 960  
    
    
3. Potential Greedy Solutions: 
    a. Optimal Greedy solution 
    Highest Impact per Unit (Optimal)
        Medical Kits(12) --> Hygiene Kits(10)  -->  Blankets(6)  --> Food Packs(5) --> Water Bottles(3) 
    
    Highest IPU is Medical Kits
    Medical Kits available = 120
    C = Storage capacity = 60
    So take 60 from Medical Kits
    Total optimal impact = 60 * 12 = 720
    -------------------------------------
    b. Non-Optimal Greedy Solution
    
    1) Highest Total Impact
        Medical Kits(1440) --> Food Packs(1200) -->  Water Bottles(1080) --> Blankets(1080)  --> Hygiene Kits(960)
   
    Highest Total Impact is Medical Kits
    Medical Kits available = 120
    C = Storage capacity = 60
    So take 60 from Medical Kits
    Total optimal impact = 60 * 12 = 720
    
    here the non-optimal strategy happens to match the optimal because the first choice is the same in both high IPU and high impact
    ------------------------------------
    2) Smallest Quantity First
        Hygiene Kits(96)  --> Medical Kits(120) --> Blankets(180)  -->  Food Packs(240) -->  Water Bottles(360)  
        
        Smallest Quantity is Hygiene Kits 
        Hygiene Kits available = 96
        C = Storage capacity = 60       
        So take 60 from Hygiene Kits
        Total optimal impact = 60 * 10 = 600

----------------------------------------------------        
4. Discussion 
a. Why the optimal greedy algorithm works

The greedy algorithm chooses the supply with the highest impact per unit (IPU) first.
This works because:

1)Greedy choice property:
Taking the item that gives the most impact for each unit of storage is always the best local decision.
Since every unit of storage has the same cost, choosing the highest IPU item gives the best return.

2)Optimal substructure:
After choosing the best item, the remaining problem is the same but with smaller storage.
So the best solution to the full problem is made from the best solution to the smaller remaining problem.

Because both properties are true, the greedy approach gives the maximum total impact.

b. Why non-optimal strategies fail

Other strategies do not look at the IPU, so they make bad choices.

1)Highest Total Impact First:
This looks at total quantity × IPU, but we cannot take all the quantity.
Storage is limited, so this number is misleading.
It may choose a lower-value item even though a higher-value one exists.

2)Smallest Quantity First:
This chooses the item with the smallest amount, not the highest impact.
It fills the storage with items that give less impact, leaving no room for better ones.

Because these strategies ignore the true measure of value (IPU), they lead to lower total impact compared to the optimal greedy algorithm.    
"""

def main():
    #create a list that contains dictionaries of all information about each supply 
    Supplies =[ {"Supply Type" : "Food Packs",
                 "Quantity"    :  240        ,
                 "IPU"         :  5          ,
                 "Total Impact":  1200},
    
                {"Supply Type" : "Water Bottles",
                "Quantity"    :  360       ,
                "IPU"         :  3           ,
                "Total Impact":  1080},
            
                {"Supply Type" : "Medical Kits",
                "Quantity"    :  120       ,
                "IPU"         :  12           ,
                "Total Impact":  1440},
            
            
                {"Supply Type" : "Blankets",
                "Quantity"    :  180       ,
                "IPU"         :  6           ,
                "Total Impact":  1080},
                
                {"Supply Type" : "Hygiene Kits",
                "Quantity"    :  96       ,
                "IPU"         :  10           ,
                "Total Impact":  960}
                ]
     
    #initilize the capacity       
    Storage_capacity  = 60 

    #call the function that response of dispaling menu     
    Display_Menu(Supplies)

#==================================================================

"""
This function response of sorting the elements descending or ascending depending on what put on the argument reverse

@parm : data / list that want to sorted
@parm : key  / target element
@parm : reverse (False for ascending , and true for descending)  
         
    Set n = number of items in the list.
    Repeat until no swaps happen:
    Set swapped = False.
    
    For each pair of neighbors in the list:
        If reverse = False (ascending):
            If left item > right item, swap them and set swapped = True.
        If reverse = True (descending):
            If left item < right item, swap them and set swapped = True.
    
    When a full pass happens with no swaps, stop.

@Return the list(data).
"""
def bubbleSort(data,key,reverse = False):
    n = len(data)
    for i in range(n):
        swapped = False        
        for j in range(n-i-1):
            
            if reverse:    #descending
                if data[j][key] < data[j+1][key]:
                    data[j],data[j+1] = data[j+1],data[j]
                    swapped = True
                    
            else:         # ascending
                if data[j][key] > data[j+1][key]:
                    data[j],data[j+1] = data[j+1],data[j]
                    swapped = True
                    
        if (swapped == False):
            break
    return data 
   
#==================================================================
#a. Implement the optimal greedy algorithm for selecting supplies.
"""
Algorithim of this function:
    
1- Make a copy of the list of supplies so the original data does not change.
2- Sort the copied list in descending order of IPU (Impact Per Unit)
3- Use bubble sort (highest IPU first).

4- Set:
capacity = 60, Remaining_storage = 60 , total_impact = 0, Chosen = empty list

5- For each supply in the sorted list:
    1- Determine the quantity we can take:
    taken_quantity = min(supply quantity, Remaining_storage)
    
    2- Calculate impact:
    impact = taken_quantity × IPU
    
    3- Add an entry to Chosen with:    
    supply type, taken quantity, IPU, total impact
    
    4- Add the impact to total_impact
    
    5- Reduce remaining storage:
    Remaining_storage = Remaining_storage - taken_quantity
    
    6- If storage becomes 0, stop the loop.

6- For each selected item, print its supply type.
7- Finally, print the total impact.
"""

def optimal_greedy(Supplies):
    
    #copy the data in new list to be sure dont change in orginal data
    data = []
    for dic in Supplies:
        copy_dict = dic.copy()
        data.append(copy_dict)

    # Sort by highest IPU (Impact Per Unit)
    bubbleSort(data, "IPU", reverse=True)

    Choosen = []
    capacity = 60
    Remaining_storage = capacity
    total_impact = 0

    # Greedy select the highest IPU items first
    for supply in data:
        taken_quantity = min(supply["Quantity"], Remaining_storage)
        impact = taken_quantity * supply["IPU"]

        Choosen.append({
            "Supply Type": supply["Supply Type"],
            "Quantity": taken_quantity,
            "IPU": supply["IPU"],
            "Total impact": impact
        })

        total_impact += impact
        Remaining_storage -= taken_quantity

        if Remaining_storage == 0:
            break

    for item in Choosen:
        print("Selected Suppliers: ['%s']" % item["Supply Type"])

    print("Total Impact:", total_impact)



#==================================================================
#b. Implement the two non-optimal strategies     
"""
Algorithim of this function:
    
1- Set:
capacity = 60, Remaining_storage = 60 , total_impact = 0, Chosen = empty list

2- For each supply in the sorted list:
    1- Determine the quantity we can take:
    taken_quantity = min(supply quantity, Remaining_storage)
    
    2- Calculate impact:
    impact = taken_quantity × IPU
    
    3- Add an entry to Chosen with:    
    supply type, taken quantity, IPU, total impact
    
    4- Add the impact to total_impact
    
    5- Reduce remaining storage:
    Remaining_storage = Remaining_storage - taken_quantity
    
    6- If storage becomes 0, stop the loop.

3- For each selected item, print its supply type.
4- Finally, print the total impact.
"""

def Non_Optimal_Greedy(data):
   
    Choosen = []
    capacity = 60
    Remaining_storage = capacity
    total_impact = 0
    
    for supply in data:
        taken_quantity = min(supply["Quantity"],Remaining_storage)
        impact =  taken_quantity * supply["IPU"]
        
        Choosen.append({"Supply Type" : supply["Supply Type"],
                        "Quantity": taken_quantity,
                        "IPU": supply["IPU"],
                        "Total impact": impact
                        })
        
        total_impact += impact
        Remaining_storage -= taken_quantity
        
        if Remaining_storage == 0:
            break
        
    for item in Choosen:
        print("Selected Suppliers: ['%s']" % item['Supply Type'])

    
    print("Total Impact: ", total_impact) 


# -------- Strategy 1: Highest Total Impact ---------
"""
Algorithim of this function:    
    1- Make a copy of the list of supplies so the original data does not change.
    2- Sort the copied list in descending order of Total_Impact by bubblesort function
    3- return list
"""
def Highest_Total_Impact(Supplies):
    
    #copy the data in new list to be sure dont change in orginal data
    data = []
    for dic in Supplies:
        copy_dict = dic.copy()
        data.append(copy_dict)
    
    #call bubbleSort function that sort the dictionaries according to the total impact descending  
    bubbleSort(data ,"Total Impact",reverse = True)
    
    return data



# -------- Strategy 2: Smallest Quantity -------------
"""
Algorithim of this function:    
    1- Make a copy of the list of supplies so the original data does not change.
    2- Sort the copied list in ascending order of quantity by bubblesort function
    3- return list
"""
def Smallest_Quantity(Supplies):
    #copy the data in new list to be sure dont change in orginal data
    data = []
    for dic in Supplies:
        copy_dict = dic.copy()
        data.append(copy_dict)
        
        
    #call bubbleSort function that sort the dictionaries according to the quantity ascending  
    bubbleSort(data ,"Quantity",reverse = False)
    
    return data



 
#==============================================================
#c. Include a menu for the user to select different strategies and display the total impact 
"""
Algorithim of this function:
    1- Create a list called Menu containing four strategy names:
        Highest Impact per Unit (Optimal)
        Highest Total Impact
        Smallest Quantity First
        Quit
    
    2- Display the message: "Select Greedy Strategy:"
    
    3- For each item in the Menu list:
        Print its number (starting from 1) and name.
    
    4- Ask the user to enter a choice (1–4) and store it in choice.
    
        If choice = 1: Call optimal_greedy(Supplies)
        Else if choice = 2: Call Non_Optimal_Greedy( Highest_Total_Impact(Supplies) )
        Else if choice = 3: Call Non_Optimal_Greedy( Smallest_Quantity(Supplies) )    
        Else if choice = 4: Exit the function.
        Else: Print “Invalid choice! Please select from shown strategies.”
"""
def Display_Menu(Supplies):
    Menu = [ "Highest Impact per Unit (Optimal)",
             "Highest Total Impact",
             "Smallest Quantity First",
             "Quiet"]
    
    print("Select Greedy Strategy:")
    for i in range(len(Menu)):
        print(i+1,". ", Menu[i])
    
    choice = int(input("Enter choice: "))
    
    if choice == 1:
       optimal_greedy(Supplies)
        
    elif choice == 2:
       Non_Optimal_Greedy(Highest_Total_Impact(Supplies))
        
    elif choice == 3:
        Non_Optimal_Greedy(Smallest_Quantity(Supplies))
    
    elif choice == 4:
        return
        
    else:
        print("Invalid choice !! Please select from shown strategies")
    
    

main()


"""
PART B:
    
    
a. Maximize coverage per volunteer-hour.

    the budget = storage capicity = 60
    B = C = 60
    Coverage per Hour = Coverage value / Total Hours

    Shift      Volunteers    Coverage     Hours per      Total         Coverage per 
                Required      value       Volunteer      Hours            Hour
    ----------------------------------------------------------------------------------------
    Shift1       5            50            3            3*5 = 15       50/15 = 3.33
    Shift2       3            30            2            3*2 = 6        30/6  = 5
    Shift3       8            80            4            8*4 = 32       80/32 = 2.5
    Shift4       2            20            1            2*1 = 2        20/2  = 10
    Shift5       6            60            3            6*3 = 18       60/18 = 3.33
    Shift6       4            40            2            4*2 = 8        40/8  = 5

Shift4 (10) --> Shift2 (5) --> Shift6 (5) --> Shift1 (3.33) --> Shift5 (3.33) --> Shift3 (2.5)

b. Determine the total coverage achievable within the budget.
B = budget = 60 hours                                                                                          

Shift 4: 
    Needs 2 hours 
    Remaining budget = 60 − 2 = 58 
    Add coverage 20 
    Total coverage = 20

Shift 2: 
    Needs 6 hours 
    Remaining budget = 58 − 6 = 52 
    Add coverage 30 
    Total coverage = 20 + 30 = 50

Shift 6: 
    Needs 8 hours 
    Remaining budget = 52 − 8 = 44
    Add coverage 40
    Total coverage = 50 + 40 = 90

Shift 1:
    Needs 15 hours 
    Remaining budget = 44 − 15 = 29 
    Add coverage 50 
    Total coverage = 90 + 50 = 140

Shift 5: 
    Needs 18 hours 
    Remaining budget = 29 − 18 = 11 
    Add coverage 60 
    Total coverage = 140 + 60 = 200

Shift 3:
Needs 32 hours
Remaining budget = 11 
Not enough --> Skip       
--------------------------

Total coverage = 200
Selected shifts = 4, 2, 6, 1, 5  


2. Evaluate Greedy Applicability:
a. Discuss whether the greedy strategy guarantees an optimal solution.  
    Not always greedy strategy guarantees an optimal solution.  
    Greedy selects based on coverage per hour, which may ignore combinations of smaller shifts that fit better in the budget.

b. counterexample where it might fail. 
let B = budget = 10 hours and have two shifts:

Shift	Volunteers	Coverage     	Hours	Coverage/hr
-------------------------------------------------------
shift1	    4           50	          4	       12.5
shift2	    6	        100	          6	       16.67

Greedy pick Shift 2(has highest Coverage/hr):
    Needs 6 hours 
    Remaining budget = 10-6 = 4
    Add coverage 100 
    Total coverage = 100
    
but cannot pick shift 1

Optimal Approach: pick both shift 1, shift 2 
      budget = 10
      4+6 = 10 hours 
      Total coverage = 50+100 = 150   

Greedy fails here because it doesn’t consider full combinations.                                                                   
"""


