|  |  |  |
| --- |

| --- |
| **Поле** |

| **Описание** |
| **Шаблоны ссылок** |

| |
| URL, ведущий на страницу прохождения теста |

| Указывается путь к странице прохождения теста. |
| URL, ведущий на страницу с детальным просмотром курса |

| Указывается путь к странице с детальным просмотром курса. |
| **Дополнительные настройки** |

| |
| Идентификатор теста |

| Указывается имя переменной, которой передается идентификатор теста. |
| Устанавливать заголовок страницы |

```
<?$APPLICATION->IncludeComponent("bitrix:learning.student.gradebook","",Array(

		"TEST_DETAIL_TEMPLATE" => "course/index.php?COURSE_ID=#COURSE_ID#&TEST_ID=#TEST_ID#", 

		"COURSE_DETAIL_TEMPLATE" => "course/index.php?COURSE_ID=#COURSE_ID#&INDEX=Y", 

		"TEST_ID_VARIABLE" => "TEST_ID", 

		"SET_TITLE" => "Y" 

	),

);?>


```