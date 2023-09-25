from kivy.core.text import LabelBase
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivy.uix.carousel import Carousel
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.clock import Clock
# from kivymd.uix.boxlayout import MDFloatLayout
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelOneLine, MDExpansionPanelThreeLine, MDExpansionPanelTwoLine

Window.size = (414 , 896)

class LoginScreen(Screen):
    pass

class SignUpScreen(Screen):
    pass

class video(Screen):
    class VideoCarousel(Carousel):  
        def load_service(self, index):
            self.load_slide(self.slides[index])

        def go_to_first_slide(self):
            self.load_slide(self.slides[0])

        def on_touch_move(self,touch): 
            touch.scroll_timeout = 0

        def previous(self):
            if self.index == 0:
                app = MDApp.get_running_app() 
                app.root.current = "home"
                app.root.transition.direction = "right"
            else:
                self.load_previous()

class Phim(Screen):
    class PhimCarousel(Carousel):  
        def load_service(self, index):
            self.load_slide(self.slides[index])

        def go_to_first_slide(self):
            self.load_slide(self.slides[0])

        def on_touch_move(self,touch): 
            touch.scroll_timeout = 0

        def previous(self):
            if self.index == 0:
                app = MDApp.get_running_app() 
                app.root.current = "home"
                app.root.transition.direction = "right"
            else:
                self.load_previous()

class HomeScreen(Screen):
    pass


class ForgetPassword(Screen):
    class MyCarousel(Carousel):    
        def go_to_first_slide(self):
            self.load_slide(self.slides[0])

        def on_touch_move(self,touch): 
            touch.scroll_timeout = 0

        def previous(self):
            if self.index == 0:
                app = MDApp.get_running_app() 
                app.root.current = "login"
                app.root.transition.direction = "right"
            else:
                self.load_previous()

class project(Screen):
    pass

class payment(Screen):
    pass

class profile(Screen):
    pass

class order(Screen):
    class MyCarousel(Carousel):    
        def go_to_first_slide(self):
            self.load_slide(self.slides[0])

        def on_touch_move(self,touch): 
            touch.scroll_timeout = 0

        def previous(self):
            if self.index == 0:
                app = MDApp.get_running_app() 
                app.root.current = "home"
                app.root.transition.direction = "right"
            else:
                self.load_previous()


class Tbear(MDApp):

    def build(self):
        global screen_manager
        screen_manager = ScreenManager()
        # screen_manager.add_widget(Builder.load_file("pre-splash.kv"))
        screen_manager.add_widget(Builder.load_file("KV\login.kv"))
        screen_manager.add_widget(Builder.load_file("KV\signup.kv"))
        screen_manager.add_widget(Builder.load_file(r"KV\forget-password.kv"))
        screen_manager.add_widget(Builder.load_file("KV\home.kv"))
        screen_manager.add_widget(Builder.load_file("KV\project.kv"))
        screen_manager.add_widget(Builder.load_file("KV\Phim.kv"))
        screen_manager.add_widget(Builder.load_file("KV\Video.kv"))
        screen_manager.add_widget(Builder.load_file("KV\payment.kv"))
        screen_manager.add_widget(Builder.load_file("KV\profile.kv"))
        screen_manager.add_widget(Builder.load_file("KV\order.kv"))
        return screen_manager
    
    # def on_start(self):
    #     Clock.schedule_once(self.login, 4)
    
    # def login(self, *args):
    #     screen_manager.current = "login"

if __name__ == "__main__":
    Tbear().run()
    