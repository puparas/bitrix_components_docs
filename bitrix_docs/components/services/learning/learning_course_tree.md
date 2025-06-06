|  |  |  |
| --- |

| --- |
| **Поле** |

| **Описание** |
| **Основные параметры** |

| |
| Идентификатор курса |

| Указывается идентификатор курса. |
| **Шаблоны ссылок** |

| |
| URL, ведущий на страницу с детальным просмотром курса |

| Указывается путь к странице с детальным просмотром курса. |
| URL, ведущий на страницу с главой |

| Указывается путь к странице с главой курса. |
| URL, ведущий на страницу с уроком |

| Указывается путь к странице с уроком курса. |
| URL, ведущий на страницу с самотестированием |

| Указывается путь к странице с тестом для самопроверки. |
| URL, ведущий на страницу со списком тестов |

| Указывается путь к странице со списком тестов. |
| URL, ведущий на страницу прохождения теста |

| Указывается путь к странице с прохождением теста. |
| **Дополнительные настройки** |

| |
| Проверять право доступа |

| [Y|N] При отмеченной опции будет проверяться право на доступ к курсу. |
| Устанавливать заголовок страницы |

```
<$APPLICATION->IncludeComponent("bitrix:learning.course.tree",".default",Array(

		"COURSE_ID" => $_REQUEST["COURSE_ID"], 

		"COURSE_DETAIL_TEMPLATE" => "course/index.php?COURSE_ID=#COURSE_ID#", 

		"CHAPTER_DETAIL_TEMPLATE" => "chapter.php?CHAPTER_ID=#CHAPTER_ID#", 

		"LESSON_DETAIL_TEMPLATE" => "lesson.php?LESSON_ID=#LESSON_ID#", 

		"SELF_TEST_TEMPLATE" => "self.php?LESSON_ID=#LESSON_ID#", 

		"TESTS_LIST_TEMPLATE" => "course/test_list.php?COURSE_ID=#COURSE_ID#", 

		"TEST_DETAIL_TEMPLATE" => "course/test.php?COURSE_ID=#COURSE_ID#&TEST_ID=#TEST_ID", 

		"CHECK_PERMISSIONS" => "Y", 

		"SET_TITLE" => "Y" 

	),

);?>


```