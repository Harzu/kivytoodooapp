from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.animation import Animation, AnimationTransition

Builder.load_file('views/widgets/kv/header.kv')

class Header(FloatLayout):
  
  def input_active(self, elem):
    if elem.pos_hint['center_x'] == 2:
      x = 0.4
    else:
      x = 2
    anim = Animation(pos_hint=({'center_x': x, 'center_y': 0.5}))
    anim.start(elem)