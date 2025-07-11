|  |  |  |
| --- |

| --- |
| **Поле** |

| **Описание** |
| **Основные параметры** |

| |
| Формат RSS |

| Указываются форматы экспорта данных форума, которые необходимо отобразить:  * **RSS 0.92** (**RSS1**) * **RSS 2.0** (**RSS2**) * **Atom 0.3** (**ATOM**) |
| Разрешить RSS на форумах |

| Указываются форумы, для которых будет разрешен экспорт RSS в указанном формате. |
| ID |

| Задается код, в котором передается идентификатор форума. Значение по умолчанию: **$\_REQUEST["IID"]**. |
| Вид компонента |

| В публичной части компонент будет представлен в виде RSS-ленты в указанном формате (**rss**). |
| Тип RSS |

| Указывается диапазон поддерживаемых форматов RSS. |
| **Шаблоны ссылок** |

| |
| Страница RSS |

| Указывается адрес страницы RSS форума. |
| Страница списка тем |

| Указывается адрес страницы со списком тем форума. По умолчанию поле содержит **list.php?FID=#FID#**. Такая страница может быть создана с помощью компонента [Темы (список)](/user_help/components/obschenie/forum/forum_topic_list.php). |
| Страница чтения темы |

| Указывается адрес страницы чтения темы форума. По умолчанию поле содержит **read.php?FID=#FID#&TID=#TID#&MID=#MID#**. Такая страница может быть создана с помощью компонента [Тема (чтение)](/user_help/components/obschenie/forum/forum_topic_read.php). |
| Страница профиля |

| Указывается адрес страницы просмотра профиля пользователя. По умолчанию поле содержит **profile\_view.php?UID=#UID#**. Такая страница может быть создана с помощью компонента [Пользователь (профиль)](/user_help/components/obschenie/forum/forum_user_profile_view.php). |
| **Настройки кеширования** |

| |
| Тип кеширования |

| Тип кеширования:  * **A** - Авто + Управляемое: автоматически обновляет кеш компонентов в течение заданного времени или при изменении данных; * **Y** - Кешировать: для кеширования необходимо определить время кеширования; * **N** - Не кешировать: кеширования нет в любом случае. |
| Время кеширования (сек.) |

| Время кеширования, указанное в секундах. |
| **Дополнительные настройки** |

| |
| Количество элементов для экспорта |

| Указывается количество элементов для экспорта. |
| Размер рисунка для отображения на странице |

| Указывается размер рисунка для отображения на странице в Мб. |
| Шаблон подписи для ленты RSS, если не задан ни один форум |

| Подпись, которая будет выводиться, если не задан форум. При пустом поле ввода: **#SITE\_NAME# [форум]** Вы можете использовать след. переменные: **#FORUM\_TITLE#**, **#FORUM\_DESCRIPTION#**, **#TOPIC\_TITLE#**, **#TOPIC\_DESCRIPTION#**, **#SITE\_NAME#**, **#SERVER\_NAME#**. |
| Шаблон подписи для ленты RSS, если задан форум |

| Подпись, которая будет выводиться, если задан форум. При пустом поле ввода: **#SITE\_NAME# [форум: #FORUM\_TITLE#]** Вы можете использовать след. переменные: **#FORUM\_TITLE#**, **#FORUM\_DESCRIPTION#**, **#TOPIC\_TITLE#**, **#TOPIC\_DESCRIPTION#**, **#SITE\_NAME#**, **#SERVER\_NAME#**. |
| Шаблон подписи для ленты RSS, если задана тема |

| Подпись, которая будет выводиться, если задана тема форума для RSS. При пустом поле ввода: **#SITE\_NAME# [тема: #TOPIC\_TITLE#]** Вы можете использовать след. переменные: **#FORUM\_TITLE#**, **#FORUM\_DESCRIPTION#**, **#TOPIC\_TITLE#**, **#TOPIC\_DESCRIPTION#**, **#SITE\_NAME#**, **#SERVER\_NAME#**. |
| Формат показа даты и времени |

```
<?$APPLICATION->IncludeComponent(  
	"bitrix:forum.rss",  
	"",  
	Array(  
		"TYPE_RANGE" => Array("RSS1", "RSS2", "ATOM"),  
		"FID_RANGE" => Array("8"),  

```