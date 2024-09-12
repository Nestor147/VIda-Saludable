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
    estado = models.IntegerField()



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
    desayuno = models.IntegerField()  # Indica si hubo desayuno
    almuerzo = models.IntegerField()  # Indica si hubo almuerzo
    cena = models.IntegerField()      # Indica si hubo cena
    # Cambiar los campos de string a booleanos para indicar si fue saludable
    desayuno_saludable = models.IntegerField() 
    almuerzo_saludable = models.IntegerField()
    cena_saludable = models.IntegerField()
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
    estado = models.IntegerField()
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


class DatosFormularioUsuario(models.Model):
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)  # Relación con el modelo de usuario
    fecha = models.DateField()
    nombres_apellidos = models.CharField(max_length=255)
    sexo = models.CharField(max_length=10)
    edad = models.IntegerField()
    estado_civil = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField()
    grado_instruccion = models.CharField(max_length=50)
    procedencia = models.CharField(max_length=100)
    religion = models.CharField(max_length=50)
    cigarrillos = models.CharField(max_length=5)
    num_cigarrillos = models.IntegerField()
    anio_consumo = models.IntegerField()
    presion_arterial = models.CharField(max_length=10)
    resultado_presion_arterial = models.CharField(max_length=50)
    frecuencia_cardiaca = models.IntegerField()
    frecuencia_respiratoria = models.IntegerField()
    temperatura = models.DecimalField(max_digits=3, decimal_places=1)
    saturacion_oxigeno = models.IntegerField()
    talla_m = models.DecimalField(max_digits=3, decimal_places=2)
    peso_kg = models.DecimalField(max_digits=4, decimal_places=1)
    imc_resultado = models.CharField(max_length=50)
    observaciones = models.TextField()
    perimetro_abdominal_cm = models.IntegerField()
    porcentaje_gc = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True)
    porcentaje_gv = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True)
    porcentaje_musculo = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True)
    glicemia_basal = models.DecimalField(max_digits=4, decimal_places=1)
    colesterol = models.DecimalField(max_digits=4, decimal_places=1)
    hdl = models.DecimalField(max_digits=4, decimal_places=1)
    trigliceridos = models.DecimalField(max_digits=4, decimal_places=1)
    ldl = models.DecimalField(max_digits=4, decimal_places=1)
    consumo_3_comidas_horario_fijo = models.IntegerField()
    consumo_5_porciones_frutas_verduras = models.IntegerField()
    consumo_3_porciones_proteinas = models.IntegerField()
    ingiero_otros_alimentos = models.IntegerField()
    consumo_carbohidratos = models.IntegerField()
    consumo_alimentos_fritos = models.IntegerField()
    consumo_alimentos_hechos_en_casa = models.IntegerField()
    consumo_liquidos_mientras_como = models.IntegerField()
    bebo_solo_agua_pura = models.IntegerField()
    bebo_8_vasos_agua = models.IntegerField()
    bebidas_con_azucar = models.IntegerField()
    bebo_agua_al_despertar = models.IntegerField()
    bebo_agua_antes_comidas = models.IntegerField()
    bebo_agua_para_dormir = models.IntegerField()
    consumo_bebidas_alcoholicas = models.IntegerField()
    eventos_sociales_alcohol = models.IntegerField()
    consumo_sustancias_estimulantes = models.IntegerField()
    consumo_refrescos_cola = models.IntegerField()
    consumo_cigarrillos = models.IntegerField()
    consumo_comida_chatarra = models.IntegerField()
    pedir_mas_comida = models.IntegerField()
    agregar_mas_azucar = models.IntegerField()
    agregar_mas_sal = models.IntegerField()
    satisfecho_trabajo = models.IntegerField()
    tenso_nervioso_estresado = models.IntegerField()
    tiempo_libre_redes_sociales = models.IntegerField()
    satisfecho_relaciones_sociales = models.IntegerField()
    apoyo_familia_decisiones = models.IntegerField()
    realizo_actividad_deportiva = models.IntegerField()
    ejercicio_fisico_diario = models.IntegerField()
    practico_deporte_tiempo_libre = models.IntegerField()
    dedicacion_30_minutos_ejercicio = models.IntegerField()
    ejercicio_carrera_bicicleta = models.IntegerField()
    duermo_7_8_horas = models.IntegerField()
    despertar_durante_noche = models.IntegerField()
    dificultad_sueno_reparador = models.IntegerField()
    horario_sueno_diario = models.IntegerField()
    despertar_horario_diario = models.IntegerField()
    exposicion_sol_diaria = models.IntegerField()
    exposicion_sol_horas_seguras = models.IntegerField()
    exposicion_sol_20_minutos = models.IntegerField()
    uso_bloqueador_solar = models.IntegerField()
    tecnica_respiraciones_profundas = models.IntegerField()
    tiempo_tecnica_respiraciones = models.IntegerField()
    horario_tecnica_respiraciones_manana = models.IntegerField()
    horario_tecnica_respiraciones_noche = models.IntegerField()
    ser_supremo_interviene = models.IntegerField()
    leo_biblia = models.IntegerField()
    practico_oracion = models.IntegerField()
    orar_y_estudiar_biblia_desarrollo_personal = models.IntegerField()

    def __str__(self):
        return f"{self.nombres_apellidos} ({self.fecha})"