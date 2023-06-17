import datetime


def last_day_of_month(any_day):
    next_month = any_day.replace(day=28) + datetime.timedelta(days=4)
    return next_month - datetime.timedelta(days=next_month.day)


value = "Dezembro"
if(value.find("/") != -1):
    if(len(value) > 7):
        if(len(value.split("/")[0]) == 4):
            data = last_day_of_month(
                datetime.datetime.strptime(value, '%Y/%m/%d'))
        else:
            data = last_day_of_month(
                datetime.datetime.strptime(value, '%d/%m/%Y'))
    else:
        data = last_day_of_month(datetime.datetime.strptime(value, '%d/%m'))
else:
    month = ['Janeiro', 'Fevereiro', "Marco", "Abril", "Maio", "Junho",
             "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    index = str(month.index(value) + 1)
    data = last_day_of_month(datetime.datetime.strptime(index, '%m'))


print(data)


# 99/99
# 99/99/9999
# 9999/99/99
# Junho
