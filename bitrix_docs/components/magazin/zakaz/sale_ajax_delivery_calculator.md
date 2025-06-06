```
...

<?$APPLICATION->IncludeComponent('bitrix:sale.ajax.delivery.calculator', '', array(

	"NO_AJAX" => $arParams["SHOW_AJAX_DELIVERY_LINK"] == 'S' ? 'Y' : 'N',

	"ORDER_WEIGHT" => $arResult["ORDER_WEIGHT"],

	"ORDER_PRICE" => $arResult["ORDER_PRICE"],

	"LOCATION_TO" => $arResult["DELIVERY_LOCATION"],

	"CURRENCY" => $arResult["BASE_LANG_CURRENCY"],

	"DELIVERY_ID" => 21    //21 - идентификатор службы доставки. Если служба доставки с профилями, то идентификатор конкретного профиля.

	));

?>

...


```