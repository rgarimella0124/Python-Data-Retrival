import pandas as pd

file1 = pd.read_csv("./data/MOCK_DATA1.csv", sep=",")
file2 = pd.read_csv("./data/MOCK_DATA2.csv", sep=",")
file3 = pd.read_csv("./data/MOCK_DATA3.csv", sep=",")


def onefile(arr, key):
    if 0 in arr:
        print(file1[key])
        return file1[key]
    elif 1 in arr:
        print(file2[key])
        return file2[key]
    else:
        print(file3[key])
        return file3[key]


def multipleone(arr, key):
    if 0 in arr and 1 in arr:
        print(file1[key], file2[key])
        return (file1[key], file2[key])
    elif 0 in arr and 2 in arr:
        print(
            file1[key], file2[key],
        )
        return (file1[key], file2[key])
    elif 1 in arr and 2 in arr:
        print(
            file2[key], file3[key],
        )
        return (file2[key], file3[key])


def multipletwo(arr, key):
    print(file1[key], file2[key], file3[key])
    return (file1[key], file2[key], file3[key])


def multiple(arr, key):
    if len(arr) == 2:
        multipleone(arr, key)
    else:
        multipletwo(arr, key)


def main(arr, key):
    if key == '1':
        print("name")
        if len(arr) == 1:
            onefile(arr, "name")
        else:
            multiple(arr, "name")
    elif key == '2':
        print("email")
        if len(arr) == 1:
            onefile(arr, "email")
        else:
            multiple(arr, "email")
    elif key == '3':
        print("number")
        if len(arr) == 1:
            onefile(arr, "number")
        else:
            multiple(arr, "number")
    else:
        print("company")
        if len(arr) == 1:
            onefile(arr, "company")
        else:
            multiple(arr, "company")

x = input("Enter a Column Number: ")
num_array = list()
num = input("How Many Files Do You Want to select")
print("Enter numbers in array: ")
for i in range(int(num)):
    n = input("num :")
    num_array.append(int(n))
print("ARRAY: ", num_array)
print("Input: ", x)
main(num_array, x)




# import pandas as pd

# file1 = pd.read_csv("./data/MOCK_DATA1.csv", sep=",")
# file2 = pd.read_csv("./data/MOCK_DATA2.csv", sep=",")
# file3 = pd.read_csv("./data/MOCK_DATA3.csv", sep=",")


# def onefile(arr, key):
#     if 0 in arr:
#         print(file1[key])
#         return file1[key]
#     elif 1 in arr:
#         print(file2[key])
#         return file2[key]
#     else:
#         print(file3[key])
#         return file3[key]


# def multipleone(arr, key):
#     if 0 in arr and 1 in arr:
#         print(file1[key], file2[key])
#         return (file1[key], file2[key])
#     elif 0 in arr and 2 in arr:
#         print(
#             file1[key], file2[key],
#         )
#         return (file1[key], file2[key])
#     elif 1 in arr and 2 in arr:
#         print(
#             file2[key], file3[key],
#         )
#         return (file2[key], file3[key])


# def multipletwo(arr, key):
#     print(file1[key], file2[key], file3[key])
#     return (file1[key], file2[key], file3[key])


# def multiple(arr, key):
#     if len(arr) == 2:
#         multipleone(arr, key)
#     else:
#         multipletwo(arr, key)


# def main(arr, key):
#     if key == "1":
#         print("name")
#         if len(arr) == 1:
#             onefile(arr, "name")
#         else:
#             multiple(arr, "name")
#     elif key == "2":
#         print("email")
#         if len(arr) == 1:
#             onefile(arr, "email")
#         else:
#             multiple(arr, "email")
#     elif key == "3":
#         print("number")
#         if len(arr) == 1:
#             onefile(arr, "number")
#         else:
#             multiple(arr, "number")
#     else:
#         print("company")
#         if len(arr) == 1:
#             onefile(arr, "company")
#         else:
#             multiple(arr, "company")


# x = input("Enter a Column Number: ")
# num_array = list()
# num = input("How Many Files Do You Want to select")
# print("Enter numbers in array: ")
# for i in range(int(num)):
#     n = input("num :")
#     num_array.append(int(n))
# print("ARRAY: ", num_array)
# print("Input: ", x)
# main(num_array, x)

