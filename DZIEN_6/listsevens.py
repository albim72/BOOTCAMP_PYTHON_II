def evens_using_for_loop(count):
    evens = []
    for i in range(count):
        if i%2 == 0:
            evens.append(i)
    return evens


def evens_using_list_comp(count):
    return [i for i in range(count) if i%2==0]

def enumerate_elements(elements):
    for index, element in enumerate(elements):
        print(index, element)

if __name__ == '__main__':
    print(f"wyliczenie liczb parzystych 0-10 [pętla for]: {evens_using_for_loop(11)}")
    print(f"wyliczenie liczb parzystych 0-10 [list comprehension]: {evens_using_list_comp(11)}")
    print(f"wyliczenie liczb parzystych 0-10 [enumeracja]:")
    {enumerate_elements(evens_using_list_comp(11))}
