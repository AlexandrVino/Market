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
