from PIL import Image, ImageOps
import requests
from io import BytesIO

tl = (773 * 3, 735  * 3) # top left corner main image
tl_taskbar = (702 * 3, 1972  * 3) # top left corner main image

img = Image.open("reference.png")
img = img.resize((img.size[0] * 3, img.size[1] * 3), Image.NEAREST)

img_taskbar = Image.open("taskbar.png")
img_taskbar = img_taskbar.resize((img_taskbar.size[0] * 3, img_taskbar.size[1] * 3), Image.NEAREST)

mask_url = "https://media.discordapp.net/attachments/267492253168173056/959625681141104700/mask.png"
response = requests.get(mask_url)
mask_i = Image.open(BytesIO(response.content))
mask = Image.new("1", (3000, 3000), 0)
mask.paste(mask_i)

final_img = Image.new('RGBA', (3000, 3000))
unmasked_img = Image.new('RGBA', (3000, 3000))
unmasked_img.paste(img, tl)
unmasked_img.paste(img_taskbar, tl_taskbar)
final_img = Image.composite(final_img, unmasked_img, mask)
final_img.save("superstonk_overlay.png")
