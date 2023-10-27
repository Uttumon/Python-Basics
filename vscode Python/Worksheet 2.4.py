#Q1
# d = [(1,2,3),(4,5,6),(7,8,9)]
# for i in range(len(d)): d[i] = d[i][0],d[i][1],0

# print(d)
#Q2
# def Remove(tuples):
#     tuples = [t for t in tuples if t] 
#     return tuples
# tuples = [(), ('Utkarsh','15','8'), (), ('Aryan', 'sita'),
# ('krishna', 'Priya', '45'), ('',''),()] 
# print(Remove(tuples))
#Q3
# def product_tuple(nums): 
#     temp = list(nums) 
#     product = 1
#     for x in temp: 
#         product *= x
#         return product

# nums1 = (4, 3, 2, 2, -1, 18)
# print ("Original Tuple: ") 
# print(nums1)
# print("Product - multiplying all the numbers of the said tuple:",product_tuple(nums1))

# nums2 = (2, 4, 8, 8, 3, 2, 9)
# print ("\nOriginal Tuple: ") 
# print(nums2)
# print("Product - multiplying all the numbers of the said tuple:",product_tuple(nums2))
#Q4
# a = ['1','4','3','6','7']
# print("Original tuple: "+str(a))
# a = tuple(map(int, a)) 
# print("Modified tuple: "+str(a))
#Q5
def check_in_tuples(colors, c): 
    result = any(c in tu for tu in colors) 
    return result

colors = (
('Red', 'White', 'Blue'),
('Green', 'Pink', 'Purple'),
('Orange', 'Yellow', 'Lime'),
)
print("Original list:") 
print(colors)
c1 = 'White'
print(c1,"is presenet in colors or not!") 
print(check_in_tuples(colors, c1))
c1 = 'Pink'
print(c1,"is presenet in colors or not!") 
print(check_in_tuples(colors, c1))
c1 = 'Olive'
print(c1,"is presenet in colors or not!") 
print(check_in_tuples(colors, c1))
