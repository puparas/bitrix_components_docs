|  |  |  |
| --- |

| --- |
| **Поле** |

| **Описание** |
| **Шаблоны ссылок** |

| |
| URL, ведущий на страницу с детальным просмотром курса |

| Указывается путь к странице с детальным просмотром курса. |
| URL, ведущий на страницу со списком тестов |

| Указывается путь к странице со списком тестов. |
| **Дополнительные настройки** |

| |
| Устанавливать заголовок страницы |

```
<$APPLICATION->IncludeComponent("bitrix:learning.student.certificates","",Array(

		"COURSE_DETAIL_TEMPLATE" => "course/index.php?COURSE_ID=#COURSE_ID#&INDEX=Y", 

		"TESTS_LIST_TEMPLATE" => "course/index.php?COURSE_ID=#COURSE_ID#&TEST_LIST=Y", 

		"SET_TITLE" => "Y" 

	),

);?>


```