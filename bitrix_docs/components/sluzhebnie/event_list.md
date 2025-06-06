# Журнал изменений

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

Журнал изменений

# Журнал изменений

Одностраничный компонент позволяет вывести историю изменений, произошедших на проекте.

### Описание

В компоненте отображаются следующие действия:

* пользователи (добавление, изменение, удаление);
* страницы (изменение, добавление, удаление);
* меню (изменение, создание, удаление);
* файлы (изменение, добавление, удаление, перемещение, копирование, переименование);
* разделы (добавление, изменение, удаление, перемещение, копирование, переименование);
* инфоблоки (все события инфоблоков);
* форумы общие и в рамках социальных сетей (сообщение: скрытие,показ, изменение, перенос, удаление; тема: показ, скрытие, прикрепление, открепление, открытие, закрытие, удаление, изменение).

В визуальном редакторе компонент расположен в разделе: *Служебные*.

Компонент относится к [Главному модулю](/user_help/settings/settings/index.php).

### Настройки компонента

|  |  |  |
| --- | --- | --- |
| **Поле** | **Параметр** | **Описание** |
| **Шаблоны ссылок** | | |
| Шаблоны путей к странице пользователя | **USER\_PATH** | Шаблон пути необходимо поменять, если он был изменен в рамках всего проекта. |
| Шаблоны путей к форуму | **FORUM\_PATH** | Шаблон пути необходимо поменять, если он был изменен в рамках всего проекта. |
| Шаблоны путей к теме форума | **FORUM\_TOPIC\_PATH** | Шаблон пути необходимо поменять, если он был изменен в рамках всего проекта. |
| Шаблоны путей к сообщению форума | **FORUM\_MESSAGE\_PATH** | Шаблон пути необходимо поменять, если он был изменен в рамках всего проекта. |
| **Дополнительные настройки** | | |
| Количество отображаемых записей на странице | **PAGE\_NUM** | Число записей на странице. При превышении указанного числа, включается постраничная навигация |
| **Настройки фильтра** | | |
| Элементы в фильтре | **FILTER** | Выбор сущностей, по которым возможна фильтрация данных. |

### Пример вызова

```
<?$APPLICATION->IncludeComponent(
	"bitrix:event_list",
	"",
	Array(
		"PAGE_NUM" => "10",
		"FILTER" => array("FORUM","USERS","PAGE_EDIT","MENU_EDIT"),
		"USER_PATH" => "company/personal/user/#user_id#/",
		"FORUM_PATH" => "community/forum/forum#FORUM_ID#/",
		"FORUM_TOPIC_PATH" => "community/forum/forum#FORUM_ID#/topic#TOPIC_ID#/",
		"FORUM_MESSAGE_PATH" => "community/forum/messages/forum#FORUM_ID#/topic#TOPIC_ID#/message#MESSAGE_ID#/#message#MESSAGE_ID#"
	)
);?>  
  

```

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх