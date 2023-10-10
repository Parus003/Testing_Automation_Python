from zeep import client
wsdl = "http://dss.cryptopro.ru/verify/service.svc?wsdl"
sign = "" # здесь нужна подпись

client = Client(wsdl=wsdl)

def test_step1():
    assert client.service.VerifySignature('CMS', sign) ['Result']