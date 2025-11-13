from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, help_text="Nome da peça")  # Piece name
    material_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0, help_text="Custo do material")
    hours = models.IntegerField(default=0, help_text="Horas gastos")
    minutes = models.IntegerField(default=0, help_text="Minutos gastos")
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2, default=0, help_text="Valor por hora")
    fixed_expenses = models.DecimalField(max_digits=10, decimal_places=2, default=0, help_text="Despesas fixas")
    profit_margin = models.DecimalField(max_digits=10, decimal_places=2, default=0, help_text="Margem de lucro")
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0, help_text="Preço total (após cálculo)")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
