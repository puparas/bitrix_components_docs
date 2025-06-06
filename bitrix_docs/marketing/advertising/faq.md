```
  ob_start();
  ```

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