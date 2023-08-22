def create_an_empty_list():
    return []

def create_a_list():
    create_a_list= ["orangaes", "Bananas", "potatoes", "mangoes"]
    return create_a_list

def add_element_to_end_of_list(l, element):
    l.append(element)
    return l

def add_element_to_start_of_list(l, element):
    l.insert(0, element)
    return l


def remove_element_from_end_of_list(input_list):
    if len(input_list) == 0:
        return input_list
    else:
        input_list.pop()  
        return input_list

def remove_element_from_start_of_list(input_list):
    if len(input_list) == 0:
        return input_list
    else:
        input_list.remove(input_list[0])  
        return input_list
    
def retrieve_first_element_from_list(input_list):
    if len(input_list) > 0:
        return input_list[0]
    else:
        return None  

def retrieve_element_from_index(input_list, index):
    if 0 <= index < len(input_list):
        return input_list[index]
    else:
        return None  


def retrieve_last_element_from_list(input_list):
    if len(input_list) > 0:
        return input_list[-1]  # Return the last element
    else:
        return None
