import pygame
import random
import sys
import os

# 第一步：实现游戏窗口
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 750
# 初始化分数：
# 初始化操作
pygame.display.init()
# 创建窗口
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# 设置菜单栏上的游戏名称
pygame.display.set_caption('Deer Looks For Master')
# 天蓝色
COLOR_BLUE = pygame.color.Color(135, 206, 250)
# 字体红色
COLOR_PURPLE=pygame.color.Color(220,210,255)
COLOR_RED = pygame.color.Color(220, 20, 60)
# 障碍物颜色
COLOR_GREEN = pygame.color.Color(0, 255, 0)
# 加载图片
bird = pygame.image.load('img/deer.png')
bird=pygame.transform.scale(bird, (250, 250))
# 位置
top = (SCREEN_HEIGHT - 50)/2
bird_rect = bird.get_rect(left=150, top=top)
bird_speed = 1
FILE_NAME = 'File/SCORE.txt'
beijing0 = pygame.image.load('img/background2.jpeg')
beijing1 = pygame.image.load('img/bg7.jpeg')
beijing2 = pygame.image.load('img/background3.jpeg')
beijing3 = pygame.image.load('img/background4.jpeg')
beijing4 = pygame.image.load('img/夜晚.bmp').convert_alpha()
beijing5 = pygame.image.load('img/bg8.jpeg').convert_alpha()
beijing6 = pygame.image.load('img/bg5.jpeg').convert_alpha()
beijing7= pygame.image.load('img/8.jpeg').convert_alpha()
beijing8= pygame.image.load('img/9.jpeg').convert_alpha()
beijing9= pygame.image.load('img/10.jpeg').convert_alpha()
beijing10= pygame.image.load('img/11.jpeg').convert_alpha()
beijing11= pygame.image.load('img/12.jpeg').convert_alpha()
beijing12= pygame.image.load('img/13.jpeg').convert_alpha()
beijing13= pygame.image.load('img/14.jpeg').convert_alpha()
beijing14= pygame.image.load('img/15.jpeg').convert_alpha()
beijing15= pygame.image.load('img/傍晚2.bmp').convert_alpha()
beijing16= pygame.image.load('img/16.jpeg').convert_alpha()
beijing17= pygame.image.load('img/17.jpeg').convert_alpha()
beijing18= pygame.image.load('img/18.jpeg').convert_alpha()
beijing19= pygame.image.load('img/19.jpeg').convert_alpha()
b=pygame.image.load('img/end (2).jpeg').convert_alpha()
b= pygame.transform.scale(b, (1000, 800))
d=pygame.image.load('img/故事2.jpeg').convert_alpha()
d= pygame.transform.scale(d, (1000, 800))
other=pygame.image.load('img/傍晚1.bmp').convert_alpha()
other= pygame.transform.scale(other, (1000, 800))


bg2list=[]
bg_list = [beijing0,beijing1, beijing2, beijing3, beijing4,beijing5,
           beijing6,beijing7,beijing8,beijing9,beijing10,
           beijing11,beijing12,beijing13,beijing14,beijing15,beijing16,beijing17,beijing18,beijing19]
for bg in bg_list:
    bg= pygame.transform.scale(bg, (1000, 800))
    bg2list.append(bg)
# 播放音乐
pygame.mixer.init()
pygame.mixer.music.load("music/Lightscape - Hope.mp3")
pygame.mixer.music.play(2000)
def height_score(FILE_NAME):
    if os.path.exists(FILE_NAME):
        f = open(FILE_NAME, 'r', encoding='utf-8')
        # 最高分从文件中读取
        height_score1 = f.read()
        if len(height_score1) > 0:
            height_score = int(height_score1)
        else:
            f = open(FILE_NAME, 'w', encoding='utf-8')
            height_score = 0
        f.close()
    else:
        f = open(FILE_NAME, 'w', encoding='utf-8')
        height_score = 0
    return height_score
# 开始时间
start_time = 0
is_over = False
# 存储所有柱子的列表
pillar_list = []
is_over = False
score=0

