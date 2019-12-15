import pygame
from pygame import *
import random
import leveldata
from leveldata import *

#Global Variables - includes customer user events and songs list information
SCREEN_SIZE = pygame.Rect((0, 0, 1200, 800))
TILE_SIZE = 64 
GRAVITY = pygame.Vector2((0, 0.3))
_songs = ["Media\\Music\\DownUnder.mp3","Media\\Music\\HorseNoName.mp3",
          "Media\\Music\\dreaming.mp3","Media\\Music\\Rain.mp3","Media\\Music\\Buffalo.mp3"]
_currently_playing_song = None
LEVEL = pygame.USEREVENT + 2
RETURNLEVEL = pygame.USEREVENT + 5

#effect_lev0intro = pygame.mixer.Sound('')
#effect_lev1intro = pygame.mixer.Sound('')
#effect_lev2intro = pygame.mixer.Sound('')
#effect_lev3intro = pygame.mixer.Sound('')

#randomly picks next song from list to play during game
def play_a_different_song():
    global _currently_playing_song, _songs
    next_song = random.choice(_songs)
    while next_song == _currently_playing_song:
        next_song = random.choice(_songs)
    _currently_playing_song = next_song
    pygame.mixer.music.load(next_song)
    pygame.mixer.music.play()

#Screen Draw and Camera Logic
class CameraAwareLayeredUpdates(pygame.sprite.LayeredUpdates):
    def __init__(self, target, world_size):
        super().__init__()
        self.target = target
        self.cam = pygame.Vector2(0, 0)
        self.world_size = world_size
        if self.target:
            self.add(target)

    def update(self, *args):
        super().update(*args)
        if self.target:
            x = -self.target.rect.center[0] + SCREEN_SIZE.width/2
            y = -self.target.rect.center[1] + SCREEN_SIZE.height/2
            self.cam += (pygame.Vector2((x, y)) - self.cam) * 0.05
            self.cam.x = max(-(self.world_size.width-SCREEN_SIZE.width), min(0, self.cam.x))
            self.cam.y = max(-(self.world_size.height-SCREEN_SIZE.height), min(0, self.cam.y))

    def draw(self, surface):
        spritedict = self.spritedict
        surface_blit = surface.blit
        dirty = self.lostsprites
        self.lostsprites = []
        dirty_append = dirty.append
        init_rect = self._init_rect
        for spr in self.sprites():
            rec = spritedict[spr]
            newrect = surface_blit(spr.image, spr.rect.move(self.cam))
            if rec is init_rect:
                dirty_append(newrect)
            else:
                if newrect.colliderect(rec):
                    dirty_append(newrect.union(rec))
                else:
                    dirty_append(newrect)
                    dirty_append(rec)
            spritedict[spr] = newrect
        return dirty            

