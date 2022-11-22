import AreaVolume
 
if __name__ == '__main__':
    r = float(input("请输入半径："))
    print("圆的面积：{0:.2f}，球的体积：{1:.2f}".\
          format(AreaVolume.area(r), AreaVolume.volume(r)))
 
