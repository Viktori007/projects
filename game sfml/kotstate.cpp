#include "gamegovna2.h"
void kotstate(){
        if (State1==4 && fx>5 && fx<=720) { //влево
			figsprite.move(-speed, 0);//происходит само движение персонажа влево
			State1=0;
		}

		else if (State1==5 && fx>=5 && fx<720 ) { //вправо
			figsprite.move(speed, 0);
            State1=0;

		}

		else if (State1==1 && fx>=5 && fx<=720) { //прыжок
            if (ground) figsprite.move(0, - speed);//происходит само движение персонажа вверх
			else figsprite.move(0, speed);

			if (timerjump>3) ground=0;
            timerjump++;
            if (timerjump>9) { timerjump=0; ground=1;State1=0;}
		}

		else if (State1==2 && fx>5 && fx<=720) { //прыжок влево
           if (ground) figsprite.move(-speed, - speed);//происходит само движение персонажа вверх
			else figsprite.move(-speed, speed);

			if (timerjump>3) ground=0;
            timerjump++;
            if (timerjump>9) { timerjump=0; ground=1;State1=0;}
		}

		else if (State1==3 && fx>=5 && fx<720) {  //прыжок враво
            if (ground) figsprite.move(speed, - speed);//происходит само движение персонажа вверх
			else figsprite.move(speed, speed);

			if (timerjump>3) ground=0;
            timerjump++;
            if (timerjump>9) { timerjump=0; ground=1;State1=0;}

		}
		else {
                State1=0;
                fx = figsprite.getPosition().x;
                fy = figsprite.getPosition().y;
                if (!fy==248) figsprite.move(0,15);
                if (fy>248 && fy<223) figsprite.setPosition(fx,248);

		}

		fx = figsprite.getPosition().x;
        fy = figsprite.getPosition().y;

        if (fy>248 && State1==0) figsprite.setPosition(fx,248);

		 if (fx<5) figsprite.setPosition(5,248);
         if (fx>720) figsprite.setPosition(720,248);

    }
