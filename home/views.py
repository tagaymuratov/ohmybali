import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .models import TourPage

@csrf_exempt
def booking_view(request):
  if request.method == "POST":
    data = json.loads(request.body)
    page_id = data.get("page_id")

    try:
      page = TourPage.objects.get(id=page_id)
    except TourPage.DoesNotExist:
      return JsonResponse({"error": "Page not found"}, status=404)

    booking_data = {
        "name": data.get("name"),
        "email": data.get("email"),
        "phone": data.get("phone"),
        "guests": data.get("guests"),
        "cost": data.get("cost"),
    }

    page.send_to_telegram(booking_data)
    return JsonResponse({"status": "ok"})
  else:
    return JsonResponse({"error": "Method not allowed"}, status=405)