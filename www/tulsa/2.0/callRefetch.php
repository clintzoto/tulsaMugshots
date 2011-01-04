<?php
$person_id = $_REQUEST['person_id'];
exec(`python ../../../utils/refetch.py $person_id`);
?>
