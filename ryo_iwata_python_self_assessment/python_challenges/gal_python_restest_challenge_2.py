def remove_item(list_items, item_to_remove, all_or_one = "one"):
    result = []
    if item_to_remove not in list_items:
        return('The item is not in the list')
    x = 0
    for items in list_items:
        if items == item_to_remove: #each item is iterated through to see if it's the item to be removed
            if all_or_one == "all" or x == 0: #item must not be added to new list if all of the items need to be removed or is the first(and only) one to be removed
                pass
            elif x >= 1: # this appends any duplicates of the item to be removed if you only want to remove one case
                result.append(items)
            x += 1
        elif items != item_to_remove:
            result.append(items)

    return(result)

list_items = [1,3,7,8,0,7]

print(remove_item(list_items, 7, "one"))
print(remove_item(list_items, 7, "all"))
