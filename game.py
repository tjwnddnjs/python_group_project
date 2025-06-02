import pygame
import random
import os

def play_game(words):
    
    # 단어장 불러옴
    word_dict = words
    pygame.init()

    WIDTH, HEIGHT = 800, 600

    correct = pygame.image.load("correct.png")
    correct = pygame.transform.scale(correct, (350, 350))

    wrong = pygame.image.load("wrong.png")
    wrong = pygame.transform.scale(wrong, (350, 350))
    #무지성 푸앙이 도배

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("산성비 타자 게임")

    font_path = "C:/Windows/Fonts/malgun.ttf"

    font = pygame.font.Font(font_path, 20) #떨어지는 단어 크기
    input_font = pygame.font.Font(font_path, 24) #입력 단어, 점수 표시 단어 크기기

    clock = pygame.time.Clock()

    class FallingWord:
        def __init__(self, eng, kor):
            self.eng = eng
            self.kor = kor
            self.x = random.randint(50, WIDTH - 100)
            self.y = 0
            self.speed = random.uniform(0.7, 1.5) #떨어지는 단어 속도 조절!

        def move(self):
            self.y += self.speed

        def draw(self):
            text = font.render(self.kor, True, (255, 255, 255))
            screen.blit(text, (self.x, self.y))

    def show_feedback(image):
        img_width, img_height = image.get_size()
        x = WIDTH // 2 - img_width // 2
        y = HEIGHT // 2 - img_height // 2

        screen.blit(image, (x, y))
        pygame.display.flip()
        pygame.time.delay(250)  # 0.25초 보여줌

    falling_words = []
    spawn_timer   = 0
    score         = 0
    user_input    = ""

    running = True
    while running:
        screen.fill((0, 0, 0))

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
                    matched = None
                    for word in falling_words:
                        if user_input.strip().lower() == word.eng:
                            matched = word
                            break
                    if matched:
                        falling_words.remove(matched)
                        score += 1
                        show_feedback(correct) 
                    else:
                        show_feedback(wrong)
                        if score != 0:
                           score -=1 
                           
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
        input_surface = input_font.render("입력: " + user_input, True, (255, 255, 255)) #입력 표시 단어 설정
        screen.blit(input_surface, (20, HEIGHT - 40))

        # 점수 표시
        score_surface = input_font.render(f"점수: {score}", True, (255, 255, 255)) #점수 표시 단어 설정
        screen.blit(score_surface, (20, 20))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    return
