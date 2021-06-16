#include "World.h"
#include "SFML/Graphics.hpp"

#define EPSILON 100
#define ALPHA 100

float distance(Entity* x, Entity* y){
    sf::Vector2f d1 = x->getPosition();
    sf::Vector2f d2 = y->getPosition();

    float dx = d1.x - d2.x;
    float dy = d1.y - d2.y;

    return dx * dx + dy * dy;
}

sf::Vector2f direction(Entity* x, Entity* y){
    return x->getPosition() - y->getPosition();
}

World::World()
{
    //ctor
}

void World::addEntity(Entity* e){
    this->entities.push_back(e);
}

std::vector<Entity*> World::getEntities(){
    return entities;
}

void World::update(int time){
    double G = 0.001;
    for(auto it = this->entities.begin(); it != this->entities.end(); it++){
        sf::Vector2f force(0.0f, 0.0f);
        for(auto jt = this->entities.begin(); jt != this->entities.end(); jt++){
            if((*it) != (*jt)){
                float multiplier = this->multipliers[(*it)->getType()][(*jt)->getType()];
                double d = distance((*it), (*jt));
                sf::Vector2f dir = direction((*it), (*jt));

                if(d <= EPSILON)
                    force += sf::Vector2f(10 * dir.x * abs(multiplier), 10 * dir.y * abs(multiplier));
                else if (d <= ALPHA * ALPHA)
                    force -= sf::Vector2f(dir.x * multiplier / d, dir.y * multiplier / d);
            }
        }
        sf::Vector2f pos = (*it)->getPosition();
        float d1 = pos.x + 500;
        float d2 = pos.x - 500;
        float d3 = pos.y + 500;
        float d4 = pos.y - 500;

        force.x += 100 / (d1 * d1);
        force.x -= 100 / (d2 * d2);
        force.y += 100 / (d3 * d3);
        force.y -= 100 / (d4 * d4);

        // Normalize
        force = sf::Vector2f(force.x * G , force.y * G);
        (*it)->applyForce(force);
    }

    for(auto it = this->entities.begin(); it != this->entities.end(); it++){
        (*it)->update(time);
    }
}
