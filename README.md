# Speed & Sport Souvenirs
## Што е ова?
Speed & Sport Souvenirs e број еден онлајн продавница за страсните љубители на мотоспортот. Целта на оваа продавница е да им помогне на фановите на различните тркачки серии да најдат сувенири за да ја искажат нивната љубов кон спортот.

## Некои главни карактеристики:

* Прикажување на различни производи поврзани со мотоспортот
* Пребарување на производи со текстуално поле на пребарување
* Филтрирање на производи според тркачка серија, тим и категорија во која припаѓаат
* Прикажување на тимови во зависност од тоа во која тркачка серија учествуваат
* Прикажување на производи со детални информации и повеќе слики на една страна
* Регистрација и најава на корисници
* Задржување на најава со користење на колачиња, иако го исклучите пребарувачот
* Профилни страни за сите корисници, во кои може да се видат сите производи кои ги нудат за продажба

## Како да се пристапи до апликацијата?
До апликацијата може да се пристапи на два начина, со пристапување до страната каде е хостирана или со клонирање на оваа репозиториум и со извршување на локална верзија.

На првиот начин, може да пристапите преку линкот:

http://striker52.pythonanywhere.com/

и едноставно започнувате со користење на продавницата!

На вториот начин, потребно е прво во Git терминал да ја клонирате овој репозиториум со наредбата. За да започнете, навигирајте до место каде сакате да ја зачувате оваа апликација со:
    
    cd //Патека

Потоа го клонирате репозиториумот со:

    git clone https://github.com/BorisTodor0v/Speed-N-Sport-Souvenirs

Ја користите "cd" наредбата повторно за да влезете внатре во апликацијата

    cd Speed-N-Sport-Souvenirs

Прво треба да ги инсталирате потребните зависности со наредбата

    pip install -r requirements.txt

Откако ќе заврши инсталацијата на зависностите го започнувате локалниот сервер со:

    python manage.py runserver

Потоа може да пристапите до апликацијата со следниот линк

    http://127.0.0.1:8000/

## Admin страна
Доколку сакате да разгледате како се поврзани различните модели кои се користат во апликацијата, може да пристапите до Admin страната преку линкот

    http://127.0.0.1:8000/admin/

За да може да ја користите оваа страна, мора да имате дефинирано superuser корисник. Тоа може да го направите со прекинување на локалниот сервер и со извршување на наредбата

    python manage.py createsuperuser

Каде можете да внесете корисничко име, емаил и лозинка за superuser, со кој ќе имате админ пермисии во апликацијата.

### Важна напомена:
Ниеден од производите прикажан на страната е достапен за продажба, тие се земени од други веб страни кои нудат слични услуги како оваа апликација и служат само како примери да се претстави функционалноста. Овие производи НЕ се достапни за купување преку оваа апликација и цените кои што се претставени не се точни. Во оваа апликација не се извршуваат никакви апликации. На некои места каде што се бара од вас да внесете лични податоци, не внесувајте вистински податоци или платежни информации. Сите информации кои се користат на страната се користат само за претставување на функционалноста и нема да бидат зачувани или искористени за вистински трансакции.
