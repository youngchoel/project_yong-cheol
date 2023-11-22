import random
import pygame
from datetime import datetime, timedelta

pygame.init()
bullets = []
spawn_bullet_time = pygame.time.get_ticks()
spawn_bullet_interval = 1000  # Set a shorter interval for continuous bullets

# 폰트 설정
font = pygame.font.Font(None, 36)

# 디스플레이에 시간 띄우는 함수
def display_time(elapsed_time):
    elapsed_time_str = str(timedelta(seconds=elapsed_time))
    time_text = font.render(elapsed_time_str, True, (255, 255, 255)) 
    screen.blit(time_text, (10, 10))  

# 화면의 크기
screen_width = 480  # 가로 크기
screen_height = 640  # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))  # 이게 화면 크기다 하하하

# FPS
clock = pygame.time.Clock()

# 배경 이미지
background = pygame.image.load(r'C:\Users\chosun\Desktop\dodge-the-bullets-main\background.png')

# 솔져 스프라이트
sol = pygame.image.load(r"C:\Users\chosun\Desktop\dodge-the-bullets-main\sol.png")
sol_size = sol.get_rect().size
sol_width = sol_size[0]
sol_height = sol_size[0]
sol_x_pos = (screen_width / 2) - (sol_width / 2)
sol_y_pos = screen_height - sol_height

# 솔져의 속도
to_x = 0
sol_speed = 10

# 총알 미사일 대포 난몰라
bullet_image = pygame.image.load(r"C:\Users\chosun\Desktop\dodge-the-bullets-main\bullet.png")
bullet_size = bullet_image.get_rect().size
bullet_width = bullet_size[0]
bullet_height = bullet_size[1]
bullet_speed = 5

# 스코어 정의
score = 0
score_time = pygame.time.get_ticks()
score_interval = 10000  # 10000밀리초마다 점수 상승 구간 

# 타임 정의 
start_time = pygame.time.get_ticks()  # 게임시작 할때 초기 시간값 
spawn_bullet_time = start_time  # 시간 측정을 위한 변수
# 메인문 
running = True
while running:
    dt = clock.tick(60)  # 게임 화면의 초당 프레임 수
    current_time = pygame.time.get_ticks()
    elapsed_time = (current_time - start_time) // 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT: #창이 닫히는 이벤트가 발생하였는가? 
            running = False #창이 닫힌다 = 게임도 진행이 멈춘다.

        if event.type == pygame.KEYDOWN: #키를 눌렀을때
            if event.key == pygame.K_LEFT: #왼쪽을 누르면 왼쪽으로
                to_x -= sol_speed
            elif event.key == pygame.K_RIGHT: #오른쪽을 누르면 오른쪽으로
                to_x += sol_speed

        if event.type == pygame.KEYUP: #아무것도 누르지 않으면 안가는 코드 !!
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

    sol_x_pos += to_x

    if sol_x_pos < 0:
        sol_x_pos = 0
    elif sol_x_pos > screen_width - sol_width:
        sol_x_pos = screen_width - sol_width

    sol_rect = sol.get_rect()
    sol_rect.left = sol_x_pos
    sol_rect.top = sol_y_pos

    # 시간마다 생성되는 총알 
    if current_time - spawn_bullet_time >= spawn_bullet_interval:
        spawn_bullet_time = current_time
        if spawn_bullet_time % 30000 == 0:
            bullet_speed += 1
            print(f"Bullet speed increased to {bullet_speed}")

        # 새로운 총알 
        new_bullet = {
            'x_pos': random.randint(0, screen_width - bullet_width),
            'y_pos': 0,
            'speed': bullet_speed
        }
        bullets.append(new_bullet)

    # 기존총알 업그레이드 
    for bullet in bullets:
        bullet['y_pos'] += bullet['speed']

        # 결과값
        if sol_rect.colliderect(pygame.Rect(bullet['x_pos'], bullet['y_pos'], bullet_width, bullet_height)):
            print("군필자가 아니시군요.")
            elapsed_time = (pygame.time.get_ticks() - start_time) // 1000  # Calculate elapsed time in seconds
            print(f"{elapsed_time}초 동안 게임 했습니다.")
            print(f"{score}점 나왔습니다")
            running = False

    # 삭제 구문 
    bullets = [bullet for bullet in bullets if bullet['y_pos'] <= screen_height]

    #10초가 지날때마다 추가되는 스코어 
    if current_time - score_time >= score_interval:
        score_time = current_time
        score += 1
        print(f"Score increased to {score}")

    screen.blit(background, (0, 0))
    screen.blit(sol, (sol_x_pos, sol_y_pos))

    # 총알 여러개 소환 
    for bullet in bullets:
        screen.blit(bullet_image, (bullet['x_pos'], bullet['y_pos']))

    # 스코어 추가하는 구문 
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (screen_width - 150, 10))

    display_time(elapsed_time)

    pygame.display.update()

pygame.quit()
