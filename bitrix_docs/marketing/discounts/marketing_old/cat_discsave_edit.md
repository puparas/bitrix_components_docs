# Создание и редактирование накопительной программы

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

[A/B-тестирование](/user_help/marketing/ab_testing/index.php)

[Автоконтекст](/user_help/marketing/context_adv/index.php)

[Товарный маркетинг](/user_help/marketing/discounts/index.php)

[Предустановленный список маркетинговых акций](/user_help/marketing/discounts/sale_discount_preset_list.php)
[Создание и редактирование скидки с помощью мастера](/user_help/marketing/discounts/sale_discount_preset_detail.php)
[Правила работы с корзиной](/user_help/marketing/discounts/sale_discount.php)
[Создание и редактирование правил работы с корзиной](/user_help/marketing/discounts/sale_discount_edit.php)
[Купоны правил корзины](/user_help/marketing/discounts/sale_discount_coupons.php)
[Создание и редактирование купона правила корзины](/user_help/marketing/discounts/sale_discount_coupon_edit.php)

[Скидки каталога и магазина до конвертации](/user_help/marketing/discounts/marketing_old/index.php)

[Скидки на товар](/user_help/marketing/discounts/marketing_old/cat_discount_admin.php)
[Создание и редактирование скидки на товар](/user_help/marketing/discounts/marketing_old/cat_discount_edit.php)
[Купоны скидок на товар](/user_help/marketing/discounts/marketing_old/cat_discount_coupon.php)
[Создание и редактирование купона](/user_help/marketing/discounts/marketing_old/cat_discount_coupon_edit.php)
[Правила работы с корзиной](/user_help/marketing/discounts/marketing_old/basket_rules.php)
[Создание и редактирование правила работы с корзиной](/user_help/marketing/discounts/marketing_old/rule_edit.php)
[Купоны правил корзины](/user_help/marketing/discounts/marketing_old/sale_discount_coupons.php)
[Создание и редактирование купона правила корзины](/user_help/marketing/discounts/marketing_old/sale_discount_coupon_edit.php)
[Накопительные скидки](/user_help/marketing/discounts/marketing_old/cat_discsave_admin.php)
[Создание и редактирование накопительной программы](/user_help/marketing/discounts/marketing_old/cat_discsave_edit.php)

[Email-маркетинг](/user_help/marketing/sender/index.php)

[Триггерные рассылки](/user_help/marketing/triggered_emails/index.php)

[Поисковая оптимизация](/user_help/marketing/seo/index.php)

[Баннерная реклама](/user_help/marketing/advertising/index.php)

[Пульс конверсии](/user_help/marketing/conversion_pulse.php)
[Бизнес модель интернет-магазина](/user_help/marketing/web_store_business_model.php)
[Реклама](/user_help/marketing/ads.php)

[Магазин](/user_help/store/index.php)

[Клиенты](/user_help/clients/index.php)

[Сервисы](/user_help/service/index.php)

[Веб-аналитика](/user_help/statistic/index.php)

[Marketplace](/user_help/marketplace/index.php)

[Настройки](/user_help/settings/index.php)

[Компоненты](/user_help/components/index.php)

[Описание компонентов решений](/user_help/description_decisions/index.php)

[Дополнительно](/user_help/additional/index.php)

[Маркетинг](/user_help/marketing/index.php)

[Товарный маркетинг](/user_help/marketing/discounts/index.php)

[Скидки каталога и магазина до конвертации](/user_help/marketing/discounts/marketing_old/index.php)

Создание и редактирование накопительной программы

**Недоступно в редакциях:**Малый бизнес, Стандарт, Старт

# Создание и редактирование накопительной программы

### Накопительная программа

| Поле | Описание |
| --- | --- |
| ID | Идентификатор накопительной программы в базе данных. Поле отображается только при редактировании программы. |
| Активность | Флаг активности. Только активные программы могут быть применены. |
| \*Название накопительной программы | Любое название программы, дающее представление о случаях применения, величине и т.д. по желанию. |
| \*Сайт | Сайт, к ценам на товары которого применяется накопительная программа. |

\* - поля, обязательные для заполнения.

### Скидки накопительной программы

| Поле | Описание |
| --- | --- |
| Период для расчета скидок | Указывается период времени, за который следует произвести суммирование заказов для расчета скидки. Доступны следующие значения:  * **За все время**. * **За период**. При выбранной опции становятся доступны поля **Дата начала периода** и **Дата окончания периода**. * **За последние**. При выбранной опции становится доступно поле **Выбрать оплаченные заказы за последний(е)**. |
| Срок действия скидок | Указывается период действия скидок. Доступны следующие значения:  * **Бессрочно**. * **Период**. При выбранной опции становятся доступны поля **Дата начала действия скидок** и **Дата окончания действия скидок**. * **Время с момента получения**. При выбранной опции становится доступно поле **Период действия скидок (с момента получения скидки)**. |
| \*Валюта сумм оплаченных заказов и скидок | Указывается валюта, в которой оплачены заказы и выдается скидка. |
| Сумма оплаченных заказов | Минимальная сумма оплаченных заказов, необходимая для получения скидки. |
| Величина скидки | Скидка, получаемая при указанной сумме оплаченных заказов. Может быть выставлена как в процентах, так и в виде фиксированной суммы. |

\* - поля, обязательные для заполнения.

### Ограничения

| Поле | Описание |
| --- | --- |
| \*Группы пользователей | В данном поле выбираются группы пользователей, которые могут воспользоваться скидкой. |

\* - поля, обязательные для заполнения.

### Дополнительно

| Поле | Описание |
| --- | --- |
| Внешний код | Символьный код, используемый для связи накопительной программы с внешним источником данных. |
| Сортировка | Относительный "вес" накопительной программы. Используется для вывода элемента в общем списке. |

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх