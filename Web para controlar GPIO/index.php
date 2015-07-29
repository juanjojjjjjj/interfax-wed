<!DOCTYPE html>
<HTML lang="es">
	<HEAD>
		<TITLE>Raspberry PI WEB controlador GPIO</TITLE>
		<META CHARSET="utf-8"/>
<?php

// Funciones PHP del pin GPIO 4
	if ($_POST[Activar4]) { 
		$a=exec("sudo python /var/www/Web\ para\ controlar\ GPIO/GPIO/4/activar.py");
		echo $a;
	}

	if ($_POST[Desacticar4]) { 
		$a=exec("sudo python /var/www/Web\ para\ controlar\ GPIO/GPIO/4/apagar.py");
		echo $a;
	}

	if ($_POST[UNparpadeo4]) { 
		$a=exec("sudo python /var/www/Web\ para\ controlar\ GPIO/GPIO/4/1parpadeo.py");
		echo $a;
	}

	if ($_POST[Parpadear4]) { 
		$a=exec("sudo python /var/www/Web\ para\ controlar\ GPIO/GPIO/4/parpadear.py");
		echo $a;
	}
// Fin de las funciónes del pin GPIO 4
?>
	</HEAD>
	
	<BODY>
<!--ACCIONES PARA GPIO4-->
		<FORM action="" method="post">
			GPIO 4 <INPUT type="submit" name="Activar4" value="Activar"/>
			<INPUT type="submit" name="Desactivar4" value="Desactivar"/>
			<INPUT type="submit" name="UNparpadeo4" value="1Parpadeo"/>
			<INPUT type="submit" name="Parpadear4" value="Parpadear"/>
		</FORM>
	</BODY>
</HTML>
			

