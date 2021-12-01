def printTest():
    print("Hello world!")


if __name__ == '__main__':
    # printTest()
    # 071
    sports_list = ["baseball", "basketball"]
    inSport = input("What sports do you like the most :")
    sports_list.append(inSport)
    for i in sports_list:
        print(i)

    # 069 & 070
    # countries = ("korea", "usa", "turkey", "japan", "china")
    # for i in countries:
    #     print(i)
    # orderCountry = int(input("Type the country order :"))
    # print(f"The country that you chose is {countries[orderCountry - 1]}")
    # inCountry = input("Type the country name :")
    # print(f"The index that you chose is {countries.index(inCountry)}")

    # x = [100, 200, 300]
    # #num = int(input("Type the text :"))
    # x.insert(2, 250)
    # x.remove(100)
    # x.append(1000)
    # for i in x:
    #     print(i)
