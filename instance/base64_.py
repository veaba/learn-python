import base64
import re
import io 
from PIL import Image
#一段base64图片存储
def deal_inspect_img(base64_str):
    """裁剪base64字符串的图片"""
    base64_data = re.sub('^data:image/.+;base64,', '', base64_str)
    byte_data = base64.b64decode(base64_data)
    # BytesIO 对象
    image_data = io.BytesIO(byte_data)
    # 得到Image对象
    img = Image.open(image_data)
    # 裁剪图片(左，上，右，下)，笛卡尔坐标系
    img2 = img.crop((962, 485, 1897, 810))

    # BytesIO 对象
    imgByteArr = io.BytesIO()
    # 写入BytesIO对象
    img2.save(imgByteArr, format='PNG')
    # 获得字节
    imgByteArr = imgByteArr.getvalue()
    base64_str = base64.b64encode(imgByteArr)
    return base64_str
# 如果需要保存

base64_str = 'xxxxxxxxxxxxxxxxxxxxxxx'
imgdata = base64.b64decode(base64_str)
with open('iss.png', 'wb') as f:
    f.write(imgdata)


# 入参base64，然后裁剪后，出来base64
# cartesian(左、上、右、下、）
def crop_base64_img(base64_str, cartesian):
    if not isinstance(cartesian, tuple):
        raise RuntimeError('cartesian参数错误：格式为(a,b,c,d)')
    base64_data = re.sub('^data:image/.+;base64,', '', base64_str)
    byte_data = base64.b64decode(base64_data)
    # BytesIO 对象
    image_data = io.BytesIO(byte_data)
    # 得到Image对象
    img = Image.open(image_data)
    # 裁剪图片（左、上、右、下、），笛卡尔
    new_img = img.crop(cartesian)
    # BytesIo 对象
    img_byte_array = io.BytesIO()
    new_img.save(img_byte_array, format='PNG')
    # 获得字节
    img_byte_array = img_byte_array.getvalue()
    base64_str = base64.b64encode(img_byte_array)
    return str(base64_str, encoding='utf-8')