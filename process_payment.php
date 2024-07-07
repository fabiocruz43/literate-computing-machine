<?php
require 'vendor/autoload.php'; // Certifique-se de que o autoload do Composer está configurado corretamente

use MercadoPago\SDK;
use MercadoPago\Payment;
use MercadoPago\Payer;

SDK::setAccessToken('YOUR_ACCESS_TOKEN');

$payload = json_decode(file_get_contents('php://input'), true);

$payment = new Payment();
$payment->transaction_amount = (float)$payload['transaction_amount'];
$payment->token = $payload['token'];
$payment->description = $payload['description'];
$payment->installments = (int)$payload['installments'];
$payment->payment_method_id = $payload['payment_method_id'];
$payment->issuer_id = (int)$payload['issuer_id'];

$payer = new Payer();
$payer->email = $payload['payer']['email'];
$payer->identification = array(
    "type" => $payload['payer']['identification']['type'],
    "number" => $payload['payer']['identification']['number']
);
$payment->payer = $payer;

$payment->save();

$response = array(
    "status" => $payment->status,
    "status_detail" => $payment->status_detail,
    "id" => $payment->id,
    "date_approved" => $payment->date_approved,
    "payer" => $payment->payer,
    "payment_method_id" => $payment->payment_method_id,
    "payment_type_id" => $payment->payment_type_id,
    "refunds" => $payment->refunds
);

echo json_encode($response);
?>
