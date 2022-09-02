from random import randint
def merge_lists(list1, list2):
    len1 = len(list1)
    len2 = len(list2)
    big_list = []
    counter1 = 0
    counter2 = 0
    while counter1 < len1 and counter2 < len2:
        if list1[counter1] < list2[counter2]:
            big_list.append(list1[counter1])
            counter1 += 1
        else:
            big_list.append(list2[counter2])
            counter2 += 1
    if counter1 == len1:
        big_list.extend(list2[counter2:])
    else:
        big_list.extend(list1[counter1:])
    return big_list

def test_merge_lists():
    list1 = sorted([randint(-100, 100) for i in range(100)])
    list2 = sorted([randint(-100, 100) for i in range(100)])
    assert merge_lists(list1, list2) == sorted(list1 + list2)
test_merge_lists()


