# 能够具体定位到某个dom上的截图

from selenium import webdriver
from PIL import Image
import time
import math

def go(off_h=200):
    driver=webdriver.Chrome()
    driver.get('https://tensorflow.google.cn/api_docs/python/tf')
    body=driver.find_element_by_css_selector('.devsite-article-body')
    # width= body.size['width'] # 854
    # height=body.size['height'] # 11755
    labels=body.find_elements_by_css_selector('p')

    def js(h):
            return ''+'window.scroll(0,'+str(h-off_h)+')'+''
    # todo 这里假设一个p 只有一个svg
    for item in labels:
        svgs =item.find_elements_by_css_selector('svg')
        for svg in svgs:
            print('svg:',svg.location)          # svg: {'x': 715, 'y': 7267}
            left=svg.location['x']
            scroll_y =svg.location['y']
            top=off_h
            # 具体滚动： window.scroll(0,6967)
            driver.execute_script(js(scroll_y))
            # 重新定位取图区域
            right=left+math.floor(svg.size['width'])
            bottom=top+math.floor(svg.size['height'])
            time.sleep(1)
            driver.save_screenshot('temp.png')
            im= Image.open('temp.png')
            # (all_width,all_height)= im.size # 获取需要裁剪图片的尺寸
            im=im.crop((left,top,right,bottom))
            im.save('new.png')

go()

# 爬取的区域
# 拿到宽高,拿到location

