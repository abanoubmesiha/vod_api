from django.http import JsonResponse
from django.core.paginator import Paginator
from django.db.models import Q

from .utils import envelope
from ..models import Movie, Series, Genre

def get(request):
    activePageNo = request.GET.get('activePageNo')
    ratingFrom = request.GET.get('ratingFrom')
    ratingTo = request.GET.get('ratingTo')
    releaseYearFrom = request.GET.get('releaseYearFrom')
    releaseYearTo = request.GET.get('releaseYearTo')
    genreId = request.GET.get('genreId')

    filters = Q(rating__gte = ratingFrom) & Q(rating__lte = ratingTo) & Q(release_year__gte = releaseYearFrom) & Q(release_year__lte = releaseYearTo)
    if genreId:
        filters &= Q(genres__in = [genreId])
    
    movies = Movie.objects.filter(filters).distinct()

    series = Series.objects.filter(filters).distinct()

    serialized_movies = [movie.serialize() for movie in movies]
    serialized_series = [s.serialize() for s in series]
    list = serialized_movies + serialized_series

    paginator = Paginator(list, 24)
    page_obj = paginator.get_page(activePageNo)

    data = {
        "data": page_obj.object_list,
        "number_of_pages": paginator.num_pages,
        "page": page_obj.number
    }

    return JsonResponse(envelope(data))