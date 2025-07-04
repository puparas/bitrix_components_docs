|  |  |  |
| --- |

| --- |
| **Поле** |

| **Описание** |
| **Основные параметры** |

| |
| Тип инфоблока |

| Указывается один из созданных в системе типов информационных блоков. |
| Инфоблок |

| Для выбранного типа инфоблоков указывается идентификатор информационного блока, фотографии из которого будут выводиться. |
| Режим работы галереи |

| Указывается режим работы фотогалереи:  * **SIMPLE** - обычный режим, т.е. один пользователь; * **USER** - многопользовательский режим.  Если параметр принимает значение **USER**, то необходимо настроить параметры **USER\_ALIAS**     |  |  |  | | --- | --- | --- | | Код галереи | **USER\_ALIAS** | Указывается имя переменной, в которой передается код галереи. Например **={$\_REQUEST["USER\_ALIAS"]}**. |  ,  **GALLERY\_SIZE**    Данный параметр заполняется в пункте **Дополнительные настройки**.  |  |  |  | | --- | --- | --- | | Размер галереи | **GALLERY\_SIZE** | Задается размер галереи одного пользователя в Мб (параметр задается при выборе многопользовательского режима). |  и **GALLERY\_URL.**    Данный параметр заполняется в пункте **Шаблоны ссылок**.  |  |  |  | | --- | --- | --- | | Содержимое галереи | **GALLERY\_URL** | Указывается адрес страницы просмотра содержимого галереи пользователя. | |
| ID раздела |

| В поле указывается код, в котором передается идентификатор раздела (альбома). |
| Дополнительные параметры выбора фото |

| Указываются дополнительные параметры выбора фото:  * **none** - нет; * **count** - выбирать несколько последних фото (ID); * **time** - выбирать фото за последние несколько дней; * **period** - выбирать фото за период.  Если параметр принимает значение **выбирать несколько последних фото (ID)**, то необходимо настроить параметр **ELEMENTS\_LAST\_COUNT**.     |  |  |  | | --- | --- | --- | | Количество последних фото для выбора | **ELEMENTS\_LAST\_COUNT** | Указывается количество последних фото для выбора. |     Если параметр принимает значение **выбирать фото за последние несколько дней**, то необходимо настроить параметр **ELEMENTS\_LAST\_TIME**.     |  |  |  | | --- | --- | --- | | Количество дней для выбора фото | **ELEMENTS\_LAST\_TIME** | Указывается количество дней для выбора фото. | |
| Первое поле сортировки фото |

| Указывается первое поле, по которому будет происходить сортировка фотографий:  * **SHOW\_COUNTER** – по количеству просмотров в среднем; * **SORT** – по индексу сортировки; * **TIMESTAMP\_X** – по дате последнего изменения; * **NAME** – по названию; * **ID** – по идентификатору; * **PROPERTY\_RATING** – по популярности; * **PROPERTY\_FORUM\_MESSAGE\_CNT** – по количеству комментариев на форуме; * **PROPERTY\_BLOG\_COMMENTS\_CNT** – по количеству комментариев в блоге. |
| Порядок сортировки фото |

| Указывается порядок сортировки фотографий:  * **по возрастанию** (**asc**); * **по убыванию** (**desc**). |
| Второе поле сортировки фото |

| Указывается второе поле, по которому будет происходить сортировка фотографий:  * **SHOW\_COUNTER** – по количеству просмотров в среднем; * **SORT** – по индексу сортировки; * **TIMESTAMP\_X** – по дате последнего изменения; * **NAME** – по названию; * **ID** – по идентификатору; * **PROPERTY\_RATING** – по популярности; * **PROPERTY\_FORUM\_MESSAGE\_CNT** – по количеству комментариев на форуме; * **PROPERTY\_BLOG\_COMMENTS\_CNT** – по количеству комментариев в блоге. |
| Порядок сортировки фото |

