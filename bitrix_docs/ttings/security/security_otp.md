# Двухэтапная авторизация

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

[Адреса и местоположения](/user_help/settings/location/index.php)

[Избранное](/user_help/settings/favorites/index.php)

[Пользователи](/user_help/settings/users/index.php)

[Поиск](/user_help/settings/search/index.php)

[Проактивная защита](/user_help/settings/security/index.php)

[Проактивная защита. Настройки модуля](/user_help/settings/security/settings.php)
[Сканер безопасности](/user_help/settings/security/security_scanner.php)
[Панель безопасности](/user_help/settings/security/security_panel.php)
[Проактивный фильтр](/user_help/settings/security/security_filter.php)
[Веб-антивирус](/user_help/settings/security/security_antivirus.php)
[Журнал вторжений](/user_help/settings/security/event_log.php)
[Двухэтапная авторизация](/user_help/settings/security/security_otp.php)

[Поиск троянов](/user_help/settings/security/xscan/index.php)

[Контроль целостности](/user_help/settings/security/security_file_verifier.php)
[Защита административного раздела](/user_help/settings/security/security_iprule_admin.php)
[Защита сессий](/user_help/settings/security/security_session.php)
[Защита редиректов](/user_help/settings/security/security_redirect.php)
[Защита от фреймов](/user_help/settings/security/security_frame.php)
[Контроль активности](/user_help/settings/security/security_stat_activity.php)
[Стоп-лист](/user_help/settings/security/security_iprule_list.php)
[Создание и редактирование правила стоп-листа](/user_help/settings/security/security_iprule_edit.php)
[Хосты/домены](/user_help/settings/security/security_hosts.php)

[DAV (КП)](/user_help/settings/dav/index.php)

[Push and Pull](/user_help/settings/pull/index.php)

[REST API](/user_help/settings/rest_api/index.php)

[Валюты](/user_help/settings/currency/index.php)

[Веб-кластер](/user_help/settings/cluster/index.php)

[Веб-сервисы](/user_help/settings/webservice/index.php)

[Диск (КП)](/user_help/settings/disk/index.php)

[Конвертер файлов (КП)](/user_help/settings/transformer/index.php)

[Коннекторы для внешних мессенджеров (КП)](/user_help/settings/imconnector/index.php)

[Открытые линии (КП)](/user_help/settings/imopenlines/index.php)

[Распознавание лиц (КП)](/user_help/settings/faceid/index.php)

[Сервер конвертации файлов (КП)](/user_help/settings/transformercontroller/index.php)

[Служба сообщений](/user_help/settings/message_service/index.php)

[Телефония](/user_help/settings/voximplant/index.php)

[Облако 1С-Битрикс](/user_help/settings/bitrixcloud/index.php)

[Облачные хранилища](/user_help/settings/clouds/index.php)

[AD/LDAP интеграция](/user_help/settings/ldap/index.php)

[Перевод](/user_help/settings/translate/index.php)

[XMPP сервер (КП)](/user_help/settings/xmpp/index.php)

[Настройки продукта (главный модуль)](/user_help/settings/settings/index.php)

[Инструменты](/user_help/settings/utilities/index.php)

[Монитор производительности](/user_help/settings/perfmon/index.php)

[ЧатБоты (КП)](/user_help/settings/imbot/index.php)

[Компрессия](/user_help/settings/compression/index.php)

[Компоненты](/user_help/components/index.php)

[Описание компонентов решений](/user_help/description_decisions/index.php)

[Дополнительно](/user_help/additional/index.php)

[Настройки](/user_help/settings/index.php)

[Проактивная защита](/user_help/settings/security/index.php)

Двухэтапная авторизация

**Недоступно в редакциях:**Старт

# Двухэтапная авторизация

Закладки

