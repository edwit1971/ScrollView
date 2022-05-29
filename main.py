#############################################################
# File Name : main.py
#
# Scrolling App to demonstrate screen scrolling
#
# Created :   May 2022 
#############################################################

from kivymd.app import MDApp

from kivymd.uix.label import MDLabel
from kivymd.uix.floatlayout import MDFloatLayout

from kivy.core.window import Window

from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.floatlayout    import FloatLayout
from kivy.uix.scrollview     import ScrollView

from Misc_DrawStuff import DrawStuff


##############################################################
##############################################################

class ScrollViewApp(MDApp):

    def __init__(self, **kwargs):
        ##########################
        super(ScrollViewApp, self).__init__(**kwargs)
        ##########################
        self.Win_To_Draw = MDFloatLayout()
        self.Label1      = MDLabel()
        self.Draw_Lines1 = DrawStuff()
        self.Draw_Lines2 = DrawStuff()
        self.ScrViewWin  = ScrollView()
        self.Scrolling   = RelativeLayout()
        ##########################
        return

    def build(self):
        ScrollViewApp.title = 'ScrollViewApp'
        #############################################
        self.Win_To_Draw.size = Window.size
        #############################################
        self.Draw_Lines1.Show_Instructions(self.Win_To_Draw)
        self.Draw_Lines2.Show_Instructions(self.Scrolling)
        self.Draw_Lines2.Clear_IG()
        #############################################
        Screen_Width  = self.Win_To_Draw.width
        Screen_Height = self.Win_To_Draw.height
        Xc = int(Screen_Width * 0.5)
        Yc = int(Screen_Height * 0.5)
        Screen_Xo = Xc - int(Screen_Width * 0.5)
        Screen_Yo = Yc - int(Screen_Height * 0.5)
        Screen_Xf = Screen_Xo + Screen_Width
        Screen_Yf = Screen_Yo + Screen_Height
        #############################################
        ###########  ScrollView #####################
        #############################################
        self.Scr_Width  = int(Screen_Width * 0.3333)
        self.Scr_Height = int(Screen_Height * 0.75)
        #################
        self.Scr_Xo   = Xc - int(self.Scr_Width * 0.5)
        self.Scr_Xf   = self.Scr_Xo + self.Scr_Width
        #################
        self.Scr_Yo = Yc - int(self.Scr_Height * 0.5)
        self.Scr_Yf = self.Scr_Yo + self.Scr_Height
        #############################################
        self.Draw_Lines1.Draw_Fill_Rectangle(pXo = self.Scr_Xo, \
                                             pXf = self.Scr_Xf, \
                                             pYo = self.Scr_Yo, \
                                             pYf = self.Scr_Yf, \
                                             pR = 0.8, \
                                             pG = 0.8, \
                                             pB = 0.8, \
                                             pW = 2)
        self.Draw_Lines1.Draw_Rectangle(pXo = self.Scr_Xo, \
                                        pXf = self.Scr_Xf, \
                                        pYo = self.Scr_Yo, \
                                        pYf = self.Scr_Yf, \
                                        pR = 0, \
                                        pG = 0, \
                                        pB = 0, \
                                        pW = 3)
        #############################################
        ###########  ScrollView #####################
        #############################################
        self.Scrolling.width     = self.Scr_Width
        self.Scrolling.height    = self.Scr_Height * 2.0
        self.Scrolling.size_hint = (1, None)
        #self.Scrolling.size_hint = (1, 1)
        self.ScrViewWin.do_scroll_x = False
        self.ScrViewWin.do_scroll_y = True
        self.ScrViewWin.scroll_type = ['content']
        self.ScrViewWin.width       = self.Scr_Width
        self.ScrViewWin.height      = self.Scr_Height
        self.ScrViewWin.x           = self.Scr_Xo
        self.ScrViewWin.y           = self.Scr_Yo
        #############################################
        y_bottom = 5
        y_top = self.ScrViewWin.height - 5
        y_incr = int((y_top - y_bottom) / 4)
        y = y_bottom
        for i in range(5):
            # Relative Coordinates
            self.Draw_Lines2.Draw_Line(pX1 = 10, \
                                       pY1 = y, \
                                       pX2 = self.Scr_Width - 10, \
                                       pY2 = y, \
                                       pR  = 0.4, \
                                       pG  = 0, \
                                       pB  = 0, \
                                       pW  = 4)
            y = y + y_incr
        #############################################
        self.Label1.font_style = 'Subtitle2'
        self.Label1.font_size  = 18
        self.Label1.size_hint  = (None, None)
        self.Label1.width      = int(self.Win_To_Draw.width / 4)
        self.Label1.height     = int(self.Win_To_Draw.height / 30)
        self.Label1.text_size  = (self.Label1.width, self.Label1.height)
        self.Label1.x          = 0
        self.Label1.y          = 0
        self.Label1.halign     = 'left'
        self.Label1.valign     = 'bottom'
        self.Label1.color      = (0, 0, 0, 1)
        self.Label1.text       = 'Testing...'
        if(self.Label1.parent == None):
            self.Scrolling.add_widget(self.Label1)
        #############################################
        if(self.Scrolling.parent == None):
            self.ScrViewWin.add_widget(self.Scrolling)
        if(self.ScrViewWin.parent == None):
            self.Win_To_Draw.add_widget(self.ScrViewWin)
        #############################################
        self.ScrViewWin.scroll_y = 1  # 0 Bottom touches bottom or 1
        #############################################
        return self.Win_To_Draw

ScrollViewApp().run()

##############################################################
##############################################################