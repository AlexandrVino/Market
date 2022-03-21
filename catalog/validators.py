from django.core.exceptions import ValidationError


def validate(value):
    must_word = {'Превосходно', 'Роскошно', 'Amazing', 'Wonderful'}
    if not any(filter(lambda x: x.lower() in value.lower(), must_word)):
        raise ValidationError(
            f'Обязательно используйте одно из слов "{" ".join(must_word)}"!')
