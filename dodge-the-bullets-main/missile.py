import random
import pygame
from datetime import datetime, timedelta

pygame.init()
bullets = []
A_images = [] 
B_images = []
spawn_bullet_time = pygame.time.get_ticks()
spawn_bullet_interval = 3000
korean='C:/Users/chosun/Desktop/dodge-the-bullets-main/korean.ttf'
# 폰트 설정
font = pygame.font.Font(korean, 30)

# 디스플레이에 시간 띄우는 함수
def display_time(elapsed_time):
    elapsed_time_str = str(timedelta(seconds=elapsed_time))
    time_text = font.render(elapsed_time_str, True, (255, 255, 255)) 
    screen.blit(time_text, (10, 10))  

# 화면의 크기
screen_width = 960  # 가로 크기
screen_height = 556  # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))  # 이게 화면 크기다

# FPS
clock = pygame.time.Clock()

# 배경 이미지
background = pygame.image.load(r'C:\Users\chosun\Desktop\dodge-the-bullets-main\background.png')
# 엔딩 이미지 
ending_image = pygame.image.load(r'C:\Users\chosun\Desktop\dodge-the-bullets-main\졸업.png')
#배드엔딩 이미지
bad_ending_image=pygame.image.load(r'C:\Users\chosun\Desktop\dodge-the-bullets-main\학사경고.png')

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
# F 학점
bullet_image = pygame.image.load(r"C:\Users\chosun\Desktop\dodge-the-bullets-main\bullet.png")
bullet_size = bullet_image.get_rect().size
bullet_width = bullet_size[0]
bullet_height = bullet_size[1]
bullet_speed = 2
#A학점 
A_image = pygame.image.load(r"C:\Users\chosun\Desktop\dodge-the-bullets-main\A.png")
A_size = A_image.get_rect().size
A_width = A_size[0]
A_height = A_size[1]
A_speed = 3

#B학점
B_image = pygame.image.load(r"C:\Users\chosun\Desktop\dodge-the-bullets-main\B.png")
B_size = B_image.get_rect().size
B_width = B_size[0]
B_height = B_size[1]
B_speed = 4
# 스코어 정의
score = 0
score_time = pygame.time.get_ticks()
score_interval = 10000  # 10000밀리초마다 점수 상승 구간 
# 타임 정의 
start_time = pygame.time.get_ticks()  # 게임시작 할때 초기 시간값 
spawn_bullet_time = start_time  # 시간 측정을 위한 변수
spawn_A_time = start_time
A_interval = 15000
spawn_B_time = start_time
B_interval = 12500
# 메인문 
running = True
ending_display_time = 10000  # 엔딩 이미지를 표시할 시간 (5초로 설정, 단위: 밀리초)
ending_start_time = 0

