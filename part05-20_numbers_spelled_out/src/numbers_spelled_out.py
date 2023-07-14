# Write your solution here
def dict_of_numbers():
    new_dict = {}
    for num in range(100):
        new_dict[num] = number(num)
    return new_dict
    
def number(Number):
    num2words = {0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six',
                7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve',
                13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
                17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty', \
                50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', \
                90: 'ninety', 0: 'zero'}
    if 0 <= Number <= 19:
        return num2words[Number]
    elif 20 <= Number <= 99:
        tens, remainder = divmod(Number, 10)
        if remainder == 0:
            return num2words[Number]
        return num2words[tens*10] + '-' + num2words[remainder] 
    
    
