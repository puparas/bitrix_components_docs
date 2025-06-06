# Навигационная цепочка

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

Навигационная цепочка

# Навигационная цепочка

Компонент выводит навигационную цепочку в шаблоне.

### Описание **breadcrumb**

Настройки этого компонента позволяют регулировать уровень вложенности разделов (корень сайта - ноль), начиная с которого начнет выводиться навигационная цепочка. Также возможно переопределить путь, для которого цепочка будет построена и т.д. Компонент является стандартным и входит в дистрибутив модуля.

В визуальном редакторе компонент расположен по пути: *Служебные > Навигация > Навигационная цепочка*.

Компонент относится к [Главному модулю](/user_help/settings/settings/index.php).

### Параметры

|  |  |  |
| --- | --- | --- |
| **Поле** | **Параметр** | **Описание** |
| **Дополнительные настройки** | | |
| Номер пункта, начиная с которого будет построена навигационная цепочка | **START\_FROM** | Указывается номер пункта, начиная с которого будет построена навигационная цепочка. В поле может быть задано числовое значение, определяющее уровень вложенности раздела на сайте.   Например, 0 (ноль) означает, что построение навигационной цепочки начнется от корня сайта. Если 1, то с первого уровня текущего раздела и так далее. |
| Путь, для которого будет построена навигационная цепочка (по умолчанию, текущий путь) | **PATH** | Указывается путь, по которому будет построена навигационная цепочка. Если поле не заполнено совсем, то навигационная цепочка будет строиться для текущего пути. |
| Cайт (устанавливается в случае многосайтовой версии, когда DOCUMENT\_ROOT у сайтов разный) | **SITE\_ID** | Указывается сайт для построения навигационной цепочки. Параметр устанавливается в случае многосайтовой версии, когда **DOCUMENT\_ROOT** у сайтов разный. |

### Пример вызова

```
<?$APPLICATION->IncludeComponent("bitrix:breadcrumb","",Array(  
		"START_FROM" => "0",   
		"PATH" => "",   
		"SITE_ID" => "s1"   

```

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

| 14  **Роберт Басыров** 29.05.2009 15:07:24 |
| --- |
| Чтобы последний пункт в цепочке не был ссылкой (чтоб не проставлялся тег <a>) необходимо отредактировать шаблон компонента.  Измените в шаблоне строку  | Код | | --- | | ```  if($arResult[$index]["LINK"] <> "")  ``` |  на  | Код | | --- | | ``` if($arResult[$index]["LINK"] <> ""&&$index<(count($arResult)-1)) ``` | |
|  |

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх