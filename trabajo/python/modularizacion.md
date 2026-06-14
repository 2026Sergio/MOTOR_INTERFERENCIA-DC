# Sistema Experto para Diagnóstico de Computadoras

## Introducción

Este proyecto comenzó a partir de un sistema experto básico para el diagnóstico de problemas en computadoras. 

Inicialemte todo estaba en un solo archivo, el cual lo modularize para separarlo y aparte agregarle las siguiente funciones para cumplir con las reglas establecidad pedidas en el enunciado.

---

# Desarrollo del Proyecto

Antes de comenzar el proyecto analize el codigo y lo ejecute el cual si funcionaba pero estaba todo junto.

---

# Modularización del Sistema

Uno de los principales cambios realizados fue la modularización del código. En lugar de mantener toda la lógica en un solo archivo, se dividió en varios módulos con responsabilidades específicas.

La estructura final del proyecto quedó organizada de la siguiente manera:

```text
python/
│
├── conocimiento.py
├── inferencia.py
├── interfaz.py
├── main.py
└── modularizacion.md
```

### conocimiento.py

Este actua como un Json que contiene la base de conocimiento del sistema, incluyendo las reglas de diagnóstico y las preguntas utilizadas para recopilar síntomas.

### inferencia.py

Contiene el motor de inferencia encargado de realizar la equiparación de reglas, identificar diagnósticos posibles y generar los resultados.

### interfaz.py

Gestiona la interacción con el usuario mediante preguntas y construye la base de hechos a partir de las respuestas obtenidas.

### main.py

Actúa como punto de entrada principal del sistema y coordina la ejecución de todos los módulos.

La modularizacion me permite entender mas el codigo y saber que funcion hace tal cosa al estar separados por funciones.

---

# Mejoras Implementadas

Además de la modularización, se implementaron dos desafíos adicionales para extender la funcionalidad del sistema.
Ambos desafios son:
```text
Desafíos de extensión
Una vez que el código base funciona, extiéndelo a al menos 2 de estos desafíos:

Nivel 1 — Agregar reglas: Agrega 3 reglas nuevas al sistema. Inventa nuevos síntomas y diagnósticos. Verifica que la equiparación las detecte correctamente con pruebas manuales.
Nivel 2 — Múltiples diagnósticos: Modifica el motor para que retorne TODOS los diagnósticos posibles ordenados por confianza, en lugar de solo el de mayor confianza. El usuario puede ver el ranking completo.
```

## Desafío 1: Nuevas Reglas de Diagnóstico

Se agregaron tres nuevas reglas a la base de conocimiento para ampliar la capacidad de diagnóstico:

- Fuente insuficiente.
- Posible virus.
- Monitor desconectado.

Estas reglas permiten detectar problemas que no estaban contemplados en la versión inicial del sistema.

---

## Desafío 2: Múltiples Diagnósticos

Originalmente el sistema mostraba únicamente el diagnóstico con mayor nivel de confianza.

Se modificó el motor de inferencia para que ahora muestre todos los diagnósticos compatibles con los síntomas ingresados por el usuario, ordenados de mayor a menor confianza.

Esto proporciona una visión más completa de las posibles causas del problema y mejora el proceso de toma de decisiones.

---

# Componentes del Sistema Experto

El sistema desarrollado incluye los cinco componentes fundamentales de un sistema experto:

1. Base de conocimiento.
2. Base de hechos.
3. Motor de inferencia.
4. Sistema de explicación.
5. Interfaz de usuario.

Estos componentes trabajan de forma conjunta para analizar síntomas y generar recomendaciones basadas en reglas predefinidas.

---

# Conclusión

El proyecto permitió aplicar los conceptos fundamentales de los sistemas expertos mediante la construcción de un sistema de diagnóstico funcional. Además, la modularización del código y la implementación de nuevas reglas y múltiples diagnósticos mejoraron significativamente la organización, mantenibilidad y capacidad de análisis del sistema.