| Поле | Описание |
| --- |

|
| ID | Уникальный идентификатор купона. Поле отображается при редактировании существующего купона. |
| \*Активность |

|
| \*Правило корзины | В выпадающем списке выбирается одно из имеющихся в системе правил корзины, к которому будет относиться создаваемый купон. |
| \*Купон |

|
| \*Тип купона | Указывается вид купона:  * **на одну позицию заказа** - купон можно применить только к одному товару и только один раз. Если в заказе несколько товаров, то купон применяется к самому дорогому товару; * **на один заказ** - купон можно применить один раз на   один любой заказ      Если один покупатель использовал такой купон в заказе, то другие покупатели воспользоваться им уже не смогут.   ; * **многоразовый** - купон может применяться к заказам неограниченное количество раз (в том числе и   одним покупателем      Функционал Многоразового купона, который может быть применён каждым пользователем один раз, пока не реализован.   ).      | Ещё раз об использовании многоразовых купонов |   | --- |   | + Обратите внимание на поля **Владелец купона** и **Максимальное число использований**:        coupon.png    - Если указан Владелец, но не число использований - сколько угодно заказов с этим купоном может сделать только он.   - Если прописано Максимальное число использований, но не Владелец - столько заказов с этим купоном может быть создано любым покупателем.   - Если указаны оба параметра, то конкретный клиент сможет ограниченное число заказав сделать с этим купоном. + Не забывайте проверять условия самой скидки и подпадают ли под эти условия покупатели, на которых выписывается купон. Например, если покупатель принадлежит к группе **Розничные покупатели**, а условия скидки распространяются только на **Оптовиков**, то купон не сработает. | |
| Период активности |

|
| Владелец купона | Пользователь, к которому привязан купон. Если пользователь не задан, то купон может применить любой пользователь. |
| Максимальное число использований |

|
| Комментарий | Пояснение к купону. |

\* - поля, обязательные для заполнения.

<!--
<h2>Кнопки управления

| Кнопка | Описание |
| --- |

|
| Сохранить | Сохранение внесённых изменений. Переход на страницу со списком купонов. |
| Применить |