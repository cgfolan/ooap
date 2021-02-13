# """
#     =========== Exercise 1 =============

#     Add a docstring to the function below.
#     The function takes a list and prints all 
#     the items in the list.

#     Bonus: Try using type declaration for the argument.
# """

# def print_list(list_to_parse: str):
#     """Prints items in a list
    
#     Parameters

#     list_to_parse: (str)
#         list of items to be printed

#     Returns
#     (str)
#         all items in list
#     """
#     for item in list_to_parse:
#         print(item)

# Exercise 2
breakfast = ['sausages', 'eggs', 'noodles', 'coffee']

def delete_item(list_to_parse: list, item_index: int):
    """Takes a list, removes an item at the 
    specified index and returns the list
    
    Parameters
    ----------
    list_to_parse:
        The list to remove the item from

    item_index:
        The index to remove an item from
    
    Returns
    -------
    The list with the item removed
    """
    del list_to_parse[item_index]
    print(list_to_parse)



