import os as os
import json as js

extensiones = (".jpg", ".jpeg", ".png", ".webp")
foticas = [n for n in os.listdir("Fotos") if n.lower().endswith(extensiones)]
videicos = [n for n in os.listdir("Videos") if n.lower().endswith(".mp4")]

with open("fotos.js", "w", encoding = "UTF-8") as tal:
    tal.write("conts_fotos = " + js.dumps(foticas) + ";")

with open("videos.js", "w", encoding = "UTF-8") as tal:
    tal.write("conts_videos = " + js.dumps(videicos) + ";")