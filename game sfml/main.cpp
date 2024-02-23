#include <SFML/Graphics.hpp>//подключение заголовочного файла
//#include "gamegovna.h"
//#include "gamegovna2.h"
using namespace sf;//прописываем здесь, чтобы не писать при использовании его функций

int g=0 /*счетчик*/, vx[100], vy[100], randvrag[100]/*рандом картинок*/, konec=2;
int timenewvr=0, ground=1, timerjump=0, speed=20,fx=0,fy=0,State1=0; //это таймер создания новых врагов
Clock clock2; //время нужно для счета расстояния пройденного котом
Image figimage, vragimage;//создаем переменную, хранящую картинку
    Texture figtexture,vragtexture; //создаем переменную, хранящую текстуру
    Sprite figsprite,vragsprite[101]; //создаем переменную, хранящую спрайт
 float  chetanim=1,PosTek = 5;//хранит текущий кадр

void kotanim(){//создает анимацию фигуры кота на месте,попеременно вырезая и присваивая картинку
 if (int(chetanim)==5) figsprite.setTextureRect(IntRect(0,0,111,110)); //анимация кота
     if (int(chetanim)==4) figsprite.setTextureRect(IntRect(111,0,111,110));
     if (int(chetanim)==3) figsprite.setTextureRect(IntRect(222,0,111,110));
     if (int(chetanim)==2) figsprite.setTextureRect(IntRect(331,0,111,110));
     if (int(chetanim)==1) figsprite.setTextureRect(IntRect(444,0,111,110));
     if (int(chetanim)>=5) chetanim=1;
     chetanim+=0.8;//счетчик для более плавной смены картинок
}

void kotstate(){ //перемещения кота
        //влево
        if (State1==4 && fx>5 && fx<=720) { //ограничиваем передвижения до краев окна, давая возможность уйти влево на правом краю поля
			figsprite.move(-speed, 0);//перемещаем влево на speed пикселей
			State1=0;//возвращает состояние покоя
		}

		//вправо
		else if (State1==5 && fx>=5 && fx<720 ) {//ограничиваем передвижения до краев окна, давая возможность уйти вправо на левом краю поля
			figsprite.move(speed, 0);//перемещаем вправо на speed пикселей
            State1=0;//возвращает состояние покоя

		}

		//прыжок
		else if (State1==1 && fx>=5 && fx<=720) { //ограничиваем передвижения до краев окна
            if (ground) figsprite.move(0, - speed);//происходит движение персонажа вверх на speed пикселей
			else figsprite.move(0, speed);//происходит движение персонажа вниз на speed пикселей

			if (timerjump>3) ground=0;//позволяем коту упасть
            timerjump++;
            if (timerjump>9) {timerjump=0; ground=1;State1=0;}//кот вернулся на землю, обнуляем счетчик прыжка и возвращаем состояние покоя
		}

		//прыжок влево
		else if (State1==2 && fx>5 && fx<=720) { //ограничиваем передвижения до краев окна, давая возможность уйти влево на правом краю поля
           if (ground) figsprite.move(-speed, - speed);//происходит движение персонажа вверх и влево на speed пикселей
			else figsprite.move(-speed, speed);//происходит движение персонажа вниз и влево на speed пикселей

			if (timerjump>3) ground=0;//позволяем коту упасть
            timerjump++;
            if (timerjump>9) {timerjump=0; ground=1;State1=0;}//кот вернулся на землю, обнуляем счетчик прыжка и возвращаем состояние покоя
		}

		//прыжок враво
		else if (State1==3 && fx>=5 && fx<720) { //ограничиваем передвижения до краев окна, давая возможность уйти вправо на левом краю поля
            if (ground) figsprite.move(speed, - speed);//движение персонажа вверх и вправо на speed пикселей
			else figsprite.move(speed, speed);//происходит движение персонажа вниз и вправо на speed пикселей

			if (timerjump>3) ground=0;//позволяем коту упасть
            timerjump++;
            if (timerjump>9) {timerjump=0; ground=1;State1=0;}//кот вернулся на землю, обнуляем счетчик прыжка и возвращаем состояние покоя
		}
		else {//если ничего не подошло
                State1=0;//на всякий случай обнуляем состояние
            }

		fx = figsprite.getPosition().x;//присваиваем позицию кота по х
        fy = figsprite.getPosition().y;//присваиваем позицию кота по у

        if (fy>248 && State1==0) figsprite.setPosition(fx,248);//если по какой-то причине кот в покое, но не на земле возвращаем его туда

		 if (fx<5) figsprite.setPosition(5,248);//если при перемещении кот ушел за пределы поля, возвращаем его на границу
         if (fx>720) figsprite.setPosition(720,248);//если при перемещении кот ушел за пределы поля, возвращаем его на границу

    }


void nol(){//функция обнуляет все значения для перезапуска
    clock2.restart();//обнуляем время
    if(Keyboard::isKeyPressed(Keyboard::Space)) konec=0;//если нажат пробел, то начинаем игру сначала
    g=0;//счетчик массива спрайтов врага
    timenewvr=0; //таймер появления врагов
    timerjump=0; //таймер прыжка
    ground=1;//положение = на земле
    State1=0;//состояние покоя
    figsprite.setPosition(50, 248);//ставим на начальную позицию

    fx=figsprite.getPosition().x;//получаем значения по х
    fy=figsprite.getPosition().y;// и по у
    for (int i=0;i<100;i++) {
            vragsprite[i].setPosition(1000,310);//все спрайты врагов премещаем за пределы поля
            randvrag[i]=0;//обнуляем массив рандома врагов
            vx[i]=vragsprite[i].getPosition().x;//обнуляем массив позии врага
            vragsprite[i].setTextureRect(IntRect(0,0,0,0));//и обнуляем все картинки
            }
}

void proverkastate(){//прописываем состояние игры проигрыш=1
    for (int i=0; i<100;i++){
        vx[i]=vragsprite[i].getPosition().x;//получаем позицию каждого врага
        for (int j=0;j<60;j++){//создаем область размеро 60 пикселей в коте для проверки столкновения
          //все картинки врагов имею разную ширину, поэтому каждую просматриваем отдельно
         if(randvrag[i]==1 && (fx+20+j==vx[i]+20) && fy>200) konec=1;//с помощью цикла попиксельно сравниваем
         if(randvrag[i]==2 && (fx+20+j==vx[i]+30) && fy>200) konec=1;//отступая у кота с краев по 20 пикселей
         if(randvrag[i]==3 && ( fx+20+j==vx[i]+17) && fy>200) konec=1;//а у врагов находим середину
        }
}
}

int statekot(){ //возвращает состояние кота по нажатию кнопок
    if (State1==0){//меняем только при состоянии покоя
       if (Keyboard::isKeyPressed(Keyboard::Left) || (Keyboard::isKeyPressed(Keyboard::A))) State1=4;//влево
        if ((Keyboard::isKeyPressed(Keyboard::Right) || (Keyboard::isKeyPressed(Keyboard::D)))) State1=5;//вправо

        if (Keyboard::isKeyPressed(Keyboard::Up) || Keyboard::isKeyPressed(Keyboard::W) || Keyboard::isKeyPressed(Keyboard::Space)) State1=1; //прыжок                                                                                   //просто прыжок
            if ((Keyboard::isKeyPressed(Keyboard::Up) || Keyboard::isKeyPressed(Keyboard::W) || Keyboard::isKeyPressed(Keyboard::Space))
                &&(Keyboard::isKeyPressed(Keyboard::Left) || (Keyboard::isKeyPressed(Keyboard::A)))) State1=2; //прыжок влево
            if ((Keyboard::isKeyPressed(Keyboard::Up) || Keyboard::isKeyPressed(Keyboard::W) || Keyboard::isKeyPressed(Keyboard::Space)) &&
                ((Keyboard::isKeyPressed(Keyboard::Right) || (Keyboard::isKeyPressed(Keyboard::D))))) State1=3; //прыжок враво
        }
        return State1;//возвращаем значение
}

void voidstate(){
        if (State1==4 || State1==2) { //если фигура движется влево, то анимируем двидение кота в соответствующую сторону
			PosTek -= 0.005*160;//счетчик появления кадров
			//читаем картинку справа налево
			if (PosTek < 0) PosTek += 5;//обнуляем значение
			if (int(PosTek)==3) figsprite.setTextureRect(IntRect(111 * int(PosTek)-2+111, 0, -111, 110));
			//обрезаем коту ногу в 3 кадре,т.к. картанка немного отличается по размеру
			else figsprite.setTextureRect(IntRect(111 * int(PosTek)+111, 0, -111, 110));//остальные идентичны
        }
        else{ //вправо анимация
            PosTek -= 0.005*160;
            //счетчик появления кадров
			//читаем картинку слева направо
			if (PosTek < 0) PosTek += 5;//обнуляем значение
			if (int(PosTek)==3) figsprite.setTextureRect(IntRect(111 * int(PosTek)-2, 0, 111, 110));
			//обрезаем коту ногу в 3 кадре,т.к. картанка немного отличается по размеру
			else figsprite.setTextureRect(IntRect(111 * int(PosTek), 0, 111, 110)); //остальные идентичны
        }
    }

