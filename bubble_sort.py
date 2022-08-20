def bubble_sort(unordered_list):
    stop = False

    # Repeat up to have every item in the right position
    while not stop:

        for item in range(len(unordered_list) - 1):
            item_1 = unordered_list[item]
            item_2 = unordered_list[item + 1]

            if item_1 > item_2:
                unordered_list.pop(item)
                unordered_list.pop(item)

                unordered_list.insert(item, item_2)
                unordered_list.insert(item + 1, item_1)

        # Check if list is ordered
        count = 0
        for x in range(len(unordered_list)):
            for y in range(len(unordered_list)):
                if x < y and unordered_list[x] > unordered_list[y]:
                    stop = False
                    count += 1  

        if count == 0:
            stop = True
    
    ordered_list = unordered_list
            
    return ordered_list
            

        