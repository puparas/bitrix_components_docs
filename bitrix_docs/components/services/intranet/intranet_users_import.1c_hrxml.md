|  |  |  |
| --- |

| --- |
| **Поле** |

| **Описание** |
| **Основные параметры** |

| |
| Тип инфоблока |

| Указывается тип инфоблока, в который будут импортироваться данные оргструктуры. |
| Инфоблок подразделений |

| Указывается инфоблок подразделений. |
| Инфоблок графика отсутствий |

| Указывается инфоблок графика отсутствий. |
| Инфоблок кадровых перестановок |

| Указывается инфоблок кадровых перестановок. |
| Сайт для привязки пользователей |

| Указывается идентификатор сайта, к которому будет привязка пользователей. |
| Группы, пользователям которых разрешена загрузка |

| Указываются группы пользователей, которым разрешен импорт оргструктуры. |
| E-mail по умолчанию |

| Указывается e-mail, на который по умолчанию будут направляться информационные сообщения. Например, сообщения об успешном импорте, ошибках и т.д. |
| Формировать уникальный e-mail |

| [Y|N] При отмеченной опции будет формироваться уникальный e-mail |
| Шаблон автоматического формирования логина |

| Указывается шаблон автоматического формирования логина пользователей. |
| Обновляемые свойства |

| Указываются свойства, которые будут обновляться при импорте оргструктуры. |
| **Уведомление пользователей** |

| |
| E-mail-уведомление новым пользователям |

| Выбор действия отсылки e-mail-уведомлений новым пользователям:  * **N** - не отсылать; * **E** - только если указан e-mail; * **Y** - всем. |
| Отсылать уведомления сразу |

| [Y|N] При отмеченной опции e-mail-уведомлений новым пользователям будут отправлять сразу при импорте данных. |
| **LDAP** |

| |
| XML-идентификатор свойства "Учетная запись AD" |

| Указывается XML-идентификатор свойства "Учетная запись AD". |
| Сервер LDAP |

```


<?$APPLICATION->IncludeComponent("bitrix:intranet.users.import.1c.hrxml","",

	Array(

		"IBLOCK_TYPE" => "structure",

		"DEPARTMENTS_IBLOCK_ID" => "5",

		"ABSENCE_IBLOCK_ID" => "3",

		"STATE_HISTORY_IBLOCK_ID" => "6",

		"SITE_ID" => "s1",

		"GROUP_PERMISSIONS" => array("1"),

		"FILE_SIZE_LIMIT" => "204800",

		"USE_ZIP" => "Y",

		"DEFAULT_EMAIL" => "admin@myexample.com",

		"UNIQUE_EMAIL" => "Y",		

		"LOGIN_TEMPLATE" => "user_#",

		"EMAIL_NOTIFY" => "E",

		"EMAIL_NOTIFY_IMMEDIATELY" => "Y",

		"UPDATE_PROPERTIES" => array("NAME", "SECOND_NAME", "LAST_NAME", "PERSONAL_PROFESSION", "PERSONAL_WWW", "PERSONAL_BIRTHDAY", "PERSONAL_ICQ", "PERSONAL_GENDER", "PERSONAL_PHOTO", "PERSONAL_PHONE", "PERSONAL_FAX", "PERSONAL_MOBILE", "PERSONAL_PAGER", "PERSONAL_STREET", "PERSONAL_CITY", "PERSONAL_STATE", "PERSONAL_ZIP", "PERSONAL_COUNTRY", "WORK_POSITION", "WORK_PHONE", "UF_DEPARTMENT", "UF_PHONE_INNER", "UF_INN", "UF_DISTRICT", "UF_SKYPE", "UF_TWITTER", "UF_LINKEDIN", "UF_XING", "UF_WEB_SITES", "UF_SKILLS", "UF_INTERESTS", "UF_BXDAVEX_CALSYNC", "UF_PUBLIC", "UF_WORK_BINDING", "UF_TIMEMAN", "UF_TM_MAX_START", "UF_TM_MIN_FINISH", "UF_TM_MIN_DURATION", "UF_TM_REPORT_REQ", "UF_TM_REPORT_TPL", "UF_TM_FREE", "UF_TM_TIME", "UF_TM_DAY", "UF_TM_REPORT_DATE", "UF_REPORT_PERIOD", "UF_DELAY_TIME", "UF_LAST_REPORT_DATE", "UF_SETTING_DATE", "UF_TM_ALLOWED_DELTA"),

		"LDAP_ID_PROPERTY_XML_ID" => ""

	),

false

);?>


```