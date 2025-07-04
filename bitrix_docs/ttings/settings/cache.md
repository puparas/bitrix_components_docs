| Поле | Описание |
| --- |

|
| Маска включения | Укажите файлы и типы файлов, которые будут обрабатываться HTML кешем. |
| Маска исключения |

|
| Дисковая квота (мегабайт) | Дисковая квота кеша (задается в мегабайтах). |

Для сохранения настроек нажмите кнопку **Сохранить настройки HTML кеша**.

Для установки значений параметров равными значениям по умолчанию нажмите кнопку **Установить настройки по умолчанию**.

**Внимание!** Есть и ограничения в использовании. В частности, мы **не советуем** включать HTML кеш (или включать обдуманно по разделам) для редакций, которые содержат веб-аналитику и модуль рекламы.

Механизм HTML-кеширования лучше всего включить на какой-нибудь редко изменяющийся раздел с регулярным посещением анонимных посетителей, так как при включенном HTML-кешировании происходят следующие процессы:

* механизмом HTML-кеша обрабатываются только страницы, не указанные в маске исключения и указанные в маске включения;
* если на такие страницы заходит не авторизованный пользователь, то выполняется проверка существования файла кеша и если таковой найден, то выдается страница из кеша, не задействуя никакие модули продукта; например, не будет работать модуль статистики (не засчитаются хиты этого пользователя), модуль рекламы, главный и другие модули;
* при этом если на момент включения кеша был установлен модуль компрессии, то страница будет отдаваться в сжатом виде;
* если страница в кеше не найдена, то код исполняется в обычном режиме; когда страница полностью сформирована, ее копия сохраняется в HTML-кеш;

Очистка кеша:

* если сохраняемый объем приводит к превышению дисковой квоты кеша, то кеш полностью очищается;
* так же полная очистка кеша происходит при любом изменении данных в административной части системы;
* если в публичной части сайта происходит POST данных (например, добавление комментария или голосование), то сбрасывается соответствующая часть кеша;

Из всего вышесказанного следует, что:

* не ведется учет статистики;
* модуль рекламы будет работать только в момент создания кеша (это не относится к внешней динамической рекламе (Begun и пр.));
* необходимо обязательно задать дисковую квоту во избежание DoS-атаки по дисковому пространству;
* после включения механизма HTML-кеширования необходимо проверить весь функционал раздела, к которому применен кеш (например, может не сработать публикация комментариев со старыми шаблонами блогов);

### Очистка файлов кеша

Эта закладка используется для удаления файлов кеша, содержащих устаревшую или сбойную информацию.

| Поле | Описание |
| --- |

|
| Только устаревшие | Файлы, время жизни которых закончилось. |
| Все |

|
| Меню | Меню может быть закешировано, если происходят проверки доступа к различным пунктам меню, разделам. Данный пункт позволяет очистить этот кеш. |
| Весь управляемый |