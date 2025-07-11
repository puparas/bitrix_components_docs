|  |  |  |
| --- |

| --- |
| **Поле** |

| **Описание** |
| **Основные параметры** |

| |
| Тип инфо-блока |

| Указывается один из созданных в системе типов информационного блока. |
| Инфо-блок |

| Для выбранного типа инфоблока указывается идентификатор информационного блока, фотографии из которого будут выводиться. |
| ID раздела |

| Указывается числовой код, в котором передается идентификатор раздела. Поле может быть оставлено пустым, если указан **Код раздела**. |
| ID элемента |

| Указывается числовой код, в котором передается идентификатор элемента. Поле может быть оставлено пустым, если указан **Код элемента**. |
| Код раздела |

| Указывается символьный код раздела, из которого будут выбраны фотографии. Поле может быть оставлено пустым, если указан **ID раздела**. |
| Код элемента |

| Указывается символьный код элемента, из которого будут выбраны фотографии. Поле может быть оставлено пустым, если указан **ID элемента**. |
| **Источник данных** |

| |
| По какому полю отсортировать фотографии для ссылок "след." и "пред." |

| Указывается поле, по которому будут отсортированы фотографии для ссылок "следующая" и "предыдущая":  * **SHOWS** – по количеству просмотров в среднем; * **SORT** – по индексу сортировки; * **TIMESTAMP\_X** – по дате последнего изменения; * **NAME** – по названию; * **ID** – по идентификатору; * **ACTIVE\_FROM** – по дате активности с; * **ACTIVE\_TO** – по дате активности по. |
| В каком порядке отсортировать фотографии для ссылок "след." и "пред." |

| Задается порядок сортировки фотографий для ссылок "следующая" и "предыдущая":  * **ASC** – **По возрастанию**; * **DESC** – **По убыванию**. |
| Поля |

| Указываются поля, которые будут отображены на странице. Заполняется из публичной части редактора, удерживая клавишу Ctrl либо в коде, указывая массив:  ``` Array("NAME","PREVIEW_TEXT","PREVIEW_PICTURE","DETAIL_TEXT",""), ```  При выборе пункта **(не выбрано)->** и без указания вычисления полей в строках ниже (т.е. если задан пустой массив), на странице списка будут выведены поля по умолчанию. |
| Свойства |

| Указываются свойства, которые будут отображены на странице. Заполняется из публичной части редактора, удерживая клавишу Ctrl либо в коде, указывая массив. При выборе пункта **(не выбрано)->** и без указания вычисления полей в строках ниже, на странице детального просмотра свойства не будут выведены. |
| **Шаблоны ссылок** |

| |
| URL, ведущий на страницу с содержимым раздела |

| Указывается адрес страницы с содержимым раздела. |
| URL, ведущий на страницу с содержимым элемента раздела |

| Указывается адрес страницы с содержимым элемента раздела. |
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
| Учитывать права доступа |

| [Y|N] При отмеченной опции будут учитываться права доступа при кешировании. |
| **Дополнительные настройки** |

| |
| Установить ключевые слова страницы из свойства |

| Среди всех свойств, определенных для данного инфоблока, выбирается то, в котором содержатся ключевые слова. |
| Установить описание страницы из свойства |

| Среди всех свойств, определенных для данного инфоблока, выбирается то, в котором содержится описание. |
| Установить заголовок окна браузера из свойства |

| Среди всех свойств, определенных для данного инфоблока, выбирается то, в котором содержится заголовок окна браузера. |
| Устанавливать заголовок страницы |

| [Y|N] При отмеченной опции в качестве заголовка страницы будет установлено название фотографии. |
| Устанавливать в заголовках ответа время модификации страницы |

| [Y|N] При отмеченной опции http-ответ сервера будет содержать время последнего изменения страницы ([заголовок Last-Modified](http://last-modified.com/ru/if-modified-since.html)). |
| **Настройки 404 ошибки** |

| |
| Устанавливать статус 404 |

| [Y|N] Опция служит для включения обработки ошибки 404 в компоненте. |
| Показ специальной страницы |

``` Array("NAME","PREVIEW_TEXT","PREVIEW_PICTURE","DETAIL_TEXT",""), ```

```
<?$APPLICATION->IncludeComponent("bitrix:photo.detail","",Array(

		"AJAX_MODE" => "N",

		"IBLOCK_TYPE" => "photos",

		"IBLOCK_ID" => "22",

		"SECTION_ID" => $_REQUEST["SECTION_ID"],

		"ELEMENT_ID" => $_REQUEST["ELEMENT_ID"],

		"SECTION_CODE" => "",

		"ELEMENT_CODE" => "",

		"ELEMENT_SORT_FIELD" => "sort",

		"ELEMENT_SORT_ORDER" => "asc",

		"FIELD_CODE" => Array(),

		"PROPERTY_CODE" => Array(),

		"SECTION_URL" => "",

		"DETAIL_URL" => "",

		"META_KEYWORDS" => "-",

		"META_DESCRIPTION" => "-",

		"BROWSER_TITLE" => "-",

		"SET_TITLE" => "Y",

		"SET_STATUS_404" => "Y",

		"SHOW_404" => "Y",

		"MESSAGE_404" => "",

		"SET_LAST_MODIFIED" => "Y",

		"CACHE_TYPE" => "A",

		"CACHE_TIME" => "3600",

		"CACHE_GROUPS" => "Y",

		"AJAX_OPTION_JUMP" => "N",

		"AJAX_OPTION_STYLE" => "Y",

		"AJAX_OPTION_HISTORY" => "N"

	),

);?>


```