def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE.size)
    background = pygame.image.load("Media\\Graphics\\background.png").convert()
    background = pygame.transform.scale(background, (1200,800))
    screen.blit(background, [0, 0])
    pygame.display.set_caption("Santa's Dungeon Escape")
    timer = pygame.time.Clock()
    
    effect_start = pygame.mixer.Sound("Media\\Sounds\\effect_start.wav")
    effect_start_reverse = pygame.mixer.Sound("Media\\Sounds\\effect_start_reverse.wav")
    effect_walk = pygame.mixer.Sound("Media\\Sounds\\effect_walk.wav")
    effect_run = pygame.mixer.Sound("Media\\Sounds\\effect_run.wav")
    effect_jump = pygame.mixer.Sound("Media\\Sounds\\effect_jump.wav")
    effect_levelload = pygame.mixer.Sound("Media\\Sounds\\effect_level.wav")
    effect_collide = pygame.mixer.Sound("Media\\Sounds\\effect_collide.wav")
    
    SONG_END = pygame.USEREVENT + 1
    pygame.mixer.music.set_endevent(SONG_END)
    pygame.mixer.music.load(_songs[0])
    pygame.mixer.music.play()
    
    free_channel = pygame.mixer.find_channel()

    levelcounter = 0 
    level = levels[levelcounter]
    
    platforms = pygame.sprite.Group()
    player = Player(platforms, (TILE_SIZE, TILE_SIZE))
    level_width  = len(level[0])*TILE_SIZE
    level_height = len(level)*TILE_SIZE
    entities = CameraAwareLayeredUpdates(player, pygame.Rect(0, 0, level_width, level_height))

    # build the level
    x = y = 0
    for row in levels[levelcounter]:
        for col in row:
            if col == "P":
                Platform((x, y), platforms, entities)
            if col == "S":
                SnowPlatform((x, y), platforms, entities)                
            if col == "W":
                Walls((x, y), platforms, entities)
            if col == "E":
                ExitBlock((x, y), platforms, entities)
            if col == "L":
                LevelBlock((x, y), platforms, entities)
            x += TILE_SIZE
        y += TILE_SIZE
        x = 0
    
    effect_start.set_volume(5)
    free_channel.play(effect_start)
    
    while 1:

        for e in pygame.event.get():
            if e.type == QUIT: 
                pygame.quit()
            if e.type == KEYDOWN and e.key == K_ESCAPE:
                pygame.quit()
            if e.type == SONG_END:
                play_a_different_song()
            if e.type == LEVEL:
                effect_levelload.set_volume(5)
                free_channel.play(effect_levelload)
                levelcounter += 1
                screen.fill((0, 0, 0))
                timer = pygame.time.Clock()
                platforms = pygame.sprite.Group()
                player = Player(platforms, (72, 1400))
                level_width  = len(level[0])*TILE_SIZE
                level_height = len(level)*TILE_SIZE
                entities = CameraAwareLayeredUpdates(player, pygame.Rect(0, 0, level_width, level_height))
                x = y = 0
                for row in levels[levelcounter]:
                    for col in row:
                        if col == "P":
                            Platform((x, y), platforms, entities)
                        if col == "S":
                            SnowPlatform((x, y), platforms, entities)                            
                        if col == "E":
                            ExitBlock((x, y), platforms, entities)
                        if col == "L":
                            LevelBlock((x, y), platforms, entities)
                        if col == "W":
                            Walls((x, y), platforms, entities)
                        if col == "R":
                            ReturnBlock((x, y), platforms, entities)                            
                        x += TILE_SIZE
                    y += TILE_SIZE
                    x = 0
                free_channel.play(effect_start)                
            if e.type == RETURNLEVEL:
                levelcounter -= 1
                screen.fill((0, 0, 0))
                timer = pygame.time.Clock()
                platforms = pygame.sprite.Group()
                player = Player(platforms, (2696, 1400))
                level_width  = len(level[0])*TILE_SIZE
                level_height = len(level)*TILE_SIZE
                entities = CameraAwareLayeredUpdates(player, pygame.Rect(0, 0, level_width, level_height))
                x = y = 0
                for row in levels[levelcounter]:
                    for col in row:
                        if col == "P":
                            Platform((x, y), platforms, entities)
                        if col == "S":
                            SnowPlatform((x, y), platforms, entities)                                            
                        if col == "E":
                            ExitBlock((x, y), platforms, entities)
                        if col == "L":
                            LevelBlock((x, y), platforms, entities)
                        if col == "W":
                            Walls((x, y), platforms, entities)
                        if col == "R":
                            ReturnBlock((x, y), platforms, entities)
                        x += TILE_SIZE
                    y += TILE_SIZE
                    x = 0
                effect_start_reverse.set_volume(5)   
                free_channel.play(effect_start_reverse)

        entities.update()

        screen.blit(background, [0, 0])
        entities.draw(screen)
        pygame.display.update()
        timer.tick(60)
        
class Entity(pygame.sprite.Sprite):
    def __init__(self, color, pos, *groups):
        super().__init__(*groups)
        self.image = Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=pos)

