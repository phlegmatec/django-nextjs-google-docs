import os

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def healthz_view(request):
    query_params = request.GET
    return JsonResponse(
        {
            "status": "ok",
            "frontend_url": os.getenv("FRONTEND_URL"),
            "query_params": dict(query_params),
        }
    )
