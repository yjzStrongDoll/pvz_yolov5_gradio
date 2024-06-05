import mss
import mss.tools
from PIL import Image
with mss.mss() as m:
    rect = m.monitors[0]
    t = time.time()
    img = m.grab(rect)
    
    pim = Image.new("RGB",img.size)
    pim.frombytes(img.rgb)
    pim.save("grab.jpg",quality=95)
    #95的满级quality(品质)可以保持原来的高清晰度
    del img,pim
