# Rutas de combis/micros en Puno y sus empresas
rutas_combis_puno = {
    "Ruta 01": "Empresa de Transportes Ancco Hermanos S.R.L.",
    "Ruta 07": "Empresa de Transportes 4 de Noviembre S.R.L.",
    "Ruta 15": "Empresa de Transportes Virgen de Fátima S.R.L.",
    "Ruta 19": "Empresa de Transportes Tupac Amaru S.R.L.",
    "Ruta 25": "Empresa de Transportes Señor de los Milagros S.R.L.",
    "Ruta 33": "Empresa de Transportes 2 de Febrero S.R.L. / Empresa Virgen de la Candelaria S.R.L."
}

print("Rutas de combis en Puno y sus empresas:")
for ruta, empresa in rutas_combis_puno.items():
    print(f"{ruta}: {empresa}")
