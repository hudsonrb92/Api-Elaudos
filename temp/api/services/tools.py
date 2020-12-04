def modalidade(i):
    switcher = {
        'RAIOSX': 'CR',
        'ULTRASSONOGRAFIA': 'US',
        'TOMOGRAFIA': 'CT',
        'RESSONANCIA': 'MR',
        'MAMOGRAFIA': 'MG',
        'DENSITOMETRIA OSSEA': 'OT',
        'CINTILOGRAFIA 1': 'NM',
        'RM': 'MR',
        'TC': 'CT',
        'RX': 'CR',
        'DX': 'CR'
    }
    return switcher.get(i, i)
