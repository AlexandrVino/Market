from django.core.exceptions import ValidationError


def validate_catalog_text(value: str) -> None:
    """
    Проыеряет корректность описание товара
    """

    necessary_fields = ['роскошно', 'превосходно']
    value = value.lower()

    if not any(filter(lambda x: x in value, necessary_fields)):
        raise ValidationError(
            f"Пожалуйста, используйте одно из обязательных слов: "
            f"{', '.join(necessary_fields)}"
        )

    if len(value.split()) < 2:
        raise ValidationError("Пожалуйста, используйте хотя бы 2 слова")


def validate_fields(value: str) -> None:
    """
    """
    letters = 'qwertyuiopasdfghjklzxcvbnm'
    numbers = '01234567890'
    special_chars = '-_'
    all_symbols = letters + numbers + special_chars

    value = value.lower()

    if not (all([item in all_symbols for item in value]) and
            set(letters).intersection(set(value))):

        raise ValidationError(
            f"Разрешено использовать латинские буквы, цифры и символы -_"
        )


def validate_password(value: str) -> None:
    """
    """
    numbers = '01234567890'
    special_chars = '-_'

    value = value.lower()
    validate_fields(value)

    if not (set(numbers).intersection(set(value)),
            set(special_chars).intersection(set(value))):

        raise ValidationError(
            f"Разрешено использовать латинские буквы, цифры и символы -_"
        )
