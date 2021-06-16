#include "Entity.h"
#include "bits/stdc++.h"
#include "SFML/Graphics.hpp"

#include "random"

std::random_device dev;
std::mt19937 rng(dev());


double rand(double first, double second){

    std::uniform_real_distribution<float> dist(first, second); // distribution in range [1, 6]
    return dist(rng);
}

Entity::Entity(sf::Vector2i position, int type)
{
    this->radius = 5;
    this->shape = sf::CircleShape(this->radius);
    shape.setPosition(sf::Vector2f(position));
    this->position = sf::Vector2f(position);

    this->type = type;
    this->velocity = sf::Vector2f(0, 0);
}

sf::CircleShape Entity::getShape(){
    return this->shape;
}


void Entity::update(int time){
    this->velocity += sf::Vector2f(force.x , force.y );

    // Clamp velocity
    velocity.x = std::max(-0.1f, velocity.x);
    velocity.x = std::min(0.1f, velocity.x);
    velocity.y = std::max(-0.1f, velocity.y);
    velocity.y = std::min(0.1f, velocity.y);

    this->position += velocity;

    shape.setPosition(position);

    switch(type){
        case 0: shape.setFillColor(sf::Color(255, 0, 0)); break;
        case 1: shape.setFillColor(sf::Color(0, 255, 0)); break;
        case 2: shape.setFillColor(sf::Color(0, 0, 255)); break;
        case 3: shape.setFillColor(sf::Color(255, 0, 255)); break;
        case 4: shape.setFillColor(sf::Color(0, 255, 255)); break;
    }
}

sf::Vector2f Entity::getPosition(){
    return this->position;
}

int Entity::getType(){
    return this->type;
}

void Entity::applyForce(sf::Vector2f force){
    this->force = force;
}


