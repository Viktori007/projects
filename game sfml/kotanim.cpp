#include "gamegovna2.h"
 void kotanim(){
 if (int(chetanim)==5) figsprite.setTextureRect(IntRect(0,0,111,110)); //анимация кота
     if (int(chetanim)==4) figsprite.setTextureRect(IntRect(111,0,111,110));
     if (int(chetanim)==3) figsprite.setTextureRect(IntRect(222,0,111,110));
     if (int(chetanim)==2) figsprite.setTextureRect(IntRect(331,0,111,110));
     if (int(chetanim)==1) figsprite.setTextureRect(IntRect(444,0,111,110));
     if (int(chetanim)>=5) chetanim=1;
     chetanim+=0.8;
}
