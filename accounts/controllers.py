from PIL import Image, ImageDraw, ImageFont
import random, string
from django.conf import settings

def generate_captch(value, file):
    font = ImageFont.truetype(settings.STATICFILES_DIRS[0]+"/fonts/arial.ttf", 24)
    img = Image.new('RGB', (200,40), color = (73, 109, 137))
    draw = ImageDraw.Draw(img)
    draw.text((50,10), value, fill=(255,255,0), font=font)
    img.save(file)
    
def generate_random_string(max_len):
    gen_string = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(max_len))
    return gen_string