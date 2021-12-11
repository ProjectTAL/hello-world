import math

if __name__ == '__main__':

    # 051
    num = 5
    while True:
        answer = int(input("There are {} green bottles hanging on the wall, {}  green bottles hanging on the wall, and if 1 green bottle should accidentally fall.  How many green bottles will be hanging on the wall? ".format(num, num)))
        if answer == (num - 1):
            print("There will be {} green bottles hanging on the wall".format(num))
            if num == 1:
                break
            num = num - 1
        else:
            print("No try again")

    print("There are no more green bottles hanging on the wall")

    #
    # num = 5
    # print("There are", num, "green bottles hanging on the wall")
    # print(num, "green bottles hanging on the wall, and if 1 green bottle should accidentally fall")
    # guess = int(input("How many green bottles will be hanging on the wall? :"))
    # while guess == num or num == 0:
    #     print("no, try again")
    #     num = num - 1
    #     guess = int(input("How many green bottles will be hanging on the wall? :"))
    # print("There will be", num, "green bottles hanging on the wall")

    # 050
    # num = int(input("Enter the number: "))
    # while num < 10 or num > 20:
    #     if num < 10:
    #         print("Too low")
    #     else:
    #         print("Too high")
    #     num = int(input("Enter the number: "))
    # print("Thank you")
    # 049
    # compnum = 50
    # num = int(input("Enter the number: "))
    # count = 1
    # while num != compnum:
    #
    #     if num < compnum:
    #         print("up")
    #     else:
    #         print("down")
    #     count = count + 1
    #     num = int(input("Enter the number: "))
    # print("Well done, you took", count, "attempt")

    # 048
    # count = 0
    # name = input("Enter the name of the person you want to invite to the party: ")
    # print(name, "has now been invited")
    # count = count + 1
    # again = input("Do you want to invite other person(y,n): ")
    # again = "y"
    # while again == "y":
    #     other = input("Enter the name of the other person you want to invite to the party: ")
    #     print(other, "has now been invited")
    #     count = count + 1
    #     again = input("Do you want to invite other person(y,n): ")
    # print(count, "person attended the party.")

    # 047
    # num = int(input("Enter the number: "))
    # num1 = int(input("Enter the other number: "))
    # total = num + num1
    # again = input("Do you want to loop: ")
    # again = "y"
    # while again == "y":
    #     other = int(input("Enter the other number: "))
    #     total = total + other
    #     again = input("Do you want to loop again: ")
    # print(total)

    # 046
    # num = int(input("Enter the number: "))
    # while num < 6:
    #     num = int(input("Enter the number: "))
    # print("The last number you entered was a", num)

    # 045
    # total = 0
    # while total < 50:
    #     num = int(input("Enter the number: "))
    #     total = total + num
    #     print("The total is...", total)
