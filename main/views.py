from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.models import User
from .models import Note
from .serializers import UserSerializer, NoteSerializer

# Create your views here.

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class LoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'access': token.key,
            'user_id': user.pk,
            'email': user.email
        })

class AddNoteView(generics.CreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ListNotesView(generics.ListAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def calculate(request):
    data = request.data
    # Lógica de cálculo (exemplo simples)
    material_cost = data.get('materialCost', 0)
    hours = data.get('hours', 0)
    minutes = data.get('minutes', 0)
    hourly_rate = data.get('hourlyRate', 0)
    fixed_expenses = data.get('fixedExpenses', 0)
    profit_margin = data.get('profitMargin', 0)
    
    total_hours = hours + (minutes / 60)
    labor_cost = total_hours * hourly_rate
    total_cost = material_cost + labor_cost + fixed_expenses
    selling_price = total_cost / (1 - (profit_margin / 100))
    
    return Response({
        'labor_cost': round(labor_cost, 2),
        'total_cost': round(total_cost, 2),
        'selling_price': round(selling_price, 2)
    })
