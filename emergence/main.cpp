#include <SFML/Graphics.hpp>
#include <bits/stdc++.h>
#define WIDTH 1000
#define HEIGHT 1000

#include <World.h>
#include <Entity.h>
#include <chrono>
int main()
{
    sf::RenderWindow window(sf::VideoMode(WIDTH, HEIGHT), "Emergence");
    sf::View view(sf::Vector2f(0.0f, 0.0f), sf::Vector2f(WIDTH, HEIGHT));
    sf::Vector2i offset(WIDTH / 2, HEIGHT / 2);

    std::chrono::steady_clock::time_point start = std::chrono::steady_clock::now();

    World* world = new World();

    while (window.isOpen())
    {
        sf::Event event;
        while (window.pollEvent(event))
        {
            if (event.type == sf::Event::Closed)
                window.close();
            if (event.type == sf::Event::MouseButtonPressed){
                if(event.mouseButton.button == sf::Mouse::Left)
                    world->addEntity(new Entity(sf::Mouse::getPosition(window) - offset , 0));
                else
                    world->addEntity(new Entity(sf::Mouse::getPosition(window) - offset , 1));
            }
            if(event.type == sf::Event::KeyPressed){
                if(event.key.code == sf::Keyboard::Num1)
                    world->addEntity(new Entity(sf::Mouse::getPosition(window) - offset , 2));
                if(event.key.code == sf::Keyboard::Num2)
                    world->addEntity(new Entity(sf::Mouse::getPosition(window) - offset , 3));
                if(event.key.code == sf::Keyboard::Num3)
                    world->addEntity(new Entity(sf::Mouse::getPosition(window) - offset , 4));
                if(event.key.code == sf::Keyboard::Enter)
                    std::cout<<world->getEntities().size()<<"\n";
            }
        }

        window.clear();
        window.setView(view);

        std::vector<Entity*> entities = world->getEntities();
        std::chrono::steady_clock::time_point current = std::chrono::steady_clock::now();
        int time = std::chrono::duration_cast<std::chrono::milliseconds>(current - start).count();
        start = current;

        for(auto it = entities.begin(); it != entities.end(); it++){
            window.draw((*it)->getShape());
        }

        world->update(time);

        window.display();
    }

    return 0;
}
