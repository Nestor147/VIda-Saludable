from django.db import models

class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Usuario(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=100)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.name} {self.last_name}"


class Proyecto(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(blank=True, null=True)
    estado = models.BooleanField(default=False, blank=True, null=True) 



    def __str__(self):
        return self.nombre


class UsuarioProyecto(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
   
    class Meta:
        unique_together = ('usuario', 'proyecto')

    def __str__(self):
        return f"{self.usuario} - {self.proyecto}"


class Alimentacion(models.Model):
    fecha = models.DateField()
    desayuno_hora = models.TimeField()
    almuerzo_hora = models.TimeField()
    cena_hora = models.TimeField()
    desayuno = models.BooleanField(default=False)  # Indica si hubo desayuno
    almuerzo = models.BooleanField(default=False)  # Indica si hubo almuerzo
    cena = models.BooleanField(default=False)      # Indica si hubo cena
    # Cambiar los campos de string a booleanos para indicar si fue saludable
    desayuno_saludable = models.BooleanField(default=False, blank=True, null=True)  
    almuerzo_saludable = models.BooleanField(default=False, blank=True, null=True)
    cena_saludable = models.BooleanField(default=False, blank=True, null=True)
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.tipo_alimento} ({self.fecha} {self.hora})"


class Agua(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()
    cantidad = models.IntegerField()  # En mililitros
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.cantidad}ml ({self.fecha} {self.hora})"


class Esperanza(models.Model):
    fecha = models.DateField()
    tipo_practica = models.CharField(max_length=50)  # oracion, leer la biblia
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.tipo_practica} ({self.fecha})"


class Sol(models.Model):
    fecha = models.DateField()
    tiempo = models.IntegerField()  # Cantidad de minutos
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.tiempo} minutos ({self.fecha})"


class Aire(models.Model):
    fecha = models.DateField()
    tiempo = models.IntegerField()  # Cantidad de minutos
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.tiempo} minutos ({self.fecha})"


class Dormir(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return f"Sueño ({self.fecha} {self.hora})"
        


class Despertar(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()
    estado = models.BooleanField(default=False) 
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return f"Despertar ({self.fecha} {self.hora})"


class Ejercicio(models.Model):
    fecha = models.DateField()
    tipo = models.CharField(max_length=50)  # caminata lenta, rápida, carrera, ejercicio guiado
    tiempo = models.IntegerField()  # Cantidad de minutos
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return f"Ejercicio ({self.tipo} - {self.fecha})"


class DatosUsuario(models.Model):
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    peso = models.DecimalField(max_digits=5, decimal_places=2)  # kg
    altura = models.DecimalField(max_digits=4, decimal_places=2)  # metros
    imc = models.DecimalField(max_digits=4, decimal_places=2)  # Índice de Masa Corporal
    presion_sistolica = models.IntegerField(null=True, blank=True)  # mmHg
    presion_diastolica = models.IntegerField(null=True, blank=True)  # mmHg
    radio_abdominal = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # cm
    grasa_corporal = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # %
    grasa_visceral = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # %
    frecuencia_cardiaca = models.IntegerField(null=True, blank=True)  # latidos/min
    frecuencia_respiratoria = models.IntegerField(null=True, blank=True)  # respiraciones/min
    colesterol_total = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # mg/dL
    colesterol_hdl = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # mg/dL
    colesterol_ldl = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # mg/dL
    trigliceridos = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # mg/dL
    glucosa = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # mg/dL
    frecuencia_cardiaca_en_reposo = models.IntegerField(null=True, blank=True)  # reposo
    frecuencia_cardiaca_despues_de_45_segundos = models.IntegerField(null=True, blank=True)  # después de 30 sentadillas
    frecuencia_cardiaca_1_minuto_despues = models.IntegerField(null=True, blank=True)  # 1 minuto después
    resultado_test_rufier = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # opcional
    fecha = models.DateField()  # Fecha de la medición
    tipo = models.CharField(max_length=20)  # 'inicial' o 'final'
    fecha_nacimiento = models.DateField()  # Fecha de nacimiento
    edad = models.IntegerField()  # Se calculará a partir de la fecha de nacimiento
    sexo = models.CharField(max_length=20)  # 'inicial' o 'final'


    def __str__(self):
        return f"Datos {self.tipo.capitalize()} ({self.user})"
