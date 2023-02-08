import cv2
import numpy as np
import os
import sys

def divide_images_in_folder(imgPath):
    file_num_count = 0
    for (root, dirs, files) in os.walk(imgPath):
        if len(files) > 0:
            for file_name in files:
                file_num_count += 1
                fname = os.path.basename(file_name)
                divide_image(root, fname, file_num_count)
                
                

def divide_image(imgPath,imgName, file_num_count):
    img = cv2.imread(imgPath+imgName)
    savePath = "./NewDividedImage/"
    # savePath = savePath + imgName +"/"  # seperated by folder
    savePath = savePath +"/"  
    if not os.path.isdir(savePath):
        os.mkdir(savePath)
        
    height, width = img.shape[:2]

    window_size_row = 640
    window_size_col = 640
    
    moving_size_row = 300
    moving_size_col = 300
    
    gap_row = window_size_row - moving_size_row
    gap_col = window_size_col - moving_size_col
    
    a = (width - window_size_row)
    b = (height - window_size_col)
        
    n_image_in_row = a // moving_size_row if a % moving_size_row == 0 else (a // moving_size_row)+1
    n_image_in_col = b // moving_size_col if b % moving_size_col == 0 else (b // moving_size_col)+1 
    
    count = 1

    for y in range(0, n_image_in_col+1):
        y1= y*moving_size_col
        y2 = (window_size_col + y*moving_size_col) if height > (window_size_col + y*moving_size_col) else height
            
        for x in range(0,n_image_in_row+1):
            
            x1 = x*moving_size_row
            x2 = (window_size_row + x*moving_size_row) if width > (window_size_row + x*moving_size_row) else width
            
            if y1 < height and x1 < width:
                tmp_img=img[y1:y2, x1:x2]
                img_num = str(count).zfill(4)

                tmp_title = imgName + "_"+img_num+".jpg"
                # tmp_title = str(file_num_count).zfill(6) + img_num + ".jpg"
                cv2.imwrite(savePath+tmp_title, tmp_img)
            count+=1
    print("Done!")


if __name__ == '__main__':
    BASE_DIR = os.path.dirname(os.path.realpath(__file__)).replace('\\','/',15)
    PARENT_DIR = os.path.dirname(os.path.dirname(__file__))
    RESULT_DIR = "./NewDividedImage/"


    if not os.path.isdir(RESULT_DIR):
        print("There is no folder: "+RESULT_DIR)
        sys.exit()
    
    arg = sys.argv
    FILE_NAME = arg[0]
    IMG_PATH = ""
    IMG_NAMES = []
    
    if len(arg) == 2:
        IMG_PATH = arg[1]
    
        if os.path.isdir(IMG_PATH):
            divide_images_in_folder(IMG_PATH)
            
        elif os.path.isfile(IMG_PATH):
            IMG_NAME = os.path.basename(IMG_PATH)            
            divide_image(IMG_PATH,IMG_NAME[:-4])            
        else:
            print("There is no folder or file: "+ IMG_PATH)
            sys.exit()
    else:
        print(len(arg)) 
        print("잘못된 커맨드 명령어입니다. 'ImageDivider.py [이미지 파일 경로]' 의 형태로 입력해주세요 ")
        sys.exit()




    

    

    
