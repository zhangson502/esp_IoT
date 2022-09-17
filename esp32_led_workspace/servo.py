from machine import Pin,PWM   #导入PWM库
import time

class Servo:
  def __init__(self,port=0,minAngle=-90,maxAngle=90):
    self.port=PWM(Pin(port))
    self.port.freq(50)        #舵机的控制以20ms为周期，所以PWM的频率调整为50Hz
    self.port.duty(0)         #暂时关闭舵机
    self.minAngle=minAngle    #舵机的最小角度
    self.maxAngle=maxAngle    #舵机的最大角度
    
  def Set_Angle(self,angle=0):
    '''
      配置舵机的角度
      舵机的最大角度对应2.5ms脉宽，最小角度对应0.5ms脉宽
      在20ms周期的前提下，对应的PWM占空比分别是12.5%以及2.5%
    '''
    rotate_Percentage=(angle-self.minAngle)/(self.maxAngle-self.minAngle)
    self.port.duty((int)((rotate_Percentage*0.1*1024)+0.025*1024))


