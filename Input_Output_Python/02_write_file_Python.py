def Write_list_file():
    print("Creating file with lists")
    city_name = []
    print("Enter any 5 city names")
    for i in range(5):
        town = input()
        city_name.append(town)
    with open("cityname.txt","w") as city_files:
        for city in city_name:
            print(city,file=city_files)
    print()
    print(city_name)
    for city in city_name:
        print(city)

def write_tuple_file():
    print("Creating file with Tuples")
    imelda = "More Mayhem", "Imelda May", "2011", (
        (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz"))
    with open("imelda3.txt", "w") as imelda_file:
        print(imelda, file=imelda_file)



if __name__ == "__main__":
    print("Chose any of the following")
    print("1.\tWrite on  List File")
    print("2.\tWrite on Tuple File")
    choice =input()
    if choice == "1":
        Write_list_file()
    elif choice == "2":
        write_tuple_file()