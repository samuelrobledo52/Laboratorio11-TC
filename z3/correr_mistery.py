import os
import subprocess
import sys
from pathlib import Path

base = Path(__file__).resolve().parent
plantilla = (base / "mistery_11.smt2").read_text(encoding="utf-8")
z3_exe = Path(sys.prefix) / "bin" / ("z3.exe" if os.name == "nt" else "z3")

def ejecutar(x):
    codigo = plantilla.replace("(assert (mistery 11))", f"(assert (mistery {x}))")
    r = subprocess.run([str(z3_exe), "-in"], input=codigo,
                       capture_output=True, text=True)
    return r.stdout.strip()

lineas = ["x  | resultado", "---+----------"]
for x in range(1, 21):
    lineas.append(f"{x:<2} | {ejecutar(x)}")
tabla = "\n".join(lineas)
print(tabla)
(base / "salidas.txt").write_text(tabla + "\n", encoding="utf-8")
