|  |  |  |
| --- |

| --- |
| **Поле** |

| **Описание** |
| **Основные параметры** |

| |
| Название веб-сервиса |

| Задаются имя используемого веб-сервиса. |
| Модуль веб-сервис |

| Указывается модуль, который будет подключен при вызове сервиса. |
| Конфигурирующий класс |

```
<?$APPLICATION->IncludeComponent("bitrix:webservice.server","",Array(

		"WEBSERVICE_NAME" => "WebService EndPoint: Bitrix",

		"WEBSERVICE_MODULE" => "",

		"WEBSERVICE_CLASS" => "CGenericWSStub"

	),

);?>


```