| Указывается порядок сортировки фотографий:  * **по возрастанию** (**asc**); * **по убыванию** (**desc**). |
| Свойства |

| Выберите свойства фотографий, которые должны быть отображены. |
| Использовать обратную навигацию |

| [Y|N] При отмеченной опции будет использоваться обратная постраничная навигацию для списка фотографий. |
| Количество фото на странице |

| Указывается количество фотографий, выводимых на одной странице. Остальные фотографий будут выведены с помощью постраничной навигации. |
| Название шаблона для постраничной навигации |

| Указывается название шаблона для постраничной навигации. |
| **Шаблоны ссылок** |

| |
| Содержимое галереи |

| Указывается адрес страницы просмотра содержимого галереи пользователя (параметр задается при выборе многопользовательского режима). |
| Страница детального просмотра |

| Указывается адрес страницы детального просмотра альбома. |
| Страница слайд-шоу |

| Указывается адрес страницы слайд-шоу. |
| Страница поиска |

| Указывается адрес страницы поиска. |
| Путь к профилю пользователя |

| Указывается путь к странице профиля пользователя фотогалереи. |
| **Настройки отзывов** |

| |
| Разрешить отзывы |

| [Y|N] При отмеченной опции будет доступен функционал отзывов, появятся дополнительные поля.    Дополнительные поля:  |  |  |  | | --- | --- | --- | | Компонент комментариев | **COMMENTS\_TYPE** | Указывается компонент, с помощью которого будут добавляться комментарии:  * **Блоги** (**blog**); * **Форум** (**forum**).  Если указать **Блоги**, то необходимо настроить следущие параметры: **BLOG\_URL**, **PATH\_TO\_BLOG**.   Если указать **Форум**, то необходимо настроить следущие параметры: **FORUM\_ID**, **URL\_TEMPLATES\_READ**, **URL\_TEMPLATES\_PROFILE\_VIEW**, **USE\_CAPTCHA**, **SHOW\_LINK\_TO\_FORUM**, **PREORDER**. | | Количество комментариев на странице | **COMMENTS\_COUNT** | Указывается количество комментариев на странице. | | Путь относительно корня сайта к папке со смайлами | **PATH\_TO\_SMILE** | Указывается путь к папке со смайликами относительно корня сайта. | | Блог для комментариев | **BLOG\_URL** | Указывается один из созданных в системе блогов, который будет использован для комментариев. | | Путь к блогу | **PATH\_TO\_BLOG** | Указывается путь к месту расположения блога. | | ID форума для отзывов | **FORUM\_ID** | Указывается один из созданных в системе форумов, который будет использован для комментариев. | | Страница чтения темы | **URL\_TEMPLATES\_READ** | Указывается адрес страницы чтения темы форума. | | Страница пользователя | **URL\_TEMPLATES\_PROFILE\_VIEW** | Указывается адрес страницы профиля пользователя относительно корня сайта. | | Использовать CAPTCHA | **USE\_CAPTCHA** | [Y|N] При отмеченной опции будет выводиться изображение и поле ввода **CAPTCHA** в форме добавления комментария в публичной части. | | Выводить сообщения в прямом порядке | **PREORDER** | [Y|N] При отмеченной опции собщения будут отсортированы по дате создания по возрастанию. | | Начинать тему текстом элемента | **POST\_FIRST\_MESSAGE** | [Y|N] При отмеченной опции в обсуждении на форуме будет выведено первое сообщение отзыва. | |
| **Настройки кеширования** |

| |
| Тип кеширования |

| Тип кеширования:  * **A** - Авто + Управляемое: автоматически обновляет кеш компонентов в течение заданного времени или при изменении данных; * **Y** - Кешировать: для кеширования необходимо определить время кеширования; * **N** - Не кешировать: кеширования нет в любом случае. |
| Время кеширования (сек.) |

| Время кеширования, указанное в секундах. |
| **Дополнительные настройки** |

| |
| Устанавливать заголовок страницы |

| [Y|N] При отмеченной опции в качестве заголовка страницы будет установлено **Список фотографий**. |
| Отображение имени |

| Указывается шаблон для отображения ФИО пользователя социальной сети. По умолчанию - значение **Формат сайта** (т.е используются значение **Формат имени**, указанное в закладке **Параметры** страницы [Редактирование сайта](/user_help/settings/settings/sites/site_edit.php)). Указав пункт **другое->**, можно задать свой шаблон. Допустимы шаблоны: **#NAME#** - имя, **#LAST\_NAME#** - фамилия, **#SECOND\_NAME#** - отчество, **#NAME\_SHORT#**, **#LAST\_NAME\_SHORT#**, **#SECOND\_NAME\_SHORT#** - сокращенные до одной буквы имя, фамилия и отчество. |
| Использовать дополнительное ограничение доступа |

| [Y|N] При отмеченной опции будет ограничен доступ к детальной информации элементов инфоблока. Группы пользователей, имеющие доступ к детальной информации, указываются в парметре **GROUP\_PERMISSIONS**. |
| Группы пользователей, имеющие доступ к детальной информации |

| Указываются группы пользователей, имеющие доступ к детальной информации. |
| Формат вывода даты |

| Указывается формат показа даты и времени. В выпадающем списке перечислены все возможные варианты показа даты, формируемые внутри компонента. Выбрав пункт *(другое)->*, можно сформировать свой вариант на основании php-функции **date**. |
| Устанавливать статус 404, если не найдены элемент или раздел |

| [Y|N] При отмеченной опции будет установлен статус 404, если не будут найдены элементы или раздел фотогалереи. |
||

|  |  |
| --- |

| --- |
| Дополнительные эскизы |

| Выбираются типы эскизов для просмотра фотографий. |
| Активный эскиз (один из множества дополнительных и основных эскизов) |

| Указывается тип эскиза, с которого начинается просмотр фотографий альбома. |
| Размер галереи |

| Задается размер галереи одного пользователя в Мб (параметр задается при выборе многопользовательского режима). |
| Показывать логин, если не задано имя |

| [Y|N] При отмеченной опции будет отображен логин пользователя, если не задано имя. |
| Размер фотографии-анонса (px) |

| Указывается размер фотографии-анонса в пикселях (px). Размер задается для одной стороны картинки, вторая сторона изображения будет высчитана пропорционально. |
| Показывать навигацию |

| Указывается место отображения навигации:  * **none** - не показывать; * **top** - сверху; * **bottom** - снизу; * **both** - сверху и снизу. |
| Показывать голосования |

| [Y|N] При отмеченной опции будут показаны голосования. |
| Показывать количество показов |

| [Y|N] При отмеченной опции будет отображено количество показов. |
| Показывать количество комментариев |

| [Y|N] При отмеченной опции будет отображено количество комментариев. |
| Максимальный балл |

| Указывается максимально возможный балл, т.е. число возможных оценок. |
| Подписи к баллам |

| Указываются подписи к каждому баллу. В коде вводится массив, в котором задаются подписи к баллам в таком виде:   ``` "VOTE_NAMES" => Array("0","1","2","3","4","5"),  ```  Если подписи заданы, то они будут выведены вместо оценок-цифр. Если массив не задан, то будут использованы значения по умолчанию. |
| В качестве рейтинга показывать |

| Указывается одно из значений, которое должно быть показано в качестве рейтинга:  * **Рейтинг** (**rating**) - высчитывается на основе формулы: **Rating** = (SUM(vote)+3.125\*10) / (COUNT(\*)+10), где:  3.125 - это стартовый рейтинг. То есть изначально (при отсутствии голосов) рейтинг фотографии равен 3.125.  10 - это константа, определяющая количество голосов, "утяжеляющих" первоначальное значение рейтинга (3.125). Это исключает случай, когда, например, трое проголосовавших человека могут вознести или опустить фотографию всего тремя голосами.  При такой формуле расчета значение рейтинга получается более "плавное" и не так скачет при небольшом количестве голосующих. Чем больше голосов, тем больше рейтинг приближается к среднему арифметическому. * **Среднее значение** (**vote\_avg**) - высчитывается как среднее арифметическое всех баллов к фотографии; * **Рейтинг (главного модуля)** (**rating\_main**) - использование [рейтинга главного модуля](/user_help/service/rating/rating_settings.php). **Подробнее:** - см. главу [Рейтинги](http://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=48&CHAPTER_ID=1232);     - в блоге [Рейтинги: создание собственного критерия рейтингования](http://dev.1c-bitrix.ru/community/blogs/hazz/2303.php);    - в блоге [Саморегулируемое сообщество, построенное на двухфакторном рейтинге](http://dev.1c-bitrix.ru/community/blogs/rsv-dev/2386.php). |
| Вид кнопок рейтинга (главного модуля) |

``` "VOTE_NAMES" => Array("0","1","2","3","4","5"),  ```

```
<?$APPLICATION->IncludeComponent("bitrix:photogallery.detail.list.ex","",Array(

		"THUMBNAIL_SIZE" => "120",

		"SHOW_PAGE_NAVIGATION" => "none",

		"SHOW_RATING" => "Y",

		"SHOW_SHOWS" => "Y",

		"SHOW_COMMENTS" => "Y",

		"MAX_VOTE" => "5",

		"VOTE_NAMES" => array("1","2","3","4","5"),

		"DISPLAY_AS_RATING" => "rating",

		"RATING_MAIN_TYPE" => "",

		"IBLOCK_TYPE" => "gallery",

		"IBLOCK_ID" => "10",

		"BEHAVIOUR" => "USER",

		"SET_TITLE" => "Y",

		"CACHE_TYPE" => "A",

		"CACHE_TIME" => "3600",

		"CACHE_NOTES" => "",

		"USER_ALIAS" => $_REQUEST["USER_ALIAS"],

		"SECTION_ID" => $_REQUEST["SECTION_ID"],

		"ELEMENT_LAST_TYPE" => "period",

		"ELEMENTS_LAST_TIME_FROM" => "",

		"ELEMENTS_LAST_TIME_TO" => "",

		"ELEMENT_SORT_FIELD" => "SORT",

		"ELEMENT_SORT_ORDER" => "asc",

		"ELEMENT_SORT_FIELD1" => "SHOW_COUNTER",

		"ELEMENT_SORT_ORDER1" => "asc",

		"PROPERTY_CODE" => array(),

		"GALLERY_URL" => "gallery.php?USER_ALIAS=#USER_ALIAS#",

		"DETAIL_URL" => "detail.php?SECTION_ID=#SECTION_ID#&ELEMENT_ID=#ELEMENT_ID#",

		"DETAIL_SLIDE_SHOW_URL" => "slide_show.php?SECTION_ID=#SECTION_ID#&ELEMENT_ID=#ELEMENT_ID#",

		"SEARCH_URL" => "search.php",

		"USE_PERMISSIONS" => "Y",

		"GROUP_PERMISSIONS" => array(),

		"USE_DESC_PAGE" => "Y",

		"PAGE_ELEMENTS" => "50",

		"PAGE_NAVIGATION_TEMPLATE" => "",

		"DATE_TIME_FORMAT" => "d.m.Y",

		"SET_STATUS_404" => "Y",

		"ADDITIONAL_SIGHTS" => array(),

		"PICTURES_SIGHT" => "real",

		"GALLERY_SIZE" => "",

		"PATH_TO_USER" => "/company/personal/user/#USER_ID#",

		"NAME_TEMPLATE" => "#NOBR##LAST_NAME# #NAME##/NOBR#",

		"SHOW_LOGIN" => "Y"

	),

false

);?> 


```