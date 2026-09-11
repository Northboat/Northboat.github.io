from PIL import Image, ImageDraw, ImageSequence

im = Image.open("./gg.webp")
frames = []
for frame in ImageSequence.Iterator(im):
    frame = frame.convert("RGBA")
    w, h = frame.size
    radius = min(w, h) // 5  # 圆角半径，按需调整

    mask = Image.new("L", (w, h), 0)
    draw = ImageDraw.Draw(mask)
    draw.rounded_rectangle((0, 0, w, h), radius=radius, fill=255)

    frame.putalpha(mask)
    frames.append(frame)

frames[0].save(
    "output.webp",
    save_all=True,
    append_images=frames[1:],
    loop=0,
    duration=im.info.get("duration", 100),
    disposal=2,
)