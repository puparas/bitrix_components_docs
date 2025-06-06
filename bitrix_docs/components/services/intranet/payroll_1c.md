# Расчетные листки сотрудников

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

Расчетные листки сотрудников

# Расчетные листки сотрудников

### Описание **payroll.1c**

Компонент позволяет подключаться к web-платформе "1С: ЗУП" и выводить зарплатные листки сотрудников компании. Компонент стандартный и входит в дистрибутив модуля.

В визуальном редакторе компонент находится в *Компоненты > Служебные > Расчетные листки сотрудников*.

### Параметры

|  |  |  |
| --- | --- | --- |
| **Поле** | **Параметр** | **Описание** |
| **Основные параметры** | | |
| Список организаций | **ORG\_LIST** | Указывается организация, зарплатные листки сотрудников которой будут выводится. Обязательно нужно нажать на кнопку **ОК**. Форма перезагрузится и появится группа настроек **Настройки для организации**. |
| Таймаут соединения, сек | **PR\_TIMEOUT** | Указывается таймаут соединения с web-платформой "1С: ЗУП" в секундах. |
| Пространство имен | **PR\_NAMESPACE** | Указывается пространство имен для подключения к порталу. |
| **Настройки кеширования** | | |
| Тип кеширования | **CACHE\_TYPE** | Указывается тип кеширования:  * **A** - Авто: действует при включенном кешировании в течение заданного времени; * **Y** - Кешировать: для кеширования необходимо определить время кеширования; * **N** - Не кешировать: кеширования нет в любом случае. |
| Время кеширования (сек.) | **CACHE\_TIME** | Время кеширования, указанное в секундах. |
| **Настройки для организации** | | |
| URL веб-сервиса | **PR\_URL** | Указывается адрес сервиса, полученный от администратора программы "1С: ЗУП". Настройки на стороне "1С: ЗУП" описаны тут. |
| Порт | **PR\_PORT** | Указывается порт сервиса, полученный от администратора программы "1С: ЗУП". |
| Имя пользователя | **PR\_LOGIN** | Указывается логин сервиса, полученный от администратора программы "1С: ЗУП". |
| Пароль | **PR\_PASSWORD** | Указывается пароль сервиса, полученный от администратора программы "1С: ЗУП". |

### Пример вызова

```

<?$APPLICATION->IncludeComponent("bitrix:payroll.1c","",Array(
		"ORG_LIST" => array("Моя компания"),
		"PR_TIMEOUT" => "25",
		"PR_NAMESPACE" => "http://test_server.ru",
		"CACHE_TYPE" => "A",
		"CACHE_TIME" => "3600",
		"PR_URL_0" => "http://test_server.ru/zupws/ws/zupws",
		"PR_PORT_0" => "80",
		"PR_LOGIN_0" => "demo",
		"PR_PASSWORD_0" => "demo"  
	)
);?>

```

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх