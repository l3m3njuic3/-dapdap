def binarySearch(records):

    print(records)
    print("\n-------Search record by Package Name using Binary Search and update record-------")
    # Taking the packageName from the dictionary and putting it into a list
    packageList = [records[record]["packageName"] for record in records]
    while True:
        packageName = input("Package Name to search: ")
        if packageName != "":
            customerPackageList = []
            for package in sorted(packageList):
                for record in records:
                    if records[record]["packageName"] == package:
                        customerPackageList.append(record)
            # Binary Search code:
            index = -1 # If the target exist in the records, it would not be -1
            low = 0
            high = len(customerPackageList)
            # low starts with the first element which is 0 for the first instance, high is the len of the array.
            while (high >= low):

                mid = low + ((high - low) // 2)  # Middle element

                if mid >= len(customerPackageList):
                    break

                # if element is present at the middle itself
                if packageName.lower() == records[customerPackageList[mid]]["packageName"].lower():
                    index = mid
                    break

                # If target is smaller than mid:
                elif records[customerPackageList[mid]]["packageName"].lower() > packageName.lower():
                    high = mid - 1

                else:   # If target is greater than middle
                    low = mid + 1

            if index == -1:
                print("Package",packageName,"is not found.")
            else:
                print("\nRecord Found - Customer Name:",customerPackageList[index],"|| Package Name:",records[customerPackageList[index]]["packageName"],
                      "|| Number of Pax:",records[customerPackageList[index]]["Pax"],"|| Package Cost Per pax: $",records[customerPackageList[index]]["packageCost"])
                print("What do you wish to update?"
                      "\n1. Customer Name"
                      "\n2. Package Name"
                      "\n3. Number of Pax"
                      "\n4. Package Cost Per Pax")
                print(records[customerPackageList[index]]["packageName"])
                while True: # This loop is for input validation
                    updateChoice = input("What choice do you wish to update: ")
                    if updateChoice == "":
                        print("Choose one of the choices please")
                        continue
                    if updateChoice.isnumeric() == True:
                        updateChoice = int(updateChoice)
                        if int(updateChoice)>0 and int(updateChoice) < 5:
                            break
                    print("Invalid input detected - Please input again")
                if updateChoice != "":
                    if updateChoice == 1:
                        while True:
                            update = input("New Customer Name: ")
                            if update != "":
                                records[update] = records[customerPackageList[index]]
                                del records[customerPackageList[index]]
                                print("Updated! Returning back to Menu")
                            elif update == "":
                                print("Please put in a name: ")
                                continue
                            break

                    elif updateChoice == 2:
                        while True:
                            update = input("New Package Name: ")
                            if update != "":
                                records[customerPackageList[index]]["packageName"] = update

                                print("Updated! Returning back to Menu")
                            elif update == "":
                                print("Please put in a package name: ")
                                continue
                            break
                    elif updateChoice == 3:
                        while True: # This loop is for input validation
                            update = input("New number of Pax: ")
                            if update.isnumeric() == True:
                                records[customerPackageList[index]]["Pax"] = int(update)
                                print("Updated! Returning back to Menu")
                                break
                            elif update is not int:
                                print("Please put an integer")
                                continue
                            break
                    elif updateChoice == 4:
                        while True: # This loop is for input validation
                            update = input("New Package Cost Per Pax: ")
                            if update.isnumeric() == True:
                                records[customerPackageList[index]]["packageCost"] = int(update)
                                print("Updated! Returning back to Menu")
                                break
                            elif update is not int:
                                print("Please put an integer")
                                continue
                            break
                break
        elif packageName == "":
            print("Please input something lols")
        continue

records = {
    "Mike" : {"packageName":"Wedding","Pax":2,"packageCost":770},
    "India" : {"packageName":"Holiday","Pax":4,"packageCost":380},
    "Chipo" : {"packageName":"Business","Pax":1,"packageCost":130},
    "Jusly" : {"packageName":"Kenthouse","Pax":5,"packageCost":560},
    "Poh" : {"packageName":"Castle","Pax":2,"packageCost":280},
    "Brigg" : {"packageName":"Grand","Pax":6,"packageCost":225},
    "John" : {"packageName":"Treehouse","Pax":7,"packageCost":330},
    "Ahgong" : {"packageName":"Birthday","Pax":8,"packageCost":210},
    "Ligma" : {"packageName":"Disney","Pax":4,"packageCost":660},
    "Yrom" : {"packageName":"Date","Pax":5,"packageCost":925}

}
while True:
    print("\n-------Staycation Package Deal Inventory Menu-------"
          "\n1. Display All Records"
          "\n2. Sort record by Customer Name using Bubble sort"
          "\n3. Sort record by Package Name using Selection sort"
          "\n4. Sort record by Package Cost using Insertion sort"
          "\n5. Search record by Customer Name using Linear Search and update record"
          "\n6. Search record by Package Name using Binary Search and update record"
          "\n7. List records range filter")
    while True: # This loop is for input validation
        choice = input("What would like to do today? (Press enter to exit program): ")
        if choice == "":
            print("Thank you for using Staycation Package Deal Inventory Menu!")
            break
        if choice.isnumeric() == True:
            choice = int(choice)
            if int(choice)>0 and int(choice) < 8:
                break
        print("Invalid input detected - Please input again")

    if choice == 6:
        binarySearch(records)
