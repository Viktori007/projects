#include "gamegovna.h"
void voidgovno(int State1){
        if (State1==4 || State1==2) { //влево анимация
			PosTek -= 0.005*160;
			if (PosTek < 0) PosTek += 5;//читаем в обратном порядке
			if (int(PosTek)==3) figsprite.setTextureRect(IntRect(111 * int(PosTek)-2+111, 0, -111, 110));//обрезает коту ногу
			else figsprite.setTextureRect(IntRect(111 * int(PosTek)+111, 0, -111, 110));//читаем картинку справа налево
        }
        else{ //вправо анимация
            PosTek -= 0.005*160;
			if (PosTek < 0) PosTek += 5;
			if (int(PosTek)==3) figsprite.setTextureRect(IntRect(111 * int(PosTek)-2, 0, 111, 110));
			else figsprite.setTextureRect(IntRect(111 * int(PosTek), 0, 111, 110));
        }
    }
