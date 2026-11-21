import os as os
import json as js

extensiones = (".jpg", ".jpeg", ".png", ".webp")
foticas = [n for n in os.listdir("Fotos") if n.lower().endswith(extensiones)]

with open("fotos.js", "w", encoding = "UTF-8") as tal:
    tal.write("conts_fotos = " + js.dumps(foticas) + ";")