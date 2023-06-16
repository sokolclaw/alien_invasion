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