while running:
    dt = clock.tick(60)  # 게임 화면의 초당 프레임 수
    current_time = pygame.time.get_ticks()
    elapsed_time = (current_time - start_time) // 1000
    #움직이는 이벤트 
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
    # A 이미지 떨어뜨리기
    # 시간마다 생성되는 A
    if current_time - spawn_A_time >= A_interval:
        spawn_A_time = current_time
    # 새로운 A 이미지
        new_A = {
            'x_pos': random.randint(0, screen_width - A_width),
            'y_pos': 0,
            'speed': A_speed
        }
        A_images.append(new_A)
    # 시간마다 생성되는 B
    if current_time - spawn_B_time >= B_interval:
        spawn_B_time = current_time
    # 새로운 B 이미지
        new_B = {
            'x_pos': random.randint(0, screen_width - B_width),
            'y_pos': 0,
            'speed': B_speed
        }
        B_images.append(new_B)

    # 시간마다 생성되는 총알 
    if current_time - spawn_bullet_time >= spawn_bullet_interval:
        spawn_bullet_time = current_time
        bullet_speed += 0.2
        

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
            print("F 이미지를 획득하였습니다!")
            score -= 5.0
            print(f"현재 스코어: {score}")
            bullets.remove(bullet)
    # 기존 A 이미지 업그레이드        
    for A in A_images:
        A['y_pos'] += A['speed']
        if sol_rect.colliderect(pygame.Rect(A['x_pos'], A['y_pos'], A_width, A_height)):
            print("A 이미지를 획득하였습니다!")
            score += 4.5
            print(f"현재 스코어: {score}")
            
            A_images.remove(A)
    # 기존 B 이미지 업그레이드         
    for B in B_images:
        B['y_pos'] += B['speed']
        if sol_rect.colliderect(pygame.Rect(B['x_pos'], B['y_pos'], B_width, B_height)):
            print("B 이미지를 획득하였습니다!")
            score += 3.5
            print(f"현재 스코어: {score}")
            B_images.remove(B)        
            
    sol_x_pos += to_x    
    #화면 밖으로 못나가는 학생
    if sol_x_pos < 0:
        sol_x_pos = 0
    elif sol_x_pos > screen_width - sol_width:
        sol_x_pos = screen_width - sol_width

    sol_rect = sol.get_rect()
    sol_rect.left = sol_x_pos
    sol_rect.top = sol_y_pos
        
    # 삭제 구문 
    bullets = [bullet for bullet in bullets if bullet['y_pos'] <= screen_height]
   
    # A삭제 구문 
    A_images = [A for A in A_images if A['y_pos'] <= screen_height]
    # B삭제 구문 
    B_images = [B for B in B_images if B['y_pos'] <= screen_height]
            
    #10초가 지날때마다 추가되는 스코어 
    if current_time - score_time >= score_interval:
        score_time = current_time
        score += 1
        print(f"Score increased to {score}")

    screen.blit(background, (0, 0))
    screen.blit(sol, (sol_x_pos, sol_y_pos))
    #140학점을 이수해야 졸업 가능 
    if  score > 140:
        elapsed_time = (pygame.time.get_ticks() - start_time) // 1000
        ending_start_time = pygame.time.get_ticks()
        screen.blit(ending_image, (0, 0))
        # 가운데에 졸업을 축하합니다 메시지 표시
        text_surface = font.render("졸업을 축하합니다!", True, (0, 0, 0))
        text_surface1 = font.render("140학점이 넘어 졸업했습니다.", True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(screen_width // 2, screen_height // 2))
        text_rect1 = text_surface1.get_rect(center=(screen_width // 2+25, screen_height // 2+25))
        screen.blit(text_surface, text_rect)
        screen.blit(text_surface1, text_rect1)
        # 엔딩 이미지를 표시할 시간이 지나면 게임 종료
        if pygame.time.get_ticks() - ending_start_time > ending_display_time:
            break
    elif score<0:
         # bed 엔딩 이미지 표시
            screen.blit(bad_ending_image, (0, 0))
            text_surface = font.render("학사경고", True, (0, 0, 0))
            text_surface1 = font.render("당신은 졸업하지 못했습니다 !", True, (0, 0, 0))
            text_rect = text_surface.get_rect(center=(screen_width // 2, screen_height // 2))
            text_rect1 = text_surface1.get_rect(center=(screen_width // 2+25, screen_height // 2+25))
            screen.blit(text_surface, text_rect)
            screen.blit(text_surface1, text_rect1)

            # bed 엔딩이 표시될 때 ending_start_time을 업데이트
            ending_start_time = pygame.time.get_ticks()

            # ending_display_time이 지날 때까지 대기 후 종료
            if pygame.time.get_ticks() - ending_start_time > ending_display_time:
                break       
    else:   
    # 총알 여러개 소환 
        for bullet in bullets:
            screen.blit(bullet_image, (bullet['x_pos'], bullet['y_pos']))
    # A여러개 소환     
        for A in A_images:
            screen.blit(A_image, (A['x_pos'], A['y_pos']))
    # B여러개 소환   
        for B in B_images:
            screen.blit(B_image, (B['x_pos'], B['y_pos']))    
    # 기존 A,B 이미지 업그레이드 이후에 삭제 구문을 따로 두어 remove 에러를 방지    
        A_images = [A for A in A_images if A['y_pos'] <= screen_height] 
        B_images = [B for B in B_images if B['y_pos'] <= screen_height]    
    # 스코어 띄워놓는 구문 
        score_text = font.render(f"학점: {score}", True, (255, 255, 255))
        screen.blit(score_text, (screen_width - 150, 10))

    display_time(elapsed_time)
    pygame.display.update()
    

    

pygame.quit()
