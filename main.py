from transformers import pipeline
import torch

# Sprawdzenie czy Python widzi GPU i wybór urządzenia (0 to pierwsza karta RTX 3080)
device = 0 if torch.cuda.is_available() else -1

# Połączenie: Ładowanie modelu AI do pamięci karty graficznej
classifier = pipeline("sentiment-analysis", device=device)

# Test AI
text = "Python and RTX 3080 are a powerful combination!"
result = classifier(text)

print(f"Wynik analizy AI: {result}")