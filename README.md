# Описание архитектуры - в файле Architecture.
Тесты для создания юнитов

Игра основывается на книгах о Перси Джексона. В игре существуют две "стороны" - полубоги (Demigods) и монстры (Monsters).
В начале игрок должен будет выбрать, на чьей он стороне. Исходя из его выбора, будет создана конкретная фабрика (DemigodsArmy
или MonstersArmy соответсвенно). Далее игроку будет предложено создать нужных ему юнитов-бойцов, при этом в начале игры будет 
выделяться ограниченное число коинов, за которые можно будет вербовать персонажей ("стоимость" каждого прописана в классе в
поле cost). Все классы бойцов - наследники абстрактного класса Fighter (более подробно увидеть структуру воинов для каждой 
армии можно увидеть в файле Architecture). 
