# Сканирование файлов

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

[Операционная система](/user_help/settings/security/xscan/operating_system.php)
[Проверка .htaccess](/user_help/settings/security/xscan/htaccess_check.php)
[Сканирование файлов](/user_help/settings/security/xscan/scanning_files.php)

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

[Поиск троянов](/user_help/settings/security/xscan/index.php)

Сканирование файлов (23.0.0)

# Сканирование файлов

На странице **Поиск троянов** (*Настройки > Проактивная защита > Поиск троянов > Сканирование файлов*) запускается скрипт, который сканирует сайт в поисках определённых шаблонов потенциально вредоносного кода и формирует список подозрительных файлов. Потенциально вредоносный код может быть как в отдельно созданных файлах, так и в модифицированных файлах сайта.

**Примечание.** Помните, что не все результаты срабатывания сканера на самом деле являются троянами – иногда разработчики сайтов пишут код, который сканер может принять за потенциально вредоносный.

  

### Контекстная панель

| Кнопка | Описание |
| --- | --- |
| Начальный путь | Указывается путь, от которого начнётся сканирование. По умолчанию сканирование выполняется от корня сайта – от папки `/home/bitrix/www`. |
| Начать поиск | Кнопка запускает процесс сканирования сайта от заданного начального пути. |

### Фильтр

Приведённая ниже таблица описывает параметры, по которым могут выбираться записи результатов сканирования.

| Поле | Описание |
| --- | --- |
| Дата модификации | Фильтр по дате модификации файла. |
| Дата создания | Фильтр по дате создания файла. |
| tags | Фильтр по тегу. Доступные значения:  * **core**; * **no\_prolog**; * **obfuscator**; * **lang**; * **hidden**; * **random\_name**; * **marketplace**/ |
| preset | Фильтр по предустановленным условиям:  * по папке `/bitrix/admin`; * по папке `/bitrix/modules`; * по папке `/bitrix/components`; * по всем папкам, кроме `/bitrix/modules`; * по частым местам. |

### Список файлов

| Поле | Описание |
| --- | --- |
| id | Номер файла. |
| Имя | Расположение и название файла. Представляет собой ссылку, при клике на которую откроется страница детального просмотра. |
| Тип опасности | Системные сообщения об обнаруженных типах опасности    Полный перечень типов:  [337] strings from black list  [630] long line  [321] base64\_encoded code   . |
| Размер | Размер файла. |
| Действия | В списке файлов можно сразу отправить выбранный файл в карантин. При этом файл останется в своей текущей директории, но будет переименован – вместо **.php** в расширении файла будет **.ph\_** (в таком виде файл не будет выполнятся и, соответственно, не принесёт вреда). Учтите, что если файл используется на сайте, переименование файла приведёт к неработоспособности сайта. Для возврата из карантина кликните по кнопке **Восстановить** в списке файлов. **Примечание.** При запуске нового сканирования все файлы, отправленные в карантин, перестанут отображаться в общем списке обнаруженных файлов. |
| Оценка | Оценка вероятной угрозы варьируется от 0 до 1. Чем больше срабатываний по файлу и опаснее он, тем выше оценка. Однако следует внимательно анализировать все файлы, так как троян может иметь низкую оценку. |
| Дата модификации | Дата и время модификации файла. |
| Дата создания | Дата и время создания файла. |
| tags | Присвоенный тег:  * **core**; * **no\_prolog**; * **obfuscator**; * **lang**; * **hidden**; * **random\_name**; * **marketplace**/ |
| Скрыть | Кнопка позволяет скрыть выбранный файл из результатов сканирования. Чтобы его вернуть, потребуется повторить сканирование. |

В списке также можно отметить нужные результаты и скачать их, чтобы проверить обычным антивирусом или на сайте [www.virustotal.com](https://www.virustotal.com/).

### Детальный просмотр

При клике по файлу открывается страница детального просмотра, на которой отображаются название и расположение файла, дата его создания и модификации, оценка вероятной угрозы от 0 до 1, информационное сообщение о результатах проверки, а также особо выделен подозрительный код. В самом низу приведено содержимое файла.

Доступны следующие действия:

* Переместить **В карантин**. При этом файл останется в своей текущей директории, но будет переименован – вместо **.php** в расширении файла будет **.ph\_** (в таком виде файл не будет выполнятся и, соответственно, не принесёт вреда). Учтите, что если файл используется на сайте, переименование файла приведёт к неработоспособности сайта. Для возврата из карантина кликните по кнопке
  Восстановить



  ![](/images/admin_expert/security/recover_from_quarantine.png)
  в списке файлов, либо же найдите файл в его директории и переименуйте расширение обратно в **.php**;

  **Примечание.** При запуске нового сканирования все файлы, отправленные в карантин, перестанут отображаться в общем списке обнаруженных файлов.
* **Скрыть** из результатов сканирования. Чтобы его вернуть, потребуется повторить сканирование;
* **Редактировать** – при клике по этой кнопке откроется новое окно, в котором можно отредактировать файл;
* **Закрыть** – кнопка закроет окно детального просмотра, и вы вернётесь к списку файлов.

**Важно!** Убедитесь, что у вас есть доступ к ftp/ssh для отката изменений.

Если у вас несколько сайтов на одном хосте, вам необходимо отдельно обновлять и проверять каждый сайт.

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх