# Управление

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

[Веб-аналитика](/user_help/statistic/index.php)

[Marketplace](/user_help/marketplace/index.php)

[Настройки](/user_help/settings/index.php)

[Компоненты](/user_help/components/index.php)

[CRM (КП)](/user_help/components/crm/index.php)

[Корпоративный портал (КП)](/user_help/components/intranet/index.php)

[Сайты 24](/user_help/components/landing/index.php)

[Управление](/user_help/components/landing/landing_start.php)
[Наполнение страницы](/user_help/components/landing/landing_landing_view.php)
[Предпросмотр шаблона](/user_help/components/landing/landing_demo_preview.php)
[Публикация страницы](/user_help/components/landing/landing_pub.php)
[Редактирование домена](/user_help/components/landing/landing_domain_edit.php)
[Редактирование сайта](/user_help/components/landing/landing_site_edit.php)
[Редактирование страницы](/user_help/components/landing/landing_landing_edit.php)
[Создание сайта / страницы по шаблону](/user_help/components/landing/landing_demo.php)
[Список доменов](/user_help/components/landing/landing_domains.php)
[Список сайтов](/user_help/components/landing/landing_sites.php)
[Список страниц](/user_help/components/landing/landing_landings.php)
[Фильтр](/user_help/components/landing/landing_filter.php)

[Контент](/user_help/components/content/index.php)

[Сервисы](/user_help/components/services/index.php)

[Общение](/user_help/components/obschenie/index.php)

[Магазин](/user_help/components/magazin/index.php)

[Служебные](/user_help/components/sluzhebnie/index.php)

[Описание компонентов решений](/user_help/description_decisions/index.php)

[Дополнительно](/user_help/additional/index.php)

[Компоненты](/user_help/components/index.php)

[Сайты 24](/user_help/components/landing/index.php)

Управление

# Управление

### Описание **landing.start**

Комплексный компонент управления сайтами и страницами.

В визуальном редакторе компонент расположен по пути *Сайты 24 > Управление.*

Компонент относится к модулю [Сайты 24](/user_help/components/landing/index.php).

### Параметры

|  |  |  |  |
| --- | --- | --- | --- |
| **Поле** | **Параметр** | **Описание** | **Примечание** |
| **Управление адресами страниц** | | | |
| Включить поддержку ЧПУ | **SEF\_MODE** | [Y/N] При отмеченной опции будет включена поддержка ЧПУ.  Если режим ЧПУ **включен**, то необходимо настроить следующие параметры:    Настраиваемые параметры при включенном режиме поддержки ЧПУ:  |  |  |  | | --- | --- | --- | | Каталог ЧПУ (относительно корня сайта) | **SEF\_FOLDER** | Каталог ЧПУ: путь до папки, с которой работает компонент. Этот путь может как совпадать с физическим путём, так и не совпадать. | | Адреса страниц | **SEF\_URL\_TEMPLATES** | Указываются адреса следующих страниц:  * **Список сайтов** - ; * **Страница сайта (список лендингов)** ; * **Страница редактирования сайта** ; * **Страница редактирования лендинга** ; * **Страница просмотра/наполнения лендинга** ; * **Список доменов** ; * **Страница редактирования домена** ; |  **SEF\_FOLDER** и **SEF\_URL\_TEMPLATES**.  Если режим ЧПУ **выключен**, то необходимо настроить параметр VARIABLE\_ALIASES     |  |  |  | | --- | --- | --- | | Имена переменных | **VARIABLE\_ALIASES** | Имена переменных для управления страницами:  * **site\_show** - переменная ID сайта (просмотр); * **site\_edit** - переменная ID сайта (редактирование); * **landing\_edit** - переменная ID лендинга (редактирование); * **landing\_view** - переменная ID лендинга (просмотр/наполнение); * **domain\_edit** - переменная ID домена (редактирование); * **domains** - идентификатор страницы доменов; * **sites** - идентификатор страницы сайтов. | |  |
| **Дополнительные настройки** | | | |
| Тип сайтов | **TYPE** | Выбирается тип сайта из списка:    * **Лендинг** * **Магазин** * **Проект** * **База знаний** * **Группы** |  |

### Пример вызова

```
  
$APPLICATION-IncludeComponent(
	"bitrix:landing.start",
	"",
	Array(
		"SEF_MODE" => "N",
		"TYPE" => "PAGE",
		"VARIABLE_ALIASES" => Array("domain_edit"=>"domain_edit","domains"=>"domains","landing_edit"=>"landing_edit","landing_view"=>"landing_view","site_edit"=>"site_edit","site_show"=>"site_show","sites"=>"sites")
	)
);?>
  
```

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх