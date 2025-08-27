# 4. Cálculo de interés compuesto con más variables y 7 decimales
capital_inicial = 10000.00
tasa_interes = 0.05  # 5% anual
periodos = 3
aportacion_anual = 500.00

monto_final = capital_inicial
for i in range(periodos):
    monto_final = (monto_final + aportacion_anual) * (1 + tasa_interes)

print(f"Monto final después de {periodos} años y aportaciones: ${monto_final:.7f}")
