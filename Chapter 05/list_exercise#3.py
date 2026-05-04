# filter odd even
# define  a function
# input
# list ---> [1,2,3,4,5,6,7]
# output --> [[1,3,5,7],[2,4,6]]


def filter_odd_eve(_list):
    odd_nums_list = []
    even_nums_list = []
    for i in _list:
        if i % 2 == 0:
            even_nums_list.append(i)
        else:
            odd_nums_list.append(i)
    output_list = [odd_nums_list, even_nums_list]
    return output_list          


nums_list = [1, 2, 3, 4, 5, 6, 7]
print(filter_odd_eve(nums_list))
