total_data = 2
batch_sizes = [100, 200, 150]
for batch in batch_sizes:
    total_data /= batch
print(total_data) # Salida: 450
