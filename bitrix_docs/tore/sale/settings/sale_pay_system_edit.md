# Создание и редактирование платежной системы

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

[Настройки магазина](/user_help/store/sale/settings/index.php)

Создание и редактирование платежной системы

**Недоступно в редакциях:**Стандарт, Старт

# Создание и редактирование платежной системы

В форме создания и редактирования платежной системы вы можете задать или изменить значения параметров системы.

### Закладка Ограничения

На закладке задаются ограничения по использованию текущей платежной системы. Закладка доступна в форме редактирования существующей платежной системы.

| Поле | Описание |
| --- | --- |
| кнопка *Добавить ограничение* | Служит для добавления ограничения путем заполнения данных во всплывающей форме. Ограничения могут быть:  * по типу плательщика; * по цене; * % от стоимости заказа (актуально для платёжной системы "Внутренний счёт" - указывается % от стоимости заказа, который можно оплатить с помощью средств внутреннего   счёта покупателя      **Счет покупателя** - пополняемый "кошелек" пользователя в рамках магазина, с которого он проводит расчеты с магазином по мере необходимости.     [Подробнее](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=42&LESSON_ID=12449)...   ); * по службе доставки; * по сайтам; * по категории товара; * по конкретным товарам. |
| кнопка *Настроить* | Позволяет перейти к диалогу настройки внешнего вида таблицы со списком ограничений. |
| *таблица со списком ограничений* | | Поле | Описание | | --- | --- | | Действия | Действия над ограничением:  * **Редактировать** - редактирование параметров ограничения во всплывающем окне; * **Удалить** - удаление ограничения. | | ID | Идентификатор ограничения. | | Сортировка | Относительный "вес" ограничения. | | Тип ограничения | Тип ограничения. | | Параметры | Параметры ограничения. | |

### Файлы-обработчики

Файлы работы с платежной системой обрабатываются следующим образом:

* **Файл-обработчик** вызывается непосредственно после оформления заказа, а также при выборе клиентом функции повторения платежа в персональном разделе. Этот файл может содержать скрипт, отображающий на экране необходимый платежный документ, или форму для отправки данных электронной платежной системе. Подробности смотрите в разделе [Обработка платежных систем](/user_help/store/sale/settings/sale_pay_system_file.php).
* **Обработчик результатов** вызывается сайтом для запроса параметров оплаты заказа у электронной платежной системы. Если платежная система не возвращает параметры заказа (успешна ли оплата, сколько реально оплачено и т.п.), то задавать обработчик результатов не нужно.

### Смотрите также

* [Платежные системы (курс "Администратор. Бизнес")](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=42&CHAPTER_ID=03076)

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх