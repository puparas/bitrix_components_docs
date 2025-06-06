# Список своих результатов

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

[Веб-форма (комплексный компонент)](/user_help/components/services/web_forms/form.php)
[Заполнение веб-формы](/user_help/components/services/web_forms/form_result_new.php)
[Просмотр результата](/user_help/components/services/web_forms/form_result_view.php)
[Редактирование результата](/user_help/components/services/web_forms/form_result_edit.php)
[Список результатов](/user_help/components/services/web_forms/form_result_list.php)
[Список своих результатов](/user_help/components/services/web_forms/form_result_list_my.php)

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

[Веб-формы](/user_help/components/services/web_forms/index.php)

Список своих результатов

**Недоступно в редакциях:**Старт

# Список своих результатов

### Описание **form.result.list.my**

Компонент выводит список своих результатов по нескольким формам. Компонент стандартный и входит в дистрибутив модуля.

В структуре визуального редактора компонент расположен по пути *Сервисы > Веб-формы > Список своих результатов*.

Компонент относится к модулю [Веб-формы](/user_help/service/form/index.php).

### Параметры

|  |  |  |
| --- | --- | --- |
| **Поле** | **Параметр** | **Описание** |
| **Основные параметры** | | |
| Формы (если не указано ни одной, то выборка будет по всем формам сайта) | **FORMS** | Указываются формы, по которым будет осуществлятся выборка для отображения результата. Если не указано ни одной, то выборка будет по всем формам сайта. |
| **Дополнительные настройки** | | |
| Количество результатов на одну форму | **NUM\_RESULTS** | Указывается количество результатов на одну форму. |
| Страница со списком результатов | **LIST\_URL** | Указывается адрес страницы со списком результатов. |
| Страница просмотра результата | **VIEW\_URL** | Указывается адрес страницы просмотра результата. |
| Страница редактирования результата | **EDIT\_URL** | Указывается адрес страницы редактирования результата. |

### Пример вызова

```
<?$APPLICATION->IncludeComponent("bitrix:form.result.list.my","",Array(
		"FORMS" => Array(), 
		"NUM_RESULTS" => "10", 
		"LIST_URL" => "my_result_list.php?WEB_FORM_ID=#FORM_ID#", 
		"VIEW_URL" => "my_result_view.php?WEB_FORM_ID=#FORM_ID#&RESULT_ID=#RESULT_ID#", 
		"EDIT_URL" => "my_result_edit.php?WEB_FORM_ID=#FORM_ID#&RESULT_ID=#RESULT_ID#" 
	)
);?>

```

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх