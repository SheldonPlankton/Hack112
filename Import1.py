#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 15-112: Fundamentals of Comp-Sci
# Template by Evan Tipping
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Name: Evan Tipping
# Andrew ID: eftippin
# Recitation: H

# Hack112 Gui Portion
# Created 10/28/2018

# Version 0.1
# Updated 11/9/2018
# No updates to report!


# Planned features / updates:
#   o Create a working UI

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Imports:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import json
import textwrap
import wx


imps = set(sys.modules) & set(globals())

                #==========================================#
            #~~~~~~~~~~~~]        Versions        [~~~~~~~~~~~~#
                #==========================================#

# Top level header code that prints out each imported module along with
#available methods and version number (if available).

for mod in imps:
    print()
    try:
        print("Running " + sys.modules[mod].__name__ +
               " version: " + sys.modules[mod].__version__)

    except:
        print("No version found for " + sys.modules[mod].__name__ + "!")

    finally:
        print("Available methods:")
        for line in textwrap.wrap(str(dir(sys.modules[mod]))):
            print("\t\t" + str(line))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Body:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

                #==========================================#
            #~~~~~~~~~~~~]         Helpers         [~~~~~~~~~~~~#
                #==========================================#

                #==========================================#
            #~~~~~~~~~~~~]        Subheader        [~~~~~~~~~~~~#
                #==========================================#

                #==========================================#
            #~~~~~~~~~~~~]        Functions        [~~~~~~~~~~~~#
                #==========================================#

class Applet(wx.Frame):

    def __init__(self, *args, **kw):
        super(Applet, self).__init__(*args, **kw)

        self.InitUI()

    def InitUI(self):

        wx.StaticText(self, label='x:', pos=(10,10))
        wx.StaticText(self, label='y:', pos=(10,30))

        self.st1 = wx.StaticText(self, label='', pos=(30, 10))
        self.st2 = wx.StaticText(self, label='', pos=(30, 30))

        self.Bind(wx.EVT_MOVE, self.OnMove)

        self.SetSize((350, 250))
        self.SetTitle('Move event')
        self.Centre()

    def OnMove(self, e):

        x, y = e.GetPosition()
        self.st1.SetLabel(str(x))
        self.st2.SetLabel(str(y))

def main():

    app = wx.App()
    ex = Applet(None)
    ex.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()
