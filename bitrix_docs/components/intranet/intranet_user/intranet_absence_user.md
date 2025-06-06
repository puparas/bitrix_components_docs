# Отсутствия пользователя

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

[HR](/user_help/components/intranet/intranet_user/index.php)

[Календарь отсутствий](/user_help/components/intranet/intranet_user/intranet_absence_calendar.php)
[Отсутствующие сотрудники](/user_help/components/intranet/intranet_user/intranet_structure_informer_absent.php)
[Доска почета](/user_help/components/intranet/intranet_user/intranet_structure_honour.php)
[Доска почета пользователя](/user_help/components/intranet/intranet_user/intranet_structure_honour_user.php)
[Отсутствия пользователя](/user_help/components/intranet/intranet_user/intranet_absence_user.php)
[Кадровые изменения](/user_help/components/intranet/intranet_user/intranet_structure_events.php)
[Новые сотрудники](/user_help/components/intranet/intranet_user/intranet_structure_informer_new.php)
[Дни рождения](/user_help/components/intranet/intranet_user/intranet_structure_birthday_nearest.php)

[Бронирование переговорных](/user_help/components/intranet/intranet_reserve/index.php)

[Оргструктура](/user_help/components/intranet/intranet_search/index.php)

[Собрания и планерки](/user_help/components/intranet/meetings/index.php)

[Учет рабочего времени](/user_help/components/intranet/timeman/index.php)

[Руководство подразделениями](/user_help/components/intranet/intranet_structure_head_user.php)

[Сайты 24](/user_help/components/landing/index.php)

[Контент](/user_help/components/content/index.php)

[Сервисы](/user_help/components/services/index.php)

[Общение](/user_help/components/obschenie/index.php)

[Магазин](/user_help/components/magazin/index.php)

[Служебные](/user_help/components/sluzhebnie/index.php)

[Описание компонентов решений](/user_help/description_decisions/index.php)

[Дополнительно](/user_help/additional/index.php)

[Компоненты](/user_help/components/index.php)

[Корпоративный портал (КП)](/user_help/components/intranet/index.php)

[HR](/user_help/components/intranet/intranet_user/index.php)

Отсутствия пользователя

# Отсутствия пользователя

### Описание **intranet.absence.user**

Компонент выводит график отсутствия конкретного пользователя.

В визуальном редакторе компонент находится в *Компоненты > Корпоративный портал > HR*.

### Параметры

|  |  |  |
| --- | --- | --- |
| **Поле** | **Параметр** | **Описание** |
| **Основные параметры** | | |
| Идентификатор пользователя | **ID** | Указывается ID пользователя. |
| Тип инфоблока с календарями сотрудников | **CALENDAR\_IBLOCK\_TYPE** | Выбирается один из существующих типов инфоблоков. |
| Инфоблок с календарями сотрудников | **CALENDAR\_IBLOCK\_ID** | Выбирается один из существующих инфоблоков. |
| **Настройки кеширования** | | |
| Тип кеширования | **CACHE\_TYPE** | Указывается тип кеширования:  * **A** - Авто + Управляемое: автоматически обновляет кеш компонентов в течение заданного времени или при изменении данных; * **Y** - Кешировать: для кеширования необходимо определить время кеширования; * **N** - Не кешировать: кеширования нет в любом случае. |
| Время кеширования (сек.) | **CACHE\_TIME** | Время кеширования, указанное в секундах. |

### Пример вызова

```
<?$APPLICATION->IncludeComponent(
	"bitrix:intranet.absence.user",
	"",
	Array(
		"CACHE_TIME" => "3600",
		"CACHE_TYPE" => "A",
		"CALENDAR_IBLOCK_ID" => "1",
		"CALENDAR_IBLOCK_TYPE" => "news",
		"ID" => $USER->GetID()
	),
);?>

```

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх