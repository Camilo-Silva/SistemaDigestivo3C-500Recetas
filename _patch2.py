#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re

file_path = r'd:\15.VidaEnCalma\landing-500Recetas\index-Sistema-Digestivo3C.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Wrap each bare <img class="ep-card-img" ... /> with the new div wrapper
def wrap_img(m):
    src = m.group(1)
    alt = m.group(2)
    return f'<div class="ep-card-img-wrap"><img class="ep-card-img" src="{src}" alt="{alt}" /></div>'

new_content = re.sub(
    r'<img class="ep-card-img" src="([^"]+)" alt="([^"]+)" />',
    wrap_img,
    content
)

changes = content.count('<img class="ep-card-img"') - new_content.count('<img class="ep-card-img"')
print(f"Imágenes envueltas: {6 - changes} (debería ser 0 cambios en count ya que ahora están dentro del wrapper)")
wrapped = new_content.count('ep-card-img-wrap')
print(f"Wrappers insertados: {wrapped}")

with open(file_path, 'w', encoding='utf-8', newline='\r\n') as f:
    f.write(new_content)

print("OK")
