import torch
from ultralytics import YOLO

def main():
    model_list = [
        #'yolov5n.pt',
        #'yolov8n.pt',
        #'yolov10n.pt',
        #'yolo11n.pt',
        #'yolo11s.pt',
        #'yolo11m.pt',
        #'yolo11l.pt',
        'yolo11x.pt',
    ]
    for model_name in model_list:
        model = YOLO(model_name)

        model.train(
            data='SD10.yaml',
            epochs=1000,
            patience=20,
            batch=-1,
            project=f'runs/{model_name.split(".")[0]}',
            exist_ok=True,
            seed=42,
            multi_scale=True,
            cos_lr=True,
            profile=True,
            plots=True,
            mixup=1.0,
            copy_paste_mode='mixup',
            auto_augment='autoaugment',
        )
        torch.cuda.empty_cache()



if __name__ == '__main__':
    main()
