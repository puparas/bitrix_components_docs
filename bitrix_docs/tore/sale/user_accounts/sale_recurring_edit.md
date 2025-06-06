# Создание и редактирование продления подписки

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

[Мастер магазина](/user_help/store/storeassist.php)

[Интернет-магазин](/user_help/store/sale/index.php)

[Интернет-магазин. Настройки модуля](/user_help/store/sale/settings_sale.php)
[Конвертация интернет-магазина](/user_help/store/sale/sale_converter.php)
[Интеграция с CRM](/user_help/store/sale/sale_crm.php)
[Синхронизация заказов с Б24](/user_help/store/sale/sale_order_crm.php)

[Заказы](/user_help/store/sale/orders/index.php)

[Кассы ККМ](/user_help/store/sale/cashbox/index.php)

[Покупатели](/user_help/store/sale/user_accounts/index.php)

[Список покупателей](/user_help/store/sale/user_accounts/buyers_list.php)
[Просмотр профиля покупателя](/user_help/store/sale/user_accounts/profile_view.php)
[Редактирование профиля](/user_help/store/sale/user_accounts/sale_buyers_profile_edit.php)
[Корзины](/user_help/store/sale/user_accounts/baskets.php)
[Внутренние счета покупателей](/user_help/store/sale/user_accounts/sale_account_admin.php)
[Создание и редактирование счета](/user_help/store/sale/user_accounts/sale_account_edit.php)
[Продление подписки](/user_help/store/sale/user_accounts/sale_recurring_admin.php)
[Создание и редактирование продления подписки](/user_help/store/sale/user_accounts/sale_recurring_edit.php)
[Транзакции](/user_help/store/sale/user_accounts/sale_transact_admin.php)
[Выполнение новой транзакции](/user_help/store/sale/user_accounts/sale_transact_edit.php)
[Пластиковые карты](/user_help/store/sale/user_accounts/sale_ccards_admin.php)
[Создание и редактирование пластиковой карты](/user_help/store/sale/user_accounts/sale_ccards_edit.php)
[Список подписок](/user_help/store/sale/user_accounts/cat_subscription_list.php)

[Аффилиаты](/user_help/store/sale/affiliates/index.php)

[Отчеты](/user_help/store/sale/statistic/index.php)

[Настройки магазина](/user_help/store/sale/settings/index.php)

[Торговый каталог](/user_help/store/catalog/index.php)

[Клиенты](/user_help/clients/index.php)

[Сервисы](/user_help/service/index.php)

[Веб-аналитика](/user_help/statistic/index.php)

[Marketplace](/user_help/marketplace/index.php)

[Настройки](/user_help/settings/index.php)

[Компоненты](/user_help/components/index.php)

[Описание компонентов решений](/user_help/description_decisions/index.php)

[Дополнительно](/user_help/additional/index.php)

[Магазин](/user_help/store/index.php)

[Интернет-магазин](/user_help/store/sale/index.php)

[Покупатели](/user_help/store/sale/user_accounts/index.php)

Создание и редактирование продления подписки

**Недоступно в редакциях:**Малый бизнес, Стандарт, Старт

# Создание и редактирование продления подписки

### Поля формы

| Поле | Описание |
| --- | --- |
| ID | Идентификатор записи о продлении подписки в системе.   Отображается в режиме редактирования продления подписки. |
| Дата последнего изменения | Дата и время последнего изменения подписки.   Отображается в режиме редактирования продления подписки. |
| \*Пользователь | Регистрационный код пользователя, для которого оформляется продление подписки. Выбор кода осуществляется из списка, открываемого с помощью кнопки [**...**]. |
| Отменено | Признак недействительности продления подписки.   Если выбрана данная опция, то продление подписки считается недействительным (т.е. продление отменяется). |
| Причины отмены | Если продление подписки отменяется, то в данном поле указываются причины отмены. |
| Модуль | Название модуля, право на доступ к контенту которого продлевается. |
| \*Товар | Идентификационный номер товара, подписка на использование которого продлевается. |
| Название товара | Полное наименование товара. |
| Ссылка на товар | Ссылка на страницу с информацией о товаре. |
| Дата последнего продления (DD.MM.YYYY HH:MI:SS) | Дата и время оформления предыдущего продления подписки. |
| \*Дата очередного продления (DD.MM.YYYY HH:MI:SS) | Дата и время предстоящего продления подписки. |
| Предыдущая попытка выполнения успешна | Признак успешности предыдущего оформления продления подписки. |
| Осталось попыток продления | Если продление подписки осуществляется автоматически, то в данном поле указывается количество возможных попыток продления. Если значение поля равно **0**, то попытка продления подписки производиться не будет. |
| \*Код базового заказа | Код продлеваемого заказа. |
| Описание | Произвольное описание записи о продлении подписки. |

\* - поля, обязательные для заполнения.

### Смотрите также

* [Продление подписки (учебный курс "Администратор. Бизнес")](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=42&LESSON_ID=3199)

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх