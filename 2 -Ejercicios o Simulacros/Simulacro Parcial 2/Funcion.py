def conversor(tiempo):
    horas = int(tiempo / 3600)
    minutos = int(tiempo % 3600 / 60)
    segundos = int(tiempo % 3600 % 60)

    return horas, minutos, segundos
