import json
from datetime import date


def calculate_age(born):
    today = date.today()
    return today.year - born.year - (
        (today.month, today.day) < (born.month, born.day)
    )


def filters_user(params):
    kwargs = {}

    if type(params) is str:
        params = json.loads(params)

    if 'same_sex' in params.keys():
        kwargs['genre__name'] = params['same_sex']
    if 'age' in params.keys():
        kwargs['age'] = params['age']
    if 'range_age' in params.keys():
        age = int(params['range_age'])
        kwargs['age__gte'] = age - 3
        kwargs['age__lte'] = age + 3

    if 'hobbies' in params.keys():
        hobbies = params.getlist('hobbies')
        hobbies = hobbies[0].split(',')
        print(hobbies)
        kwargs['hobbies__name__in'] = hobbies

    return kwargs
