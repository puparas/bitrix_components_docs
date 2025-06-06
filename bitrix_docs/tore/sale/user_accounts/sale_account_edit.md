# Создание и редактирование  счета

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

Создание и редактирование счета

**Недоступно в редакциях:**Малый бизнес, Стандарт, Старт

# Создание и редактирование счета

<!--
<h4 id="topictoctitle">В этом разделе
- [Контекстная панель](#menu)
- [Поля формы](#fields)
- [Кнопки управления](#buttons)
--!>

Данная форма служит для создания и настройки внутренних счетов пользователей.

#### Контекстная панель

| Кнопка | Описание |
| --- | --- |
| Список счетов | Переход на страницу со [списком](/user_help/store/sale/user_accounts/sale_account_admin.php) внутренних счетов пользователей. |
| Добавить счет | Переход к форме создания нового внутреннего счета. Кнопка отображается при редактировании существующего счета. |
| Удалить счет | Удаление редактируемого счета. |

#### Поля формы

| Поле | Описание |
| --- | --- |
| ID | Идентификатор счета в системе. Поле отображается при редактировании существующего счета. |
| Дата последнего изменения | Дата и время последнего изменения параметров счета. Поле отображается при редактировании существующего счета. |
| \*Пользователь | Идентификатор пользователя-владельца счета.   При создании счета идентификатор пользователя выбирается в списке, открываемом с помощью кнопки [**...**]. |
| \*Сумма на счете | Общая сумма на счете и валюта счета. |
| Заблокировать/Разблокировать бюджет | Возможность вручную заблокировать, разблокировать счёт (бюджет) пользователя. При ручной (не автоматической) блокировке разблокирование возможно только через 1 час. |
| Заметки | Произвольный комментарий к создаваемому счету. |
| Основание изменения суммы на счете | Указывается событие, в связи с которым изменяется сумма на счете. |

\* - поля, обязательные для заполнения.

<!--
<h4>Кнопки управления

| Кнопка | Описание |
| --- | --- |
| Сохранить | Сохранение выполненных изменений. Переход к списку внутренних счетов пользователей. |
| Применить | Сохранение внесённых изменений. Продолжение редактирования параметров счета. |
| Отменить | Отмена внесённых изменений. Возврат первоначальных значений параметров. |

--!>

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх