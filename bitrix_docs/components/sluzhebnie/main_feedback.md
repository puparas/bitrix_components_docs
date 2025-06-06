# Форма обратной связи

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

Форма обратной связи

# Форма обратной связи

### Описание **main.feedback**

Компонент выводит форму для отправки сообщения с сайта на E-mail. Компонент является стандартным и входит в дистрибутив модуля.

Для работы формы не требуется модуль **Почта**.

Компонент относится к [Главному модулю](/user_help/settings/settings/index.php).

### Параметры

|  |  |  |
| --- | --- | --- |
| **Поле** | **Параметр** | **Описание** |
| **Основные параметры** | | |
| Использовать защиту от автоматических сообщений (CAPTCHA) для неавторизованных пользователей | **USE\_CAPTCHA** | [Y|N] При отмеченной опции для неавторизованных пользователей будет использоваться **CAPTCHA** при создании сообщений. |
| Сообщение, выводимое пользователю после отправки | **OK\_TEXT** | Задается текст сообщения, выводимый пользователю после отправки. |
| E-mail, на который будет отправлено письмо | **EMAIL\_TO** | Задается E-mail, на который будет отправлено письмо (будет отображен в форме для отправки сообщений в поле **Ваш E-mail**). |
| Обязательные поля для заполнения | **REQUIRED\_FIELDS** | Указываются поля формы, которые будут обязательными для заполнения. |
| Почтовые шаблоны для отправки письма | **EVENT\_MESSAGE\_ID** | Указывается почтовый шаблон, на основе которого будут отправляться письма. |

Если компонент размещён на сайте, настроен, но сообщения не приходят, необходимо:

* С помощью [Проверки системы](/user_help/settings/utilities/site_checker.php) необходимо убедиться что почта уходит с сайта.
* Убедиться, что есть активный [почтовый шаблон](/user_help/settings/settings/mail_events/message_admin.php) FEEDBACK\_FORM.
* Убедиться, что в шаблоне проставлен валидный адрес в поле **Кому**.

### Пример вызова

```
<?$APPLICATION->IncludeComponent("bitrix:main.feedback","",Array(
		"USE_CAPTCHA" => "Y",
		"OK_TEXT" => "Спасибо, ваше сообщение принято.",
		"EMAIL_TO" => "my@email.com",
		"REQUIRED_FIELDS" => Array("NAME","EMAIL","MESSAGE"),
		"EVENT_MESSAGE_ID" => Array("5")
	)
);?>
```

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх