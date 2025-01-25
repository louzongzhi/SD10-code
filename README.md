# SD10 Dataset for YOLO Object Detection

## Overview

The SD10 dataset is designed for object detection tasks, specifically tailored for identifying various types of surface defects. This dataset contains a total of 9822 images for training, 2105 images for validation, and 2107 images for testing. The dataset is structured to work with YOLO (You Only Look Once) object detection models.

## Dataset Structure

The dataset is organized as follows:

- **Path**: `../datasets/SD10`
- **Training Images**: `images/train`
- **Validation Images**: `images/val`
- **Testing Images**: `images/test`

## Classes

The SD10 dataset categorizes defects into 10 classes:

| Class ID | Class Name       |
|----------|------------------|
| 0        | crazing          |
| 1        | inclusion        |
| 2        | patches          |
| 3        | pitted_surface   |
| 4        | rolled-in_scale  |
| 5        | scratches        |
| 6        | blowhole         |
| 7        | fray             |
| 8        | break            |
| 9        | uneven           |

## Benchmark Results

Several YOLO models were tested on the SD10 dataset, and the results are summarized below. The metrics used for evaluation are Precision (P), Recall (R), mAP50 (mean Average Precision at IoU=0.5) and Mean Average Precision (mAP) and inference speed.

### YOLOv5n

- **Layers**: 193
- **Parameters**: 2,504,894
- **GFLOPs**: 7.1
- **mAP50**: 0.595
- **Speed**: 1.0ms per image

### YOLOv8n

- **Layers**: 168
- **Parameters**: 3,007,598
- **GFLOPs**: 8.1
- **mAP50**: 0.714
- **Speed**: 0.9ms per image

### YOLOv10n

- **Layers**: 285
- **Parameters**: 2,698,316
- **GFLOPs**: 8.2
- **mAP50**: 0.74
- **Speed**: 0.9ms per image

### YOLO11n

- **Layers**: 238
- **Parameters**: 2,584,102
- **GFLOPs**: 6.3
- **mAP50**: 0.762
- **Speed**: 0.9ms per image

### YOLO11s

- **Layers**: 238
- **Parameters**: 9,416,670
- **GFLOPs**: 21.3
- **mAP50**: 0.8
- **Speed**: 1.2ms per image

### YOLO11m

- **Layers**: 303
- **Parameters**: 20,037,742
- **GFLOPs**: 67.7
- **mAP50**: 0.806
- **Speed**: 2.3ms per image

### YOLO11l

- **Layers**: 464
- **Parameters**: 25,287,022
- **GFLOPs**: 86.6
- **mAP50**: 0.806
- **Speed**: 2.8ms per image

### YOLO11x

- **Layers**: 464
- **Parameters**: 56,838,574
- **GFLOPs**: 194.5
- **mAP50**: 0.793
- **Speed**: 4.8ms per image

## Usage

To use the SD10 dataset with YOLO models, follow these steps:

1. **Download the Dataset**: Clone the repository or download the dataset from [GitHub](https://github.com/louzongzhi/SD10).
2. **Extract the Dataset**: Ensure the dataset is extracted to the specified path (`../datasets/SD10`).
3. **Configure the YAML File**: Use the provided YAML configuration file to set up the dataset paths and class names.
4. **Train/Validate/Test**: Run the YOLO model training, validation, or testing using the dataset.

## Acknowledgments

- The dataset and models are based on the work by Ultralytics.
- Special thanks to the contributors and maintainers of the YOLO project.

## License

This dataset is released under the [LICENSE] license.

## Contact

For any questions or suggestions, please open an issue on the GitHub repository or contact [2871561809@qq.com](mailto:2871561809@qq.com).

---

**