class MiExcepcion(Exception):
    def __init__(self,err):
        print(f"Cometiste el siguoente error: {err}")
try:
    #raise ZeroDivisionError("Has intentado dividir entre cero")
    raise MiExcepcion("Un error demasiado importante")
except:
    print("Como has podido cometer ese error")