from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import F, Sum


# Create your models here.
percentage_validators=[MinValueValidator(0), MaxValueValidator(100)]
score_validators=[MinValueValidator(0), MaxValueValidator(9)]

class BuyOrSell(models.TextChoices):
    BUY = 'B', "BUY"
    SELL = 'S', "SELL"
class InvestmentType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)
    max_limit = models.PositiveIntegerField(validators=percentage_validators, default=0)
    risk_score = models.FloatField(validators=score_validators, default=0.0)
    value = models.FloatField(default=0.0)
    status = models.BooleanField(default=True)

    

    @property
    def portfolio_weight(self):
        total_value_temp = InvestmentType.objects.aggregate(Sum('value'))
        total_value = total_value_temp["value__sum"]

        if total_value == 0.0:
            return 0.0
        else:
            return self.value / total_value

    @property
    def risk_contribution(self):
        return self.portfolio_weight * self.risk_score

    @property
    def is_overlimit(self):
        if self.portfolio_weight <= (self.max_limit/100):
            return False
        else:
            return True
        
    

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Principal(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60, unique=True)
    status = models.BooleanField(default=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Investment(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60, unique=True)
    investment_type = models.ForeignKey(InvestmentType, on_delete=models.CASCADE, related_name="inv_type_ref")
    principal = models.ForeignKey(Principal, on_delete=models.CASCADE, related_name="principal_ref")
    status = models.BooleanField(default=True)

    class Meta:
        ordering = ['name']


    def __str__(self):
        return self.name

class Transaction(models.Model):
    id = models.AutoField(primary_key=True)
    trx_date = models.DateField()
    investment = models.ForeignKey(Investment, on_delete=models.CASCADE, related_name="inv_ref")
    buysell = models.CharField(max_length=1, choices=BuyOrSell.choices)
    price = models.FloatField(default=0.0)
    volume = models.FloatField(default=0.0,)
    amount = models.FloatField(default=0.0,)

    def save(self, *args, **kwargs):
        super(Transaction, self).save(*args, **kwargs)

        # update balance on InvestmentType
        if self.buysell == BuyOrSell.BUY:
            InvestmentType.objects.filter(id = self.investment.investment_type.id).update(value=F('value') + self.amount)
        else:
            InvestmentType.objects.filter(id = self.investment.investment_type.id).update(value=F('value') - self.amount)



        # update
    class Meta:
        ordering = ['-trx_date']

    def __str__(self):
        return self.investment.name

class InvestmentTypeBalance(models.Model):
    id = models.AutoField(primary_key=True)
    investment_type = models.ForeignKey(InvestmentType, on_delete=models.CASCADE, related_name="bal_inv_type_ref")
    value = models.DecimalField(max_digits=15, decimal_places=2, default=0)

    class Meta:
        ordering = ['investment_type__name']

    def __str__(self):
        return self.investment_type__name







