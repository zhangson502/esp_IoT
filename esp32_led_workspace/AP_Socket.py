import network
import machine
import time
from machine import Timer,Pin
import socket
from oled import *
class AP:
  '''
    ESP8266热点的通讯
  '''
  def __init__(self,ap_Name='servo_Ctrl',passwd='12345678',port=8889):
    '''
    '''
    self.ap_if=network.WLAN(network.AP_IF)   #建立AP网络对象
    self.ap_if.active(True)                     #启动ESP的AP网络
    self.ap_if.config(essid=ap_Name,password='69696969')     #ESP网络配置
    self.ap_if.ifconfig(('192.168.0.1', '255.255.255.0', '192.168.0.1', '8.8.8.8'))    #配置ESP热点的网段和网关
    sock=socket.socket()    #建立一个侦听socket
    sock.settimeout(None)   #设置延时为None，阻塞通讯
    print("AAAAAAA")
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)    #端口复用，防止端口被占用
    sock.bind(('192.168.0.1',port))     #开启端口
    sock.listen(5)                      #开启侦听端口
    self.connected=True
    self.conn=None
    #缓存变量
    self.cmdID=0    #指令
    self.datLen=0   #数据长度
    self.data=[]    #数据缓存
    # LED控制
    self.pp=Pin(2,Pin.OUT)
    self.pp.value(1)
    time.sleep_ms(500)
    self.pp.value(0)
    time.sleep_ms(500)
    self.pp.value(1)
    time.sleep_ms(500)
    self.pp.value(0)
    time.sleep_ms(500)
    self.pp.value(1)
    
    '''
      等待客户端连接
    '''
    while True:
      self.conn,addr=sock.accept()
      self.IO_AP()
      
  def IO_AP(self):
    '''
      基于数据协议的通讯
    '''
    #self.conn.send('Connected!')
    print('Connected!')
    ret=self.conn.recv(3)
    if ret[0]!=0xff: return   #数据头校验
    if ret[2]!=0x00: self.data=self.conn.recv(int(ret[2]))    #接收数据包
    '''
      根据cmdID，对数据进行处理
    '''
    if ret[1]==0x08:
      self.pp.value(self.data[0])
      self.conn.send(self.data)
    self.conn.close()
sock=AP()

















