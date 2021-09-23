import random

PrimerCandidato = 0
SegundoCandidato = 0
TercerCandidato = 0
for i in range(50000):
    Candidatos = random.randint(1, 3)
    if Candidatos == 1:
        PrimerCandidato += 1
    elif Candidatos == 2:
         SegundoCandidato += 1
    else:
        TercerCandidato += 1
    if PrimerCandidato > SegundoCandidato and PrimerCandidato > TercerCandidato:
        print("El ganador es el primer candidato")
        print(f'Cantidad de votos obtenidas: {PrimerCandidato}')
    elif SegundoCandidato > PrimerCandidato and SegundoCandidato > TercerCandidato:
        print("El ganador es el segundo candidato")
        print(f'Cantidad de votos obtenidas: {SegundoCandidato}')
    if TercerCandidato > PrimerCandidato and TercerCandidato >  SegundoCandidato:
        print("El ganador es el tercer candidato")
        print(f'Cantidad de votos obtenidas: {TercerCandidato}')
    if PrimerCandidato == SegundoCandidato and PrimerCandidato == TercerCandidato:
        print(f'Los candidatos tuvieron un empate con la cantidad de votos de: {PrimerCandidato}')
    if PrimerCandidato == SegundoCandidato:
        print(f'El primer candidato empato con el segundo candidato con un total de votos de: {PrimerCandidato}')
    elif PrimerCandidato == TercerCandidato:
        print(f'El primer candidato empato con el tercer candidato con un total de votos de: {PrimerCandidato}')
    elif SegundoCandidato == TercerCandidato:
        print(f'El segundo candidato empato con el tercer candidato con un total de votos de: {SegundoCandidato}')
    
