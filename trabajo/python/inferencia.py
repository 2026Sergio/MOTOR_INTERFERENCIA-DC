# ==================================================
# MOTOR DE INFERENCIA
# ==================================================

# El motor de inferencia evalúa los hechos ingresados por el usuario contra la base de conocimiento.

def equiparar(base_conocimiento, hechos):

    conflict_set = []

    for regla in base_conocimiento:

        if set(regla["condiciones"]).issubset(hechos):
            conflict_set.append(regla)

    return conflict_set


def inferir(base_conocimiento, hechos):

    print()
    print("━" * 60)
    print("MOTOR DE INFERENCIA")
    print("━" * 60)

    print(f"Hechos ingresados: {hechos}")
    print()

    conflict_set = equiparar(
        base_conocimiento,
        hechos
    )

    if not conflict_set:

        print("No se encontraron reglas aplicables.")
        return

    ranking = sorted(
        conflict_set,
        key=lambda r: r["confianza"],
        reverse=True
    )

    mejor = ranking[0]

    print("DIAGNÓSTICO PRINCIPAL")
    print("-" * 60)

    print(f"Regla: {mejor['id']}")
    print(f"Descripción: {mejor['descripcion']}")
    print(f"Recomendación: {mejor['conclusion']}")
    print(f"Confianza: {mejor['confianza']*100:.0f}%")

    print()
    print("RANKING COMPLETO DE DIAGNÓSTICOS")
    print("-" * 60)

    for i, regla in enumerate(ranking, start=1):

        print(
            f"{i}. "
            f"{regla['descripcion']} "
            f"({regla['confianza']*100:.0f}%)"
        )

    print()
    print("TRAZABILIDAD")

    print(
        f"Síntomas usados por la mejor regla: "
        f"{mejor['condiciones']}"
    )

    print("━" * 60)