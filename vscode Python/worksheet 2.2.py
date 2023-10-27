#Question1:
def sort(tuples):
    return sorted(tuples, key=lambda x: x[-1])
tuples_list = [(3, 1, 5), (1, 2, 3), (5, 2, 1), (4, 3, 2), (1, 2, 5)]
sorted_list = sort(tuples_list)
print(sorted_list)

#Question2: 
def remove_elements(list):
    remove = [0, 4, 5]
    return [elem for i, elem in enumerate(list) if i not in remove]
my_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
new_list = remove_elements(my_list)
print(new_list)
