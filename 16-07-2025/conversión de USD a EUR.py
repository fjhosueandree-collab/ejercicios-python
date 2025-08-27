# Conversión de USD a EUR y a otra moneda extra
monto_usd = 1000.00
tasa_cambio_eur = 0.85    # 1 USD = 0.85 EUR
tasa_cambio_mxn = 17.20   # 1 USD = 17.20 MXN

monto_eur = monto_usd * tasa_cambio_eur
monto_mxn = monto_usd * tasa_cambio_mxn

print(f"Monto en EUR: €{monto_eur:.2f}")
print(f"Monto en MXN: ${monto_mxn:.2f}")
