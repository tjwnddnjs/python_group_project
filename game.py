# -*- coding: utf-8 -*-
import pygame
import random
import sys
import os

def play_game(words):
    
    # 단어장
    word_dict = words
    pygame.init()

    # 화면 설정
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("산성비 타자 게임")

    # 한글 지원 폰트 로드
    # 1) 윈도우 기본 폰트 경로 (malgun.ttf)
    # font_path = "C:/Windows/Fonts/malgun.ttf"
    # 2) 프로젝트 내에 두고 사용할 외부 폰트 (예: fonts/NanumGothic.ttf)
    font_path = "C:/Windows/Fonts/malgun.ttf"

    if not os.path.isfile(font_path):
        raise FileNotFoundError(f"한글 폰트 파일을 찾을 수 없습니다: {font_path}")

    font      = pygame.font.Font(font_path, 48)
    input_font = pygame.font.Font(font_path, 36)

    clock = pygame.time.Clock()

    # 떨어지는 단어 클래스
    class FallingWord:
        def __init__(self, eng, kor):
            self.eng = eng
            self.kor = kor
            self.x = random.randint(50, WIDTH - 100)
            self.y = 0
            self.speed = random.uniform(1.0, 2.5)

        def move(self):
            self.y += self.speed

        def draw(self):
            # 한글 렌더링
            text = font.render(self.kor, True, (255, 255, 255))
            screen.blit(text, (self.x, self.y))

    # 게임 상태
    falling_words = []
    spawn_timer   = 0
    score         = 0
    user_input    = ""

    # 게임 루프
    running = True
    while running:
        screen.fill((20, 30, 70))

        # 단어 생성 주기
        spawn_timer += 1
        if spawn_timer > 60:  # 약 1초 간격
            eng = random.choice(list(word_dict.keys()))
            kor = word_dict[eng]
            falling_words.append(FallingWord(eng, kor))
            spawn_timer = 0

        # 이벤트 처리
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    # 입력 단어와 비교
                    matched = None
                    for word in falling_words:
                        if user_input.strip().lower() == word.eng:
                            matched = word
                            break
                    if matched:
                        falling_words.remove(matched)
                        score += 1
                    user_input = ""
                elif event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]
                else:
                    user_input += event.unicode

        # 단어 이동 및 그리기
        for word in falling_words:
            word.move()
            word.draw()
            if word.y > HEIGHT:
                print("Game Over! 최종 점수:", score)
                running = False

        # 사용자 입력 표시
        input_surface = input_font.render("입력: " + user_input, True, (255, 255, 255))
        screen.blit(input_surface, (20, HEIGHT - 40))

        # 점수 표시
        score_surface = input_font.render(f"점수: {score}", True, (255, 255, 0))
        screen.blit(score_surface, (20, 20))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()
