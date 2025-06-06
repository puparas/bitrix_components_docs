# Пункты меню

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

Пункты меню

# Пункты меню

Компонент осуществляет дополнение созданного меню названиями разделов инфоблоков. Компонент является стандартным и входит в дистрибутив модуля.

### Описание **menu.sections**

В визуальном редакторе компонент расположен по пути: *Служебные > Навигация > Пункты меню*.

Компонент относится к модулю [Информационные блоки](/user_help/content/iblock/index.php).

### Параметры

|  |  |  |
| --- | --- | --- |
| **Поле** | **Параметр** | **Описание** |
| **Основные параметры** | | |
| Включить режим совместимости с поддержкой ЧПУ | **IS\_SEF** | [Y|N] При отмеченной опции включается режим поддержки ЧПУ.   Если режим поддержки ЧПУ **включен**, то необходимо настроить следующие параметры:     |  |  |  | | --- | --- | --- | | Каталог ЧПУ (относительно корня сайта) | **SEF\_BASE\_URL** | Каталог ЧПУ: путь до папки, с которой работает компонент. Этот путь может как совпадать с физическим путём, так и не совпадать. | | Шаблон URL, ведущий на страницу с содержимым раздела | **SECTION\_PAGE\_URL** | Указывается шаблон пути, ведущий на страницу с содержимым раздела. | | Шаблон URL, ведущий на страницу с элементом | **DETAIL\_PAGE\_URL** | Указывается шаблон пути, ведущий на страницу с элементом. |  **SEF\_BASE\_URL**, **SECTION\_PAGE\_URL**, **DETAIL\_PAGE\_URL**. |
| Тип информационного блока | **IBLOCK\_TYPE** | Указывается идентификатор типа информационного блока. |
| Код информационного блока | **IBLOCK\_ID** | Для выбранного типа инфоблоков указывается идентификатор (код) инфоблока, на основе которого будет строиться меню. |
| **Источник данных** | | |
| Сколько уровней вложенности выводить | **DEPTH\_LEVEL** | Задается глубина вложений, согласно которой будет строиться меню. |
| **Настройки кеширования** | | |
| Тип кеширования | **CACHE\_TYPE** | Тип кеширования:  * **A** - Авто + Управляемое: автоматически обновляет кеш компонентов в течение заданного времени или при изменении данных; * **Y** - Кешировать: для кеширования необходимо определить время кеширования; * **N** - Не кешировать: кеширования нет в любом случае. |
| Время кеширования (сек.) | **CACHE\_TIME** | Время кеширования, указанное в секундах. По умолчанию поле содержит 3600 сек. |

### Пример вызова

```
<?$APPLICATION->IncludeComponent("bitrix:menu.sections","",Array(
		"IS_SEF" => "Y", 
		"SEF_BASE_URL" => "/catalog/phone/", 
		"SECTION_PAGE_URL" => "#SECTION_ID#/", 
		"DETAIL_PAGE_URL" => "#SECTION_ID#/#ELEMENT_ID#", 
		"IBLOCK_TYPE" => "news", 
		"IBLOCK_ID" => "1", 
		"DEPTH_LEVEL" => "1", 
		"CACHE_TYPE" => "A", 
		"CACHE_TIME" => "3600" 
	)
);?>

```

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

| 4  **Александр Щербаков** 01.09.2015 10:02:01 |
| --- |
| Живой пример для файла меню, например **.catalog.menu\_ext.php** (в модуле bitrix:menu должно быть «USE\_EXT» ⇒ «Y»)  | Код | | --- | | ```  <? if(!defined("B_PROLOG_INCLUDED") || B_PROLOG_INCLUDED!==true)die();  global $APPLICATION; $aMenuLinksExt = array();  if(CModule::IncludeModule('iblock')) {    $arFilter = array(       "TYPE" => "catalog",       "SITE_ID" => SITE_ID,    );     $dbIBlock = CIBlock::GetList(array('SORT' => 'ASC', 'ID' => 'ASC'), $arFilter);    $dbIBlock = new CIBlockResult($dbIBlock);     if ($arIBlock = $dbIBlock->GetNext())    {       if(defined("BX_COMP_MANAGED_CACHE"))          $GLOBALS["CACHE_MANAGER"]->RegisterTag("iblock_id_".$arIBlock["ID"]);        if($arIBlock["ACTIVE"] == "Y")       {          $aMenuLinksExt = $APPLICATION->IncludeComponent("bitrix:menu.sections", "", array(             "IS_SEF" => "Y",             "SEF_BASE_URL" => "",             "SECTION_PAGE_URL" => $arIBlock['SECTION_PAGE_URL'],             "DETAIL_PAGE_URL" => $arIBlock['DETAIL_PAGE_URL'],             "IBLOCK_TYPE" => $arIBlock['IBLOCK_TYPE_ID'],             "IBLOCK_ID" => $arIBlock['ID'],             "DEPTH_LEVEL" => "3",             "CACHE_TYPE" => "N",          ), false, Array('HIDE_ICONS' => 'Y'));       }    }     if(defined("BX_COMP_MANAGED_CACHE"))       $GLOBALS["CACHE_MANAGER"]->RegisterTag("iblock_id_new"); }  $aMenuLinks = array_merge($aMenuLinks, $aMenuLinksExt); ?>  ``` | |
|  |

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх