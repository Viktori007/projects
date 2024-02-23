#include "gamegovna2.h"
void proverkaanala(){
    for (int i=0; i<100;i++){
        vx[i]=vragsprite[i].getPosition().x;//получаем позицию каждого врага
        for (int j=0;j<60;j++){//создаем область размеро 60 пикселей в коте для проверки сталкновения
          if(randvrag[i]==1 && (fx+20+j==vx[i]+20) && fy>200) konec=1;
          if(randvrag[i]==2 && (fx+20+j==vx[i]+30) && fy>200) konec=1;
          if(randvrag[i]==3 && ( fx+20+j==vx[i]+17) && fy>200) konec=1;
        }//прописываем состояние игры проигрыш=1
}
}
