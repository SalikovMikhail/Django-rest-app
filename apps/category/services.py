from rest_framework.exceptions import NotFound


def get_item_from_bd(model, pk):
    """Получаем категорию из бд"""
    try:
        instance = model.objects.get(pk=pk)
    except model.DoesNotExist:
        raise NotFound('объекта с таким id не существует')

    return instance
