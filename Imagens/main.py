from rembg import remove
from PIL import Image

input_path = '(Imagem aqui).extencao'
output_path = '(Imagem aqui).png'

inp = Image.open(input_path)
output = remove(inp)
output.save(output_path)



