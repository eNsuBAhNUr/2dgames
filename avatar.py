# procedural_avatar.py
import random
from PIL import Image, ImageDraw

W, H = 512, 512

def random_color():
    return tuple(random.randint(30, 230) for _ in range(3))

def draw_procedural_human(path):
    skin = random.choice([(255,220,180),(230,190,140),(200,150,110),(140,85,60)])
    shirt = random_color()
    hair = random_color()
    img = Image.new("RGBA", (W,H), (255,255,255,0))
    d = ImageDraw.Draw(img)
    # head with optional hair top
    d.ellipse((160,50,352,232), fill=skin+(255,), outline=(0,0,0))
    # hair (simple)
    d.polygon([(160,120),(352,120),(352,92),(320,72),(192,72),(160,92)], fill=hair+(255,), outline=None)
    # body
    d.rectangle((200,232,312,380), fill=shirt+(255,), outline=(0,0,0))
    # arms (skin colored)
    d.line((200,260,140,320), fill=skin+(255,), width=22)
    d.line((312,260,372,320), fill=skin+(255,), width=22)
    # legs
    d.line((238,380,238,480), fill=(0,0,0), width=18)
    d.line((274,380,274,480), fill=(0,0,0), width=18)
    # eyes position randomized
    eye_x = random.randint(200,230)
    d.ellipse((eye_x-10,110,eye_x+10,130), fill=(0,0,0))
    d.ellipse((eye_x+72,110,eye_x+92,130), fill=(0,0,0))
    # mouth shape variant
    if random.random() < 0.5:
        d.arc((220,140,292,180), start=0, end=180, fill=(0,0,0), width=4)
    else:
        d.rectangle((230,150,282,160), fill=(0,0,0))
    img.save(path)

if __name__ == "__main__":
    for i in range(3):
        out = f"proc_human_{i+1}.png"
        draw_procedural_human(out)
        print("Saved", out)
