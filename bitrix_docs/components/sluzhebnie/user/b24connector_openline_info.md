|  |  |  |
| --- |

| --- |
| Поле |

| Описание |
| **Управление адресами страниц** |

| |
| Дополнительные данные |

| Любой текст, добавленный в это поле, транслируется в ОЛ. |
| Добавлять метку при отправке сообщения для Google Analytics |

```
<?$APPLICATION->IncludeComponent("bitrix:b24connector.openline.info","", Array(

		"COMPOSITE_FRAME_MODE" => "A",

		"COMPOSITE_FRAME_TYPE" => "AUTO",

		"DATA" => "",

		"GA_MARK" => ""

	)

);?>
```