# Вставка включаемой области

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

[Безопасность](/user_help/components/sluzhebnie/security/index.php)

[Включаемые области](/user_help/components/sluzhebnie/included_regions/index.php)

[Вставка включаемой области](/user_help/components/sluzhebnie/included_regions/main_include.php)

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

[Включаемые области](/user_help/components/sluzhebnie/included_regions/index.php)

Вставка включаемой области

# Вставка включаемой области

Компонент располагается в шаблоне дизайна сайта и определяет место расположения включаемых областей страниц и разделов.

### Описание **main.include**

Компонент может выводить содержимое произвольного файла (например, информацию об авторских правах, название компании и т.д.). Настройки компонента позволяют определить суффикс имени файла включаемой области, указать режим редактирования включаемой области по умолчанию, шаблон области по умолчанию. Компонент является стандартным и входит в дистрибутив модуля.

В визуальном редакторе компонент расположен по пути: *Служебные > Включаемые области > Вставка включаемой области*.

Компонент относится к [Главному модулю](/user_help/settings/settings/index.php).

### Параметры

|  |  |  |
| --- | --- | --- |
| **Поле** | **Параметр** | **Описание** |
| **Параметры компонента** | | |
| Показывать включаемую область | **AREA\_FILE\_SHOW** | Возможные значения:  * **sect**: показывать для раздела, область будет являться включаемой для всего раздела; * **page**: показывать для страницы, область будет являться включаемой только для текущей страницы; * **file**: показывать информацию из файла. Если компонент расположить в шаблоне дизайна сайта, то информация из файла будет выводиться на всем сайте. Установка параметра доступна только пользователю с правами **edit\_php**. |
| Путь к файлу области | **PATH** | Поле доступно, если выбрано **Показывать включаемую область из файла**. Задается полный путь от корня сайта к файлу с информацией, которую надо вывести в этой части сайта. |
| Суффикс имени файла включаемой области | **AREA\_FILE\_SUFFIX** | Поле предназначено для указания суффикса, который будет добавляться к именам файлов включаемых областей. Страницы с таким суффиксом будут восприниматься как включаемые области. |
| Рекурсивное подключение включаемых областей разделов | **AREA\_FILE\_RECURSIVE** | [Y|N] Настройка доступна при отмеченной области **Показывать включаемую область** (**AREA\_FILE\_SHOW**) в значение для раздела (**sect**). При отмеченной опции включаемые области разделов будут подключаться рекурсивно, т.е. если в папке более низкого уровня есть своя включаемая область, то она будет показана. Если же текущий раздел не имеет своей включаемой области, то рекурсивно до корня сайта будут проверяться все разделы до самого верхнего и будет выведена первая встретившаяся включаемая область. |
| Шаблон области по умолчанию | **EDIT\_TEMPLATE** | Доступны все шаблоны страниц, созданные в системе. Они располагаются в разделе **/bitrix/templates/.default/page\_templates/**. В данном поле можно указать любой другой файл в системе, указав полный путь к файлу-шаблону. |

### Пример вызова

```
<?$APPLICATION->IncludeComponent("bitrix:main.include","",Array(
		"AREA_FILE_SHOW" => "sect", 
		"AREA_FILE_SUFFIX" => "inc", 
		"AREA_FILE_RECURSIVE" => "Y", 
		"EDIT_TEMPLATE" => "standard.php" 
	)
);?>

```

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

| 6  **Алена Манчукова** 14.11.2019 10:43:45 |
| --- |
| Для примера:   <?$APPLICATION->IncludeComponent("bitrix:main.include","",Array(         "AREA\_FILE\_SHOW" => "page",          "AREA\_FILE\_SUFFIX" => "example",          "EDIT\_TEMPLATE" => "" |
|  |

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх