from django.db import models
from accounts.models import User

class Priority(models.Model):
    name = models.CharField(max_length=16)

class State(models.Model):
    name = models.CharField(max_length=16)

class ClientStatus(models.Model):
    name = models.CharField(max_length=16)

class Client(models.Model):
    name = models.CharField(max_length=16)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    geocoord = models.CharField(max_length=16)   
    status = models.ForeignKey(ClientStatus, on_delete=models.PROTECT)
    email = models.EmailField()


class Category(models.Model):
    name = models.CharField(max_length=32)
    procent = models.IntegerField(default=50)



class Orders(models.Model):
    #date
    author = models.ForeignKey(User,related_name="author_order", on_delete=models.CASCADE) # FIX
    worker = models.ForeignKey(User, related_name="worker_order", on_delete=models.CASCADE) # FIX

    regdate = models.DateTimeField(auto_now_add=True)
    date = models.DateTimeField()
    acceptdate = models.DateTimeField()
    enddate = models.DateTimeField()

    priority = models.ForeignKey(Priority, on_delete=models.PROTECT)
    state = models.ForeignKey(State, on_delete=models.PROTECT)
    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    description = models.TextField()


    comment = models.TextField()
    planamount = models.FloatField() # планируемое количество работы
    plansum = models.FloatField()   # планируемая стоимость работ
    amount = models.FloatField()  #количество выполненной работы (число)
    sum = models.FloatField() # сумма оплаты, взятая с клинта (число)
    supplysum = models.FloatField() #сумма расходников (затрат)
    total = models.FloatField() # сумма за вычетом затрат: total = sum - supplysum
    workerpercent = models.IntegerField() # %исполнителя, указывается как число проценотов, например, 70
    workersum = models.FloatField() # сумма дохода исполнителя
    profitsum = models.FloatField() #сумма дохода фирмы








