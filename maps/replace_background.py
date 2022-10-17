import os

files = [f for f in os.listdir() if f.endswith(".svg")]

for file in files:
    with open(file, 'r', encoding="utf-8") as f:
        svgtext = f.read()

    svgtext = svgtext.replace("; background-color: rgb(208, 208, 208);", "; background-color: transparent;", 1)

    with open(file, 'w', encoding="utf-8") as f:
        f.write(svgtext)
