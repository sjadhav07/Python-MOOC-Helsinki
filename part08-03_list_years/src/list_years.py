# Write your solution here
# Remember the import statement
# from datetime import date
from datetime import date
def list_years(dates: list):
    lst = []
    for item in dates:
        lst.append(item.year)
    return sorted(lst)