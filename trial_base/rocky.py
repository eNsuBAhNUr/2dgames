# mystery_avatar.py
from PIL import Image, ImageDraw

W, H = 512, 512

def draw_mystery_avatar(path):
    img = Image.new("RGBA", (W,H), (0,0,0,0))  # transparent
    d = ImageDraw.Draw(img)

    # Hood / head shroud
    d.polygon([(180,60),(332,60),(300,180),(212,180)], fill=(20,20,20,255))

    # Face shadow (just a hint)
    d.ellipse((220,100,292,172), fill=(10,10,10,255))

    # Glowing eyes
    d.ellipse((235,130,250,145), fill=(0,255,255,255))  # left eye
    d.ellipse((262,130,277,145), fill=(0,255,255,255))  # right eye

    # Cloak / flowing body
    d.polygon([(180,180),(332,180),(300,420),(212,420)], fill=(30,30,40,255))

    # Shadowed hands holding a mysterious orb
    d.ellipse((200,280,230,310), fill=(50,50,60,255))  # left hand
    d.ellipse((282,280,312,310), fill=(50,50,60,255))  # right hand
    d.ellipse((245,285,267,307), fill=(0,200,255,255))  # orb (mystery item)

    # Optional glowing emblem
    d.ellipse((250,200,262,212), fill=(255,50,200,255))

    img.save(path)

if __name__ == "__main__":
    out = "mystery_avatar.png"
    draw_mystery_avatar(out)
    print("Saved:", out)
