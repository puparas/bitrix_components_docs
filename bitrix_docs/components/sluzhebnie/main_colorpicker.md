# Элемент управления "Палитра"

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

Элемент управления "Палитра"

# Элемент управления "Палитра"

### Описание **main.colorpicker**

Компонент используется для ввода таблицы цвета. Компонент является стандартным и входит в дистрибутив модуля.

В визуальном редакторе компонент расположен по пути: *Служебные > Элемент управления "Палитра"*.

Компонент относится к [Главному модулю](/user_help/settings/settings/index.php).

### Параметры

|  |  |  |
| --- | --- | --- |
| **Поле** | **Параметр** | **Описание** |
| **Основные параметры** | | |
| Показывать кнопку | **SHOW\_BUTTON** | [Y|N] При отмеченной опции кнопки компонента будут отображены на странице. |
| Идентификатор | **ID** | Идентификатор компонента. |
| Название | **NAME** | Имя компонента, которое будет отображаться в публичной части. |
| Обработчик события выбора | **ONSELECT** | Обработчик, который будет использовать данный компонент. |

### Пример вызова

```
<?$APPLICATION->IncludeComponent("bitrix:main.colorpicker","",Array(  
		"SHOW_BUTTON" => "Y",  
		"ID" => "123",  
		"NAME" => "Выбор цвета",  
		"ONSELECT" => ""  
	),  

```

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

| 0  **Антон Долганин** 19.08.2010 01:03:54 |
| --- |
| Пример использования:   | Код | | --- | | ```  <sc ript type="text/javascript"> function OnSelectBGColor(color, objColorPicker) {    alert(color); } </script>  <?$APPLICATION->IncludeComponent(    "bitrix:main.colorpicker",    "",    Array(       "SHOW_BUTTON" => "Y",       "ID" => "color_bg_picker",       "NAME" => "Выбор цвета",       "ONSELECT" => "OnSelectBGColor"    ), $component, array("HIDE_ICONS" => "Y") );?>  ``` | |
|  |

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх