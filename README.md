# 项目概述

本项目旨在使用YOLOv5模型进行植物大战僵尸角色的角色检测。整个项目包括数据集准备、模型训练、Web界面展示等环节。通过不断优化数据集和模型参数，最终实现了较为理想的检测效果，并使用Gradio构建了友好的Web端使用界面。
更详细的使用看./USE.txt
该项目代码已共享至git托管平台：<https://github.com/yjzStrongDoll/pvz_yolov5_gradio.git>

## 集成开发环境

为了确保开发过程的顺利进行，本项目在以下环境中进行：

*   操作系统：Ubuntu 20.04&#x20;
*   编程语言：Python 3.8
*   深度学习框架：PyTorch
*   集成开发环境（IDE）：VSCode
*   依赖管理工具：pip

## 基础设施搭建方法

### 1.创建虚拟环境并进入
```bash
conda create -n yolo5 python=3.8
conda activate yolo5

```
### 2. 安装依赖

使用`pip`安装所需的Python包：

```bash
pip install -r requirements.txt

```

### 3. 准备数据集

下载并准备植物大战僵尸角色的图片数据集，可以使用datasets/extract.ipynb、labelimg训练自己的数据集，并按以下结构组织文件夹：

```markdown
datasets/
  ├── images
  │   ├── train
  │   └── val
  └── labels
      ├── train
      └── val

```

### 4.	训练模型

使用以下命令启动模型训练，根据训练结果不断调整数据增强策略和模型参数，获取更多数据以提高模型精度。验证模型效果并保存最佳权重到../runs/train/exp6/weights/best.pt。

```bash
python mytrain.py

```

### 5. 构建Web界面

安装Gradio库：

```bash
pip install gradio

```

创建mygradio.py文件，用于启动Web界面并调用检测函数。使用以下命令启动页面。

```bash
python mygradio.py 

```

运行该脚本，启动Web界面，用户可以通过浏览器上传图片并查看检测结果。

## 结论

通过本项目，您将学习如何搭建并优化YOLOv5模型进行对植物大战僵尸游戏中角色的检测与标注，从数据集准备到模型训练再到Web界面展示，涵盖了该项目的完整流程。
