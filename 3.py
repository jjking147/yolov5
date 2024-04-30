import os
import random
from shutil import copyfile


def split_dataset(image_folder, txt_folder, output_folder, split_index):
    # Ensure output folders exist
    for dataset in ['train', 'val']:
        if not os.path.exists(os.path.join(output_folder, dataset, 'images')):
            os.makedirs(os.path.join(output_folder, dataset, 'images'))
        if not os.path.exists(os.path.join(output_folder, dataset, 'txt')):
            os.makedirs(os.path.join(output_folder, dataset, 'txt'))
    train_index = os.path.join(split_index, 'train.txt')
    val_index = os.path.join(split_index, 'val.txt')
    with open(train_index, 'r') as file:
        train_images = [i.strip() for i in file.readlines()]
    with open(val_index, 'r') as file:
        val_images = [i.strip() for i in file.readlines()]

    # Copy images to respective folders
    for dataset, images_list in zip(['train', 'val'], [train_images, val_images]):
        for image_file in images_list:
            image_path = os.path.join(image_folder, image_file)
            print(image_path)
            copyfile(image_path, os.path.join(output_folder, dataset, 'images', image_file))
            txt_file = image_file + '.txt'
            txt_path = os.path.join(txt_folder, txt_file)
            print(txt_file)

            # Copy corresponding txt file if exists
            if os.path.exists(txt_path):
                copyfile(txt_path, os.path.join(output_folder, dataset, 'txt', txt_file))


if __name__ == "__main__":
    image_folder_path = "E:\yolov5-master\JPEGImages"
    txt_folder_path = "E:\yolov5-master\ImageSets\YOLOLabels"
    output_dataset_path = "E:\yolov5-master\ImageSets\YOLO_DATA"
    split_index = "E:\yolov5-master\ImageSets\Main"

    split_dataset(image_folder_path, txt_folder_path, output_dataset_path, split_index)