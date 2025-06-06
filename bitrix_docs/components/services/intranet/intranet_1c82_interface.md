# Интерфейс 1с 8.2

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

[Расчетные листки сотрудников](/user_help/components/services/intranet/payroll_1c.php)
[Интерфейс 1с 8.2](/user_help/components/services/intranet/intranet_1c82_interface.php)
[Импорт оргструктуры из 1С:ЗУП](/user_help/components/services/intranet/intranet_users_import_1c.php)
[Импорт оргструктуры из 1С:ЗУП (hrxml)](/user_help/components/services/intranet/intranet_users_import.1c_hrxml.php)

[Задачи 1.0](/user_help/components/services/intranet/intranet_tasks/index.php)

[Календарь событий](/user_help/components/services/intranet/intranet_event/index.php)

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

[Рабочий стол](/user_help/components/services/desktop.php)

[Общение](/user_help/components/obschenie/index.php)

[Магазин](/user_help/components/magazin/index.php)

[Служебные](/user_help/components/sluzhebnie/index.php)

[Описание компонентов решений](/user_help/description_decisions/index.php)

[Дополнительно](/user_help/additional/index.php)

[Компоненты](/user_help/components/index.php)

[Сервисы](/user_help/components/services/index.php)

[Интранет (КП)](/user_help/components/services/intranet/index.php)

Интерфейс 1с 8.2

# Интерфейс 1с 8.2

### Описание **intranet.1c82.interface**

Компонент позволяет подключаться к web-платформе 1С 8.2. Компонент стандартный и входит в дистрибутив модуля.

В визуальном редакторе компонент находится в *Компоненты > Служебные > Отчеты по 1С*.

### Параметры

|  |  |  |
| --- | --- | --- |
| **Поле** | **Параметр** | **Описание** |
| **Дополнительные настройки** | | |
| URL к 1C 8.2 | **1C\_URL** | Указывается путь для подключения интерфейса к web-платформе 1С 8.2. |
| Логин | **LOGIN** | Указывается логин для подключения интерфейса к web-платформе 1С 8.2. |
| Пароль | **PASS** | Указывается пароль для подключения интерфейса к web-платформе 1С 8.2. |
| Название | **NAME** | Указывается название, которое будет отображаться в заголовке страницы. |
| Открывать в отдельном окне | **BLANK\_MODE** | [Y|N] При отмеченной опции работа с web-платформой 1С 8.2 будет происходить в отдельном окне. |
| Устанавливать заголовок страницы | **SET\_TITLE** | [Y|N] При отмеченной опции в качестве заголовка страницы будет установлено **<название>**, указанное в параметре **NAME**. |

### Пример вызова

```

<?$APPLICATION->IncludeComponent("bitrix:intranet.1c82.interface","",Array(
		"1C_URL" => "http://site.ru/1c/",
		"LOGIN" => "Администратор",
		"PASS" => "123456",
		"NAME" => "Подключение к 1С 8.2",
		"BLANK_MODE" => "Y",
		"SET_TITLE" => "Y"
	)
);?>

```

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх