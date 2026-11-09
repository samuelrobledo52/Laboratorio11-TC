# Laboratorio 11 - Teoría de la Computación

Samuel Robledo, 241282
Universidad del Valle de Guatemala

## Archivos

- `Lab11_SamuelRobledo_241282.pdf`: entrega con todas las respuestas.
- `lab11.tex`: fuente LaTeX del PDF.
- `z3/mistery_11.smt2`: código del enunciado, evalúa `mistery(11)`.
- `z3/validez_demorgan.smt2`: prueba de validez de la ley de De Morgan (negación, da `unsat`).
- `z3/no_validez.smt2`: fórmula no válida, da `sat` y un contraejemplo con `get-model`.
- `z3/correr_mistery.py`: corre `mistery` para x = 1..20 y arma la tabla.
- `z3/salidas.txt`: tabla generada por el script.

## Cómo correr el script

Desde la carpeta del lab, en CMD:

```
python -m venv .venv
.venv\Scripts\python -m pip install z3-solver
.venv\Scripts\python z3\correr_mistery.py
```

El script usa el ejecutable `z3` que instala `z3-solver` en `.venv\bin` y sobrescribe `z3/salidas.txt`.
