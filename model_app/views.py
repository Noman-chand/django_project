from django.http import JsonResponse
from .models import Person
from django.db.models import Q


def data_detail(request):
    total_user = Person.objects.all().values()
    print(total_user, 'user')
    print (Q , 'q is present')

    return JsonResponse(list(total_user), safe=False)
