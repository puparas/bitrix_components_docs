# Создание и редактирование купона

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

Создание и редактирование купона

**Недоступно в редакциях:**Стандарт, Старт

# Создание и редактирование купона

### Форма редактирования

| Поле | Описание |
| --- | --- |
| ID | Уникальный идентификатор купона. Поле отображается при редактировании существующей скидки. |
| \*Скидка | В выпадающем списке выбирается одна из имеющихся в системе скидок, к которой будет относиться создаваемый купон. |
| Активность | Признак активности купона. |
| Тип купона | Указывается вид купона:  * **Купон на одну позицию заказа** - купон можно применить только к одному товару и только один раз. Если в заказе несколько товаров, то купон применяется к самому дорогому товару; * **Купон на один заказ** - купон можно применить один раз на   один любой заказ      Если один покупатель использовал такой купон в заказе, то другие покупатели воспользоваться им уже не смогут.   ; * **Многоразовый купон** - купон может применяться к заказам неограниченное количество раз (в том числе и   одним покупателем      Функционал Многоразового купона, который может быть применён каждым пользователем один раз, пока не реализован.   ). |
| \*Код купона | Код купона генерируется по кнопке *Сгенерировать код*. |
| Дата применения купона: (DD.MM.YYYY) | Дата и время, когда купон был использован. Автоматически устанавливается после применения одноразового купона. |
| Комментарий | Пояснение к купону. |

\* - поля, обязательные для заполнения.

<!--
<h2>Кнопки управления

| Кнопка | Описание |
| --- | --- |
| Сохранить | Сохранение внесённых изменений. Переход на страницу со списком купонов. |
| Применить | Применение внесённых изменений. Продолжение редактирования параметров купона. |
| Отменить | Отмена внесённых изменений. Возврат первоначальных значений параметров. |

--!>

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх