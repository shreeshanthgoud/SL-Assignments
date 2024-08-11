def vowel_consonant(str1):
    count1 =0
    count2 =0
    list1 =['a','e','i','o','u']
    for i in str1:
        if i in list1:
            count1 += 1
        elif i==" ":
            continue
        else:
            count2 += 1
    print("vowels:",count1)
    print("consonants:",count2)
str1 = input("Enter a word")
vowel_consonant(str1)