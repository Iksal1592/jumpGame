import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.properties import NumericProperty
from kivy.core.window import Window
from kivy.graphics import Rectangle, Color

kivy.require('2.0.0')


class Dinosaur(Widget):
    velocity = NumericProperty(0)

    def __init__(self, **kwargs): 
        super(Dinosaur, self).__init__(**kwargs)
        self.size = (50, 50)
        self.pos = (100, 0)
        with self.canvas:
            Color(0, 1, 0, 1)  # 초록색
            self.rect = Rectangle(pos=self.pos, size=self.size)

    def jump(self):
        if self.y == 0:  # 바닥에 있을 때만 점프 가능
            self.velocity = 15

    def update(self, dt):
        self.velocity -= 0.5  # 중력 효과
        self.y += self.velocity

        if self.y < 0:
            self.y = 0
            self.velocity = 0

        self.rect.pos = self.pos

    def reset(self):
        self.pos = (100, 0)
        self.velocity = 0


class Obstacle(Widget):
    def __init__(self, **kwargs):
        super(Obstacle, self).__init__(**kwargs)
        self.size = (50, 50)
        self.pos = (Window.width, 0)
        with self.canvas:
            Color(1, 0, 0, 1)  # 빨간색
            self.rect = Rectangle(pos=self.pos, size=self.size)

    def move(self):
        self.x -= 5
        if self.x < -self.width:
            self.x = Window.width

        self.rect.pos = self.pos

    def reset(self):
        self.pos = (Window.width, 0)


class DinoGame(Widget):
    def __init__(self, **kwargs):
        super(DinoGame, self).__init__(**kwargs)
        self.dino = Dinosaur()
        self.add_widget(self.dino)

        self.obstacle = Obstacle()
        self.add_widget(self.obstacle)

        self.game_over_flag = False

        # 키보드 입력 이벤트 리스너 추가
        Window.bind(on_key_down=self.on_key_down)

        Clock.schedule_interval(self.update, 1.0 / 60.0)

    def update(self, dt):
        if not self.game_over_flag:
            self.dino.update(dt)
            self.obstacle.move()

            if self.check_collision(self.dino, self.obstacle):
                self.game_over()

    def check_collision(self, dino, obstacle):
        return dino.collide_widget(obstacle)

    def game_over(self):
        print("Game Over")
        self.game_over_flag = True
        Clock.unschedule(self.update)

    def restart(self):
        self.dino.reset()
        self.obstacle.reset()
        self.game_over_flag = False
        Clock.schedule_interval(self.update, 1.0 / 60.0)
        print("Game Restarted")

    def on_key_down(self, window, key, *args):
        if key == 32:  # 스페이스바 키 코드
            if self.game_over_flag:
                self.restart()
            else:
                self.dino.jump()


class DinoApp(App):
    def build(self):
        game = DinoGame()
        return game


if __name__ == '__main__':
    DinoApp().run()
