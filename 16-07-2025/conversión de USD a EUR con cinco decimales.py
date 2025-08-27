# 2. Conversión de USD a EUR, MXN y PEN (Perú) con 5 decimales
monto_usd = 1000.00
tasa_cambio_eur = 0.85        # 1 USD = 0.85 EUR
tasa_cambio_mxn = 17.20       # 1 USD = 17.20 MXN
tasa_cambio_pen = 3.66920     # 1 USD = 3.66920 PEN (Sol peruano) [2025]

monto_eur = monto_usd * tasa_cambio_eur
monto_mxn = monto_usd * tasa_cambio_mxn
monto_pen = monto_usd * tasa_cambio_pen

print(f"Monto en EUR: €{monto_eur:.5f}")
print(f"Monto en MXN: ${monto_mxn:.5f}")
print(f"Monto en PEN: S/{monto_pen:.5f}")
