#------------------------------------------#
# Title: CDInventory.py
# Desc: Starter Script for Assignment 05
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# KSorge-Toomey, 2020-Aug-12, replaced lists with references, added functionality for 
#           deleting entries, adding functionality for loading data from existing file
#------------------------------------------#

# Declare variabls

strChoice = '' # User input
lstTbl = []  # list of lists to hold data
dicRow ={}  # dictionary key
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object

# Get user Input
print('The Magic CD Inventory\n')
while True:
    # 1. Display menu allowing the user to choose:
    print('[l] load Inventory from file\n[a] add CD\n[i] display Current Inventory')
    print('[d] delete CD from Inventory\n[s] save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

    if strChoice == 'x':
        # 6. Exit the program if the user chooses so
        break
    if strChoice == 'l':    # no elif necessary, as this code is only reached if strChoice is not 'exit'
        # 1. Load existing data from file
        lstTbl.clear()
        objFile = open(strFileName, 'r')
        for row in objFile:
            lstRow = row.strip().split(',')
            dicRow= {'ID': lstRow[0], 'CD Title': lstRow[1], 'Artist': lstRow[2]}
            lstTbl.append(dicRow)
        objFile.close()
        print('Data read from file\n')
    elif strChoice == 'a':
        # 2. Add data to the table (2d-list) each time the user wants to add data
        strID = input('Enter an ID: ')
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        dicRow = {'ID':strID, 'CD Title':strTitle, 'Artist':strArtist}
        lstTbl.append(dicRow)
        print('\nNew entry added\n')
    elif strChoice == 'i':
        # 3. Display the current data to the user each time the user wants to display the data
        print('Current Entries:')
        print('ID, CD Title, Artist')
        for row in lstTbl:
            print(*row.values(), sep = ', ', end = '\n')
    elif strChoice == 'd':
        # 4. Delete chosen entry
        strID = input('Which entry would you like to delete? (Enter ID number): ')
        for row in lstTbl:
            if strID == row['ID']:
                lstTbl.remove(row)
                print( strID, ' has been deleted')
            else:
                print( strID, ' doesn\'t exist in the inventory')              
    elif strChoice == 's':
        # 5. Save the data to a text file CDInventory.txt if the user chooses so
        objFile = open(strFileName, 'a')
        for row in lstTbl:
            strRow = ''
            for key in row:
                strRow += str(row[key]) + ','
            strRow = strRow[:-1] + '\n'
            objFile.write(strRow)
        objFile.close()
        print('Data written to file\n')             
    else:
        print('Please choose either l, a, i, d, s or x!')

