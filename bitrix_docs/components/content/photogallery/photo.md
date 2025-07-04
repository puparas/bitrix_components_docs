|  |  |  |
| --- |

| --- |
| **Поле** |

| **Описание** |
| **Основные параметры** |

| |
| Тип инфоблока |

| Указывается один из созданных в системе типов информационного блока. После выбора инфоблока автоматически произойдёт перезагрузка формы для вывода списка инфоблоков выбранного типа. Если автоматическая перезагрузка не произошла, нажмите кнопку **ОК**. |
| Инфоблок |

| Для выбранного типа инфоблока выбирается нужный информационный блок, фотографии из которого будут выводиться. Если вместо инфоблока будет выбрано *другое*, то в поле ниже необходимо указать идентификатор нужного инфоблока и нажать кнопку **ОК**. |
| **Управление адресами страниц** |

| |
| Включить поддержку ЧПУ |

| [Y|N] При отмеченной опции будет включена поддержка ЧПУ.     Если режим поддержки ЧПУ **включен**, то необходимо настроить следующие параметры:    Настраиваемые параметры при включенном режиме поддержки ЧПУ:  |  |  |  | | --- | --- | --- | | Каталог ЧПУ (относительно корня сайта) | **SEF\_FOLDER** | Каталог ЧПУ: путь до папки, с которой работает компонент. Этот путь может как совпадать с физическим путём, так и не совпадать. | | Адреса страниц | **SEF\_URL\_TEMPLATES** | Указываются адреса следующих страниц:  * **sections\_top** - страница списка разделов с TOP\'ом фотографий; * **section** - страница раздела фотогалереи; * **detail** - страница детального просмотра фотографии. |  **SEF\_FOLDER**, **SEF\_URL\_TEMPLATES**. |
| Имена переменных |

| Имена переменных для управления страницами. |
| **Управление режимом AJAX** |

| |
| Включить режим AJAX |

| [Y|N] При установленной опции для компонента будет включен режим AJAX. |
| Включить прокрутку к началу компонента |

| [Y|N] Если пользователь совершит AJAX-переход, то при установленой опции по окончании загрузки произойдет прокрутка к началу компонента. |
| Включить подгрузку стилей |

| [Y|N] Если параметр принимает значение "Y", то при совершении AJAX-переходов будет происходить подгрузка и обработка списка стилей, вызванных компонентом. |
| Включить эмуляцию навигации браузера |

| [Y|N] Когда пользователь выполняет AJAX-переходы, то при включенной опции можно использовать кнопки браузера **Назад** и **Вперед**. |
| **Настройки кеширования** |

| |
| Тип кеширования |

| Тип кеширования:  * **A** - Авто + Управляемое: автоматически обновляет кеш компонентов в течение заданного времени или при изменении данных; * **Y** - Кешировать: для кеширования необходимо определить время кеширования; * **N** - Не кешировать: кеширования нет в любом случае. |
| Время кеширования (сек.) |

| Время кеширования, указанное в секундах. |
| Кэшировать при установленном фильтре |

| [Y|N] При отмеченной опции каждый результат, полученный из фильтра, будет кешироваться. |
| Учитывать права доступа |

| [Y|N] При отмеченной опции будут учитываться права доступа при кешировании. |
| **Дополнительные настройки** |

| |
| Устанавливать заголовок страницы |

| [Y|N] При отмеченной опции в качестве заголовка страницы будет установлено **Фотогалерея**. |
| Устанавливать в заголовках ответа время модификации страницы |

| [Y|N] При отмеченной опции http-ответ сервера будет содержать время последнего изменения страницы ([заголовок Last-Modified](http://last-modified.com/ru/if-modified-since.html)). |
| Использовать дополнительное ограничение доступа |

| [Y|N] При отмеченной опции    Станет активным поле **Группы пользователей, имеющие доступ к детальной информации**.    |  |  |  | | --- | --- | --- | | Группы пользователей, имеющие доступ к детальной информации | **GROUP\_PERMISSIONS** | Указываются группы пользователей, имеющие доступ к детальной информации. |  будет ограничен доступ к детальной информации элементов инфоблока. |
| **Настройки голосования** |

| |
| Разрешить голосование |

| [Y|N] При отмеченной опции посетители смогут голосовать за фотографии, выставляя баллы, на странице с детальной информацией. При установленной опции становятся доступными следующие поля:    Доступные поля:  |  |  |  | | --- | --- | --- | | Максимальный балл | **MAX\_VOTE** | Указывается максимально возможный балл, т.е. число возможных оценок. | | Подписи к баллам | **VOTE\_NAMES** | Указываются подписи к каждому баллу. В коде вводится массив, в котором задаются подписи к баллам в таком виде:    ``` "VOTE_NAMES" => Array("0","1","2","3","4","5"),  ```  Если подписи заданы, то они будут выведены вместо оценок-цифр. Если массив не задан, то будут использованы значения по умолчанию. |  **MAX\_VOTE** и **VOTE\_NAMES**. |
| **Настройки отзывов** |

| |
| Разрешить отзывы |

| [Y|N] При отмеченной опции будет доступен функционал отзывов.    Функционал отзывов:  |  |  |  | | --- | --- | --- | | Количество сообщений на одной странице | **MESSAGES\_PER\_PAGE** | Параметр определяет количество выводимых на одной странице сообщений отзывов. | | Использовать CAPTCHA | **USE\_CAPTCHA** | [Y|N] При отмеченной опции будет выводиться изображение и поле ввода **CAPTCHA** в форме добавления отзыва в публичной части. | | Путь относительно корня сайта к папке со смайлами | **PATH\_TO\_SMILE** | Задается путь к папке со смайликами относительно корня сайта. | | ID форума для отзывов | **FORUM\_ID** | Указывается идентификатор форума, в котором будут храниться отзывы пользователей. | | Страница чтения темы (пусто - получить из настроек форума) | **URL\_TEMPLATES\_READ** | Указывается относительный путь к странице чтения темы на форуме. Если поле пусто, путь к странице будет получен из настроек форума. | | Показать ссылку на форум | **SHOW\_LINK\_TO\_FORUM** | [Y|N] При отмеченной опции на странице фотографии будет отображена ссылка на форум обсуждения. | | Начинать тему текстом элемента | **POST\_FIRST\_MESSAGE** | [Y|N] При отмеченной опции сообщение в отзыве будет начинаться с анонса фотографии. | |
| **Настройки фильтра** |

| |
| Показывать фильтр |

| [Y|N] При отмеченной опции становятся доступными поля настройки фильтра.    Поля настройки фильтра:  |  |  |  | | --- | --- | --- | | Фильтр | **FILTER\_NAME** | Указывается имя переменной, в которой передается массив параметров из фильтра. Служит для определения выходящих из фильтра элементов. Если поле оставлено пустым, то используется значение по умолчанию. | | Поля | **FILTER\_FIELD\_CODE** | Указываются поля элементов инфоблока, по которым будет возможна фильтрация. Заполняется из публичной части редактора, удерживая клавишу Ctrl либо в коде, указывая массив:  ``` Array("NAME","PREVIEW_TEXT","PREVIEW_PICTURE","DETAIL_TEXT",""), ```  При выборе пункта **(не выбрано)->** и без указания вычисления полей в строках ниже (т.е. если задан пустой массив), на странице списка будут выведены поля по умолчанию. | | Свойства | **FILTER\_PROPERTY\_CODE** | Указываются свойства элементов инфоблока, по которым будет возможна фильтрация. Заполняется из публичной части редактора, удерживая клавишу Ctrl либо в коде, указывая массив. При выборе пункта **(не выбрано)->** и без указания вычисления полей в строках ниже, на странице детального просмотра свойства не будут выведены. | |
| **Настройки TOP'а** |

| |
| Максимальное количество выводимых разделов |

| Задается максимальное количество выводимых разделов. |
| Максимальное количество фотографий, выводимых в каждом разделе |

| Задается максимальное количество фотографий, выводимых в TOP’е элементов в каждом разделе. |
| Количество фотографий, выводимых в одной строке таблицы списка разделов |

| Указывается количество фотографий, выводимых в одной строке таблицы списка разделов. |
| По какому полю сортируем разделы |

| Указывается поле, по которому будет происходить сортировка разделов в TOP’е элементов:  * **SORT** - по индексу сортировки; * **TIMESTAMP\_X** - по дате изменения; * **NAME** - по названию; * **ID** - по идентификатору; * **DEPTH\_LEVEL** - по уровню вложенности папки.  Можно указать код любого другого поля. |
| Порядок сортировки разделов |

| Задается порядок сортировки разделов:  * **ASC** – **По возрастанию**; * **DESC** – **По убыванию**. |
| По какому полю сортируем фотографии |

| Указывается поле, по которому будет происходить сортировка фотографий внутри каждого раздела:  * **SHOWS** – по количеству просмотров в среднем; * **SORT** – по индексу сортировки; * **TIMESTAMP\_X** – по дате последнего изменения; * **NAME** – по названию; * **ID** – по идентификатору; * **ACTIVE\_FROM** – по дате активности с; * **ACTIVE\_TO** – по дате активности по. |
| Порядок сортировки фотографий в разделе |

| Задается порядок сортировки фотографий в разделе:  * **ASC** – **По возрастанию**; * **DESC** – **По убыванию**. |
| Поля |

| Указываются поля, которые будут отображены на странице TOP'а элементов. Заполняется из публичной части редактора, удерживая клавишу Ctrl либо в коде, указывая массив:  ``` Array("NAME","PREVIEW_TEXT","PREVIEW_PICTURE","DETAIL_TEXT",""), ```  При выборе пункта **(не выбрано)->** и без указания вычисления полей в строках ниже (т.е. если задан пустой массив), на странице списка будут выведены поля по умолчанию. |
| Свойства |

| Указываются свойства, которые будут отображены на странице TOP'а элементов. Заполняется из публичной части редактора, удерживая клавишу Ctrl либо в коде, указывая массив. При выборе пункта **(не выбрано)->** и без указания вычисления полей в строках ниже, на странице детального просмотра свойства не будут выведены. |
| **Настройки списка** |

| |
| Количество элементов на странице |

| Указывается количество элементов, выводимых на одной странице. Остальные элементы будут выведены с помощью постраничной навигации. |
| Количество фотографий, выводимых в одной строке таблицы раздела |

| Указывается количество фотографий, выводимых в одной строке таблицы раздела. |
| По какому полю сортируем фотографии |

| Указывается поле, по которому будет происходить сортировка фотографий внутри каждого раздела:  * **SHOWS** – по количеству просмотров в среднем; * **SORT** – по индексу сортировки; * **TIMESTAMP\_X** – по дате последнего изменения; * **NAME** – по названию; * **ID** – по идентификатору; * **ACTIVE\_FROM** – по дате активности с; * **ACTIVE\_TO** – по дате активности по. |
| Порядок сортировки фотографий в разделе |

| Задается порядок сортировки фотографий в разделе:  * **ASC** – **По возрастанию**; * **DESC** – **По убыванию**. |
| Поля |

| Указываются поля, которые будут отображены на странице детального просмотра. Заполняется из публичной части редактора, удерживая клавишу Ctrl либо в коде, указывая массив:  ``` Array("NAME","PREVIEW_TEXT","PREVIEW_PICTURE","DETAIL_TEXT",""), ```  При выборе пункта **(не выбрано)->** и без указания вычисления полей в строках ниже (т.е. если задан пустой массив), на странице списка будут выведены поля по умолчанию. |
| Свойства |

| Указываются свойства, которые будут отображены на странице детального просмотра. Заполняется из публичной части редактора, удерживая клавишу Ctrl либо в коде, указывая массив. При выборе пункта **(не выбрано)->** и без указания вычисления полей в строках ниже, на странице детального просмотра свойства не будут выведены. |
| Установить заголовок окна браузера из свойства |

| Укажите свойство, которое будет использоваться в качестве заголовка окна браузера при просмотре списка фотографий. |
| **Настройки детального просмотра** |

| |
| Установить ключевые слова страницы из свойства |

| Среди всех свойств, определенных для данного инфоблока, выбирается то, в котором содержатся ключевые слова. |
| Установить описание страницы из свойства |

| Среди всех свойств, определенных для данного инфоблока, выбирается то, в котором содержится описание. |
| Установить заголовок окна браузера из свойства |

| Среди всех свойств, определенных для данного инфоблока, выбирается то, в котором содержится заголовок окна браузера. |
| Поля |

| Указываются поля, которые будут отображены на странице детального просмотра. Заполняется из публичной части редактора, удерживая клавишу Ctrl либо в коде, указывая массив:  ``` Array("NAME","PREVIEW_TEXT","PREVIEW_PICTURE","DETAIL_TEXT",""), ```  При выборе пункта **(не выбрано)->** и без указания вычисления полей в строках ниже (т.е. если задан пустой массив), на странице списка будут выведены поля по умолчанию. |
| Свойства |

| Указываются свойства, которые будут отображены на странице детального просмотра. Заполняется из публичной части редактора, удерживая клавишу Ctrl либо в коде, указывая массив. При выборе пункта **(не выбрано)->** и без указания вычисления полей в строках ниже, на странице детального просмотра свойства не будут выведены. |
| **Настройки постраничной навигации** |

| |
| Выводить над списком |

| [Y|N] При отмеченной опции постраничная навигация будет выведена вверху страницы, над списком. |
| Выводить под списком |

| [Y|N] При отмеченной опции постраничная навигация будет выведена внизу страницы, под списком. |
| Название категорий |

| Задается название категорий, по которым происходит перемещение при детальном просмотре (например, страница, глава и др.). |
| Выводить всегда |

| [Y|N] При отмеченной опции постраничная навигация будет выводиться всегда, даже если все элементы помещаются на одной странице. |
| Название шаблона |

| Указывается название шаблона постраничной навигации. |
| Использовать обратную навигацию |

| [Y|N] При отмеченной опции будет использоваться обратная навигация. Для обратной навигации в системе происходит обратный отсчет страниц (последняя страница считается первой). Таким образом, постоянно меняется лишь последняя страница при добавлении нового элемента. Это верно, если новые элементы попадают всегда вверх списка (отсортированы по дате начала активности по убыванию). |
| Время кеширования страниц для обратной навигации |

| Задается время кеширования страниц для обратной навигации в сегундах. |
| Показывать ссылку "Все" |

| [Y|N] При отмеченной опции в постраничную навигацию будет добавлена ссылка **Все**, с помощью которой можно отобразить все фотографии. |
| Включить обработку ссылок |

| [Y|N] При отмеченной опции доступна обработка ссылок для постраничной навигации. Станут активны дополнительные поля.    Дополнительные поля:  |  |  |  | | --- | --- | --- | | Url для построения ссылок (по умолчанию - автоматически) | **PAGER\_BASE\_LINK** | Задается адрес для построения ссылок. Если в параметре ничего не указывать, то адрес будет построен автоматически. | | Имя массива с переменными для построения ссылок в постраничной навигации | **PAGER\_PARAMS\_NAME** | Задается имя переменной, в которой передается массив с переменными для построения ссылок компонентом постраничной навигации. | |
| **Настройки 404 ошибки** |

| |
| Устанавливать статус 404 |

| [Y|N] Опция служит для включения обработки ошибки 404 в компоненте. |
| Показ специальной страницы |

``` "VOTE_NAMES" => Array("0","1","2","3","4","5"),  ```

``` Array("NAME","PREVIEW_TEXT","PREVIEW_PICTURE","DETAIL_TEXT",""), ```

``` Array("NAME","PREVIEW_TEXT","PREVIEW_PICTURE","DETAIL_TEXT",""), ```

``` Array("NAME","PREVIEW_TEXT","PREVIEW_PICTURE","DETAIL_TEXT",""), ```

``` Array("NAME","PREVIEW_TEXT","PREVIEW_PICTURE","DETAIL_TEXT",""), ```

```
<?$APPLICATION->IncludeComponent("bitrix:photo","",Array(

		"AJAX_MODE" => "Y",

		"SEF_MODE" => "Y",

		"IBLOCK_TYPE" => "photos",

		"IBLOCK_ID" => "22",

		"USE_RATING" => "Y",

		"USE_REVIEW" => "Y",

		"USE_FILTER" => "Y",

		"SECTION_COUNT" => "20",

		"TOP_ELEMENT_COUNT" => "9",

		"TOP_LINE_ELEMENT_COUNT" => "3",

		"SECTION_SORT_FIELD" => "sort",

		"SECTION_SORT_ORDER" => "asc",

		"TOP_ELEMENT_SORT_FIELD" => "sort",

		"TOP_ELEMENT_SORT_ORDER" => "asc",

		"TOP_FIELD_CODE" => Array(),

		"TOP_PROPERTY_CODE" => Array(),

		"SECTION_PAGE_ELEMENT_COUNT" => "20",

		"SECTION_LINE_ELEMENT_COUNT" => "3",

		"ELEMENT_SORT_FIELD" => "sort",

		"ELEMENT_SORT_ORDER" => "asc",

		"LIST_FIELD_CODE" => Array(),

		"LIST_PROPERTY_CODE" => Array(),

		"LIST_BROWSER_TITLE" => "-",

		"META_KEYWORDS" => "-",

		"META_DESCRIPTION" => "-",

		"BROWSER_TITLE" => "-",

		"DETAIL_FIELD_CODE" => Array(),

		"DETAIL_PROPERTY_CODE" => Array(),

		"SET_TITLE" => "Y",

		"PAGER_BASE_LINK_ENABLE" => "Y",

		"SET_STATUS_404" => "Y",

		"SHOW_404" => "Y",

		"MESSAGE_404" => "",

		"PAGER_BASE_LINK" => "",

		"PAGER_PARAMS_NAME" => "arrPager",

		"SET_LAST_MODIFIED" => "Y",

		"USE_PERMISSIONS" => "Y",

		"GROUP_PERMISSIONS" => Array("1"),

		"CACHE_TYPE" => "A",

		"CACHE_TIME" => "3600",

		"CACHE_FILTER" => "Y",

		"CACHE_GROUPS" => "Y",

		"DISPLAY_TOP_PAGER" => "N",

		"DISPLAY_BOTTOM_PAGER" => "Y",

		"PAGER_TITLE" => "Фотографии",

		"PAGER_SHOW_ALWAYS" => "Y",

		"PAGER_TEMPLATE" => "",

		"PAGER_DESC_NUMBERING" => "N",

		"PAGER_DESC_NUMBERING_CACHE_TIME" => "36000",

		"PAGER_SHOW_ALL" => "Y",

		"FILTER_NAME" => "",

		"FILTER_FIELD_CODE" => Array(),

		"FILTER_PROPERTY_CODE" => Array(),

		"MAX_VOTE" => "5",

		"VOTE_NAMES" => Array("0", "1", "2", "3", "4"),

		"MESSAGES_PER_PAGE" => "10",

		"USE_CAPTCHA" => "Y",

		"PATH_TO_SMILE" => "/bitrix/images/forum/smile/",

		"FORUM_ID" => "1",

		"URL_TEMPLATES_READ" => "",

		"SHOW_LINK_TO_FORUM" => "Y",

		"POST_FIRST_MESSAGE" => "Y",

		"AJAX_OPTION_JUMP" => "N",

		"AJAX_OPTION_STYLE" => "Y",

		"AJAX_OPTION_HISTORY" => "N",

		"AJAX_OPTION_ADDITIONAL" => "",

		"SEF_FOLDER" => "/",

		"SEF_URL_TEMPLATES" => Array(

			"sections_top" => "",

			"section" => "#SECTION_ID#/",

			"detail" => "#SECTION_ID#/#ELEMENT_ID#/"

		),

		"VARIABLE_ALIASES" => Array(

			"section" => Array(),

			"detail" => Array(),

			"sections_top" => Array(),

		)

	)

);?>


```