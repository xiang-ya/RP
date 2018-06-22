from selenium import webdriver
import win32com.client as comclt
import win32gui
from PIL import ImageOps
import pytesseract

from selenium.webdriver import ActionChains
import os
from PIL import Image, ImageEnhance
from django.shortcuts import render

import time

from cr.models import Student
from searchings.models import SpecificClass


def index(request):
    return render(request, 'CR/../core/templates/core/homepage.html')


def registed(request, student_id):
    student = Student.objects.get(pk=student_id)
    register_class_list = student.class_info.all()
    context = {
        'student': student,
        'register_class_list': register_class_list,
        'name': student.last_name + student.first_name,
    }
    return render(request, 'CR/registed.html', context)


def register(request, student_id):
    all_class_list = SpecificClass.objects.all()
    student = Student.objects.get(pk=student_id)
    context= {
        'all_class_list': all_class_list,
        'student': student,
    }
    return render(request, 'CR/register.html', context)


def login(url, username, password):
    # get the path of the chrome driver
    chromedriver = 'C:\\Users\\david\\AppData\\Local' \
                   '\\Programs\\Python\\Python36-32\\ChromeDriver.exe'
    # configure the web driver
    driver = webdriver.Chrome(chromedriver)

    actionChains = ActionChains(driver)

    # open the web page and input the url
    driver.get(url)

    # input the username, password and the safecode, choosing the identify button
    user = driver.find_element_by_id("txtUserName")
    user.send_keys(username)

    pw = driver.find_element_by_id("Textbox1")
    pw.send_keys("")

    pw = driver.find_element_by_id("TextBox2")
    pw.send_keys(password)

    try :
        os.remove("C:\\Users\\david\\Downloads\\CheckCode.png")
    except:
        pass

    sc = driver.find_element_by_id("txtSecretCode")
    wsh = comclt.Dispatch("WScript.Shell")
    actionChains.move_to_element(sc).context_click().perform()
    wsh.SendKeys("{DOWN}{DOWN}")
    wsh.SendKeys("{ENTER}")
    time.sleep(0.5)
    hwnd = win32gui.FindWindow(None, 'Save As')
    win32gui.SetForegroundWindow(hwnd)
    wsh.SendKeys("{ENTER}")
    time.sleep(0.5)
    checkcode = "checkcode.aspx"
    base = os.path.splitext(checkcode)[0]
    os.rename(checkcode, base + "png")
    sc.send_keys("")


    id = driver.find_element_by_id("RadioButtonList1_2")
    id.click()

    # # submit the form and login in to the class registration system
    # login = driver.find_element_by_id("Button1")
    # login.click()


def cleanImage():
    filePath = "C:\\Users\\david\\Downloads\\CheckCode.gif"
    base = os.path.splitext(filePath)[0]
    os.rename(filePath, base + ".png")

    imagePath = "C:\\Users\\david\\Downloads\\CheckCode.png"
    image = Image.open(imagePath)
    imgry = image.convert('L')  # 转化为灰度图

    table = get_bin_table()
    print(table)
    out = imgry.point(table, '1')
    print(out)
    # image = Image.open(imagePath)
    #
    # image = image.point(lambda x: 0 if x < 143 else 255)
    # print(image.size[0])

    # borderImage = ImageOps.expand(image, border=20, fill='white')

    out.save(imagePath)


def get_bin_table(threshold=140):
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)

    return table

# def getCheckCode(imagePath):
#
#     cleanImage(imagePath)
#
#     p = subprocess.Popen(["tesseract",
#                           "C:\\Users\\david\\Desktop\\RP\\CR\\checkcode.png",
#                           "checkcode"],
#                          stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     p.wait()
#     f = open("checkcode.txt", "r")
#
#     # Clean any whitespace characters
#     checkcodeResponse = f.read().replace(" ", "").replace("\n", "")
#
#     print("Captcha solution attempt: " + checkcodeResponse)
#     if len(checkcodeResponse) == 4:
#         return checkcodeResponse
#     else:
#         return False


