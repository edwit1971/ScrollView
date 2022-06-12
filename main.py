#############################################################
# File Name : main.py
#
# Scrolling App to demonstrate screen scrolling
#
# Created :   May 2022 
#############################################################

from kivymd.app import MDApp

from kivymd.uix.label       import MDLabel
from kivymd.uix.floatlayout import MDFloatLayout

from kivy.clock import Clock

from kivy.core.window import Window

from kivy.effects.scroll import ScrollEffect

from kivy.uix.scrollview     import ScrollView
from kivy.uix.relativelayout import RelativeLayout

from Misc_DrawStuff import DrawStuff


##############################################################
##############################################################

class ScrollViewApp(MDApp):

    def __init__(self, **kwargs):
        ##########################
        super(ScrollViewApp, self).__init__(**kwargs)
        ##########################
        self.Win_To_Draw = MDFloatLayout()
        self.LText       = MDLabel()
        self.Draw_Lines1 = DrawStuff()
        self.ScrView  = ScrollView()      #RecycleView
        self.ScrLayout   = RelativeLayout()  #RecycleLayout
        ##########################
        self.Event_Timer = Clock.create_trigger(callback = self.Callback_Timer, \
                                                timeout = 3.0, \
                                                interval = False)
        return

    def build(self):
        ScrollViewApp.title = 'ScrollViewApp'
        #############################################
        self.Win_To_Draw.size = Window.size
        self.Draw_Lines1.Show_Instructions(self.Win_To_Draw)
        #############################################
        Screen_Width  = self.Win_To_Draw.width
        Screen_Height = self.Win_To_Draw.height
        Xc = int(Screen_Width * 0.5)
        Yc = int(Screen_Height * 0.5)
        # Screen_Xo = Xc - int(Screen_Width * 0.5)
        # Screen_Yo = Yc - int(Screen_Height * 0.5)
        # Screen_Xf = Screen_Xo + Screen_Width
        # Screen_Yf = Screen_Yo + Screen_Height
        #############################################
        ###########  ScrollView #####################
        #############################################
        Scr_Width  = int(Screen_Width * 0.333)
        Scr_Height = int(Screen_Height * 0.5)
        #################
        Scr_Xo = Xc - int(Scr_Width * 0.5)
        Scr_Xf = Scr_Xo + Scr_Width
        #################
        Scr_Yo = Yc - int(Scr_Height * 0.5)
        Scr_Yf = Scr_Yo + Scr_Height
        #############################################
        self.Draw_Lines1.Draw_Fill_Rectangle(pXo = Scr_Xo, \
                                             pXf = Scr_Xf, \
                                             pYo = Scr_Yo, \
                                             pYf = Scr_Yf, \
                                             pR = 0.8, \
                                             pG = 0.8, \
                                             pB = 0.8, \
                                             pW = 2)
        self.Draw_Lines1.Draw_Rectangle(pXo = Scr_Xo, \
                                        pXf = Scr_Xf, \
                                        pYo = Scr_Yo, \
                                        pYf = Scr_Yf, \
                                        pR = 0, \
                                        pG = 0, \
                                        pB = 0, \
                                        pW = 3)
        #############################################
        self.LText.font_style = 'Subtitle2'
        self.LText.font_size  = 14
        self.LText.size_hint  = None, None
        self.LText.width      = Scr_Width
        self.LText.height     = Scr_Height
        self.LText.text_size  = (self.LText.width, None)
        self.LText.x          = 0
        self.LText.y          = 0
        self.LText.halign     = 'left'
        self.LText.valign     = 'bottom'
        self.LText.padding_y  = 5
        self.LText.theme_text_color = 'Custom'
        self.LText.color      = (0, 0, 0, 1)
        self.LText.text  = '  Some Random Things...'
        self.LText.text += '\n  PeanutButter and Jelly Sandwich'
        self.LText.text += '\n  Cuban Cigar'
        self.LText.text += '\n  Fred Flintstone'
        self.LText.text += '\n  Underwater Lost City'
        self.LText.text += '\n  Bang Zoom to the Moon'
        self.LText.text += '\n  Red White and Blue'
        self.LText.text += '\n  Duck Billed Platypus'
        self.LText.text += '\n  Green Eyed Monster'
        self.LText.text += '\n  Isosceles Triangle'
        self.LText.text += '\n  Tuba and Trumbone'
        self.LText.text += '\n  Hey Hey Ralphie Boy'
        self.LText.text += '\n  Buy One Get One Free'
        self.LText.text += '\n  Where No Man Has Gone'
        self.LText.text += '\n  Hole in One'
        self.LText.text += '\n  Here Today Gone Tomorrow'
        self.LText.text += '\n  Loose Lips Sink Ships'
        self.LText.text += '\n  Hairy Potato'
        self.LText.text += '\n  PeanutButter and Jelly Sandwich'
        self.LText.text += '\n  Cuban Cigar'
        self.LText.text += '\n  Fred Flintstone'
        self.LText.text += '\n  Underwater Lost City'
        self.LText.text += '\n  Bang Zoom to the Moon'
        self.LText.text += '\n  Red White and Blue'
        self.LText.text += '\n  Duck Billed Platypus'
        self.LText.text += '\n  Green Eyed Monster'
        self.LText.text += '\n  Isosceles Triangle'
        self.LText.text += '\n  Tuba and Trumbone'
        self.LText.text += '\n  Hey Hey Ralphie Boy'
        self.LText.text += '\n  Buy One Get One Free'
        self.LText.text += '\n  Where No Man Has Gone'
        self.LText.text += '\n  Hole in One'
        self.LText.text += '\n  Here Today Gone Tomorrow'
        self.LText.text += '\n  Loose Lips Sink Ships'
        self.LText.text += '\n  Hairy Potato'
        #############################################
        ###########  ScrollView #####################
        #############################################
        self.ScrView.size_hint   = None, None
        self.ScrView.size        = (Scr_Width, Scr_Height)
        self.ScrView.width       = Scr_Width
        self.ScrView.height      = Scr_Height
        self.ScrView.x           = Scr_Xo
        self.ScrView.y           = Scr_Yo
        self.ScrView.do_scroll_x = False
        self.ScrView.do_scroll_y = True
        self.ScrView.effect_cls  = ScrollEffect
        self.ScrView.scroll_type = ['content']
        #############################################
        self.ScrLayout.size_hint_y = None
        self.ScrLayout.width  = Scr_Width
        #self.ScrLayout.height = Scr_Height
        self.ScrLayout.x      = 0 #Scr_Xo
        self.ScrLayout.y      = 0 #Scr_Yo
        #############################################
        
        if(self.ScrView.parent == None):
            self.Win_To_Draw.add_widget(self.ScrView)
        
        if(self.ScrLayout.parent == None):
            self.ScrView.add_widget(self.ScrLayout)
        
        if(self.LText.parent == None):
            self.ScrLayout.add_widget(self.LText)
        
        #############################################
        self.Event_Timer()
        return self.Win_To_Draw
    
    
    #################################################
    def Callback_Timer(self, dt):
        width  = self.LText.texture_size[0]
        height = self.LText.texture_size[1]
        self.LText.size_hint = (None, None)
        self.LText.width     = width
        self.LText.height    = height
        self.LText.text_size = (width, None)
        self.ScrLayout.height = height + 15
        self.ScrView.scroll_y = 0  # 0 Bottom touches bottom or 1
        return
    

ScrollViewApp().run()

##############################################################
##############################################################