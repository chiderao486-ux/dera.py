#palindrome checker
Item_list = ['mummy','hannah','murder for a Jar of red rum','mom',
             'seagull','tomato','no lemon', 'no melon',
             'some men interprete nine memos', 'madam']

for item in Item_list:
    cleaned = item.replace(" ", "")
    
    if cleaned == cleaned[::-1]:
        print(item, "is a palindrome")
    else:
        print(item, "not a Palindrome")
