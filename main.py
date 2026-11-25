import os
LINE = "I take you to be my lawfully wedded co-pilot — to have and to hold, to charge and to cherish, until our ports do us part."
os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
