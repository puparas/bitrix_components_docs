# Меню

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

[Сервисы](/user_help/components/services/index.php)

[Общение](/user_help/components/obschenie/index.php)

[Магазин](/user_help/components/magazin/index.php)

[Служебные](/user_help/components/sluzhebnie/index.php)

[navigation](/user_help/components/sluzhebnie/navigation/index.php)

[Выбор сайта](/user_help/components/sluzhebnie/navigation/main_site_selector.php)
[Меню](/user_help/components/sluzhebnie/navigation/menu.php)
[Меню для мобильной платформы](/user_help/components/sluzhebnie/navigation/mobileapp_menu.php)
[Навигационная цепочка](/user_help/components/sluzhebnie/navigation/breadcrumb.php)
[Пункты меню](/user_help/components/sluzhebnie/navigation/menu_section.php)

[Безопасность](/user_help/components/sluzhebnie/security/index.php)

[Включаемые области](/user_help/components/sluzhebnie/included_regions/index.php)

[Поиск](/user_help/components/sluzhebnie/search/index.php)

[Пользователь](/user_help/components/sluzhebnie/user/index.php)

[Статистика](/user_help/components/sluzhebnie/statistic/index.php)

[Соц. закладки и сети](/user_help/components/sluzhebnie/main_share.php)
[Упрощенный HTML-редактор](/user_help/components/sluzhebnie/fileman_light_editor.php)
[Форма обратной связи](/user_help/components/sluzhebnie/main_feedback.php)
[Элемент управления "Календарь"](/user_help/components/sluzhebnie/main_calendar.php)
[Элемент управления "Палитра"](/user_help/components/sluzhebnie/main_colorpicker.php)
[Элемент управления "Часы"](/user_help/components/sluzhebnie/main_clock.php)
[Журнал изменений](/user_help/components/sluzhebnie/event_list.php)

[Описание компонентов решений](/user_help/description_decisions/index.php)

[Дополнительно](/user_help/additional/index.php)

[Компоненты](/user_help/components/index.php)

[Служебные](/user_help/components/sluzhebnie/index.php)

[navigation](/user_help/components/sluzhebnie/navigation/index.php)

Меню

# Меню

Компонент выводит меню указанного типа. Компонент является стандартным и входит в дистрибутив модуля.

### Описание **menu**

В визуальном редакторе компонент расположен по пути: *Служебные > Навигация > Меню*.

Компонент относится к [Главному модулю](/user_help/settings/settings/index.php).

В поставку продукта входят следующие шаблоны компонента **Меню (bitrix:menu)**:

* **Горизонтальное многоуровневое выпадающее меню (Яркий)** (horizontal\_multilevel);
* **Левое меню (Яркий)** (**left**);
* **Вертикальное меню по умолчанию (Встроенный шаблон)** (**.default**);
* **Голубое меню в виде закладок (Встроенный шаблон)** (**blue\_tabs**);
* **Серое меню в виде закладок (Встроенный шаблон)** (**grey\_tabs**);
* **Древовидное меню (Встроенный шаблон)** (**tree**);
* **Вертикальное многоуровневое выпадающее меню (Встроенный шаблон)** (**vertical\_multilevel**).

### Параметры

|  |  |  |
| --- | --- | --- |
| **Поле** | **Параметр** | **Описание** |
| **Основные параметры** | | |
| Тип меню для первого уровня | **ROOT\_MENU\_TYPE** | Указывается тип меню верхнего уровня, соответствующий данному меню. |
| **Настройки кеширования** | | |
| Тип кеширования | **MENU\_CACHE\_TYPE** | Тип кеширования:  * **A** - Авто: автоматически обновляет кеш компонентов в течение заданного времени; * **Y** - Кешировать: для кеширования необходимо определить время кеширования; * **N** - Не кешировать: кеширования нет в любом случае. |
| Время кеширования | **MENU\_CACHE\_TIME** | Время кеширования в секундах. |
| Учитывать права доступа | **MENU\_CACHE\_USE\_GROUPS** | При кешировании будут учитываться права доступа пользователя к тем или иным пунктам меню. Если меню построено без учета прав доступа, флажок лучше снять - размер кеша уменьшится. |
| Значимые переменные запроса | **MENU\_CACHE\_GET\_VARS** | Если отображение меню зависит от параметров страницы, то при использовании кеширования необходимо указать параметры в этом поле. Параметры вводятся через запятую. |
| **Дополнительные настройки** | | |
| Уровень вложенности меню | **MAX\_LEVEL** | В выпадающем списке выберите уровень вложенности. Доступно четыре уровня. Чем больше число, тем пункты более низких уровней будут отображены. |
| Тип меню для остальных уровней | **CHILD\_MENU\_TYPE** | Укажите тип меню для меню нижних уровней. |
| Подключать файлы с именами вида .тип\_меню.menu\_ext.php | **USE\_EXT** | [Y|N] При отмеченной опции будет разрешено подключать файлы с именами вида **.тип\_меню.menu\_ext.php**. |
| Откладывать выполнение шаблона меню | **DELAY** | [Y|N] При отмеченной опции выполнение шаблона будет происходить после загрузки страницы. Очень удобен при включенном кешировании компонента, если нужно все же выполнять какие-то действия по модификации внешнего вида пунктов меню в зависимости от текущей страницы. Например, добавление пунктов меню в компонентах.  ``` $GLOBALS['BX_MENU_CUSTOM']->AddItem('left', array( 'TEXT' => 'Моб. версия', 'LINK' => $APPLICATION-> GetCurPage(false) . '?mobile')) ```   Первый параметр - тип меню. Второй - массив, описывающий [пункт меню](http://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=3473#arr_menu). |
| Разрешить несколько активных пунктов одновременно | **ALLOW\_MULTI\_SELECT** | [Y|N] При отмеченной опции будет разрешено несколько активных пунктов меню одновременно. |
| **Параметры для ручной настройки,** в форме настройки компонента не видны | | |
|  | **CACHE\_SELECTED\_ITEMS** | Y\N. Определяет подмешивать или нет URL в кеш. По умолчанию    С версии 23.300.0. - N. Если параметр имеет значение Y, то меню кешируется отдельно для каждого раздела. Если на сайте много разделов, то [размер кеша](https://dev.1c-bitrix.ru/learning/course/?COURSE_ID=43&LESSON_ID=5402 "Проблемы при кешировании меню") меню может вызвать падение сайта из-за переполнения места на диске. Ограничение константы отключающей подмешивание URL в том, что во вложенном разделе может полностью быть переопределены пункты меню. |
|  | **MENU\_CACHE\_USE\_USERS** | Y\N. Определяет подмешивать ли в кеш id пользователя.То есть делать ли его уникальным для каждого пользователя. Нужно когда оно отличается для каждого пользователя. |

### Пример вызова

```
<?$APPLICATION->IncludeComponent("bitrix:menu",".default",Array(
		"ROOT_MENU_TYPE" => "top", 
		"MAX_LEVEL" => "1", 
		"CHILD_MENU_TYPE" => "top", 
		"USE_EXT" => "Y",
		"DELAY" => "N",
		"ALLOW_MULTI_SELECT" => "Y",
		"MENU_CACHE_TYPE" => "N", 
		"MENU_CACHE_TIME" => "3600", 
		"MENU_CACHE_USE_GROUPS" => "Y", 
		"MENU_CACHE_GET_VARS" => "" 
	)
);?>

```

### Смотрите также

* [Создание и работа с меню](http://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&CHAPTER_ID=04708) в курсе **Разработчик Bitrix Framework.**

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх