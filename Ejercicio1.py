def momento_dia(hora):
    if hora >= 6 and hora <=12:
        return 'Mañana'
    elif hora >=7 and hora <= 18:
        return 'Tarde'
    else:
        return 'Noche'

    