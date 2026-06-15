# Explicación del Proyecto — Motor de Inferencia DC

## Descripción General

Este proyecto consiste en un sistema experto para el diagnóstico de problemas en computadoras, desarrollado en Python. El sistema fue tomado de una base inicial con todo el código en un solo archivo y posteriormente fue modularizado en varios módulos con responsabilidades separadas. Además, se implementaron dos desafíos de extensión sobre el motor de inferencia original.

El sistema realiza preguntas al usuario sobre los síntomas que presenta su computadora y, mediante reglas de conocimiento y un motor de inferencia, genera diagnósticos ordenados por nivel de confianza.

---

## Estructura del Proyecto

```text
MOTOR_INTERFERENCIA-DC-main/
│
├── README.md
├── CONTRIBUTING.md
├── explicacion.md
│
└── trabajo/
    ├── docs/
    │   └── reflexion.md
    │
    └── python/
        ├── conocimiento.py
        ├── inferencia.py
        ├── interfaz.py
        ├── main.py
        └── modularizacion.md
```

---

## Modularización del Código

Uno de los cambios más importantes fue separar el código original, que estaba en un único archivo, en cuatro módulos con responsabilidades específicas.

### conocimiento.py

Funciona como la base de conocimiento del sistema.

Contiene:

- Las reglas de diagnóstico (R01–R10).
- La descripción de cada problema.
- Las condiciones necesarias para activar una regla.
- La recomendación o conclusión correspondiente.
- El nivel de confianza de cada regla.
- El diccionario de preguntas que se realiza al usuario.

### inferencia.py

Contiene el motor de inferencia.

Sus funciones principales son:

- Comparar los síntomas ingresados con las reglas disponibles.
- Identificar qué reglas se cumplen.
- Ordenar los diagnósticos según su confianza.
- Mostrar los resultados y la explicación del razonamiento utilizado.

### interfaz.py

Se encarga de la interacción con el usuario.

Su función principal recopila las respuestas del usuario y construye la base de hechos que posteriormente será analizada por el motor de inferencia.

### main.py

Es el archivo principal del sistema.

Se encarga de importar los módulos necesarios y ejecutar la aplicación.

---

## Desafío 1 — Agregar Reglas

Se agregaron tres nuevas reglas para ampliar la capacidad de diagnóstico del sistema:

| ID | Diagnóstico | Confianza |
|----|-------------|------------|
| R08 | Fuente insuficiente | 75% |
| R09 | Posible virus | 70% |
| R10 | Monitor desconectado | 82% |

Estas nuevas reglas permiten detectar problemas adicionales que no estaban contemplados en la versión inicial.

---

## Desafío 2 — Múltiples Diagnósticos

En la versión original únicamente se mostraba el diagnóstico con mayor nivel de confianza.

Se modificó el motor de inferencia para que ahora:

- Detecte todas las reglas compatibles con los síntomas ingresados.
- Ordene los diagnósticos de mayor a menor confianza.
- Muestre un ranking completo de resultados.
- Presente el diagnóstico principal y las alternativas posibles.

Esto proporciona una visión más completa del problema y ayuda al usuario a tomar mejores decisiones.

---

## Componentes del Sistema Experto

El sistema implementa los cinco componentes fundamentales de un sistema experto:

1. Base de Conocimiento.
2. Base de Hechos.
3. Motor de Inferencia.
4. Sistema de Explicación.
5. Interfaz de Usuario.

Todos estos componentes trabajan en conjunto para analizar síntomas y generar recomendaciones basadas en reglas previamente definidas.

---

## Tecnologías Utilizadas

- Python 3
- Listas
- Diccionarios
- Conjuntos (Set)
- Programación Modular
- GitHub
- Archivo `.gitignore`

---

## Conclusión

Con este proyecto aprendí cómo funciona un sistema experto y cómo utilizar Python para crear uno. También aprendí a organizar mejor el código mediante módulos y a agregar nuevas funciones para mejorar el funcionamiento del sistema. En general, fue una buena práctica para aplicar los conceptos vistos en clase.