# -*- coding: utf-8 -*-
'''
Created on 2016.06.30
@author: zw
Description : 计算器
'''

import wx
class Form(wx.Frame):
    def __init__( self, parent, id, title ):
        wx.Frame.__init__(self,parent,id,title,wx.DefaultPosition,wx.Size(300, 250))
        self.formula = False
        menuBar = wx.MenuBar()
        mnuFile = wx.Menu()
        mnuFile.Append( 22, '&Quit', 'Exit Calculator' )
        menuBar.Append( mnuFile, '&File' )
        wx.EVT_MENU( self, 22, self.OnClose )
        self.SetMenuBar( menuBar )

        self.display = wx.TextCtrl(self, -1, '', style=wx.TE_RIGHT)
        gs = wx.GridSizer(5, 4, 3, 3)
        gs.AddMany(
            [
                (wx.Button(self, 12, '-'), 0, wx.EXPAND),
                (wx.Button(self, 20, 'Cls'), 0, wx.EXPAND),
                (wx.Button(self, 21, 'Bck'), 0, wx.EXPAND),
                (wx.StaticText(self, -1, ''), 0, wx.EXPAND),
                (wx.Button(self, 22, 'Close'), 0, wx.EXPAND),
                (wx.Button(self, 1, '7'), 0, wx.EXPAND),
                (wx.Button(self, 2, '8'), 0, wx.EXPAND),
                (wx.Button(self, 3, '9'), 0, wx.EXPAND),
                (wx.Button(self, 4, '/'), 0, wx.EXPAND),
                (wx.Button(self, 5, '4'), 0, wx.EXPAND),
                (wx.Button(self, 6, '5'), 0, wx.EXPAND),
                (wx.Button(self, 7, '6'), 0, wx.EXPAND),
                (wx.Button(self, 8, '*'), 0, wx.EXPAND),
                (wx.Button(self, 10, '2'), 0, wx.EXPAND),
                (wx.Button(self, 11, '3'), 0, wx.EXPAND),
                (wx.Button(self, 9, '1'), 0, wx.EXPAND),
                (wx.Button(self, 16, '+'), 0, wx.EXPAND),
                (wx.Button(self, 15, '='), 0, wx.EXPAND),
                (wx.Button(self, 14, '.'), 0, wx.EXPAND),
                (wx.Button(self, 13, '0'), 0, wx.EXPAND)
            ]
        )
        sizer = wx.BoxSizer( wx.VERTICAL )
        sizer.Add(self.display, 0, wx.EXPAND|wx.TOP|wx.BOTTOM, 4)
        sizer.Add(gs, 1, wx.EXPAND)
        self.SetSizer(sizer)
        self.Centre()

        wx.EVT_BUTTON(self, 20, self.OnClear)
        wx.EVT_BUTTON(self, 21, self.OnBackspace)
        wx.EVT_BUTTON(self, 22, self.OnClose)
        wx.EVT_BUTTON(self, 1, self.OnNumber)
        wx.EVT_BUTTON(self, 2, self.OnNumber)
        wx.EVT_BUTTON(self, 3, self.OnNumber)
        wx.EVT_BUTTON(self, 4, self.OnFormula)
        wx.EVT_BUTTON(self, 5, self.OnNumber)
        wx.EVT_BUTTON(self, 6, self.OnNumber)
        wx.EVT_BUTTON(self, 7, self.OnNumber)
        wx.EVT_BUTTON(self, 8, self.OnFormula)
        wx.EVT_BUTTON(self, 9, self.OnNumber)
        wx.EVT_BUTTON(self, 10, self.OnNumber)
        wx.EVT_BUTTON(self, 11, self.OnNumber)
        wx.EVT_BUTTON(self, 12, self.OnFormula)
        wx.EVT_BUTTON(self, 13, self.OnNumber)
        wx.EVT_BUTTON(self, 14, self.OnFormula)
        wx.EVT_BUTTON(self, 15, self.OnEqual)
        wx.EVT_BUTTON(self, 16, self.OnFormula)

    def OnClear(self, event):
        self.display.Clear()
    def OnBackspace(self, event):
        formula = self.display.GetValue()
        self.display.Clear()
        self.display.SetValue(formula[:-1])
    def OnClose(self, event):
        self.Close()
    def OnEqual(self,event):
        if self.formula:
            return
        formula = self.display.GetValue()
        self.formula = True
        try:
            self.display.Clear()
            output = eval(formula)
            self.display.AppendText(str(output))
        except StandardError:
            self.display.AppendText("Error")

    def OnFormula(self,event):
        if self.formula:
            return
        self.display.AppendText(event.EventObject.LabelText)

    def OnNumber(self,event):
        if self.formula:
            self.display.Clear()
            self.formula=False
        self.display.AppendText(event.EventObject.LabelText)

class MyApp(wx.App):
    def OnInit(self):
        frame = Form(None, -1, "Phoenix Caculator")
        frame.Show(True)
        self.SetTopWindow(frame)
        return True

app = MyApp(0)
app.MainLoop()