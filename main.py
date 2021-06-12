import os
from tensorflow.keras.preprocessing.image import ImageDataGenerator, img_to_array, array_to_img, load_img

def generate_it(file_dir,out_name, no_of_images):
    datagen = ImageDataGenerator(rotation_range=40, width_shift_range=0.5, height_shift_range=0.5, shear_range=1, zoom_range=0.0, horizontal_flip=True, fill_mode='reflect')
    img = load_img(file_dir)
    x = img_to_array(img)
    x = x.reshape((1,)+ x.shape)
    i = 0
    for _ in datagen.flow(x, batch_size=1, save_to_dir=f"{out_name}_aug", save_prefix=out_name, save_format="jpeg"):
        i+=1
        if i==no_of_images:
            break
        pass



initials = input("Enter the initials : ")
dir_path = input("Enter the directory : ")
output_name = input("Enter the output name : ")
no_ = int(input("Enter the number of images you want to generate : "))

list_of_file_name = [_ for _ in os.listdir(dir_path) if _[:2]==initials]
list_of_file_name.sort()
os.mkdir(f"{output_name}_aug")
i = len(list_of_file_name)
for _ in list_of_file_name:
    print(f"Generating images of {_}  | remaining {i-1}")
    generate_it(f"{dir_path}/{_}", output_name, 5)
    i-=1



