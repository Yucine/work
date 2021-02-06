S = input("введите текст")
while S.find("/*") != -1:
    start = S.find("/*")
    end = S.find("*/")
    delete = S[start: end + 3]
    S = S.replace(delete,"")
print(S)
