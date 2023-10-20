"""Modul to filter redundent students"""
def return_duplicated_students(input_list) -> list:
    """
    Args:
        input_list (_list_): students

    Returns:
        _list_: duplicated students
    """
    duplicates = set()
    seen = set()
    for item in input_list:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    #duplicates = [item for item in input_list if input_list.count(item) > 1]
    return list(duplicates)
