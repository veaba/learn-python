# python 没有switch case  语法

true_map = {
        '0x09': True,
        '0x0A': True,
        '0x0B': True,
        '0x0C': True,
        '0x0D': True,
        '0x0E': True,
        '0x20': True,
        '0xA0': True,
        '0x1680': True,
        '0x202F': True,
        '0x205F': True,
        '0x3000': True,
    }


x =true_map.get('0x205F1')
print (x)