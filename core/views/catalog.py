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
    genreId = request.GET.get('genreId')
    qualityId = request.GET.get('qualityId')
    
    movies = Movie.objects.filter(
        rating__gte = ratingFrom if ratingFrom is not None else 0,
        rating__lte = ratingTo if ratingTo is not None else 10,
        release_year__gte = releaseYearFrom if releaseYearFrom is not None else 1888,
        release_year__lte = releaseYearTo if releaseYearTo is not None else 3000,
    )

    series = Series.objects.filter(
        rating__gte = ratingFrom if ratingFrom is not None else 0,
        rating__lte = ratingTo if ratingTo is not None else 10,
        release_year__gte = releaseYearFrom if releaseYearFrom is not None else 1888,
        release_year__lte = releaseYearTo if releaseYearTo is not None else 3000,
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