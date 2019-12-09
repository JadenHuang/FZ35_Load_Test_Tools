# -*- coding: utf-8 -*-
import wx
import subprocess
import thread  
from six import with_metaclass
from FZ35_Load_Test_Tools.wx_GUI import MyFrame1


if __name__ == '__main__':
  ex = wx.App() 
  WX_GUI = MyFrame1(None) 
  ex.MainLoop()


