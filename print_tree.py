import math

def print_tree_from_breadth_first_stack(stack, print_method="red_black_node"):
    def construct_print_string(print_method):
        if print_method == "element":
            return print_element
        elif print_method == "node":
            return print_node
        elif print_method == 'red_black_node':
            return print_red_black_node

    def print_element(print_str, obj, index):
        print_str[index] = str(obj) if obj else 'x'
        return  print_str

    def print_node(print_str, obj, index):
        print_str[index] = str(obj.value) if obj else 'x'
        return print_str

    def print_red_black_node(print_str, obj, index):
        print_str[index] = str(obj.value) + str(obj.color[0]) if getattr(obj, "value") else 'x'
        return print_str

    if stack == None:
        return
    print_space = 64
    num_of_levels = int(math.log(len(stack)+1, 2))

    for level_num in range(1, num_of_levels + 1):
        if level_num == 1:
            num_spaces = (print_space / 2)
            offset = 0
        else:
            math_power = int(math.log(print_space, 2)) - level_num
            num_spaces = (2 ** (math_power))
            offset = int(math.log(print_space, 2))/2*level_num

        start_index = (2 ** (level_num - 1)) - 1
        end_index = start_index + 2 ** (level_num - 1)
        print_str = [" "] * print_space
        for i in range(start_index, end_index):
            elements_at_level = end_index - start_index
            split_level = elements_at_level / 2 + .5
            element_printing_count = (i - start_index) + 1
            if element_printing_count <= split_level:
                index = (element_printing_count * num_spaces) + offset
                print_str = construct_print_string(print_method)(print_str, stack[i], index)
            elif element_printing_count >= split_level:
                index = (print_space) - ((elements_at_level + 1 - element_printing_count) * (num_spaces)) - offset
                print_str = construct_print_string(print_method)(print_str, stack[i], index)
        print ''.join(print_str)