void  vragcos(int ti){ //функция создает элементы массива спрайтов из 3  фигурок
    if (timenewvr==0 && ti<2600){//заканчиваем на расстоянии 2600 см
    vragimage.loadFromFile("image/kak.png");//импортируем изображение в переменную
    vragtexture.loadFromImage(vragimage);//затем в текстуру
    vragsprite[g].setTexture(vragtexture);//затем в спрайт
    //делаем спрайт чтобы поперенно их выпускать
    randvrag[g]=rand()%3 +1;//записываем в массив число от 1 до 3
    //затем с помощью этого рандома вырезаем определенный кадр врага
        if (randvrag[g]==1) vragsprite[g].setTextureRect(IntRect(0,0,39,50));
        else if (randvrag[g]==2) vragsprite[g].setTextureRect(IntRect(39,0,58,50));
        else vragsprite[g].setTextureRect(IntRect(97,0,33,50));

        vragsprite[g].setPosition(900,310);//сразу присваиваем спрайту положение за окном
        g++;
        if (g>103) g=0;//если массив заполнен пишем заново
    }
        timenewvr--;
        if (timenewvr<0) timenewvr=rand()%18 +10; //перезапускаем таймер появления врагов размером от 10 до 18 циклов


        for (int i=0; i<=g;i++){//передвигаем массив врагов до создавшегося
    vragsprite[i].move(-speed-6.5,0);//двигаем справа налево чуть быстрее фигуры
    }
}



int main()
{
    RenderWindow win(VideoMode(840, 580), "<->Bolt<->");//пространство имен создает окно
//сначала импортируем картинку из файла, затем в текстуру и в спрайт
     figimage.loadFromFile("image/kot2_negate.png");
    vragimage.loadFromFile("image/kak.png");
    vragtexture.loadFromImage(vragimage);
    figtexture.loadFromImage(figimage);
    figsprite.setTexture(figtexture);
    figsprite.setTextureRect(IntRect(0,0,111,110));//первый кадр
    figsprite.setPosition(50, 248);//задаем коту начальную позицию

    Sprite tortsprite;//создаем спрайт тортика
    tortsprite.setTexture(vragtexture);
    tortsprite.setTextureRect(IntRect(130,0,50,50));
    tortsprite.setPosition(920,310);//положение за границей окна

    Font font;//шрифт
	font.loadFromFile("image/CyrillicOld.ttf");//достаем из файла стили
    Text text("", font, 20);//размер текста 20
	text.setColor(Color::White);//цвет устанавливаем белый
	text.setStyle(Text::Bold);//стиль текста

    RectangleShape line(Vector2f(840, 1));//создаем линию(прямоугольник) длиной 840 и шириной 1 пиксель
    line.setPosition(0,360);//задаем позицию ниже кота

    vx[0]=1000; vy[0]=310; //объявляем положение первого врага


    while (win.isOpen() && Keyboard::isKeyPressed(Keyboard::Escape)<=0 )//пока открыто окно и не нажата кнопка эскейп
    {
        int ti= clock2.getElapsedTime().asSeconds();//получаем время в секундах
        ti*=25;//умножаем на 25 и получаем скорость 25 см/с

        Event event; //событие
        while (win.pollEvent(event))//если получено сообщение закрытия окна то закрыть
        {
            if (event.type == Event::Closed)//закрыть если закрыли
                win.close();

        }
               kotanim();
            State1=statekot();
            voidstate();
            kotstate();
         vragcos(ti); //создаем врага
        proverkastate();

        Time tim=milliseconds(120);//создаем для замедления показа кадров
        if(ti>300) tim-= milliseconds(ti/30); //уменьшаем таймер следовательно ускоряем игру
        sleep(tim);//делаем залипание с помощью этого таймера
        if (ti>2700) konec=3;//прописываем выигрыш

        win.clear();//очищает и затем рисует и показывает
        if (!konec){//если ничего нового не произошло то просто рисуем объекты и продолжаем играть

        win.draw(figsprite);//рисуем кота
        win.draw(line);//рисуем линию

        text.setPosition(0,10);//задаем позицию текста
        text.setCharacterSize(20);//размер текста
        text.setString("Kot Vasiliy");//содержание текста
        win.draw(text);//рисую этот текст

        //увелициваем размер и показываем другой текст
        text.setCharacterSize(24);
        text.setString(std::to_string(ti) + " sm");//расстояние пройденное котом в см
         text.setPosition(5,40);//задаем позицию текста
        win.draw(text);//рисую этот текст

        for (int i=0;i<100;i++)
         win.draw(vragsprite[i]);//рисуем весь массив врагов
        }

        else if (konec==3){// состояние игры победа=3
            text.setString("\t\t\t  You Win!");//задаем содержание строки
            text.setCharacterSize(30);//размер
            text.setPosition(200,100);//положение

            if (tortsprite.getPosition().x > figsprite.getPosition().x+130) tortsprite.move(-20,0);//передвигаем торт до кота
            else nol();//если корт добрался,то все обнуляем
            win.draw(text);//рисуем
            win.draw(figsprite);
            win.draw(line);
            win.draw(tortsprite);
        }
        else { //состояние игры проигрыш=1 или первый запуск=2
        //основная задача все обнулить и ничего не выводить кроме текста
            if (konec==1){
            text.setString("\t\t\t  Game over\n To start first click space");
            }
            else text.setString("\t\t\tHi!\n To start first click space");
            text.setCharacterSize(40); //размер
            text.setPosition(200,180);//позиция
            win.draw(text);//рисуем
            nol();//все обнуляем
            }

        win.display();//показывает все нарисованное
    }
    return 0;
}
