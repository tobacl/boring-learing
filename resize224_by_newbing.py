from PIL import Image
import os

def resize_image(root_path,save_path):
    for dir_name in os.listdir(root_path):  # dir_name是1,2,3,4,5，...9
        save_file_path = os.path.join(save_path, dir_name)
        if not os.path.exists(save_file_path):
            os.makedirs(save_file_path)
            for img_name in os.listdir(root_path + '//' + dir_name):
                img_path = os.path.join(root_path, dir_name, img_name)

                image = Image.open(img_path)
                width, height = image.size
                new_width = 224
                new_height = int(new_width * height / width)
                resized_image = image.resize((new_width, new_height), Image.ANTIALIAS)
                new_image = Image.new("L", (224, 224))
                new_image.paste(resized_image, (0, 0))
                new_image.save(os.path.join(save_file_path, img_name))


if __name__ == '__main__':
    resize_image('E:/yarn_twist_new/resizeyarn_dataset', 'E:/yarn_twist_new/224_dataset')

