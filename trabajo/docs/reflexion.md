# 11 Preguntas de Reflexión

## 1. ¿Cuál es la diferencia principal entre un sistema experto y un programa de software tradicional?

Un programa tradicional sigue instrucciones fijas para resolver una tarea. En cambio, un sistema experto utiliza reglas y hechos para analizar una situación y tomar decisiones similares a las de un experto en un área específica.

---

## 2. ¿Por qué se dice que los sistemas expertos tienen conocimiento separado de su motor de razonamiento? ¿Cuál es la ventaja de esto?

Porque las reglas se almacenan por separado del programa que las analiza. Esto permite agregar o modificar conocimientos sin necesidad de cambiar el motor de inferencia, haciendo el sistema más fácil de mantener y ampliar.

---

## 3. ¿Qué es la base de hechos y en qué se diferencia de la base de conocimiento?

La base de conocimiento contiene las reglas del sistema, mientras que la base de hechos almacena la información proporcionada por el usuario durante una consulta. Las reglas son permanentes y los hechos cambian según cada caso.

---

## 4. ¿Qué significa que un sistema experto pueda "explicar su razonamiento"? ¿Por qué esto es importante en medicina o derecho?

Significa que puede mostrar por qué llegó a una determinada conclusión. Esto es importante porque permite verificar si la decisión tiene sentido y genera confianza en los resultados obtenidos.

---

## 5. ¿Por qué fracasaron comercialmente los sistemas expertos en los años 90? Menciona al menos 3 razones.

- Eran costosos de mantener.
- No podían aprender automáticamente.
- Solo funcionaban en dominios muy específicos.
- Actualizar las reglas requería mucho trabajo de expertos.

---

## 6. Dada la siguiente regla: SI (fiebre AND tos) OR perdida_olfato ENTONCES sospecha_covid y los hechos: {fiebre=True, tos=False, perdida_olfato=True}. ¿Se activa la regla? ¿Por qué?

Sí se activa. Aunque la condición fiebre AND tos es falsa, la condición perdida_olfato es verdadera. Como existe un operador OR, basta con que una de las condiciones sea verdadera para activar la regla.

---

## 7. Completa la tabla de verdad para la expresión (A AND NOT B) OR (NOT A AND B).

| A | B | Resultado |
|---|---|---|
| F | F | F |
| F | V | V |
| V | F | V |
| V | V | F |

La expresión es verdadera únicamente cuando A y B tienen valores diferentes.

---

## 8. ¿Cuál es la diferencia entre encadenamiento hacia adelante y hacia atrás? Da un ejemplo de una situación real donde usarías cada uno.

**Encadenamiento hacia adelante:** parte de los hechos para llegar a una conclusión.

Ejemplo: diagnosticar una computadora utilizando síntomas ingresados por el usuario.

**Encadenamiento hacia atrás:** parte de una conclusión y busca los hechos necesarios para comprobarla.

Ejemplo: verificar si un paciente podría tener una enfermedad específica.

---

## 9. Diseña 3 reglas IF-THEN para un sistema experto que asesore a estudiantes sobre qué lenguaje de programación aprender primero.

**Regla 1**

SI el objetivo es desarrollo web  
ENTONCES recomendar JavaScript.

**Regla 2**

SI el objetivo es análisis de datos  
ENTONCES recomendar Python.

**Regla 3**

SI el objetivo es desarrollo de videojuegos  
ENTONCES recomendar C#.

---

## 10. Dibuja la red de inferencia correspondiente a las 3 reglas diseñadas.

```text
Desarrollo Web ------------> JavaScript

Análisis de Datos ---------> Python

Desarrollo de Videojuegos -> C#
```

---

## 11. ¿Qué problema de diseño podría surgir si dos reglas tienen exactamente las mismas condiciones pero conclusiones diferentes? ¿Cómo lo resolverías?

Podría generarse un conflicto porque el sistema no sabría qué conclusión elegir. Una solución es asignar niveles de confianza a las reglas o establecer prioridades para seleccionar la más adecuada.