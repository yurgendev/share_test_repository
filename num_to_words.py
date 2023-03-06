# Напишіть функцію, яка переводить число, що означає кількість доларів і центів, в прописний формат. Наприклад:
# > 123,34
# > one hundred twenty three dollars thirty four cents

global nums_dict
nums_dict = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
                 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
                 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
                 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
                 19: 'nineteen', 20: 'twenty',
                 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty',
                 70: 'seventy', 80: 'eighty', 90: 'ninty'}
def int_to_en(num):

    k = 1000
    m = k * 1000

    if num == 0 or num == 1:
        return nums_dict[num] + ' dollar'

    if num < 20:
        return nums_dict[num] + ' dollars'

    if num < 100:
        if num % 10 == 0:
            return nums_dict[num] + ' dollars'
        else:
            return nums_dict[num // 10 * 10] + ' ' + nums_dict[num % 10] + ' dollars'

    if num < k:
        if num % 100 == 0:
            return nums_dict[num // 100] + ' hundred dollars'
        else:
            return nums_dict[num // 100] + ' hundred ' + int_to_en(num % 100)

    if num < m:
        if num % k == 0:
            return int_to_en(num // k) + ' thousand dollars'
        else:
            return int_to_en(num // k) + ' thousand, ' + int_to_en(num % k) + ' dollars'




number = float(input('please enter an integer between 1 and 9999: '))
num = int(number)


# Патч для цент


def get_cents(number):
    cents = round(number - num, 2) * 100
    if cents == 0:
        return int_to_en(num) + ' dollars'
    elif cents < 20:
        return int_to_en(num) + ' dollars and ' + nums_dict[cents] + ' cents'
    elif cents % 10 == 0:
        return int_to_en(num) + ' dollars and ' + nums_dict[cents // 10 * 10] + ' cents'
    else:
        return int_to_en(num) + ' dollars and ' + nums_dict[cents // 10 * 10] + '-' + nums_dict[cents % 10] + ' cents'



print(get_cents(number))


