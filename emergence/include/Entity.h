#ifndef ENTITY_H
#define ENTITY_H

#include <bits/stdc++.h>
#include <SFML/Graphics.hpp>

class Entity
{
    private:
        // Positional attributes
        float radius;
        sf::CircleShape shape;
        sf::Vector2f position;

        sf::Vector2f velocity;
        sf::Vector2f force;
        // Simulation attributes
        int type ;

    public:
        Entity(sf::Vector2i position, int type);
        sf::CircleShape getShape();

        void update(int time);

        int getType();
        sf::Vector2f getPosition();
        void applyForce(sf::Vector2f force);
};

#endif // ENTITY_H
