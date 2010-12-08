<?php
//$cur_date = date('Y-m-d');
for($i=0; $i<7; $i++) {
    $json_dates[$i] = date('Y-m-d', strtotime('now - ' . $i . 'days')); 
}
echo json_encode($json_dates);
?>
