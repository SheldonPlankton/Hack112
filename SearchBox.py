import wx

class MainWindow(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,'Window', size = (300,200))
        panel = wx.Panel(self)

        box= wx.TextEntryDialog(None,'Enter Name or Subject','Search',
                                     'Search Here')
        if box.ShowModal() == wx.ID_OK:
            answer = box.GetValue()

        self.quote = wx.StaticText(panel, label= answer, pos=(20, 30))
        self.Show()

app = wx.PySimpleApp()
fame=MainWindow(parent=None,id=-1)
fame.Show()
app.MainLoop()
