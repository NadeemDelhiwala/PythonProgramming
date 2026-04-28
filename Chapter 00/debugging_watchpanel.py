

def calculate_average(grades: list):

    total_items = len(grades)
    total_sum = 0

    for grade in grades:
         total_sum += grade

    return total_sum / total_items


def is_passed(avg):
    return avg >= 40


grades = [98, 99, 97, 85, 99]

average = calculate_average(grades)
status = is_passed(average)

print(f'Average: {average}')
print(f'Status: {status}')

'''
data = {
'name': '',
cart_items : {
    [], ''
}
}
'''
