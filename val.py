import torch
from ultralytics import YOLO

def main():
    model_list = [
        'runs\\yolov5n\\train\\weights\\best.pt',
        'runs\\yolov8n\\train\\weights\\best.pt',
        'runs\\yolov10n\\train\\weights\\best.pt',
        'runs\\yolo11n\\train\\weights\\best.pt',
        'runs\\yolo11s\\train\\weights\\best.pt',
        'runs\\yolo11m\\train\\weights\\best.pt',
        'runs\\yolo11l\\train\\weights\\best.pt',
        'runs\\yolo11x\\train\\weights\\best.pt',
    ]
    project_list = [
        'yolov5n',
        'yolov8n',
        'yolov10n',
        'yolo11n',
        'yolo11s',
        'yolo11m',
        'yolo11l',
        'yolo11x',
    ]
    
    for model_name, project_name in zip(model_list, project_list):
        model = YOLO(model_name)

        model.val(
            data='SD10.yaml',
            split='test',
            batch=32,
            project=f'runs/{project_name}',
            exist_ok=True,
        )
        torch.cuda.empty_cache()

if __name__ == '__main__':
    main()