def sum_9_region(img, x, y):
    """
    9邻域框,以当前点为中心的田字框,黑点个数
    :param x:
    :param y:
    :return:
    """
    # todo 判断图片的长宽度下限
    cur_pixel = img.getpixel((x, y))  # 当前像素点的值
    width = img.width
    height = img.height

    if cur_pixel == 1:  # 如果当前点为白色区域,则不统计邻域值
        return 0

    if y == 0:  # 第一行
        if x == 0:  # 左上顶点,4邻域
            # 中心点旁边3个点
            sum = cur_pixel \
                  + img.getpixel((x, y + 1)) \
                  + img.getpixel((x + 1, y)) \
                  + img.getpixel((x + 1, y + 1))
            return 4 - sum
        elif x == width - 1:  # 右上顶点
            sum = cur_pixel \
                  + img.getpixel((x, y + 1)) \
                  + img.getpixel((x - 1, y)) \
                  + img.getpixel((x - 1, y + 1))

            return 4 - sum
        else:  # 最上非顶点,6邻域
            sum = img.getpixel((x - 1, y)) \
                  + img.getpixel((x - 1, y + 1)) \
                  + cur_pixel \
                  + img.getpixel((x, y + 1)) \
                  + img.getpixel((x + 1, y)) \
                  + img.getpixel((x + 1, y + 1))
            return 6 - sum
    elif y == height - 1:  # 最下面一行
        if x == 0:  # 左下顶点
            # 中心点旁边3个点
            sum = cur_pixel \
                  + img.getpixel((x + 1, y)) \
                  + img.getpixel((x + 1, y - 1)) \
                  + img.getpixel((x, y - 1))
            return 4 - sum
        elif x == width - 1:  # 右下顶点
            sum = cur_pixel \
                  + img.getpixel((x, y - 1)) \
                  + img.getpixel((x - 1, y)) \
                  + img.getpixel((x - 1, y - 1))

            return 4 - sum
        else:  # 最下非顶点,6邻域
            sum = cur_pixel \
                  + img.getpixel((x - 1, y)) \
                  + img.getpixel((x + 1, y)) \
                  + img.getpixel((x, y - 1)) \
                  + img.getpixel((x - 1, y - 1)) \
                  + img.getpixel((x + 1, y - 1))
            return 6 - sum
    else:  # y不在边界
        if x == 0:  # 左边非顶点
            sum = img.getpixel((x, y - 1)) \
                  + cur_pixel \
                  + img.getpixel((x, y + 1)) \
                  + img.getpixel((x + 1, y - 1)) \
                  + img.getpixel((x + 1, y)) \
                  + img.getpixel((x + 1, y + 1))

            return 6 - sum
        elif x == width - 1:  # 右边非顶点
            # print('%s,%s' % (x, y))
            sum = img.getpixel((x, y - 1)) \
                  + cur_pixel \
                  + img.getpixel((x, y + 1)) \
                  + img.getpixel((x - 1, y - 1)) \
                  + img.getpixel((x - 1, y)) \
                  + img.getpixel((x - 1, y + 1))

            return 6 - sum
        else:  # 具备9领域条件的
            sum = img.getpixel((x - 1, y - 1)) \
                  + img.getpixel((x - 1, y)) \
                  + img.getpixel((x - 1, y + 1)) \
                  + img.getpixel((x, y - 1)) \
                  + cur_pixel \
                  + img.getpixel((x, y + 1)) \
                  + img.getpixel((x + 1, y - 1)) \
                  + img.getpixel((x + 1, y)) \
                  + img.getpixel((x + 1, y + 1))
            return 9 - sum
# def window_enum_handler(hwnd, resultList):
#     if win32gui.IsWindowVisible(hwnd) and win32gui.GetWindowText(hwnd) != '':
#         resultList.append((hwnd, win32gui.GetWindowText(hwnd)))
#
# def get_app_list(handles=[]):
#     mlst=[]
#     win32gui.EnumWindows(window_enum_handler, handles)
#     for handle in handles:
#         mlst.append(handle)
#     return mlst
#
# appwindows = get_app_list()
#
# for i in appwindows:
#     print(i)

# login("http://202.116.160.170/default2.aspx", "201727010310", "hlidsg123")
# cleanImage()
#
#
# def initTable(threshold=140):
#     table = []
#     for i in range(256):
#         if i < threshold:
#             table.append(0)
#         else:
#             table.append(1)
#     return table
#
# pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'
# imagePath = "C:\\Users\\david\\Downloads\\CheckCode.png"
# im = Image.open(imagePath)
# im = im.convert('L')
# ffasd = pytesseract.image_to_string(im)
# print(ffasd)
# binaryImage = im.point(initTable(), '1')
# im1 = binaryImage.convert('L')
# im2 = ImageOps.invert(im1)
# im3 = im2.convert('1')
# im4 = im3.convert('L')
# fasd = pytesseract.image_to_string(im4)
# print(fasd)
# box = (30,10,90,28)
# region = im4.crop(box)
#
# out = region.resize((120,38))
# asd = pytesseract.image_to_string(out)
#
# print(asd)
