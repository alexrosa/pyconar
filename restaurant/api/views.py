from django.shortcuts import render
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.serializers import ReservationSerializer
from api.models import Reservation

class ReservationListAPI(APIView):

    def get(self, request):
        reservations = get_list_or_404(Reservation.objects.all())
        serializer = ReservationSerializer(reservations, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ReservationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class ReservationDetailAPI(APIView):
    
    def get(self, request, pk):
        reservation = get_object_or_404(Reservation.objects.all(), pk=pk)
        serializer = ReservationSerializer(reservation, many=False)
        return Response(serializer.data)
    
    def put(self, request, pk):
        reservation = get_object_or_404(Reservation.objects.all(), pk=pk)
        serializer = ReservationSerializer(reservation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        data = Reservation.objects.all()
        reservation = get_object_or_404(data, pk=pk)
        reservation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)