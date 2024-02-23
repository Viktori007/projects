#include "gamegovna2.h"
void  vragcos(int ti){ //функция создает элементы массива спрайтов из 3  фигурок
    if (timenewvr==0 && ti<2600){
    vragimage.loadFromFile("image/kak.png");
    vragtexture.loadFromImage(vragimage);
    vragsprite[g].setTexture(vragtexture);
    //делаем спрайт чтобы поперенно их выпускать
    randvrag[g]=rand()%3 +1;

        if (randvrag[g]==1) vragsprite[g].setTextureRect(IntRect(0,0,39,50));//рандомно выпускаем врагов для первого
        else if (randvrag[g]==2) vragsprite[g].setTextureRect(IntRect(39,0,58,50));
        else vragsprite[g].setTextureRect(IntRect(97,0,33,50));

        vragsprite[g].setPosition(900,310);
        g++;
        if (g>103) g=0;
    }
        timenewvr--;
        if (timenewvr<0) timenewvr=rand()%18 +10; //перезапускаем таймер появления врагов размером от 10 до 18 циклов


        for (int i=0; i<=g;i++){//передвигаем массив врагов до создавшегося
    vragsprite[i].move(-speed-6.5,0);//двигаем справа налево
    }
}
