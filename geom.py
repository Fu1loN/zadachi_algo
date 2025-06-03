from math import sqrt
import pygame
pygame.init()
def main():
    sections = []
    with open("geom.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            sections.append([float(s) for s in line.split(",")])
    print(sections)
    line_ans = None
    max_intersections = 0
    for i in  range(len(sections)):
        line = get_line(sections[i])
        if max_intersections < sum(intersect(line, s) for s in sections):
            max_intersections = sum(intersect(line, s) for s in sections)
            line_ans = line
        for j in range(i+1, len(sections)):
            line = get_line(sections[i][:2] + sections[j][:2])
            if max_intersections < sum(intersect(line, s) for s in sections):
                max_intersections = sum(intersect(line, s) for s in sections)
                line_ans = line
            line = get_line(sections[i][:2] + sections[j][2:])
            if max_intersections < sum(intersect(line, s) for s in sections):
                max_intersections = sum(intersect(line, s) for s in sections)
                line_ans = line
            line = get_line(sections[i][2:] + sections[j][:2])
            if max_intersections < sum(intersect(line, s) for s in sections):
                max_intersections = sum(intersect(line, s) for s in sections)
                line_ans = line
            line = get_line(sections[i][2:] + sections[j][2:])
            if max_intersections < sum(intersect(line, s) for s in sections):
                max_intersections = sum(intersect(line, s) for s in sections)
                line_ans = line
    print(line_ans)
    print(max_intersections)

    run = True
    screen = pygame.display.set_mode((1000, 1000))
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        screen.fill((0, 0, 0))
        pygame.draw.line(screen, (255, 0, 0), *get_section(line_ans))
        for section in sections:
            pygame.draw.line(screen, (0, 255, 0), section[:2], section[2:])
        pygame.display.flip()
    pygame.quit()   

def intersect(line, section):
    a,b,c = line
    x1,y1,x2,y2 = section
    d1 = a*x1 + b*y1 + c
    d2 = a*x2 + b*y2 + c
    return int(d1*d2 <= 0)

def get_line(section):
    x1,y1,x2,y2 = section
    a = y2 - y1
    b = x1 - x2
    c = x1*y2 - x2*y1
    d = sqrt(a**2 + b**2)
    return a/d, b/d, c/d
def get_section(line):
    a,b,c = line
    if b == 0:
        assert a == 1 or a == -1, "a must be 1 or -1"
        return (0, -c * a), (1000, -c * a)  
    x1 = 0
    y1 = -c/b
    x2 = 1000
    y2 = -(a*1000+c)/b
    return (x1,y1), (x2,y2)

if __name__ == "__main__":
    main()
