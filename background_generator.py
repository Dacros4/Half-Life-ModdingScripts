from PIL import Image

pre_img = Image.open("pre.png") #change it if necessary
w, h = 800, 600
wt, ht = w // 256, h // 256

for v in range(ht + 1):
    for i in range(wt + 1):
        crop_sz = (i * 256, v * 256, (i + 1) * 256, (v + 1) * 256)
        if i == wt and v != ht:
            crop_sz = (i * 256, v * 256, w, (v + 1) * 256)
        if i != wt and v == ht:
            crop_sz = (i * 256, v * 256, (i + 1) * 256, h)
        if i == wt and v == ht:
            crop_sz = (i * 256, v * 256, w, h)
        nim = pre_img.crop(crop_sz)
        nim.rotate(180)
        filename = "_result/" + str(w) + "_" + str(v + 1) + "_" + chr(97 + i) + "_loading.tga"
        nim.save(filename)
        print("Saved " + filename)

print("DONE")