Система [одноразовых паролей](http://ru.wikipedia.org/wiki/%D0%9E%D0%B4%D0%BD%D0%BE%D1%80%D0%B0%D0%B7%D0%BE%D0%B2%D1%8B%D0%B9_%D0%BF%D0%B0%D1%80%D0%BE%D0%BB%D1%8C) дополняет стандартную систему авторизации и позволяет значительно усилить систему безопасности интернет-проекта. Для включения системы необходимо использовать аппаратное устройство (например, [Aladdin eToken PASS](http://www.aladdin.ru/catalog/etoken/models/etoken_pass/)) или использовать соответствующее [программное обеспечение](http://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=52&LESSON_ID=6819). Система одноразовых паролей рекомендуется к использованию администраторам сайтов для повышения уровня безопасности.

  

### Двухэтапная авторизация

Включение или отключение механизма двухэтапной авторизации производится на странице **Двухэтапная авторизация** (*Настройки > Проактивная защита > Двухэтапная авторизация*) с помощью кнопки **Включить/Выключить двухэтапную авторизацию**.

### Параметры

Форма позволяет настроить параметры механизма двухэтапной авторизации.

| Поле | Описание |
| --- | --- |
| Размер окна проверки паролей | Задается размер окна проверки паролей. Настройка актуальна только для алгоритма генерации паролей **по счетчику**.    Если на устройстве была нажата кнопка несколько раз (например, случайно), но не было выполнено ни одной удачной аутентификации, то при превышении числа нажатий значения, заданного в этом параметре, произойдет нарушение синхронизации счетчика генерации, и пользователь не сможет выполнить вход на сайт. |
| Алгоритм генерации паролей по умолчанию | Выбирается алгоритм генерации паролей, который будет использоваться по умолчанию в системе:  * **по счетчику** ([HMAC-Based One-time Password](http://ru.wikipedia.org/wiki/HOTP), **HOTP**); * **по времени** ([Time-based One-time Password](http://ru.wikipedia.org/wiki/Time-based_One-time_Password_Algorithm), **TOTP**). |
| Разрешить запоминание одноразового пароля | При отмеченной опции будет разрешено запоминание введенного одноразового пароля с помощью соответствующей опции в форме авторизации.    **Примечание:** Опция позволят сохранить одноразовый пароль во всех случаях, согласно настройкам [политики безопасности](/user_help/settings/users/group_edit.php#security) (опции **маска сети для привязки сохраненной авторизации** и **срок хранения авторизации, запомненной на компьютере пользователя**) группы, в которую входит пользователь, кроме случая самостоятельного завершения сессии. |
| Разрешить использование резервных кодов | При отмеченной опции пользователю будет доступен функционал генерации резервных кодов авторизации, которые можно будет использовать для входа на сайт вместо одноразового пароля. Например, в случае утери устройства для двухэтапной авторизации, пользователь сможет *самостоятельно* авторизоваться на сайте только с помощью этих кодов. |
 Обязательность двухэтапной авторизации | || Требовать двухэтапную авторизацию | При отмеченной опции *указанным пользователям* через *заданное время* будет принудительно подключена двухэтапная авторизация. Отсчет времени начнется при первой авторизации пользователя после включения опции. Другими словами по истечении указанного времени доступ на сайт будет возможен только с использованием одноразового пароля.    В случае, если пользователь в указанный промежуток времени не подключил свое устройство для двухэтапной авторизации и не может зайти на сайт, администратор может на странице [редактирования пользователя](/user_help/settings/users/user_edit.php#pass) **отключить** для него двухэтапную авторизацию на необходимое время. |
| Количество дней для подключения | Указывается период, в течение которого пользователь должен подключить свое устройство для двухэтапной авторизации. Отсчет времени начнется при первой авторизации пользователя после включения опции **требовать двухэтапную авторизацию**. |
| Пользователи с обязательной двухэтапной авторизацией | Указываются пользователи, для которых будет принудительно подключена двухэтапная авторизация. |

### Смотрите также

* [Повышенный уровень защиты (учебный курс "Администратор. Базовый")](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=35&LESSON_ID=2674)

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх