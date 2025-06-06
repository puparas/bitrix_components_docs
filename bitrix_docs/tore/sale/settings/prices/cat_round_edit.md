# Создание и редактирование правила округления

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

[Свойства заказа](/user_help/store/sale/settings/order_props/index.php)

[Службы доставки](/user_help/store/sale/settings/delivery/index.php)

[Местоположения](/user_help/store/sale/settings/location2/index.php)

[Налоги](/user_help/store/sale/settings/tax/index.php)

[Торговые платформы](/user_help/store/sale/settings/trandingplatforms/index.php)

[Цены](/user_help/store/sale/settings/prices/index.php)

[Типы цен](/user_help/store/sale/settings/prices/cat_group_admin.php)
[Создание и редактирование типа цены](/user_help/store/sale/settings/prices/cat_group_edit.php)
[Правила округления цен](/user_help/store/sale/settings/prices/cat_round_list.php)
[Создание и редактирование правила округления](/user_help/store/sale/settings/prices/cat_round_edit.php)
[Наценки](/user_help/store/sale/settings/prices/cat_extra.php)
[Создание и редактирование наценки](/user_help/store/sale/settings/prices/cat_extra_edit.php)

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

[Цены](/user_help/store/sale/settings/prices/index.php)

Создание и редактирование правила округления (с версии 16.5.4)

**Недоступно в редакциях:**Стандарт, Старт

# Создание и редактирование правила округления

<!--
<h4 id="topictoctitle">В этом разделе
- [Контекстная панель](#menu)
- [Форма редактирования](#extra)
- [Кнопки управления](#buttons)
--!>

### Контекстная панель

| Кнопка | Описание |
| --- | --- |
| Список правил | Переход на страницу со [списком](/user_help/store/sale/settings/prices/cat_round_list.php) правил. |
| Добавить новое | Переход к форме создания нового правила округления. Кнопка отображается при редактировании существующего правила. |
| Скопировать | Переход к форме создания нового правила округления путем копирования параметров текущего. Кнопка отображается при редактировании существующего правила. |
| Удалить | Удаление редактируемого правила. Кнопка отображается при редактировании существующего правила. |

  

### Форма редактирования

| Поле | Описание |
| --- | --- |
| ID | Идентификатор правила. Поле отображается при редактировании существующего правила. |
| \*Тип цен | Тип, к ценам которого применяется правило округления. |
| \*Минимальная цена | Цена, с которой начинает работать правило округления. |
| \*Тип округления | Тип округления, применяемый в правиле: **Математическое** - по арифметическим правилам, **В пользу магазина** - в большую сторону, **В пользу клиента** - в меньшую сторону. |
| \*Точность округления    **Внимание**! Возможны ошибки округления при печати чеков, если, например, в настройках интернет-магазина установлена точность округления при расчетах 3 и более знака и при этом не настроены / настроены неправильно правила округления цен. [Как правильно настроить округление цен.](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=42&LESSON_ID=12387&LESSON_PATH=3912.4580.12387) | Величина, на которую результат должен делиться нацело    Примеры округления (тип - математическое): цена 768,67 руб. 0.01 - 768,67 0.1 - 768,7 0.2 - 768,6 1 - 769 2 - 768 10 - 770 50 - 750 100 - 800 . |

\* - поля, обязательные для заполнения.
<!--
<h4>Кнопки управления

| Кнопка | Описание |
| --- | --- |
| Сохранить | Сохранение параметров правила. Переход на страницу со списком правил округления. |
| Применить | Сохранение внесённых изменений. Продолжение редактирования параметров правила. |
| Отменить | Отмена внесённых изменений. Возврат первоначальных значений параметров. |

--!>

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх