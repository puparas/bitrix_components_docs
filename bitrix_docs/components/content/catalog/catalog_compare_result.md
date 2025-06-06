# Таблица сравнения

Документация для разработчиков

[Документация для разработчиков](https://dev.1c-bitrix.ru/api_help/)
[Документация по D7](https://dev.1c-bitrix.ru/api_d7/)
[Документация по REST](https://dev.1c-bitrix.ru/rest_help/)
[Пользовательская документация](https://dev.1c-bitrix.ru/user_help/)

Темная тема

[Основные сведения](/user_help/index.php)
[Реализация и системные требования](/user_help/reqintro.php)

[Справочная система и документация](/user_help/help/index.php)

[Контент](/user_help/content/index.php)

[Сайты 24](/user_help/sites24/index.php)

[Маркетинг](/user_help/marketing/index.php)

[Магазин](/user_help/store/index.php)

[Клиенты](/user_help/clients/index.php)

[Сервисы](/user_help/service/index.php)

[Веб-аналитика](/user_help/statistic/index.php)

[Marketplace](/user_help/marketplace/index.php)

[Настройки](/user_help/settings/index.php)

[Компоненты](/user_help/components/index.php)

[CRM (КП)](/user_help/components/crm/index.php)

[Корпоративный портал (КП)](/user_help/components/intranet/index.php)

[Сайты 24](/user_help/components/landing/index.php)

[Контент](/user_help/components/content/index.php)

[Агрегатор библиотек документов (КП)](/user_help/components/content/webdav/index.php)

[Задачи 2.0 (КП)](/user_help/components/content/tasks/index.php)

[Статьи и новости](/user_help/components/content/articles_and_news/index.php)

[Фотогалерея](/user_help/components/content/photogallery/index.php)

[Фотогалерея 2.0](/user_help/components/content/photogallery2/index.php)

[Каталог](/user_help/components/content/catalog/index.php)

[Структура разделов](/user_help/components/content/catalog/catalog_section_list.php)
[Элементы раздела](/user_help/components/content/catalog/catalog_section.php)
[Каталог (комплексный компонент)](/user_help/components/content/catalog/catalog.php)
[Поиск по каталогу](/user_help/components/content/catalog/catalog_search.php)
[Бренды](/user_help/components/content/catalog/catalog_brandblock.php)
[Элемент каталога детально](/user_help/components/content/catalog/catalog_element.php)
[Список сравниваемых элементов каталога](/user_help/components/content/catalog/catalog_compare_list.php)
[Таблица сравнения](/user_help/components/content/catalog/catalog_compare_result.php)
[Умный фильтр](/user_help/components/content/catalog/smart_filter.php)
[Фильтр по элементам](/user_help/components/content/catalog/catalog_filter.php)
[Список информационных блоков заданного типа](/user_help/components/content/catalog/catalog_main.php)
[top элементов каталога](/user_help/components/content/catalog/catalog_top.php)
[top элементов каталога по параметру (магазин) - не поддерживается с версии 12.5](/user_help/components/content/catalog/store_catalog_top.php)
[Конструктор наборов](/user_help/components/content/catalog/catalog_set_constructor.php)
[Разделы с top'ом элементов](/user_help/components/content/catalog/catalog_sections_top.php)
[Список связанных элементов](/user_help/components/content/catalog/catalog_link_list.php)

[Универсальные списки](/user_help/components/content/lists/index.php)

[Google Maps](/user_help/components/content/google_maps/index.php)

[Highload инфоблоки](/user_help/components/content/highload/index.php)

[RSS](/user_help/components/content/rss/index.php)

[Wiki](/user_help/components/content/wiki/index.php)

[Валюты](/user_help/components/content/currency/index.php)

[Добавление элементов](/user_help/components/content/adding/index.php)

[Инфоблоки](/user_help/components/content/infoblocks/index.php)

[Календарь событий](/user_help/components/content/calendar/index.php)

[Карта сайта](/user_help/components/content/sitemap/index.php)

[Медиа](/user_help/components/content/media/index.php)

[Яндекс.Карты](/user_help/components/content/yandex_map/index.php)

[Обмен с 1С](/user_help/components/content/1c_exchange/index.php)

[Социальные сервисы](/user_help/components/content/social_services/index.php)

[Сервисы](/user_help/components/services/index.php)

[Общение](/user_help/components/obschenie/index.php)

[Магазин](/user_help/components/magazin/index.php)

[Служебные](/user_help/components/sluzhebnie/index.php)

[Описание компонентов решений](/user_help/description_decisions/index.php)

[Дополнительно](/user_help/additional/index.php)

[Компоненты](/user_help/components/index.php)

[Контент](/user_help/components/content/index.php)

[Каталог](/user_help/components/content/catalog/index.php)

Таблица сравнения

# Таблица сравнения

### Описание **catalog.compare.result**

Компонент выводит таблицу сравниваемых элементов. Компонент стандартный, входит в дистрибутив модуля и содержит два шаблона: **.default** и **bootstrap\_v4**.

В визуальном редакторе компонент расположен по пути *Контент > Каталог > Таблица сравнения*.

Компонент относится к модулю [Информационные блоки](/user_help/content/iblock/index.php).

### Параметры

|  |  |  |
| --- | --- | --- |
| **Поле** | **Параметр** | **Описание** |
| **Источник данных** | | |
| Уникальное имя для списка сравнения | **NAME** | Задается имя переменной, в которой передается список сравниваемых элементов. По умолчанию **CATALOG\_COMPARE\_LIST**. |
| Тип инфо-блока | **IBLOCK\_TYPE** | Указывается один из созданных в системе типов информационных блоков. |
| Инфо-блок | **IBLOCK\_ID** | Для выбранного типа инфоблоков указывается идентификатор информационного блока, элементы которого будут отфильтрованы. |
| Поля | **FIELD\_CODE** | Указываются поля элементов (товаров), по которым будет происходить сравнение в таблице сравнения. Заполняется из публичной части редактора, удерживая клавишу Ctrl либо в коде, указывая массив:  ``` Array("NAME","PREVIEW_TEXT","PREVIEW_PICTURE","DETAIL_TEXT",""), ```  При выборе пункта **(не выбрано)->** и без указания полей в строках (т.е. если задан пустой массив), будут выведены поля по умолчанию. |
| Свойства | **PROPERTY\_CODE** | Указываются свойства инфоблока, которые будут отображены при показе в качестве полей фильтра. Заполняется из публичной части редактора, удерживая клавишу Ctrl либо в коде, указывая массив. При выборе пункта **(не выбрано)->** и без указания кодов свойств в строках, свойства выведены не будут. |
| Поля предложений | **OFFERS\_FIELD\_CODE** | Выбираются поля предложений. С помощью клавиши Ctrl можно выбрать несколько значений. Данный параметр появляется при настройке компонента на инфоблок с поддержкой SKU. |
| Свойства предложений | **OFFERS\_PROPERTY\_CODE** | Указываются свойства предложений. Можно добавлять свои. Данный параметр появляется при настройке компонента на инфоблок с поддержкой SKU. |
| По какому полю сортируем элементы | **ELEMENT\_SORT\_FIELD** | Указывается поле, по которому будет происходить сортировка элементов:  * **shows** – по количеству просмотров в среднем; * **sort** – по индексу сортировки; * **timestamp\_x** – по дате изменения; * **name** – по названию; * **id** – по идентификатору; * **active\_from** – по дате активности с; * **active\_to** – по дате активности по; * **CATALOG\_AVAILABLE** – по доступности к покупке. * **SCALED\_PRICE\_[ID]** – по типу цен (вместо [ID] - идентификатор типа цены) |
| Порядок сортировки элементов | **ELEMENT\_SORT\_ORDER** | Задается порядок сортировки элементов:  * **asc** – **По возрастанию**; * **desc** – **По убыванию**. |
| **Внешний вид** | | |
| Цветовая тема | **TEMPLATE\_THEME** | Задается цветовая схема для отображения таблицы сравнения. По умолчанию используется синяя схема (blue). |
| **Управление режимом AJAX** | | |
| Включить режим AJAX | **AJAX\_MODE** | [Y|N] При установленной опции для компонента будет включен режим AJAX. |
| Включить прокрутку к началу компонента | **AJAX\_OPTION\_JUMP** | [Y|N] Если пользователь совершит AJAX-переход, то при установленой опции по окончании загрузки произойдет прокрутка к началу компонента. |
| Включить подгрузку стилей | **AJAX\_OPTION\_STYLE** | [Y|N] Если параметр принимает значение "Y", то при совершении AJAX-переходов будет происходить подгрузка и обработка списка стилей, вызванных компонентом. |
| Включить эмуляцию навигации браузера | **AJAX\_OPTION\_HISTORY** | [Y|N] Когда пользователь выполняет AJAX-переходы, то при включенной опции можно использовать кнопки браузера **Назад** и **Вперед**. |
| **Дополнительные настройки** | | |
| URL, ведущий на страницу с содержимым элемента раздела | **DETAIL\_URL** | Указывается путь к странице с детальным описанием элемента раздела. |
| Название переменной, в которой передается код группы | **SECTION\_ID\_VARIABLE** | Задается имя переменной, в которой будет передаваться идентификатор раздела. |
| Выводить список элементов инфоблока | **DISPLAY\_ELEMENT\_SELECT\_BOX** | [Y|N] При отмеченной опции после таблицы будет добавлен список элементов текущего инфоблока, которые можно добавить в таблицу. |
| По какому полю сортируем список элементов | **ELEMENT\_SORT\_FIELD\_BOX** | Указывается поле, по которому будет происходить сортировка элементов:  * **shows** – по количеству просмотров в среднем; * **sort** – по индексу сортировки; * **timestamp\_x** – по дате изменения; * **name** – по названию; * **id** – по идентификатору; * **active\_from** – по дате активности с; * **active\_to** – по дате активности по; * **CATALOG\_AVAILABLE** – по доступности к покупке. * **SCALED\_PRICE\_[ID]** – по типу цен (вместо [ID] - идентификатор типа цены) |
| Порядок сортировки списка элементов | **ELEMENT\_SORT\_ORDER\_BOX** | Задается порядок сортировки элементов:  * **asc** – **По возрастанию**; * **desc** – **По убыванию**. |
| Поле для второй сортировки списка элементов | **ELEMENT\_SORT\_FIELD\_BOX2** | Указывается поле, по которому будет происходить сортировка элементов:  * **shows** – по количеству просмотров в среднем; * **sort** – по индексу сортировки; * **timestamp\_x** – по дате изменения; * **name** – по названию; * **id** – по идентификатору; * **active\_from** – по дате активности с; * **active\_to** – по дате активности по; * **CATALOG\_AVAILABLE** – по доступности к покупке. * **SCALED\_PRICE\_[ID]** – по типу цен (вместо [ID] - идентификатор типа цены) |
| Порядок второй сортировки списка элементов | **ELEMENT\_SORT\_ORDER\_BOX2** | Задается порядок сортировки элементов:  * **asc** – **По возрастанию**; * **desc** – **По убыванию**. |
| Не отображать недоступные товары | **HIDE\_NOT\_AVAILABLE** | [Y|N] При отмеченной опции будут скрыты товары, для которых общее количество на складах меньше либо равно нулю, включен количественный учет и не разрешена покупка при отсутствии товара. |
| **Настройки действий** | | |
| Название переменной, в которой передается действие | **ACTION\_VARIABLE** | Указывается имя переменной, в которой передается действие: **ADD\_TO\_COMPARE\_LIST**, **ADD2BASKET** и т.д. Значение поля по умолчанию **ACTION**. Значение параметра должно быть уникальным среди всех используемых компонентов на одной странице. |
| Название переменной, в которой передается код товара для покупки | **PRODUCT\_ID\_VARIABLE** | Задается имя переменной, в которой будет передаваться идентификатор товара для покупки. |
| **Цены** | | |
| Тип цены | **PRICE\_CODE** | Указывается тип цены для выводимых элементов. Если не задан ни один из типов, то цена товара и кнопки **Купить** и **В корзину** показаны не будут. |
| Использовать вывод цен с диапазонами | **USE\_PRICE\_COUNT** | [Y/N] При отмеченной опции будут отображаться цены всех типов на товары. |
| Выводить цены для количества | **SHOW\_PRICE\_COUNT** | Параметр определяет количество единиц товара, для которых выводить стоимость. |
| Включать НДС в цену | **PRICE\_VAT\_INCLUDE** | [Y|N] При отмеченной опции цены будут показаны с учетом НДС. |
| Показывать цены в одной валюте | **CONVERT\_CURRENCY** | При установке флажка цены будут выводиться в одной валюте, даже если в каталоге они будут заданы в разных валютах; станет доступным дополнительное поле     |  |  |  | | --- | --- | --- | | Валюта, в которую будут сконвертированы цены | **CURRENCY\_ID** | Выбор валюты, в которой будут отображаться цены. |  . При выборе этой опции кеш компонента будет автоматически сбрасываться при изменении курсов валют тех товаров, что показываются компонентом. К примеру, если выбрана конвертация в рубли, а цены в инфоблоке сохранены в евро, то кеш сбросится при изменении курса евро или рубля. Изменения остальных валют на кеш не окажут влияния. |
| **Добавление в корзину** | | |
| URL, ведущий на страницу с корзиной покупателя | **BASKET\_URL** | Указывается путь к странице с корзиной покупателя. |

### Пример вызова

```
<?$APPLICATION->IncludeComponent (
"bitrix:catalog.compare.result",
	"",
	Array(
		"AJAX_MODE" => "Y",
		"NAME" => "CATALOG_COMPARE_LIST",
		"IBLOCK_TYPE" => "news",
		"IBLOCK_ID" => "2",
		"FIELD_CODE" => array(),
		"PROPERTY_CODE" => array(),
		"OFFERS_FIELD_CODE" => array(),
		"OFFERS_PROPERTY_CODE" => array(),
		"ELEMENT_SORT_FIELD" => "sort",
		"ELEMENT_SORT_ORDER" => "asc",
		"DETAIL_URL" => "",
		"BASKET_URL" => "/personal/basket.php",
		"ACTION_VARIABLE" => "action",
		"PRODUCT_ID_VARIABLE" => "id",
		"SECTION_ID_VARIABLE" => "SECTION_ID",
		"PRICE_CODE" => array(),
		"USE_PRICE_COUNT" => "Y",
		"SHOW_PRICE_COUNT" => "1",
		"PRICE_VAT_INCLUDE" => "Y",
		"DISPLAY_ELEMENT_SELECT_BOX" => "Y",
		"ELEMENT_SORT_FIELD_BOX" => "name",
		"ELEMENT_SORT_ORDER_BOX" => "asc",
		"ELEMENT_SORT_FIELD_BOX2" => "id",
		"ELEMENT_SORT_ORDER_BOX2" => "desc",
		"HIDE_NOT_AVAILABLE" => "N",
		"AJAX_OPTION_SHADOW" => "Y",
		"AJAX_OPTION_JUMP" => "Y",
		"AJAX_OPTION_STYLE" => "Y",
		"AJAX_OPTION_HISTORY" => "Y",
		"CONVERT_CURRENCY" => "Y",
		"CURRENCY_ID" => "RUB",
		"TEMPLATE_THEME" => "blue",
	)
);?>

```

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх