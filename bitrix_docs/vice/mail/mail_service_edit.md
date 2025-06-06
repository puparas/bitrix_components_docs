# Создание и редактирование почтового сервиса

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

[Бизнес-процессы](/user_help/service/bizproc/index.php)

[Блоги](/user_help/service/blogs/index.php)

[Веб-мессенджер](/user_help/service/im/index.php)

[Веб-формы](/user_help/service/form/index.php)

[Видеоконференциии (КП)](/user_help/service/video/index.php)

[Внешние источники данных (КП)](/user_help/service/xdi/index.php)

[Интранет (КП)](/user_help/service/intranet/index.php)

[Календарь событий](/user_help/service/event_calendar/index.php)

[Конструктор отчетов (КП)](/user_help/service/report/index.php)

[Экстранет (КП)](/user_help/service/extranet/index.php)

[Контроллер](/user_help/service/controller/index.php)

[Менеджер идей](/user_help/service/idea/index.php)

[Опросы, голосования](/user_help/service/vote/index.php)

[Обучение](/user_help/service/learning/index.php)

[Подписка, рассылки](/user_help/service/subscribe/index.php)

[Почта](/user_help/service/mail/index.php)

[Почта. Настройки модуля](/user_help/service/mail/settings.php)
[Почтовые ящики](/user_help/service/mail/mail_mailbox_admin.php)
[Создание и редактирование почтового ящика](/user_help/service/mail/mail_mailbox_edit.php)
[Правила](/user_help/service/mail/mail_filter_admin.php)
[Создание и редактирование правила](/user_help/service/mail/mail_filter_edit.php)
[Журнал работы](/user_help/service/mail/mail_log.php)
[Письма](/user_help/service/mail/mail_message_admin.php)
[Просмотр сообщения](/user_help/service/mail/mail_message_view.php)
[Почтовые сервисы](/user_help/service/mail/mail_services.php)
[Создание и редактирование почтового сервиса](/user_help/service/mail/mail_service_edit.php)

[Рейтинги](/user_help/service/rating/index.php)

[Смайлы](/user_help/service/smile/index.php)

[Социальная сеть (КП)](/user_help/service/socialnetwork/index.php)

[Социальные сервисы](/user_help/service/socialservices/index.php)

[Стикеры](/user_help/service/stickers/index.php)

[Техподдержка](/user_help/service/support/index.php)

[Учет рабочего времени (КП)](/user_help/service/timeman/index.php)

[Форум](/user_help/service/forum/index.php)

[CRM (КП)](/user_help/service/crm/index.php)

[Веб-аналитика](/user_help/statistic/index.php)

[Marketplace](/user_help/marketplace/index.php)

[Настройки](/user_help/settings/index.php)

[Компоненты](/user_help/components/index.php)

[Описание компонентов решений](/user_help/description_decisions/index.php)

[Дополнительно](/user_help/additional/index.php)

[Сервисы](/user_help/service/index.php)

[Почта](/user_help/service/mail/index.php)

Создание и редактирование почтового сервиса

**Недоступно в редакциях:**Малый бизнес, Стандарт, Старт

# Создание и редактирование почтового сервиса

Форма **редактирования свойств почтового сервиса** служит для создания новых и редактирования уже созданных сервисов электронной почты. Для создания нового почтового сервиса вам следует заполнить поля формы и нажать кнопку **Сохранить**.

  

### Контекстная панель

| Кнопка | Описание |
| --- | --- |
| Список почтовых сервисов | Позволяет вернуться к [списку почтовых сервисов](/user_help/service/mail/mail_services.php). |
| Добавить новый сервис | Создание нового почтового сервиса, переход к форме создания сервиса. |
| Удалить данный сервис | Удаление данного сервиса.   Отображается только при редактировании. |

### Закладка Почтовый сервис

| Поле | Описание |
| --- | --- |
| Код | Код сервиса, создаётся автоматически при создании.  Поле отображается при редактировании почтового ящика. |
| Сайт | Сайт, в котором данный сервис активен. |
| Активен | Признак активности почтового сервиса. |
| Логотип | Выбирается файл с логотипом почтового сервиса. |
| \*Название | Произвольное название почтового сервиса. |
| Тип | При добавлении нового сервиса можно выбрать тип почтового сервера:  * **imap**; * domain      Если при добавлении нового сервиса выбран тип почтового сервера **domain**, то в форме добавления появляются два новых поля: **Доменное имя** и **Токен**        domain.png        В эти поля вносятся данные, полученные у доменного регистратора. Уточняйте процедуру их получения у вашего регистратора. Например, о получении **ПДД** (Почта для домена)-токена Яндекс можно почитать [здесь](https://yandex.ru/dev/pdd/doc/concepts/access-docpage/).  | Описание | Произвольное описание почтового ящика. | | Почтовый сервер (IMAP) / порт | Адрес сервера, соединение с которым будет использоваться для работы почты.   Порт, к которому должно осуществляться подключение. | | Использовать безопасное соединение (TLS) | Использование безопасного TLS соединения.   **Примечание:** для использования безопасного соединения в **PHP** должно быть установлено расширение **OpenSSL**. | | Адрес веб-интерфейса | Указывается адрес веб-интерфейса. | | Сортировка | Указывается индекс сортировки в общем списке сервисов. | |

\* - поля, обязательные для заполнения.

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх