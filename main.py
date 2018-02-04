import kivy
kivy.require('1.9.0')
from kivy.app import App

from kivy.config import Config
Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '640')
Config.set('graphics', 'resizable', 0)

from kivy.uix.screenmanager import ScreenManagerException
from kivy.core.text import LabelBase
from views.screenmanager import sm, screens
from kivymd.theming import ThemeManager

from settings import FONTS

class TooDoo(App):
  title = 'TooDoo app'
  screen_manager = None
  target_screen = 'none'
  theme_cls = ThemeManager()
  theme_cls.devide_color = 'red'
  def init_app(self):
    self.screen_manager = sm
    self.switch_screen('base')
    for font in FONTS:
      LabelBase.register(**font)
  
  def switch_screen(self, screen_name):
    if screen_name in screens.keys():
      if self.target_screen == screen_name:
        return
      screen = screens[screen_name](name=screen_name)
      self.screen_manager.switch_to(screen)
      self.target_screen = screen_name
      return
    else:
      raise ScreenManagerException('Screen {} not found'.format(screen_name))

  
  def build(self):
    self.init_app()
    return self.screen_manager

if __name__ == '__main__':
  TooDoo().run()