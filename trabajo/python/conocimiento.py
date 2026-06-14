# ==================================================
# BASE DE CONOCIMIENTO
# ==================================================

# Actua como un json y da porcentaje a base de preguntas si o no.

base_de_conocimiento = [
    {
        "id": "R01",
        "descripcion": "Fuente de poder dañada",
        "condiciones": ["no_enciende", "sin_luces", "sin_sonido"],
        "conclusion": "Revisar o reemplazar la fuente de poder",
        "confianza": 0.92
    },
    {
        "id": "R02",
        "descripcion": "Falla de RAM",
        "condiciones": ["enciende", "pitidos_arranque", "sin_video"],
        "conclusion": "Probar con módulos de RAM de a uno",
        "confianza": 0.88
    },
    {
        "id": "R03",
        "descripcion": "Falla de tarjeta de video",
        "condiciones": ["enciende", "pantalla_negra", "sin_pitidos"],
        "conclusion": "Revisar tarjeta de video y conexiones del monitor",
        "confianza": 0.80
    },
    {
        "id": "R04",
        "descripcion": "Problemas de almacenamiento",
        "condiciones": ["enciende", "inicia_lento", "disco_al_100"],
        "conclusion": "Verificar salud del disco duro con herramienta SMART",
        "confianza": 0.85
    },
    {
        "id": "R05",
        "descripcion": "Infección por malware",
        "condiciones": ["enciende", "inicia_lento", "ventilador_siempre_activo"],
        "conclusion": "Escanear con antivirus y revisar procesos en segundo plano",
        "confianza": 0.72
    },
    {
        "id": "R06",
        "descripcion": "Driver o RAM dañada",
        "condiciones": ["enciende", "pantalla_azul_frecuente"],
        "conclusion": "Actualizar drivers y testear memoria RAM con MemTest86",
        "confianza": 0.87
    },
    {
        "id": "R07",
        "descripcion": "Sobrecalentamiento",
        "condiciones": ["enciende", "se_apaga_solo", "calor_excesivo"],
        "conclusion": "Limpiar ventiladores y reaplicar pasta térmica",
        "confianza": 0.90
    },

    # NUEVAS REGLAS

    {
        "id": "R08",
        "descripcion": "Fuente insuficiente",
        "condiciones": ["enciende", "se_apaga_solo"],
        "conclusion": "Revisar capacidad de la fuente de poder",
        "confianza": 0.75
    },
    {
        "id": "R09",
        "descripcion": "Posible virus",
        "condiciones": ["enciende", "inicia_lento"],
        "conclusion": "Realizar análisis antivirus completo",
        "confianza": 0.70
    },
    {
        "id": "R10",
        "descripcion": "Monitor desconectado",
        "condiciones": ["enciende", "sin_video", "sin_pitidos"],
        "conclusion": "Verificar cable HDMI/VGA y alimentación del monitor",
        "confianza": 0.82
    }
]

PREGUNTAS = {
    "no_enciende": "¿El equipo NO enciende (sin luces, sin sonido)?",
    "sin_luces": "¿No hay ninguna luz LED encendida?",
    "sin_sonido": "¿No se escucha ningún sonido al encender?",
    "enciende": "¿El equipo SÍ enciende (hay luces y/o sonido)?",
    "pitidos_arranque": "¿Se escuchan pitidos (beeps) al encender?",
    "sin_video": "¿La pantalla no muestra absolutamente nada?",
    "pantalla_negra": "¿La pantalla queda en negro (sin pitidos)?",
    "sin_pitidos": "¿No se escuchan pitidos?",
    "inicia_lento": "¿El equipo tarda más de 3 minutos en iniciar?",
    "disco_al_100": "¿El administrador de tareas muestra disco al 100%?",
    "ventilador_siempre_activo": "¿El ventilador está siempre a máxima velocidad?",
    "pantalla_azul_frecuente": "¿Aparece pantalla azul (BSOD) con frecuencia?",
    "se_apaga_solo": "¿El equipo se apaga solo sin advertencia?",
    "calor_excesivo": "¿El chasis está muy caliente al tacto?"
}