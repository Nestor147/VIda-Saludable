-- Tabla de roles
CREATE TABLE role (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE
);

-- Tabla de usuarios con relación a roles
CREATE TABLE usuario (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    phone VARCHAR(100),
    email VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(100) NOT NULL,
    role_id INT,
    FOREIGN KEY (role_id) REFERENCES roles(id) ON DELETE SET NULL
);

-- Tabla de proyectos
CREATE TABLE proyecto (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL UNIQUE,
    descripcion TEXT,
    fecha_inicio DATE NOT NULL,
    fecha_fin DATE
);

-- Tabla de relación entre usuarios y proyectos
CREATE TABLE usuarios_proyecto (
    id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    proyecto_id INT NOT NULL,
    PRIMARY KEY (user_id, proyecto_id),
    FOREIGN KEY (user_id) REFERENCES usuarios(id) ON DELETE CASCADE,
    FOREIGN KEY (proyecto_id) REFERENCES proyectos(id) ON DELETE CASCADE
);

-- Tabla de alimentación
CREATE TABLE alimentacion (
    id SERIAL PRIMARY KEY,
    fecha DATE NOT NULL,
    hora TIME NOT NULL,
    tipo_alimento VARCHAR(100) NOT NULL, // //  desayuno, almuerzo, cena otro solo esos podran ser elejidos
    saludable VARCHAR(50),
    user_id INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES usuarios(id) ON DELETE CASCADE
);

-- Tabla de agua
CREATE TABLE agua (
    id SERIAL PRIMARY KEY,
    fecha DATE NOT NULL,
    hora TIME NOT NULL,
    cantidad INT NOT NULL, //solo se medira en mililitros
    user_id INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES usuarios(id) ON DELETE CASCADE
);

-- Tabla de esperanza
CREATE TABLE esperanza (
    id SERIAL PRIMARY KEY,
    fecha DATE NOT NULL,
    tipo_practica VARCHAR(50) NOT NULL,  // 1 oracion leer 2 la biblia. solo se pueden esas 2
    user_id INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES usuarios(id) ON DELETE CASCADE
);

-- Tabla de sol
CREATE TABLE sol (
    id SERIAL PRIMARY KEY,
    fecha DATE NOT NULL,
    tiempo INT NOT NULL, // se calculara cantidad de minutos
    user_id INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES usuarios(id) ON DELETE CASCADE
);

-- Tabla de aire
CREATE TABLE aire (
    id SERIAL PRIMARY KEY,
    fecha DATE NOT NULL,
    tiempo INT NOT NULL, // Cantidad de minutos
    user_id INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES usuarios(id) ON DELETE CASCADE
);

-- Tabla de sueño
CREATE TABLE dormir (
    id SERIAL PRIMARY KEY,
    fecha DATE NOT NULL,
    hora TIME NOT NULL,
    user_id INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES usuarios(id) ON DELETE CASCADE
);

-- Tabla de despertar
CREATE TABLE despertar (
    id SERIAL PRIMARY KEY,
    fecha DATE NOT NULL,
    hora TIME NOT NULL,
    estado VARCHAR(20) NOT NULL, // solo se podra ingresar si durmio "bien" o "mal"
    user_id INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES usuarios(id) ON DELETE CASCADE
);

-- Tabla de ejercicio
CREATE TABLE ejercicio (
    id SERIAL PRIMARY KEY,
    fecha DATE NOT NULL,
    tipo VARCHAR(50) NOT NULL, // solo se podra ingresar estos datos [caminata lenta, rapida, carrera o ejercicio guiado]
    tiempo INT NOT NULL, // solo sera en cantidad de minutos
    user_id INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES usuarios(id) ON DELETE CASCADE
);







 CREATE TABLE datos_usuario (
    id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    peso DECIMAL(5, 2),               -- Peso en kg
    altura DECIMAL(4, 2),             -- Altura en metros
    imc DECIMAL(4, 2),                -- Índice de Masa Corporal
    presion_sistolica INT,            -- Presión Arterial Sistólica en mmHg
    presion_diastolica INT,           -- Presión Arterial Diastólica en mmHg
    radio_abdominal DECIMAL(5, 2),    -- Radio Abdominal en cm
    grasa_corporal DECIMAL(5, 2),     -- Grasa Corporal en %
    grasa_viseral DECIMAL(5, 2),      -- Grasa Visceral en %
    frecuencia_cardiaca INT,          -- Frecuencia Cardíaca en latidos/min
    frecuencia_respiratoria INT,      -- Frecuencia Respiratoria en respiraciones/min
    colesterol_total DECIMAL(5, 2),   -- Colesterol Total en mg/dL
    colesterol_hdl DECIMAL(5, 2),     -- Colesterol HDL en mg/dL
    colesterol_ldl DECIMAL(5, 2),     -- Colesterol LDL en mg/dL
    trigliceridos DECIMAL(5, 2),      -- Triglicéridos en mg/dL
    glucosa DECIMAL(5, 2),            -- Glucosa en mg/dL
    frecuencia_cardiaca_en_reposo INT,                           -- Frecuencia cardíaca en reposo
    frecuencia_cardiaca_despues_de_45_segundos INT,                           -- Frecuencia cardíaca después de 30 sentadillas en 45 segundos
    frecuencia_cardiaca_1_minuto_despues INT,                           -- Frecuencia cardíaca 1 minuto después de las sentadillas
    resultado_test_rufier DECIMAL(5, 2),  -- Resultado del Test de Ruffier (opcional)
    fecha DATE NOT NULL, 
    tipo VARCHAR(20) NOT NULL,   -- 'inicial' o 'final'             -- Fecha de la medición
    fecha_nacimiento DATE NOT NULL,
    edad INT -- esta el usuario no lo registrara se calculara directamente basandonos a la fecha de nacimiento 
    sexo VARCHAR(20) NOT NULL,   

    FOREIGN KEY (user_id) REFERENCES usuarios(id) ON DELETE CASCADE
);