while True:
    pygame.init()
    # 为窗口填充颜色
    #window.blit(other,(0,0))
    # 背景变换
    if score==0:
        window.blit(d,(0,0))
    else:
        window.blit(bg2list[int(score%20)],(0,0))
    # 加载小鸟
    window.blit(bird, bird_rect)
    # 新增事件处理
    event_list = pygame.event.get()
    bird_speed += 0.2
    if not is_over:
        bird_rect = bird_rect.move(0, bird_speed)
    for e in event_list:
        # 退出事件
        if e.type == pygame.QUIT:
            sys.exit()
        # 键盘事件：
        if e.type == pygame.KEYDOWN:
            # 当按下空格时响应
            if e.key == pygame.K_SPACE:
                bird_speed = -6
            if is_over and e.key == pygame.K_SPACE:
                # 小鸟回到初始位置
                bird_rect = bird.get_rect(left=150, top=top)
                # 速度清空
                bird_speed = 1
                # 分数清空
                score = 0
                # 障碍物清空
                pillar_list.clear()
                # is_over 状态改变
                is_over = False
    # 每间隔3秒生成一次障碍物
    # 获取当前的系统时间
    end_time = pygame.time.get_ticks()
    if not is_over:
        if end_time-start_time >= 3500:
            start_time = end_time
            x = 500
            y = 0
            width = 50
            height = random.randint(30, 150)
            pillar_rect_top = pygame.rect.Rect(x, y, width, height)
            pillar_rect_bottom = pygame.rect.Rect(500, height+450, 50, SCREEN_HEIGHT - height + 120)
            pillar_list.append(pillar_rect_top)
            pillar_list.append(pillar_rect_bottom)
            #  得分计算：
            for p in pillar_list:
                if p.x < bird_rect.x and p.y > bird_rect.y:
                    score += 1
            if score > height_score(FILE_NAME):
                score_w = open(FILE_NAME, 'w', encoding='utf-8')
                score_w.write(str(score))
                score_w.close()
            else:
                pass

    else:
        pillar_list.clear()

    # 将所有障碍物加载出来
    for p in pillar_list:
        window.fill(COLOR_PURPLE, p)

    # 障碍物的移动
    for p in pillar_list:
        if p.x > 0:
            p.x -= 1
        else:
            pillar_list.remove(p)

    # 处理小鸟的死亡
    for p in pillar_list:
        if p.colliderect(bird_rect):
            is_over = True
    if bird_rect.y > SCREEN_HEIGHT - bird_rect.height or bird_rect.y < 0:
        is_over = True
    font = pygame.font.SysFont("arial", 30)
    font1 = pygame.font.SysFont("arial", 20)
    fail_text = font.render('GAME OVER !', True, COLOR_RED)
    score_text = font.render(f'SCORE:{score}', True, COLOR_RED)
    score_text1 = font1.render(f'SCORE:{score}', True, COLOR_RED)
    height_text = font1.render(f'HIGH_SCORE: {height_score(FILE_NAME)}', True, COLOR_RED)
    text_width, text_height = 200, 100
    score_width, score_height = 200, 100
    score_text1_width, score_text1_height = 100, 50
    fail_rect = pygame.Rect((SCREEN_WIDTH - text_width) / 2,
                            (SCREEN_HEIGHT - text_height) / 2 - 30,
                            text_width, text_height)
    score_rect = pygame.Rect((SCREEN_WIDTH - text_width) / 2 + 25,
                            (SCREEN_HEIGHT - text_height) / 2,
                            score_width, score_height)
    time_score_rect = pygame.Rect(0, 0, score_text1_width, score_text1_height)
    window.blit(score_text1, time_score_rect)
    window.blit(height_text, (SCREEN_WIDTH / 2, 0))


    if score==100:
        window.blit(d)
        is_over=False


    if is_over:
        # 游戏结束
        window.blit(fail_text, fail_rect)
        window.blit(score_text, score_rect)

        restart = font1.render('Press space to play again', True, COLOR_RED)
        restart_width, restart_height = 200, 100
        restart_rect = pygame.Rect((SCREEN_WIDTH - text_width) / 2 - 20,
                                    (SCREEN_HEIGHT - text_height) / 2 + 50,
                                   restart_width, restart_height)
        window.blit(restart, restart_rect)


    # 让程序每10毫秒执行一次
    pygame.time.wait(10)
    pygame.display.update()

