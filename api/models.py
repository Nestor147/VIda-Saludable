from django.db import models

class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Usuario(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=100)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.role.name

class Alimentacion(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()
    tipo_alimento = models.CharField(max_length=100)
    saludable = models.CharField(max_length=50, blank=True, null=True)
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.tipo_alimento} ({self.fecha} {self.hora})"

class Agua(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()
    cantidad = models.IntegerField()
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.cantidad}ml ({self.fecha} {self.hora})"

class Esperanza(models.Model):
    fecha = models.DateField()
    tipo_practica = models.CharField(max_length=50)
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.tipo_practica} ({self.fecha})"

class Sol(models.Model):
    fecha = models.DateField()
    tiempo = models.CharField(max_length=40)
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.tiempo} ({self.fecha})"

class Aire(models.Model):
    fecha = models.DateField()
    tiempo = models.CharField(max_length=40)
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.tiempo} ({self.fecha})"

class Sleep(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Sleep ({self.fecha} {self.hora})"

class Despertar(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()
    estado = models.CharField(max_length=20)
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Despertar ({self.fecha} {self.hora})"

class Ejercicio(models.Model):
    fecha = models.DateField()
    tipo = models.CharField(max_length=50)
    tiempo = models.CharField(max_length=30)
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Ejercicio ({self.fecha} {self.tipo})"
