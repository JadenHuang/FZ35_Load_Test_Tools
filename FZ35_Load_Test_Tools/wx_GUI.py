# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import os
import time
import datetime
import subprocess
import re
import thread 
from wx.lib.masked import numctrl
import serial
import sys
import serial.tools.list_ports  

wx.ID_Choice = 1000
wx.ID_but1 = 1001
wx.ID_but2 = 1002
wx.ID_but3 = 1003
wx.ID_edit = 1004

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"FZ35_Load_Test_Tools v0.01", pos = wx.DefaultPosition, size = wx.Size( 380,580 ), style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER ^ wx.MAXIMIZE_BOX )
		COM_List = []
		msg=" "
		self.loop_refresh =False
		self.com_success = False
		port_list = list(serial.tools.list_ports.comports())
		if len(port_list) <= 0:
			msg = "The Serial port can't find!"
		else:
			for i in range(len(port_list)):
				COM_List.append(list(port_list[i])[0])
			msg = str(COM_List)

		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )
		
		gbSizer2 = wx.GridBagSizer( 0, 0 )
		gbSizer2.SetFlexibleDirection( wx.BOTH )
		gbSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		m_choice1Choices = COM_List
		self.m_choice1 = wx.Choice( self, wx.ID_Choice, wx.DefaultPosition, wx.Size( 130,-1 ), m_choice1Choices, 0 )
		self.m_choice1.SetSelection( 0 )
		gbSizer2.Add( self.m_choice1, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"选择端口", wx.DefaultPosition, wx.Size( 95,-1 ), wx.ALIGN_CENTRE )
		self.m_staticText2.Wrap( -1 )
		self.m_staticText2.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		self.m_staticText2.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOTEXT ) )
		
		gbSizer2.Add( self.m_staticText2, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"x.xxA", wx.DefaultPosition, wx.Size( 95,-1 ), wx.ALIGN_LEFT )
		self.m_staticText3.Wrap( -1 )
		self.m_staticText3.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		self.m_staticText3.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOTEXT ) )
		
		gbSizer2.Add( self.m_staticText3, wx.GBPosition( 4, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"LVP:xx.x", wx.DefaultPosition, wx.Size( 95,-1 ), wx.ALIGN_LEFT )
		self.m_staticText4.Wrap( -1 )
		self.m_staticText4.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		self.m_staticText4.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOTEXT ) )
		
		gbSizer2.Add( self.m_staticText4, wx.GBPosition( 5, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"OVP:xx.x", wx.DefaultPosition, wx.Size( 95,-1 ), wx.ALIGN_LEFT )
		self.m_staticText5.Wrap( -1 )
		self.m_staticText5.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		self.m_staticText5.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOTEXT ) )
		
		gbSizer2.Add( self.m_staticText5, wx.GBPosition( 6, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"OCPx.xx", wx.DefaultPosition, wx.Size( 95,-1 ), wx.ALIGN_LEFT )
		self.m_staticText6.Wrap( -1 )
		self.m_staticText6.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		self.m_staticText6.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOTEXT ) )
		
		gbSizer2.Add( self.m_staticText6, wx.GBPosition( 7, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"OPP:xx.xx", wx.DefaultPosition, wx.Size( 95,-1 ), wx.ALIGN_LEFT )
		self.m_staticText8.Wrap( -1 )
		self.m_staticText8.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		self.m_staticText8.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOTEXT ) )
		
		gbSizer2.Add( self.m_staticText8, wx.GBPosition( 8, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"OAH:x.xxxx", wx.DefaultPosition, wx.Size( 95,-1 ), wx.ALIGN_LEFT )
		self.m_staticText9.Wrap( -1 )
		self.m_staticText9.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		self.m_staticText9.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOTEXT ) )
		
		gbSizer2.Add( self.m_staticText9, wx.GBPosition( 9, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"OHP:xx.xx", wx.DefaultPosition, wx.Size( 95,-1 ), wx.ALIGN_LEFT )
		self.m_staticText10.Wrap( -1 )
		self.m_staticText10.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		self.m_staticText10.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOTEXT ) )
		
		gbSizer2.Add( self.m_staticText10, wx.GBPosition( 10, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"\n输出显示：", wx.Point( -1,-1 ), wx.Size( 95,100 ), wx.ALIGN_CENTRE )
		self.m_staticText1.Wrap( -1 )
		self.m_staticText1.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		self.m_staticText1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOTEXT ) )
		
		gbSizer2.Add( self.m_staticText1, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_button1 = wx.Button( self, wx.ID_but1, u"刷新显示", wx.DefaultPosition, wx.Size( 95,50 ), 0 )
		gbSizer2.Add( self.m_button1, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_button12 = wx.Button( self, wx.ID_but1, u"读取产品\n参数设置", wx.DefaultPosition, wx.Size( 95,50 ), 0 )
		gbSizer2.Add( self.m_button12, wx.GBPosition( 2, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer2.Add( self.m_textCtrl2, wx.GBPosition( 4, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer2.Add( self.m_textCtrl1, wx.GBPosition( 7, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_textCtrl5 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer2.Add( self.m_textCtrl5, wx.GBPosition( 8, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_textCtrl6 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer2.Add( self.m_textCtrl6, wx.GBPosition( 9, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_textCtrl7 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer2.Add( self.m_textCtrl7, wx.GBPosition( 10, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_textCtrl3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer2.Add( self.m_textCtrl3, wx.GBPosition( 5, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_textCtrl4 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer2.Add( self.m_textCtrl4, wx.GBPosition( 6, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_button2 = wx.Button( self, wx.ID_but2, u"开启负载", wx.DefaultPosition, wx.Size( 95,50 ), 0 )
		gbSizer2.Add( self.m_button2, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_button7 = wx.Button( self, wx.ID_ANY, u"设置负载电流", wx.DefaultPosition, wx.Size( 95,-1 ), 0 )
		gbSizer2.Add( self.m_button7, wx.GBPosition( 4, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_button4 = wx.Button( self, wx.ID_ANY, u"设置欠压", wx.DefaultPosition, wx.Size( 95,-1 ), 0 )
		gbSizer2.Add( self.m_button4, wx.GBPosition( 5, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_button5 = wx.Button( self, wx.ID_ANY, u"设置过压", wx.DefaultPosition, wx.Size( 95,-1 ), 0 )
		gbSizer2.Add( self.m_button5, wx.GBPosition( 6, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_button8 = wx.Button( self, wx.ID_ANY, u"设置过流", wx.DefaultPosition, wx.Size( 95,-1 ), 0 )
		gbSizer2.Add( self.m_button8, wx.GBPosition( 7, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_button9 = wx.Button( self, wx.ID_ANY, u"设置功率", wx.DefaultPosition, wx.Size( 95,-1 ), 0 )
		gbSizer2.Add( self.m_button9, wx.GBPosition( 8, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_button10 = wx.Button( self, wx.ID_ANY, u"设置最大容量", wx.DefaultPosition, wx.Size( 95,-1 ), 0 )
		gbSizer2.Add( self.m_button10, wx.GBPosition( 9, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_button11 = wx.Button( self, wx.ID_ANY, u"设置放电时间", wx.DefaultPosition, wx.Size( 95,-1 ), 0 )
		gbSizer2.Add( self.m_button11, wx.GBPosition( 10, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_button6 = wx.Button( self, wx.ID_but3, u"关闭负载", wx.DefaultPosition, wx.Size( 95,50 ), 0 )
		gbSizer2.Add( self.m_button6, wx.GBPosition( 3, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_edit, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,100 ), 0 )
		self.m_staticText1.Wrap( -1 )
		self.m_staticText1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOTEXT ) )
		self.m_staticText1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )
		
		gbSizer2.Add( self.m_staticText1, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 5 ), wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( gbSizer2 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_choice1.Bind( wx.EVT_CHOICE, self.ComChoice )
		self.m_button1.Bind( wx.EVT_BUTTON, self.RefreshDisplay )
		self.m_button12.Bind( wx.EVT_BUTTON, self.ReadSetClick )
		self.m_button2.Bind( wx.EVT_BUTTON, self.StartClick )
		self.m_button7.Bind( wx.EVT_BUTTON, self.SetCurrentChick )
		self.m_button4.Bind( wx.EVT_BUTTON, self.SetUndervoltageChick )
		self.m_button5.Bind( wx.EVT_BUTTON, self.SetOvervoltageChick )
		self.m_button8.Bind( wx.EVT_BUTTON, self.SetOvercurrentChick )
		self.m_button9.Bind( wx.EVT_BUTTON, self.SetPowerChick )
		self.m_button10.Bind( wx.EVT_BUTTON, self.Set_MaximumCapacityChick )
		self.m_button11.Bind( wx.EVT_BUTTON, self.Set_Discharge_TimeChick )
		self.m_button6.Bind( wx.EVT_BUTTON, self.StopClick )
		self.Show(True)

	
	# Virtual event handlers, overide them in your derived class
	def RefreshDisplay( self, event ):
		if self.com_success == True:
			flag = True
			self.ser.write('start')
			while flag == True:
				readvalue = self.ser.readline()
				if readvalue[:4] == "fail":
					self.m_staticText1.SetLabel(u"刷新读数失败")
					flag = False
				elif readvalue[:6] == "sucess":
					readvalue1 = self.ser.readline()
					readvalue2 = self.ser.readline()
					self.m_staticText1.SetLabel(u"刷新读数："+"\n"+readvalue2)
					flag = False


				self.ser.write('stop')
		else:
			self.m_staticText1.SetLabel(u"请正确打开COM口")

	def ReadSetClick( self, event ):
		if self.com_success == True:
			self.ser.write('read')
			readvalue = self.ser.readline()
			if readvalue[:4] == "fail":
				self.m_staticText1.SetLabel(u"读取当前读数失败")
				flag = False
			else:
				self.m_staticText1.SetLabel(u"参数："+"\n"+readvalue[:30]+"\n"+readvalue[30:])
				flag = False
		else:
			self.m_staticText1.SetLabel(u"请正确打开COM口")

	def StartClick( self, event ):
		if self.com_success == True:
			flag = True
			self.ser.write('on')
			while flag == True:
				readvalue = self.ser.readline()
				if readvalue[:4] == "fail":
					self.m_staticText1.SetLabel(u"启动负载失败")
					flag = False
				elif readvalue[:6] == "sucess":
					self.m_staticText1.SetLabel(u"成功启动负载")
					flag = False
		else:
			self.m_staticText1.SetLabel(u"请正确打开COM口")

	def StopClick( self, event ):
		if self.com_success == True:
			flag = True
			self.ser.write('off')
			while flag == True:
				readvalue = self.ser.readline()
				if readvalue[:4] == "fail":
					self.m_staticText1.SetLabel(u"关闭负载失败")
					flag = False
				elif readvalue[:6] == "sucess":
					self.m_staticText1.SetLabel(u"成功关闭负载")
					flag = False
		else:
			self.m_staticText1.SetLabel(u"请正确打开COM口")

	def SetCurrentChick( self,event):
		if self.com_success == True:
			flag = True
			setcurrent = self.m_textCtrl2.GetValue()
			if setcurrent.strip() != '':
				receiver = self.ser.write(setcurrent.encode())
				while flag == True:
					readvalue = self.ser.readline()
					if readvalue[:4] == "fail":
						self.m_staticText1.SetLabel(u"电流设置失败")
						flag = False
					elif readvalue[:6] == "sucess":
						self.m_staticText1.SetLabel(u"成功设置电流")
						flag = False
			else:
				self.m_staticText1.SetLabel(u"请输入数值!!!")

		else:
			self.m_staticText1.SetLabel(u"请正确打开COM口")


	def SetUndervoltageChick( self, event ):
		if self.com_success == True:
			flag = True
			setcurrent = self.m_textCtrl3.GetValue()
			if setcurrent.strip() != '':
				self.ser.write(setcurrent.encode())
				while flag == True:
					readvalue = self.ser.readline()
					if readvalue[:4] == "fail":
						self.m_staticText1.SetLabel(u"欠压设置失败")
						flag = False
					elif readvalue[:6] == "sucess":
						self.m_staticText1.SetLabel(u"成功设置欠压")
						flag = False
			else:
				self.m_staticText1.SetLabel(u"请输入数值!!!")
		else:
			self.m_staticText1.SetLabel(u"请正确打开COM口")

	def SetOvervoltageChick( self, event ):
		if self.com_success == True:
			flag = True
			setcurrent = self.m_textCtrl4.GetValue()
			if setcurrent.strip() != '':
				self.ser.write(setcurrent.encode())
				while flag == True:
					readvalue = self.ser.readline()
					if readvalue[:4] == "fail":
						self.m_staticText1.SetLabel(u"过压设置失败")
						flag = False
					elif readvalue[:6] == "sucess":
						self.m_staticText1.SetLabel(u"成功设置过压")
						flag = False
			else:
				self.m_staticText1.SetLabel(u"请输入数值!!!")
		else:
			self.m_staticText1.SetLabel(u"请正确打开COM口")

	def SetOvercurrentChick( self, event ):
		if self.com_success == True:
			flag = True
			setcurrent = self.m_textCtrl1.GetValue()
			if setcurrent.strip() != '':
				self.ser.write(setcurrent.encode())
				while flag == True:
					readvalue = self.ser.readline()
					if readvalue[:4] == "fail":
						self.m_staticText1.SetLabel(u"过流设置失败")
						flag = False
					elif readvalue[:6] == "sucess":
						self.m_staticText1.SetLabel(u"成功设置过流")
						flag = False
			else:
				self.m_staticText1.SetLabel(u"请输入数值!!!")

		else:
			self.m_staticText1.SetLabel(u"请正确打开COM口")

	def SetPowerChick( self, event ):
		if self.com_success == True:
			flag = True
			setcurrent = self.m_textCtrl5.GetValue()
			if setcurrent.strip() != '':
				self.ser.write(setcurrent.encode())
				while flag == True:
					readvalue = self.ser.readline()
					if readvalue[:4] == "fail":
						self.m_staticText1.SetLabel(u"功率设置失败")
						flag = False
					elif readvalue[:6] == "sucess":
						self.m_staticText1.SetLabel(u"成功设置功率")
						flag = False
			else:
				self.m_staticText1.SetLabel(u"请输入数值!!!")
		else:
			self.m_staticText1.SetLabel(u"请正确打开COM口")


	def Set_MaximumCapacityChick( self, event ):
		if self.com_success == True:
			flag = True
			setcurrent = self.m_textCtrl6.GetValue()
			if setcurrent.strip() != '':
				self.ser.write(setcurrent.encode())
				while flag == True:
					readvalue = self.ser.readline()
					if readvalue[:4] == "fail":
						self.m_staticText1.SetLabel(u"最大容量设置失败")
						flag = False
					elif readvalue[:6] == "sucess":
						self.m_staticText1.SetLabel(u"成功设置最大容量")
						flag = False
			else:
				self.m_staticText1.SetLabel(u"请输入数值!!!")

		else:
			self.m_staticText1.SetLabel(u"请正确打开COM口")


	def Set_Discharge_TimeChick( self, event ):
		if self.com_success == True:
			flag = True
			setcurrent = self.m_textCtrl7.GetValue()
			if setcurrent.strip() != '':
				self.ser.write(setcurrent.encode())
				while flag == True:
					readvalue = self.ser.readline()
					if readvalue[:4] == "fail":
						self.m_staticText1.SetLabel(u"最大时间设置失败")
						flag = False
					elif readvalue[:6] == "sucess":
						self.m_staticText1.SetLabel(u"成功设置最大时间")
						flag = False
			else:
				self.m_staticText1.SetLabel(u"请输入数值!!!")
		else:
			self.m_staticText1.SetLabel(u"请正确打开COM口")

	def ComChoice( self, event ):
		port_serial = self.m_choice1.GetString(self.m_choice1.GetSelection())
		try:
			self.ser = serial.Serial(port_serial,9600,timeout = 60)
			self.m_staticText1.SetLabel(u"成功打开端口："+port_serial)
			self.com_success = True


		except:
			self.m_staticText1.SetLabel(u"打开端口失败！")