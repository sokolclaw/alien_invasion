class Settings():

    def __init__(self):

        '''Параметры экрана игры'''
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = ((230, 230, 230))

        '''Параметры корабля'''
        self.ship_speed = 1.5
        self.ship_limit = 3

        '''Параметры выстрелов'''
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        '''Параметры инопланетян'''
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # 1 вправо, -1 влево
        self.fleet_direction = 1

        self.speedup_scale = 1.1
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        '''Инициализация настроек, изменяющих ход игры'''
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3.0
        self.alien_speed_factor = 1.0
        # 1 вправо, -1 влево
        self.fleet_direction = 1

        self.alien_points = 25

    def increase_speed(self):
        '''Увеличивает настройки скорости'''
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)