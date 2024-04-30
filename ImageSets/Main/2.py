import os
import xml.etree.ElementTree as ET


def convert_folder_to_yolov5(input_folder, output_folder):
    # Ensure output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Loop through each XML file in the input folder
    for xml_file_name in os.listdir(input_folder):
        if xml_file_name.endswith('.xml'):
            xml_file_path = os.path.join(input_folder, xml_file_name)

            # Generate corresponding output txt file path
            txt_file_name = os.path.splitext(xml_file_name)[0] + '.txt'
            txt_file_path = os.path.join(output_folder, txt_file_name)

            # Convert XML to Yolov5 format and save to txt file
            convert_to_yolov5(xml_file_path, txt_file_path)


def convert_to_yolov5(xml_file, output_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    with open(output_file, 'w') as f:
        for obj in root.findall('object'):
            class_name = obj.find('name').text
            if class_name == 'face':  # Assuming 'disease' is the class of interest
                xmin = int(obj.find('bndbox/xmin').text)
                ymin = int(obj.find('bndbox/ymin').text)
                xmax = int(obj.find('bndbox/xmax').text)
                ymax = int(obj.find('bndbox/ymax').text)

                width = xmax - xmin
                height = ymax - ymin
                x_center = (xmin + xmax) / 2.0
                y_center = (ymin + ymax) / 2.0

                # Normalize coordinates and dimensions
                x_center /= int(root.find('size/width').text)
                y_center /= int(root.find('size/height').text)
                width /= int(root.find('size/width').text)
                height /= int(root.find('size/height').text)

                line = f"{0} {x_center} {y_center} {width} {height}\n"
                f.write(line)


if __name__ == "__main__":
    input_folder_path = "E:\yolov5-master\Annotations"  # voc格式标注文件
    output_folder_path = "E:\yolov5-master\ImageSets\\test"  # yolo格式保存地址

    convert_folder_to_yolov5(input_folder_path, output_folder_path)