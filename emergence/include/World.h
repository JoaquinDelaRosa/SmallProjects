#ifndef WORLD_H
#define WORLD_H
#include <Entity.h>
#include <bits/stdc++.h>

class World
{
    private:
        std::vector<Entity*> entities;
        float multipliers[5][5] = {
            {-2.0f, 200.0f, -30.0f, 300.0f, -500},
            {-200.0f, -1.0f, -12.0f, 100.0f, -500},
            {300.0f, -10.0f, 100.0f, -1.0f, -500},
            {-100.0f, -100.0f, 200.0f, 100.0f, -500},
            {500.0f, 500.0f, 500.0f, 500.0f, -1000.f}
        };

    public:
        World();
        std::vector<Entity*> getEntities();
        void addEntity(Entity* e);
        void removeEntity(Entity *e);

        void update(int time);
};

#endif // WORLD_H
