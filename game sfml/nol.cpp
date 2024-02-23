#include "gamegovna.h"
void nol(){
    clock2.restart();
    if(Keyboard::isKeyPressed(Keyboard::Space)) konec=0;
    g=0;
    timenewvr=0;
    timerjump=0;
    ground=1;
    State1=0;
    figsprite.setPosition(50, 248);

    fx=figsprite.getPosition().x;
    fy=figsprite.getPosition().y;
    for (int i=0;i<100;i++) {
            vragsprite[i].setPosition(1000,310);
            randvrag[i]=0;
            vx[i]=vragsprite[i].getPosition().x;
            vragsprite[i].setTextureRect(IntRect(0,0,0,0));
            }
}
