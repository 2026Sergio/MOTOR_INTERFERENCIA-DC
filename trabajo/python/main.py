# conectamos el motor de inferencia, la base de conocimiento y las preguntas para la interfaz
# aqui se ejecuta 

from conocimiento import (
    base_de_conocimiento,
    PREGUNTAS
)

from interfaz import consultar


def main():

    consultar(
        PREGUNTAS,
        base_de_conocimiento
    )


if __name__ == "__main__":
    main()