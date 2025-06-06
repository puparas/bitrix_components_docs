# Как импортировать список адресов подписчиков

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

[Подписка, рассылки. Настройки модуля](/user_help/service/subscribe/settings.php)
[Список рассылок](/user_help/service/subscribe/rubric_admin.php)
[Создание и редактирование рассылки](/user_help/service/subscribe/rubric_edit.php)
[Проверка шаблона рассылки](/user_help/service/subscribe/template_test.php)
[Список выпусков](/user_help/service/subscribe/posting_admin.php)
[Создание и редактирование выпуска](/user_help/service/subscribe/posting_edit.php)
[Подписчики](/user_help/service/subscribe/subscr_admin.php)
[Создание и редактирование подписчика](/user_help/service/subscribe/subscr_edit.php)
[Импорт адресов](/user_help/service/subscribe/subscr_import.php)

[Типичные задачи](/user_help/service/subscribe/sample/index.php)

[Для чего нужны списки рассылки](/user_help/service/subscribe/sample/howto_why_newsletter_list.php)
[Как добавить подписчика](/user_help/service/subscribe/sample/howto_add_subscriber.php)
[Как импортировать список адресов подписчиков](/user_help/service/subscribe/sample/howto_import_subscriber_list.php)
[Как создать список рассылки](/user_help/service/subscribe/sample/howto_create_newsletter_list.php)
[Как создать сообщение](/user_help/service/subscribe/sample/howto_create_message.php)
[Как отправить сообщение](/user_help/service/subscribe/sample/howto_send_message.php)

[Почта](/user_help/service/mail/index.php)

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

[Подписка, рассылки](/user_help/service/subscribe/index.php)

[Типичные задачи](/user_help/service/subscribe/sample/index.php)

Как импортировать список адресов подписчиков

**Недоступно в редакциях:**Старт

# Как импортировать список адресов подписчиков

Для добавления адресов подписчиков из внешнего файла вначале следует подготовить файл-источник данных.

  

### Подготовка файла

Адреса в файле могут:

* разделяться запятыми;
* начинаться с новой строки.

Другими словами, файл может выглядеть следующим образом:

```
user1@host.com,user1@host.com,user1@host.com,user1@host.com
```

или

```
user1@host.com  
user1@host.com  

```

### Импорт адресов

1. Откройте форму **Импорт адресов** (*Сервисы > Рассылки > Импорт адресов*).
2. Нажмите кнопку **Обзор...** и укажите файл, содержащий список адресов.
3. Если требуется выслать код подтверждения подписки добавляемым подписчикам, установите флаг **Выслать код подтверждения подписки**.
4. Если требуется автоматически подтвердить подписку всем добавляемым подписчикам, включите опцию **Установить флаг подтверждения подписки**.
5. Если необходимо зарегистрировать добавляемых подписчиков на сайте и создать каждому из них персональный аккаунт, выберите опцию **Как пользователей...** в поле **Добавить подписчиков**.
6. Если вы выбрали  **регистрацию** добавляемых подписчиков как пользователей на сайте, то:
   * для отсылки регистрационной информации каждому из регистрируемых пользователей, включите опцию **Выслать регистрационную информацию...**;
   * выберите группы пользователей, к которым будут приписаны регистрируемые пользователи.
7. Выберите рассылки, на которые по умолчанию будут подписаны пользователи.
8. Выберите формат рассылки для отсылки сообщений регистрируемым пользователям.
9. Нажмите кнопку **Импортировать адреса**.

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх