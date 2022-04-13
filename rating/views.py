from http import HTTPStatus

from django.http import HttpResponse
from django.shortcuts import redirect, render

from rating.forms import AddRate
from rating.models import Rating

ADD_RATING = 'rating/rate.html'


def add_rate(request, item_index) -> HttpResponse:
    """
    Возвращает страничку Списка товаров
    """

    if not request.user.is_authenticated:
        return redirect('/auth/login', status=HTTPStatus.OK,
                        context={}, content_type='text/html')

    if request.method == 'POST':
        rate = request.POST['star']

        cur_rate = Rating.manager.get_object(
            None, user_id=request.user.id, item_id=item_index)

        if any(cur_rate):
            # редактируем существующий
            cur_rate = list(cur_rate)[0]
            cur_rate.star = rate
        else:
            # Добавляем
            cur_rate = Rating(
                user_id=request.user.id, item_id=item_index, star=rate)

        cur_rate.save()
        return redirect(f'/catalog/{item_index}/', status=HTTPStatus.OK,
                        context={}, content_type='text/html')

    form = AddRate()

    return render(
        request, ADD_RATING, status=HTTPStatus.OK,
        context={
            'form': form,
        },
        content_type='text/html'
    )
