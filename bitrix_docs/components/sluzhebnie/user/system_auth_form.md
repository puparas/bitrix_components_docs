# Форма авторизации

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

[Имя пользователя с тултипом](/user_help/components/sluzhebnie/user/main_user_link.php)
[Настраиваемая регистрация](/user_help/components/sluzhebnie/user/main_register.php)
[Параметры пользователя](/user_help/components/sluzhebnie/user/main_profile.php)
[Запрос согласия пользователя](/user_help/components/sluzhebnie/user/main_userconsent_request.php)
[Компонент для авторизации виджета Битрикс24.Онлайн-чат](/user_help/components/sluzhebnie/user/b24connector_openline_info.php)
[Пароли приложений](/user_help/components/sluzhebnie/user/main_app_passwords.php)
[Управление объединением профилей](/user_help/components/sluzhebnie/user/socserv_auth_split.php)
[Форма авторизации](/user_help/components/sluzhebnie/user/system_auth_form.php)
[Форма инициализации регистрации](/user_help/components/sluzhebnie/user/system_auth_initialize.php)
[Форма отписки от писем](/user_help/components/sluzhebnie/user/main_mail_unsubscribe.php)
[Форма подтверждения регистрации](/user_help/components/sluzhebnie/user/system_auth_confirmation.php)

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

[Пользователь](/user_help/components/sluzhebnie/user/index.php)

Форма авторизации

# Форма авторизации

Компонент служит для вывода формы авторизации.

### Описание **system.auth.form**

Используется обычно в шаблоне дизайна сайта. Компонент является стандартным и входит в дистрибутив модуля.

В визуальном редакторе компонент расположен по пути: *Служебные > Пользователь > Форма авторизации*.

### Параметры

|  |  |  |
| --- | --- | --- |
| **Поле** | **Параметр** | **Описание** |
| **Дополнительно** | | |
| Страница регистрации | **REGISTER\_URL** | Указывается путь к странице регистрации пользователя. |
| Страница забытого пароля | **FORGOT\_PASSWORD\_URL** | Указывается путь к странице восстановления пароля. |
| Страница профиля | **PROFILE\_URL** | Указывается путь к странице с параметрами пользователя. |
| Показывать ошибки | **SHOW\_ERRORS** | [Y|N] При отмеченной опции будут отображаться ошибки, возникающие при авторизации в системе. |

### Пример вызова

```
<?$APPLICATION->IncludeComponent("bitrix:system.auth.form","",Array(
     "REGISTER_URL" => "register.php",
     "FORGOT_PASSWORD_URL" => "",
     "PROFILE_URL" => "profile.php",
     "SHOW_ERRORS" => "Y" 
     )
);?>
```

### Механизм восстановления пароля

Если пользователь запросил восстановление пароля, то восстановление происходит по следующему механизму:

1. Пользователь нажимает на **Забыли Пароль?** в форме авторизации.
2. Генерируется случайная строка длиной 32 символа с учетом секрета, известного только серверу.
3. Результат записывается в БД и отправляется на почту. Ссылка вида: http://site.ru/bitrix/admin/index.php?change\_password=yes⟨=ru&USER\_CHECKWORD=3farde09fay52547f11c68bf17d95760&USER\_LOGIN=market, где:
   * http://site.ru/bitrix/admin/index.php - путь к страницы авторизации или смены пароля;
   * change\_password=yes - действие смены пароля;
   * lang=ru идентификатор языка;
   * USER\_CHECKWORD=3farde09fay52547f11c68bf17d95760 - контрольная строка для смены пароля 32 символа. В строке используются символы. доступные для md5: [0-9a-f].

     При смене пароля в запросе контрольной строки вводить только контрольную строку, без `USER_CHECKWORD=`!
   * &USER\_LOGIN=market - указание для какого пользователя происходит смена пароля.
4. При сравнении контрольной строки из формы с тем, что записано в БД, учитывается время истечения, указанное в групповой политике безопасности.

**Примечание**. В форме восстановления пароля рекомендуется использовать CAPTCHA - поле **Использовать CAPTCHA при восстановлении пароля** в [настройках](/user_help/settings/settings/settings.php) Главного модуля.

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх