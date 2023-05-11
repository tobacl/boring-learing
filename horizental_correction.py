import cv2
import math
import numpy as np
from scipy import ndimage


class HorizontalCorrection:
    def __init__(self):
        self.rotate_vector = np.array([0, 1])  # 图片中地面的法线向量
        self.rotate_theta = 0  # 旋转的角度

    def process(self, img):
        img = cv2.imread(img)  # 读取图片
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 二值化
        edges = cv2.Canny(gray, 50, 150, apertureSize=3)  # canny算子

        # 霍夫变换
        lines = cv2.HoughLines(edges, 1, np.pi / 180, 50)
        sum = 0
        count = 0
        for i in range(len(lines)):
            for rho, theta in lines[i]:
                a = np.cos(theta)
                b = np.sin(theta)
                x0 = a * rho
                y0 = b * rho
                x1 = int(x0 + 1000 * (-b))
                y1 = int(y0 + 1000 * (a))
                x2 = int(x0 - 1000 * (-b))
                y2 = int(y0 - 1000 * (a))

                if x2 != x1:
                    t = float(y2 - y1) / (x2 - x1)
                    if t <= np.pi / 5 and t >= - np.pi / 5:
                        rotate_angle = math.degrees(math.atan(t))
                        sum += rotate_angle
                        count += 1
                        cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

        if count == 0:
            avg_rotate_angle = 0
        else:
            avg_rotate_angle = sum / count
        self.rotate_img = ndimage.rotate(img, avg_rotate_angle)  # 逆时针旋转
        # cv2.imwrite('./test result/1.png', self.rotate_img)
        # cv2.imshow('rotate', rotate_img)
        # cv2.waitKey()

        self.rotate_theta = avg_rotate_angle  # 向量顺时针旋转公式
        self.count_rotate_vector()

    def count_rotate_vector(self):
        v1_new = (self.rotate_vector[0] * np.cos(self.rotate_theta / 180)) - \
                 (self.rotate_vector[1] * np.sin(self.rotate_theta / 180))
        v2_new = (self.rotate_vector[1] * np.cos(self.rotate_theta / 180)) + \
                 (self.rotate_vector[0] * np.sin(self.rotate_theta / 180))
        self.rotate_vector = np.array([v1_new, v2_new])

    def manual_set_rotate_vector(self, rotate_theta):
        self.rotate_theta = rotate_theta
        self.count_rotate_vector()

    def canny_threshold(self, img_path):
        img_original = cv2.imread(img_path)
        #设置窗口
        cv2.namedWindow('Canny')
        #定义回调函数
        def nothing(x):
            pass
        #创建两个滑动条，分别控制threshold1，threshold2
        cv2.createTrackbar('threshold1','Canny',50,400,nothing)
        cv2.createTrackbar('threshold2','Canny',100,400,nothing)
        while(1):
            #返回滑动条所在位置的值
            threshold1=cv2.getTrackbarPos('threshold1','Canny')
            threshold2=cv2.getTrackbarPos('threshold2','Canny')
            #Canny边缘检测
            img_edges=cv2.Canny(img_original,threshold1,threshold2)
            #显示图片
            cv2.imshow('original',img_original)
            cv2.imshow('Canny',img_edges)
            if cv2.waitKey(1)==ord('q'):
                break
        cv2.destroyAllWindows()


if __name__ == '__main__':
    horizontal_correction = HorizontalCorrection()
    # horizontal_correction.canny_threshold(r'./test image/IMG_6386.JPG')
    horizontal_correction.process(r'E:/yarn_twist_new/test_dataset/resized_2022-10-16_19_21_35_815.bmp')
    print(horizontal_correction.rotate_theta)
    cv2.imwrite('E:/yarn_twist_new/test_dataset/.bmp', horizontal_correction.rotate_img)
    cv2.imshow('rotate', horizontal_correction.rotate_img)
    cv2.waitKey()