|  |  |  |
| --- |

| --- |
| **Поле** |

| **Описание** |
| **Основные параметры** |

| |
| Идентификатор курса |

| Указывается идентификатор курса. |
| Идентификатор урока |

| Указывается идентификатор урока. |
| **Шаблоны ссылок** |

| |
| URL, ведущий на страницу с самотестированием |

| Указывается путь к странице с тестом для самопроверки. |
| URL, ведущий на страницу с профилем пользователя |

| Указывается путь к странице профиля пользователя. |
| **Настройки кеширования** |

| |
| Тип кеширования |

| Тип кеширования:  * **A** - Авто + Управляемое: автоматически обновляет кеш компонентов в течение заданного времени или при изменении данных; * **Y** - Кешировать: для кеширования необходимо определить время кеширования; * **N** - Не кешировать: кеширования нет в любом случае. |
| Время кеширования (сек.) |

| Время кеширования, указанное в секундах. |
| **Дополнительные настройки** |

| |
| Проверять право доступа |

| [Y|N] При отмеченной опции будет проверяться право на доступ к уроку. |
| Устанавливать заголовок страницы |

```
<?$APPLICATION->IncludeComponent("bitrix:learning.lesson.detail","",Array(

		"COURSE_ID" => $_REQUEST["COURSE_ID"], 

		"LESSON_ID" => $_REQUEST["LESSON_ID"], 

		"SELF_TEST_TEMPLATE" => "self.php?COURSE_ID=#COURSE_ID#&LESSON_ID=#LESSON_ID#", 

		"PATH_TO_USER_PROFILE" => "", 

		"CHECK_PERMISSIONS" => "Y", 

		"SET_TITLE" => "Y", 

		"CACHE_TYPE" => "A", 

		"CACHE_TIME" => "3600" 

	),

);?>


```