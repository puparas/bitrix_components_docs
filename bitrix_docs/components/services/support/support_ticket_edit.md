# Создание нового, либо редактирование существующего обращения

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

[Видеоконференции (КП)](/user_help/components/services/video/index.php)

[Интранет (КП)](/user_help/components/services/intranet/index.php)

[Экстранет (КП)](/user_help/components/services/extranet/index.php)

[Контроллер](/user_help/components/services/controller/index.php)

[Частые вопросы](/user_help/components/services/faq/index.php)

[E-mail маркетинг](/user_help/components/services/email_marketing/index.php)

[Веб-Сервис](/user_help/components/services/web_service/index.php)

[Веб-формы](/user_help/components/services/web_forms/index.php)

[Менеджер идей](/user_help/components/services/ideas_manager/index.php)

[Обучение](/user_help/components/services/learning/index.php)

[Опросы, голосования](/user_help/components/services/votes/index.php)

[Рассылки](/user_help/components/services/subscribes/index.php)

[Реклама](/user_help/components/services/advertising/index.php)

[Техподдержка](/user_help/components/services/support/index.php)

[Техподдержка (комплексный компонент)](/user_help/components/services/support/support_ticket.php)
[Техподдержка с мастером (комплексный компонент)](/user_help/components/services/support/support_wizard.php)
[Создание нового, либо редактирование существующего обращения](/user_help/components/services/support/support_ticket_edit.php)
[Список обращений](/user_help/components/services/support/support_ticket_list.php)
[Мастер создания обращения](/user_help/components/services/support/iblock_wizard.php)

[Рабочий стол](/user_help/components/services/desktop.php)

[Общение](/user_help/components/obschenie/index.php)

[Магазин](/user_help/components/magazin/index.php)

[Служебные](/user_help/components/sluzhebnie/index.php)

[Описание компонентов решений](/user_help/description_decisions/index.php)

[Дополнительно](/user_help/additional/index.php)

[Компоненты](/user_help/components/index.php)

[Сервисы](/user_help/components/services/index.php)

[Техподдержка](/user_help/components/services/support/index.php)

Создание нового, либо редактирование существующего обращения

**Недоступно в редакциях:**Малый бизнес, Стандарт, Старт

# Создание нового, либо редактирование существующего обращения

### Описание **support.ticket.edit**

Компонент предназначен для вывода формы редактирования существующего обращения либо создания нового. С помощью этой формы ведется дискуссия по решению проблемы, обозначенной в обращении. Компонент является стандартным и входит в дистрибутив модуля.

В структуре визуального редактора компонент расположен по пути *Сервисы > Техподдержка > Создание нового, либо редактирование существующего обращения*.

Компонент относится к модулю [Техподдержка](/user_help/service/support/index.php).

### Параметры

|  |  |  |
| --- | --- | --- |
| **Поле** | **Параметр** | **Описание** |
| **Основные параметры** | | |
| ID обращения | **ID** | Указывается идентификатор обращения. |
| **Шаблоны ссылок** | | |
| Страница списка обращений | **TICKET\_LIST\_URL** | Указывается адрес страницы списка обращений. |
| **Дополнительные настройки** | | |
| Количество сообщений на одной странице | **MESSAGES\_PER\_PAGE** | Указывается количество сообщений, отображаемых на одной странице. |
| Максимальная длина неразрывной строки | **MESSAGE\_MAX\_LENGTH** | Задается максимальная длина фразы без пробелов или символов перевода строки. |
| Направление для сортировки сообщений в обращении | **MESSAGE\_SORT\_ORDER** | Указывается направление сортировки сообщений в обращении. Сообщения сортируются по времени добавления:  * *asc* - по возрастанию; * *desc* - по убыванию. |
| Устанавливать заголовок страницы | **SET\_PAGE\_TITLE** | При выборе значения **Да** в качестве заголовка будет установлено:  * **Новое обращение** - при создании нового обращения; * **Редактирование обращения** - при редактировании уже существующего обращения.  В противном случае (значение **Нет**) заголовок установлен не будет. |
| Показывать поле ввода купона | **SHOW\_COUPON\_FIELD** | [Y|N] При отмеченной опции будет показано поле ввода купона. |

### Пример вызова

```
<?$APPLICATION->IncludeComponent("bitrix:support.ticket.edit","",Array(
		"ID" => "$_REQUEST[\"ID\"]", 
		"TICKET_LIST_URL" => "ticket_list.php", 
		"MESSAGES_PER_PAGE" => "20", 
		"MESSAGE_MAX_LENGTH" => "70", 
		"MESSAGE_SORT_ORDER" => "asc", 
		"SET_PAGE_TITLE" => "Y", 
		"SHOW_COUPON_FIELD" => "Y" 
	)
);?>

```

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх