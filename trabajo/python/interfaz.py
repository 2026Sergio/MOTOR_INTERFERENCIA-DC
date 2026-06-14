from inferencia import inferir


def consultar(
    preguntas,
    base_conocimiento
):

    hechos = set()

    print()
    print("=" * 60)
    print("SISTEMA EXPERTO - DIAGNÓSTICO DE PC")
    print("=" * 60)

    for sintoma, pregunta in preguntas.items():

        respuesta = input(
            f"{pregunta} [s/n]: "
        ).strip().lower()

        if respuesta == "s":

            hechos.add(sintoma)

    inferir(
        base_conocimiento,
        hechos
    )