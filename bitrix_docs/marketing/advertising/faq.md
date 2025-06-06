# Частые вопросы

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

[Email-маркетинг](/user_help/marketing/sender/index.php)

[Триггерные рассылки](/user_help/marketing/triggered_emails/index.php)

[Поисковая оптимизация](/user_help/marketing/seo/index.php)

[Баннерная реклама](/user_help/marketing/advertising/index.php)

[Контракты](/user_help/marketing/advertising/adv_contract_list.php)
[Создание и редактирование рекламного контракта](/user_help/marketing/advertising/adv_contract_edit.php)
[Типы баннеров](/user_help/marketing/advertising/adv_type_list.php)
[Создание и редактирование типа баннеров](/user_help/marketing/advertising/adv_type_edit.php)
[Баннеры](/user_help/marketing/advertising/adv_banner_list.php)
[Создание и редактирование баннера](/user_help/marketing/advertising/adv_banner_edit.php)
[Баннерная реклама. Настройки модуля](/user_help/marketing/advertising/settings.php)
[Графики](/user_help/marketing/advertising/adv_graph_list.php)
[Диаграммы](/user_help/marketing/advertising/adv_diagram_list.php)
[Частые вопросы](/user_help/marketing/advertising/faq.php)

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

[Баннерная реклама](/user_help/marketing/advertising/index.php)

Частые вопросы

**Недоступно в редакциях:**Малый бизнес, Стандарт, Старт

# Частые вопросы

### Почему у меня не считается количество посетителей, просматривающих баннеры?

Суть проблемы состоит в том, что модуль **Реклама, баннеры** не может уcтановить **cookie** для посетителя просмотревшего тот или иной баннер. Данный **cookie** устанавливается в функции **CAdvBanner::Show**, но так как в большинстве случаев, данная функция вызывается уже после того как HTML-контент страницы начинает отсылаться браузеру клиента, то в соответствии с ограничениями протокола HTTP, **cookie** не может быть установлен.

Проблему можно решить следующими путями:

* Установите модуль **Компрессия** (если он не установлен). Данный модуль буферизирует результат парсинга, прежде чем сжать его и передать браузеру клиента. Буферизация позволит корректно учитывать посетителей просматривающих баннеры.
* Для всех редакции, в которых есть модуль **Веб-аналитика** в файле **/bitrix/php\_interface/dbconn.php** добавьте следующий PHP код:
    
    

  ```
  ob_start();
  ```

  Данная функция включает буферизацию парсинга PHP страниц, что позволит корректно учитывать посетителей.
* Если на вашем сайте нет возможности использовать буферизацию, то учет посетителей будет работать, если в дизайне сайта (**prolog\_main.php**, **epilog\_main.php**) использовать следующую схему:
    
    

  ```
  <?  
  // прежде чем начинается вывод страницы, необходимо получить HTML баннеров  
  if (CModule::IncludeModule("advertising")):  
  	$strBanner_top	= CAdvBanner::Show("TOP");   
  	$strBanner_bottom = CAdvBanner::Show("BOTTOM");   
  	$strBanner_left   = CAdvBanner::Show("LEFT");   
  endif;  
  ?>  
  <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">  
  <html>  
  <head></head>  
  <body>  
  	<?  
  	// выводим HTML баннеров в заранее отведенных рекламных областях  
  	echo $strBanner_top;  
  	echo $strBanner_bottom;  
  	echo $strBanner_left;  
  	?>  
  </body>  
  </html>  

  ```

  Т.е. перед тем как начинается вывод HTML-контента, вы предварительно запоминаете HTML всех баннеров в PHP переменных, а уже затем используете их вывод в том месте дизайна, где вам необходимо.

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх