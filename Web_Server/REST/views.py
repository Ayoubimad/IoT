from django.http import Http404, HttpResponse
from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView

from REST.models import Vehicle
from REST.serializers import VehicleSerializer


def get_object(vehicle_id):
    try:
        return Vehicle.objects.get(id=vehicle_id)
    except Vehicle.DoesNotExist:
        raise Http404


class VehiclesAPI(APIView):
    """
    Retrieve, update, create, or delete a vehicle instance.
    """

    def get(self, request, vehicle_id=None):
        if vehicle_id is not None:
            vehicle = get_object(vehicle_id)
            serializer = VehicleSerializer(vehicle)
            return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
        else:
            vehicles = Vehicle.objects.all()
            serializer = VehicleSerializer(vehicles, many=True)
            return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)

    def put(self, request, vehicle_id):
        vehicle = get_object(vehicle_id)
        serializer = VehicleSerializer(vehicle, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(status=status.HTTP_200_OK)
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, vehicle_id):
        try:
            vehicle = get_object(vehicle_id)
            vehicle.delete()
            return HttpResponse(status=status.HTTP_204_NO_CONTENT)
        except:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        serializer = VehicleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(status=status.HTTP_201_CREATED)
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
