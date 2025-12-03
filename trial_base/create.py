# avatar_generator.py
# Usage: python avatar_generator.py [human|car|abstract]
import sys
from PIL import Image, ImageDraw

W, H = 512, 512

def draw_human(path):
    img = Image.new("RGBA", (W,H), (255,255,255,0))
    d = ImageDraw.Draw(img)
    # head
    d.ellipse((180,60,332,212), fill=(255,220,180,255), outline=(0,0,0))
    # body
    d.rectangle((210,212,302,380), fill=(60,120,200,255), outline=(0,0,0))
    # arms
    d.line((210,240,140,320), fill=(255,220,180,255), width=24)
    d.line((302,240,372,320), fill=(255,220,180,255), width=24)
    # legs
    d.line((240,380,240,480), fill=(0,0,0), width=18)
    d.line((272,380,272,480), fill=(0,0,0), width=18)
    # eyes & smile
    d.ellipse((210,110,230,130), fill=(0,0,0))
    d.ellipse((282,110,302,130), fill=(0,0,0))
    d.arc((220,140,292,180), start=0, end=180, fill=(0,0,0), width=4)
    img.save(path)

def draw_car(path):
    img = Image.new("RGBA", (W,H), (255,255,255,0))
    d = ImageDraw.Draw(img)
    # body
    d.rounded_rectangle((60,200,452,320), radius=30, fill=(200,40,40,255), outline=(0,0,0))
    # roof
    d.polygon([(140,200),(210,140),(302,140),(372,200)], fill=(200,40,40,255), outline=(0,0,0))
    # windows
    d.polygon([(220,160),(270,160),(290,200),(200,200)], fill=(180,230,255,200))
    d.polygon([(290,160),(330,160),(360,200),(290,200)], fill=(180,230,255,200))
    # wheels
    d.ellipse((120,300,190,370), fill=(0,0,0))
    d.ellipse((320,300,390,370), fill=(0,0,0))
    # wheel hubs
    d.ellipse((145,325,165,345), fill=(180,180,180))
    d.ellipse((345,325,365,345), fill=(180,180,180))
    img.save(path)

def draw_abstract(path):
    img = Image.new("RGBA", (W,H), (255,255,255,0))
    d = ImageDraw.Draw(img)
    # rounded cube
    d.rounded_rectangle((120,120,392,392), radius=24, fill=(90,200,120,255), outline=(0,0,0))
    # eye-like circles
    d.ellipse((200,180,240,220), fill=(255,255,255))
    d.ellipse((280,180,320,220), fill=(255,255,255))
    d.ellipse((212,192,228,208), fill=(0,0,0))
    d.ellipse((292,192,308,208), fill=(0,0,0))
    # mouth
    d.rectangle((220,260,292,280), fill=(30,30,30))
    # antenna
    d.line((256,120,256,80), fill=(0,0,0), width=6)
    d.ellipse((246,60,266,80), fill=(255,200,0))
    img.save(path)

if __name__ == "__main__":
    typ = sys.argv[1].lower() if len(sys.argv) > 1 else "human"
    out = f"{typ}_avatar.png"
    if typ == "human":
        draw_human(out)
    elif typ == "car":
        draw_car(out)
    elif typ in ("abstract","object","robot"):
        draw_abstract(out)
    else:
        print("Unknown type. Use human|car|abstract")
        sys.exit(1)
    print("Saved:", out)
