# Управление налогами

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

[Управление налогами](/user_help/store/sale/settings/tax/tax_howto.php)
[Список налогов](/user_help/store/sale/settings/tax/sale_tax.php)
[Создание и редактирование налогов](/user_help/store/sale/settings/tax/sale_tax_edit.php)
[Ставки налогов](/user_help/store/sale/settings/tax/sale_tax_rate.php)
[Создание и редактирование ставок налогов](/user_help/store/sale/settings/tax/sale_tax_rate_edit.php)
[Освобождение от налогов](/user_help/store/sale/settings/tax/sale_tax_exempt.php)
[Настройка освобождения от налогов](/user_help/store/sale/settings/tax/sale_tax_exempt_edit.php)
[Ставки НДС](/user_help/store/sale/settings/tax/cat_vat_admin.php)
[Создание и редактирование ставки НДС](/user_help/store/sale/settings/tax/cat_vat_edit.php)

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

[Налоги](/user_help/store/sale/settings/tax/index.php)

Управление налогами

**Недоступно в редакциях:**Стандарт, Старт

# Управление налогами

### Настройка ставок налогов

Ставки налогов настраиваются на странице **Ставки налогов** (*Магазин > Настройки > Налоги > Ставки налогов*). На этой странице для налогов вводятся ставки в зависимости от местоположения покупателя и его типа плательщика (тип плательщика не обязателен).

Для расчёта налогов для данного заказа будут выбираться все ставки налогов, удовлетворяющие следующим условиям:

* налог, к которому относится данная ставка, принадлежит тому сайту, на котором производится заказ;
* местоположение, указанное покупателем в свойстве, у которого стоит флажок **Использовать как местоположение для налогов**, должно входить в список местоположений, на которые действует данная ставка;
* тип плательщика, установленный для данной ставки, совпадает с типом плательщика, выбранным покупателем при оформлении заказа, либо для данной ставки тип плательщика не установлен;
* данная ставка налога активна.

Если страна представлена более чем одним местоположением и необходимо задать ставку налога, которая действует на всю страну, то рекомендуется создать группу местоположений, включающую все местоположения этой страны, и при вводе ставки налога указать эту группу местоположений.

Если для данного заказа указано более одной ставки налогов, то порядок применения этих ставок следующий:

* Ставки налогов применяются по порядку в соответствии со значениями в поле **Порядок применения** ставок налогов, начиная с наименьшего.
* Ставка налога с данным порядком применения применяется к сумме, в которой уже учтены все налоги с меньшим порядком применения. Другими словами действуют сложные проценты (проценты на проценты).
* Если ставки налогов имеют один и тот же порядок применения, то они складываются, т.е. они применяются к одной и той же сумме.

### Пример вычисления стоимости заказа

Пусть покупается товар стоимостью 25 рублей. Скидка при покупке на сумму более 20 рублей равна 2%. Пусть данному заказу соответствуют следующие ставки налогов:

* **Налог 1** со ставкой **18.5%** и порядком применения **100**;
* **Налог 2** со ставкой **2.7%** и порядком применения **100**;
* **Налог 3** со ставкой **3%** и порядком применения **200**.

Тогда стоимость товара с учётом скидки будет равна **24,5** рубля (**25 - 25 \* 2 / 100**).

**Налог 1** будет равен **4,53** рубля (**24.5 \* 18.5 / 100**). **Налог 2** будет равен **0,66** рубля (**24.5 \* 2.7 / 100**). После применения **Налога 1** и **Налога 2** стоимость заказа будет равна **29,69** рублей (**24.5 + 4.53 + 0.66**).

**Налог 3** будет равен **0,89** рубля (**29.69 \* 3 / 100**).

После применения скидки и всех налогов стоимость заказа будет составлять **30,58** рублей (**29.69 + 0.89**). Далее в эту стоимость должна быть включена стоимость доставки.

### Освобождение от налогов

Эта функциональная возможность применяется, если существуют покупатели, которые освобождены от уплаты части налогов. Создайте специальную группу пользователей, выберите ее на странице **Освобождение от налогов** (*Магазин > Настройки > Налоги > Освобождение от налогов*) и укажите, какие налоги не нужно применять к членам этой группы.

После поступления от покупателя документов, удостоверяющих его право на освобождение от налогов, привяжите этого покупателя к созданной специальной группе пользователей. Тогда при оформлении заказа этому покупателю будет предоставлена возможность выбора: применять освобождение от налогов или оформить заказ на общих основаниях. Если покупатель выберет применение освобождения от налогов, то при расчёте стоимости заказа ставки тех налогов, которые выбраны на странице настроек освобождения от налогов для данной специальной группы пользователей, учитываться не будут.

### Смотрите также

* [Создание налога](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=42&LESSON_ID=12225#tarifs)
* [Создание ставки налога](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=42&LESSON_ID=12225#tarifs_settings)
* [Не определяется ставка налога](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=42&LESSON_ID=12225#stavka)
* [Сделать для новых товаров автоматом включение НДС в цену](https://dev.1c-bitrix.ru/community/webdev/user/3420/blog/549/)
* [Как установить ставку НДС для всего каталога товаров](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=42&LESSON_ID=3458#catalog_nds)

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх