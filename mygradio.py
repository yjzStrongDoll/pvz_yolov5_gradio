import torch
import gradio as gr

# model = torch.hub.load("./", "custom", path="runs/train/exp2/weights/best.pt", source="local")
# model = torch.hub.load("./", "custom", path="./yolov5s", source="local")
model = torch.hub.load("./", "custom", path="runs/train/exp6/weights/best.pt", source="local")

title = "基于YOLOv5的植物大战僵尸检测项目"

desc = "这是一个基于YOLOv5的植物大战僵尸检测项目"

base_conf, base_iou = 0.25, 0.45

def det_image(img, conf_thres, iou_thres):
    model.conf = conf_thres
    model.iou = iou_thres
    return model(img).render()[0]

gr.Interface(inputs=["image", gr.Slider(minimum=0, maximum=1, value=base_conf), gr.Slider(minimum=0, maximum=1, value=base_iou)], 
             outputs=["image"], 
             fn=det_image,
             title=title,
             description=desc,
             live=True, 
            #  examples=[["./datasets/images/train/30.jpg", base_conf, base_iou], ["./datasets/images/train/60.jpg", 0.3, base_iou]]).launch(share=True)
            #  examples=[["./data/images/bus.jpg", base_conf, base_iou], ["./data/images/zidane.jpg", 0.3, base_iou]]).launch(share=True)
             examples=[["./datasets/images/train/80.jpg", base_conf, base_iou], ["./datasets/images/train/520.jpg", 0.3, base_iou]]).launch(share=True)

