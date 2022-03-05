from django.http import JsonResponse
from rest_framework import status


def handler500(request, *args, **kwargs):
    return JsonResponse({'detail': 'Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def handler404(request, *args, **kwargs):
    return JsonResponse({'detail': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
