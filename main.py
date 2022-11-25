from src.voronoi_diagram import *
import time

def main():
    screen:pygame.Surface = pygame.display.set_mode(cfg_data.SCREEN_SCALE_DIMS)
    
    surface = generate_surface(Algorithm.D_BUFFER)
    last_surface = surface
    surface = pygame.transform.scale(surface, cfg_data.SCREEN_SCALE_DIMS)
    
    clock = pygame.time.Clock()
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                add_point(
                    pos[0]//cfg_data.SCREEN_SCALE, pos[1]//cfg_data.SCREEN_SCALE)
                
                print("Generating surface")
                start = time.time()
                
                surface = generate_surface(
                    Algorithm.D_BUFFER, last=last_surface)
                last_surface = surface
                surface = pygame.transform.scale(surface, cfg_data.SCREEN_SCALE_DIMS)
                
                end = time.time()
                print(f"Generation took: {end - start}s")
                
                               
        screen.blit(surface, (0, 0))
        
        for point in points:
            point.render(screen)
    
        pygame.display.update()
        clock.tick(30)


if __name__ == "__main__":
    pygame.init()
    main()
    pygame.quit()