class Player(Entity):
    def __init__(self, platforms, pos, *groups):
        super().__init__(Color("#0000FF"), pos)     
        self.vel = pygame.Vector2((0, 0))
        self.onGround = False
        self.platforms = platforms
        self.speed = 10
        self.jump_strength = 15
        self.image.convert()
        self.image= pygame.image.load("Media\\Graphics\\SANTA.jpg").convert()
        self.image = pygame.transform.scale(self.image, (TILE_SIZE, TILE_SIZE))

    def update(self):
        pressed = pygame.key.get_pressed()
        
        up = pressed[K_w]
        up1 = pressed[K_SPACE]
        up2 = pressed[K_UP]
        
        left = pressed[K_a]
        left1 = pressed[K_LEFT]
        
        right = pressed[K_d]
        right1 = pressed[K_RIGHT]
        
        running = pressed[K_RSHIFT]

        if up or up1 or up2:
            # only jump if on the ground
            if self.onGround: self.vel.y = -self.jump_strength
        if left or left1:
            self.image = pygame.image.load("Media\\Graphics\\SANTAFLIP.JPG")
            self.image = pygame.transform.scale(self.image,(TILE_SIZE, TILE_SIZE))            
            self.vel.x = -self.speed
        if right or right1:
            self.image = pygame.image.load("Media\\Graphics\\SANTA.JPG")
            self.image = pygame.transform.scale(self.image,(TILE_SIZE, TILE_SIZE))            
            self.vel.x = self.speed
        if running:
            self.vel.x *= 1.5
        if not self.onGround:
            # only accelerate with gravity if in the air
            self.vel += GRAVITY
            # max falling speed
            if self.vel.y > 100: self.vel.y = 100
        print(self.vel.y)
        if not(left or left1 or right or right1):
            self.vel.x = 0
        # increment in x direction
        self.rect.left += self.vel.x
        # do x-axis collisions
        self.collide(self.vel.x, 0, self.platforms)
        # increment in y direction
        self.rect.top += self.vel.y
        # assuming we're in the air
        self.onGround = False;
        # do y-axis collisions
        self.collide(0, self.vel.y, self.platforms)

    def collide(self, xvel, yvel, platforms):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):
                if isinstance(p, ExitBlock):
                    pygame.event.post(pygame.event.Event(QUIT))
                if isinstance(p, LevelBlock):
                    pygame.event.post(pygame.event.Event(LEVEL))
                if isinstance(p, ReturnBlock):
                    pygame.event.post(pygame.event.Event(RETURNLEVEL))                    
                if xvel > 0:
                    self.rect.right = p.rect.left                    
                if xvel < 0:
                    self.rect.left = p.rect.right
                if yvel > 0:
                    self.rect.bottom = p.rect.top
                    self.onGround = True
                    self.yvel = 0
                if yvel < 0:
                    self.rect.top = p.rect.bottom

class Platform(Entity):
    def __init__(self, pos, *groups):
        super().__init__(Color("#DDDDDD"), pos, *groups)
        self.image.convert()
        self.image = pygame.image.load("Media\\Graphics\\ground.png").convert()
        self.image = pygame.transform.scale(self.image, (TILE_SIZE, TILE_SIZE))

class SnowPlatform(Entity):
    def __init__(self, pos, *groups):
        super().__init__(Color("#DDDDDD"), pos, *groups)
        self.image.convert()
        self.image = pygame.image.load("Media\\Graphics\\SnowPlat.jpg").convert()
        self.image = pygame.transform.scale(self.image, (TILE_SIZE, TILE_SIZE))        

class Walls(Entity):
    def __init__(self, pos, *groups):
        super().__init__(Color("#DDDDDD"), pos, *groups)
        self.image.convert()
        self.image = pygame.image.load("Media\\Graphics\\walls.png").convert()
        self.image = pygame.transform.scale(self.image, (TILE_SIZE, TILE_SIZE))

class ExitBlock(Entity):
    def __init__(self, pos, *groups):
        super().__init__(Color("#0033FF"), pos, *groups)

class LevelBlock(Entity):
    def __init__(self, pos, *groups):
        super().__init__(Color('Black'), pos, *groups)

class ReturnBlock(Entity):
    def __init__(self, pos, *groups):
        super().__init__(Color('Black'), pos, *groups)        

if __name__ == "__main__":
    main()