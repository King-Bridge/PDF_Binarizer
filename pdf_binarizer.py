from PIL import Image
from pdf2image import convert_from_path
import cv2
import numpy as np
import os, sys
import glob
import img2pdf
import shutil
import argparse

# 将pdf文件转为图像并保存
def pdf2imgs(pdf_path):
    # pdf转为图像
    print("loading pdf...\n")
    pages = convert_from_path(pdf_path)
    print("the pdf has "+str(len(pages))+" pages\n")
    print("starting saving images...\n")
    # 循环遍历所有页面并保存为图像文件
    for i, page in enumerate(pages):
        save_path = 'img/raw_img/'+str(i)+'.png'
        page.save(save_path, 'PNG')
        print(str(i)+".png already saved...\n")
    return pages

# 将图片二值化
def binarize_imgs(pages, threshold):
    print("starting binarizing images...\n")
    for i in range (len(pages)):
        load_path = 'img/raw_img/'+str(i)+'.png'
        img = cv2.imread(load_path, cv2.IMREAD_GRAYSCALE)
        thres, binarized_img = cv2.threshold(img,threshold*255,255,cv2.THRESH_BINARY)
        save_path = 'img/bin_img/'+str(i)+'.png'
        cv2.imwrite(save_path,binarized_img)
        print(str(i+1)+".png already binarized...\n")

# 将多个图像文件合并为一个PDF文件
def imgs2pdf(output_path):
    print("starting converting to pdf...\n")
    # 获取所有图像文件
    image_files = sorted(glob.glob(os.path.join('img/bin_img/', '*.png')))
    # 将图像文件转换为PDF文档
    with open(output_path, 'wb') as f:
        f.write(img2pdf.convert(image_files))
    print("pdf binarizing finished!\n")
    print("saved as"+output_path+"\n")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("pdf_path", type=str)
    parser.add_argument("-t","--threshold", type=float, default=0.5)
    parser.add_argument("--output_path", type=str, default="output.pdf")
    args = parser.parse_args()

    os.makedirs('img/raw_img')
    os.makedirs('img/bin_img')
    
    pages = pdf2imgs(args.pdf_path)
    binarize_imgs(pages, args.threshold)
    imgs2pdf(args.output_path)

    shutil.rmtree('img')