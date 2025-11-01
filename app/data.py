import random

POKENEAS = [
    {"id": 1, "nombre": "Paisita", "altura": "1.60 m", "habilidad": "Negociar", "imagen": "https://pokenea-bucket-mariana.s3.us-east-2.amazonaws.com/pokemon1.jpg", "frase": "¡Pues claro que sí, ome!"},
    {"id": 2, "nombre": "ElRetiro", "altura": "1.70 m", "habilidad": "Carpintería", "imagen": "https://pokenea-bucket-mariana.s3.us-east-2.amazonaws.com/pokemon2.jpg", "frase": "La madera habla si uno sabe oír."},
    {"id": 3, "nombre": "Guarnezor", "altura": "1.75 m", "habilidad": "Aguante", "imagen": "https://pokenea-bucket-mariana.s3.us-east-2.amazonaws.com/pokemon3.jpg", "frase": "Más vale vereda conocida que autopista por conocer."},
    {"id": 4, "nombre": "Sabanatra", "altura": "1.68 m", "habilidad": "Sazón", "imagen": "https://pokenea-bucket-mariana.s3.us-east-2.amazonaws.com/pokemon4.jpg", "frase": "Aquí se come sabroso."},
    {"id": 5, "nombre": "Envigade", "altura": "1.62 m", "habilidad": "Orden", "imagen": "https://pokenea-bucket-mariana.s3.us-east-2.amazonaws.com/pokemon5.jpg", "frase": "Cada cosa en su lugar."},
    {"id": 6, "nombre": "BelloMon", "altura": "1.80 m", "habilidad": "Fuerza", "imagen": "https://pokenea-bucket-mariana.s3.us-east-2.amazonaws.com/pokemon6.jpg", "frase": "Siempre pa’lante."},
    {"id": 7, "nombre": "RioneGrox", "altura": "1.73 m", "habilidad": "Velocidad", "imagen": "https://pokenea-bucket-mariana.s3.us-east-2.amazonaws.com/pokemon7.jpg", "frase": "Aterrizamos y arrancamos."}
]

def get_random_pokenea():
    return random.choice(POKENEAS)
