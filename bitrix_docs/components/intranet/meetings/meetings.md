# Собрания и планерки

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

[Бронирование переговорных](/user_help/components/intranet/intranet_reserve/index.php)

[Оргструктура](/user_help/components/intranet/intranet_search/index.php)

[Собрания и планерки](/user_help/components/intranet/meetings/index.php)

[Собрания и планерки](/user_help/components/intranet/meetings/meetings.php)

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

Собрания и планерки

# Собрания и планерки

### Описание **meetings**

Комплексный компонент для управления собраниями.

В визуальном редакторе компонент находится в *Компоненты > Корпоративный портал > Собрания и планерки*.

### Параметры

|  |  |  |
| --- | --- | --- |
| **Поле** | **Параметр** | **Описание** |
| **Основные параметры** | | |
| Тип инфоблока переговорных | **RESERVE\_MEETING\_IBLOCK\_TYPE** | Выбирается тип информационного блока, используемого для бронирования переговорных |
| Инфоблок переговорных | **RESERVE\_MEETING\_IBLOCK\_ID** | Указывается инфоблок, используемый для хранения записей бронирования переговорных. |
| Тип инфоблока видеопереговорных | **RESERVE\_VMEETING\_IBLOCK\_TYPE** | Выбирается тип информационного блока, используемого для бронирования видеопереговорных |
| Инфоблок видеопереговорных | **RESERVE\_VMEETING\_IBLOCK\_ID** | Указывается инфоблок, используемый для хранения записей бронирования видеопереговорных. |
| Количество собраний на страницу | **MEETING\_COUNT** | Устанавливается число записей о собраниях, отображаемых на одной странице. |
| **Управление адресами страниц** | | |
| Включить поддержку ЧПУ | **SEF\_MODE** | [Y|N] При отмеченной опции будет включен режим поддержки ЧПУ.   Если режим поддержки ЧПУ **включен**, то необходимо настроить  следующие параметры:     |  |  |  | | --- | --- | --- | | Каталог ЧПУ (относительно корня сайта) | **SEF\_FOLDER** | Каталог ЧПУ: путь до папки, с которой работает компонент. Этот путь может как совпадать с физическим путём, так и не совпадать. | | Адреса страниц | **SEF\_URL\_TEMPLATES** | Указываются шаблоны пути к следующим страницам:  * **list** - страница списка собраний; * **meeting** - страница просмотра информации о собрании; * **meeting\_edit** - страница редактирования информации о собрании; * **meeting\_copy** - страница создания следующего собрания; * **item** - страница детальной информации о пункте повестки. |  **SEF\_FOLDER**, **SEF\_URL\_TEMPLATES**. |

### Пример вызова

```
<?$APPLICATION->IncludeComponent(
	"bitrix:meetings",
	"",
	Array(
		"MEETINGS_COUNT" => "20",
		"RESERVE_MEETING_IBLOCK_ID" => "1",
		"RESERVE_MEETING_IBLOCK_TYPE" => "news",
		"RESERVE_VMEETING_IBLOCK_ID" => "1",
		"RESERVE_VMEETING_IBLOCK_TYPE" => "news",
		"SEF_MODE" => "N",
		"VARIABLE_ALIASES" => Array("action"=>"action")
		)
	),
);?>

```

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх