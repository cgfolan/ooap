"""
    =========== Exercise 1 =============

    Add a docstring to the function below.
    The function takes a list and prints all 
    the items in the list.

    Bonus: Try using type declaration for the argument.
"""

def print_list(list_to_parse: str):
    """Prints items in a list
    
    Parameters

    list_to_parse: (str)
        list of items to be printed

    Returns
    (str)
        all items in list
    """
    for item in list_to_parse:
        print(item)

"""
    =========== Exercise 2 =============

    Implement the delete_item() function
    below, all the details to do so should
    be there for you.

    Hint: you can use del(list[index]) to remove
    an item from a list.
"""

def delete_item(list_to_parse, item_index):
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

    

shopping_list = ["eggs", "ham", "sausages"] # A test list to remove an item from

shopping_list = delete_item(shopping_list, 1) # Should remove 'ham' from the list

print(shopping_list)
