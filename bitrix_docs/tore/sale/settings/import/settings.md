# Настройка импорта

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

[Аффилиаты](/user_help/store/sale/affiliates/index.php)

[Отчеты](/user_help/store/sale/statistic/index.php)

[Настройки магазина](/user_help/store/sale/settings/index.php)

[Платежные системы](/user_help/store/sale/settings/sale_pay_system.php)
[Создание и редактирование платежной системы](/user_help/store/sale/settings/sale_pay_system_edit.php)
[Настройка возвратов](/user_help/store/sale/settings/sale_ps_handler_refund.php)
[Обработчики платежных систем](/user_help/store/sale/settings/sale_pay_system_file.php)
[Компании](/user_help/store/sale/settings/sale_company.php)
[Создание и редактирование компании](/user_help/store/sale/settings/sale_company_edit.php)
[Типы плательщиков](/user_help/store/sale/settings/sale_person_type.php)
[Создание и редактирование типа плательщика](/user_help/store/sale/settings/sale_person_type_edit.php)
[Статусы](/user_help/store/sale/settings/sale_status.php)
[Создание и редактирование информационного статуса заказа](/user_help/store/sale/settings/sale_status_edit.php)
[Соответствие значений бизнес-смыслу](/user_help/store/sale/settings/sale_business_value.php)
[Интеграция с 1С](/user_help/store/sale/settings/1c_admin.php)
[Печатные формы](/user_help/store/sale/settings/print_form.php)
[Единицы измерения](/user_help/store/sale/settings/cat_measure_list.php)
[Создание и редактирование единицы измерения](/user_help/store/sale/settings/cat_measure_edit.php)

[Экспорт](/user_help/store/sale/settings/export/index.php)

[Импорт](/user_help/store/sale/settings/import/index.php)

[Настройка импорта](/user_help/store/sale/settings/import/settings.php)
[Ручной импорт в формате CSV (профиль по умолчанию)](/user_help/store/sale/settings/import/import_csv.php)
[Ручной импорт в формате CommerceML (профиль по умолчанию)](/user_help/store/sale/settings/import/import_commerceml.php)
[Ручной импорт в формате CommerceML MySql Fast - BETA VERS (профиль по умолчанию)](/user_help/store/sale/settings/import/import_commerceml_g.php)
[Создание профилей импорта](/user_help/store/sale/settings/import/cat_import_setup_creat_prf.php)
[Импорт из 1С (загрузка данных)](/user_help/store/sale/settings/import/1c.php)

[Свойства заказа](/user_help/store/sale/settings/order_props/index.php)

[Службы доставки](/user_help/store/sale/settings/delivery/index.php)

[Местоположения](/user_help/store/sale/settings/location2/index.php)

[Налоги](/user_help/store/sale/settings/tax/index.php)

[Торговые платформы](/user_help/store/sale/settings/trandingplatforms/index.php)

[Цены](/user_help/store/sale/settings/prices/index.php)

[Торговый каталог](/user_help/store/catalog/index.php)

[Клиенты](/user_help/clients/index.php)

[Сервисы](/user_help/service/index.php)

[Веб-аналитика](/user_help/statistic/index.php)

[Marketplace](/user_help/marketplace/index.php)

[Настройки](/user_help/settings/index.php)

[Компоненты](/user_help/components/index.php)

[Описание компонентов решений](/user_help/description_decisions/index.php)

[Дополнительно](/user_help/additional/index.php)

...

[Интернет-магазин](/user_help/store/sale/index.php)

[Настройки магазина](/user_help/store/sale/settings/index.php)

[Импорт](/user_help/store/sale/settings/import/index.php)

Настройка импорта

**Недоступно в редакциях:**Стандарт, Старт

# Настройка импорта

### Настройки импорта

| Действия | ID | Название | Файл | Профиль | В меню | В агентах | На сron'e | Использован | Кем изменен | Дата изменения |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [1] | [2] | [3] | [4] | [5] | [6] | [7] | [8] | [9] | [10] | [11] |

| Поле | Описание |
| --- | --- |
| [1] Действия | Операции, которые могут быть применены к профилю/скрипту импорта:  * **Импортировать** - запуск профиля импорта; * **Добавить профиль** - запуск профиля импорта с возможностью сохранения схемы импорта. Действие недоступно для пользовательских профилей. * **Редактировать** - переход к редактированию настроек схемы импорта. Действие доступно только для пользовательских профилей. * **Копировать** - копирование существующей схемы импорта. Действие доступно только для пользовательских профилей; * **Список переменных** - отображает список импортируемых переменных в отдельном окне. Действие доступно только для пользовательских профилей. * **Добавить в меню** - добавление ссылки на профиль импорта в левое меню административной части сайта;* **Создать агента** - создание PHP функции-агента для автоматического импорта с использованием данного профиля;* **Повесить на cron** - привязка профиля к системной утилите `cron` для автоматического импорта;* **Удалить профиль** - удаление профиля. Действие недоступно для профиля "по умолчанию". |
| [2] ID | Идентификатор профиля импорта. Скрипты импорта идентификатора не имеют. |
| [3] Название | Название типа профиля импорта, например, CommerceML. |
| [4] Файл | Имя файла - PHP-скрипта, осуществляющего импорт. |
| [5] Профиль | Название профиля импорта.    Профиль "по умолчанию" каждый раз перед началом операции предлагает указать параметры импорта. При использовании пользовательского профиля, импорт осуществляется автоматически в соответствии с параметрами, указанными при создании профиля. |
| [6] В меню | Указывает, помещен ли данный профиль для быстрого доступа в левое меню административной части. Поместить профиль в левое меню можно при помощи действия **Добавить в меню** в колонке **Действия**. |
| [7] В агентах | Указывает, существует ли агент, осуществляющий в случае необходимости (по истечении определённого интервала времени) автоматическую загрузку элементов каталога. Создать агента для профиля можно при помощи действия **Создать агента** в колонке **Действия**. |
| [8] В cron'е | Указывает, привязан ли профиль к утилите `cron` для автоматической периодической загрузки данных. Привязка профиля к утилите `cron` осуществляется при помощи действия **Привязать к cron** в колонке **Действия**. |
| [9] Использован | Дата и время последнего импорта с использованием данного профиля. |
| [10] Кем изменен | Имя пользователя, внесшего последние изменения в данный профиль. |
| [11] Дата изменения | Дата и время последнего изменения данного профиля. |

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх