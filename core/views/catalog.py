from django.http import JsonResponse
from django.core.paginator import Paginator

from .utils import envelope
from ..models import Movie, Series

def get(request):
    activePageNo = request.GET.get('activePageNo')
    ratingFrom = request.GET.get('ratingFrom')
    ratingTo = request.GET.get('ratingTo')
    releaseYearFrom = request.GET.get('releaseYearFrom')
    releaseYearTo = request.GET.get('releaseYearTo')
    
    movies = Movie.objects.filter(
        rating__gte = ratingFrom,
        rating__lte = ratingTo,
        release_year__gte = releaseYearFrom,
        release_year__lte = releaseYearTo,
    )

    series = Series.objects.filter(
        rating__gte = ratingFrom,
        rating__lte = ratingTo,
        release_year__gte = releaseYearFrom,
        release_year__lte = releaseYearTo,
    )

    serialized_movies = [movie.serialize() for movie in movies]
    serialized_series = [s.serialize() for s in series]
    list = serialized_movies + serialized_series

    paginator = Paginator(list, 10)
    page_obj = paginator.get_page(activePageNo)

    data = {
        "data": page_obj.object_list,
        "number_of_pages": paginator.num_pages,
        "page": page_obj.number
    }

    return JsonResponse(envelope(data))