stateDiagram-v2
    [*] --> Initiated
    Initiated --> Processing : SubmitPayment
    Processing --> Successful : PaymentValid
    Processing --> Failed : PaymentInvalid
    Failed --> Retried : RetryPayment
    Retried --> Processing : SubmitPayment
    Successful --> [*]
