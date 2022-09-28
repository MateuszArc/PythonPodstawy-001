''' Pharma A, Vitamin C,100
    Drugstore XYZ,Penicilin, 20, pills
    Drugstore ABC,Aspirin,60
    Pharma X,Montelukast,10
    Pharma at grocery,Amoxicillin,?
    Pharmacy 123,Cephalexin,100
    Pharmacy 123,Prednisolone Sodium Phosphate
    Pharma X,Nystatin,45'''
 
import sys
try:
    file_path = r'c:\temp\data_input\orders.csv'
 
    with open(file_path,"r") as file:
 
        for line in file:
 
            line = line.replace('\n','')
            order = line.split(',')
 
            pharmacy_name = order[0]
            item = order[1]
            amount = int(order[2])
    print('Order from drugstore "%s", item "%s", amount %d', pharmacy_name, item, amount)
    print("Processing finished")
except:
    print("Something went wrong...Program have following error:", sys.exc_info())

