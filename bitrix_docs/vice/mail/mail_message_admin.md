# Письма

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

Письма

**Недоступно в редакциях:**Малый бизнес, Стандарт, Старт

# Письма

### Контекстная панель

| Кнопка | Описание |
| --- | --- |
| Получить почту | Команда получения почты с выбором почтового ящика |
| Настроить | Переход к диалогу настройки внешнего вида отчетной формы. |
| Excel | Экспорт данных из таблицы в **MS Excel**. |

Поле **Получить почту** позволяет проверить [наличие новых сообщений](#create).

### Список сообщений

| Колонка | Описание |
| --- | --- |
| Колонка флажков | Выбор сообщений, к которым предполагается применить какое-либо правило или действие. Возможные правила и действия содержатся в области **Обработка писем**. |
| Тема | Тема полученного сообщения. |
| От кого | Отправитель сообщения. В качестве отправителя отображается **имя отправителя**, которое назначил себе сам отправитель. |
| Дата | Дата получения сообщения. |
| Ящик | Название почтового ящика, с которого получено данное сообщение. |
| Размер | Размер сообщения в байтах. |
| СПАМ коэф. | Относительный показатель принадлежности сообщения к спаму (сообщения массовой несанкционированной рассылки). |
| Влож. | Количество вложений в данном сообщении.   **Примечание:** сообщения, отправленные в формате **HTML**, всегда имеют хотя бы одно вложение - само сообщение в формате **HTML**. |

### Как проверить наличие новых сообщений

Чтобы проверить наличие новых сообщений в мини-форме **Получить почту** выберите интересующий вас ящик (или все ящики) и нажмите кнопку **ОК**.

В открывшейся промежуточной форме **Получение новой почты** отобразится статус проверки по каждому из ящиков и количество полученных сообщений.

Если при получении почты с какого-либо адреса возникли ошибки, статус проверки ящика будет включать ссылку **Настройки почтового ящика**. Перейдя по этой ссылке можно изменить свойства этого ящика (например, откорректировать пароль доступа).

### Как удалить сообщения или применить другие правила и действия к сообщениям

Для применения любого возможного действия или правила к сообщению или группе сообщений:

1. Отметьте требуемые сообщения, обозначив их в **Колонке флажков**. Чтобы выделить все сообщения, поставьте флажок в заголовке таблицы.
2. В мини-форме **Обработка писем** укажите, следует ли применять правило ко всем ли сообщениям или только к выделенным.
3. Там же выберите требуемое действие, например, **Удалить** или **Пометить как спам**.
4. Нажмите кнопку **ОК**.

### Смотрите также

* [Письма (учебный курс "Администратор. Модули")](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=41&LESSON_ID=2864)

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх