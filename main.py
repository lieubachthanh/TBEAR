from kivy.core.text import LabelBase
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivy.uix.carousel import Carousel
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.clock import Clock
from kivymd.uix.dialog import MDDialog
from firebase import firebase
from kivyauth.google_auth import initialize_google, login_google, logout_google
Window.size = (414 , 896)
global user_id
user_id = ""
database = firebase.FirebaseApplication("https://webtb-3c6e6-default-rtdb.firebaseio.com/", None)
# database = firebase.FirebaseApplication("https://tbear-3369a-default-rtdb.asia-southeast1.firebasedatabase.app/", None)
client_id = r"795266604144-prvj93fau851boqpj9o21kn2lunnov2q.apps.googleusercontent.com"
client_secret = r"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"


class LoginScreen(Screen):
    def login(self, email, password):
        app = MDApp.get_running_app()
        flag = True
        result = database.get("user", '')
        for i in result.keys():
            if str(result[i]['email']) == str(email):
                if str(result[i]['password']) == str(password):
                    global user_id
                    user_id = result[i]
                    print(user_id)
                    flag = False
                    app.root.current = "home"
                    app.root.transition.direction = "left"
                    # return user_id
                    
        if flag:
            dialog = MDDialog(text='Tài khoản hoặc mật khẩu không đúng')
            dialog.open()

class SignUpScreen(Screen):
    def sign_up(self, email, user_name, password, rePass):
        app = MDApp.get_running_app()
        if email != ""  and user_name != "" and password != "" and rePass != "":
            if password == rePass:
                User = {
                    'email': email,
                    'name': user_name,
                    'role' : 'user',
                    'password': password
                }
                database.post('https://webtb-3c6e6-default-rtdb.firebaseio.com/user', User)
                
                app.root.current = "home"
                app.root.transition.direction = "left"
            else:
                dialog = MDDialog(text='Mật khẩu không trùng khớp')
                dialog.open()
        else:
            dialog = MDDialog(text='Nhập đầy đủ thông tin')
            dialog.open()


class video_2(Screen):
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


class Chup(Screen):
    class ChupCarousel(Carousel):  
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
class Nhac(Screen):
    class NhacCarousel(Carousel):  
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

class account(Screen):
    def save_change(self):
        pass

class IntroScreen(Screen):
    pass

class Tbear(MDApp):

    def build(self):
        global screen_manager 
        initialize_google(client_id, client_secret)
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file(r"KV\pre-splash.kv"))
        screen_manager.add_widget(Builder.load_file(r"KV\login.kv"))
        screen_manager.add_widget(Builder.load_file(r"KV\signup.kv"))
        screen_manager.add_widget(Builder.load_file(r"KV\forget-password.kv"))
        screen_manager.add_widget(Builder.load_file(r"KV\home.kv"))
        screen_manager.add_widget(Builder.load_file(r"KV\project.kv"))
        screen_manager.add_widget(Builder.load_file(r"KV\Phim.kv"))
        screen_manager.add_widget(Builder.load_file(r"KV\Video_v2.kv"))
        screen_manager.add_widget(Builder.load_file(r"KV\Chup.kv"))
        screen_manager.add_widget(Builder.load_file(r"KV\Nhac.kv"))
        screen_manager.add_widget(Builder.load_file(r"KV\payment.kv"))
        screen_manager.add_widget(Builder.load_file(r"KV\profile.kv"))
        screen_manager.add_widget(Builder.load_file(r"KV\account.kv"))
        screen_manager.add_widget(Builder.load_file(r"KV\intro.kv"))
        screen_manager.add_widget(Builder.load_file(r"KV\order.kv"))
        
        
        return screen_manager

    def loginGoogle(self):
        login_google()

    def on_start(self):
        Clock.schedule_once(self.login, 4)
    
    def login(self, *args):
        screen_manager.current = "login"

if __name__ == "__main__":
    
    Tbear().run()
    