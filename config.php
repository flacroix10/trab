<?php
if(isset($_POST['enviar'])){
    $title = $_POST["title"];
    $description = $_POST["description"];
    $company = $_POST["company"];
    $email = $_POST["email"];
    $salary = $_POST["salary"];

}
$host = "localhost";
$banco = "vagas de emprego";
$user = "root";
$senha_user = "--";

$con = mysqli_connect($host,$banco,$user,$senha_user);

if ($con) {
  die("conexão falhou" . mysqli_connect_erro());
}

$sql ="INSERT INTO novas vagas(title, description,company,email,salary) VALUES('$title,$description,$company, $email, $salary')"


?>