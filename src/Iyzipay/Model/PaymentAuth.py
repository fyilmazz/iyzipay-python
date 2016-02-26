from src.Iyzipay.HttpClient import HttpClient
from src.Iyzipay.IyzipayResource import IyzipayResource
from src.Iyzipay.JsonBuilder import JsonBuilder
from src.Iyzipay.RequestStringBuilder import RequestStringBuilder


class PaymentAuth(IyzipayResource):
    @classmethod
    def retrieve(cls, request, options):
        json_encoded_request = cls.retrieve_get_json_object(request)
        pki_string_request = cls.retrieve_to_pki_request_string(request)
        raw_result = HttpClient.create().post(options['base_url'] + "/payment/detail",
                                              IyzipayResource.get_http_header(pki_string_request, options),
                                              json_encoded_request)
        json_result = raw_result.json()
        return json_result

    @classmethod
    def create(cls, request, options):
        json_encoded_request = cls.get_json_object(request)
        pki_string_request = cls.to_pki_request_string(request)
        raw_result = HttpClient.create().post(options['base_url'] + "/payment/iyzipos/auth/ecom",
                                              IyzipayResource.get_http_header(pki_string_request, options),
                                              json_encoded_request)
        json_result = raw_result.json()
        return json_result

    @classmethod
    def retrieve_get_json_object(cls, request):
        json_object = JsonBuilder.from_json_object(super(PaymentAuth, cls).get_json_object(request)) \
            .add("paymentId", request.get('payment_id', None)) \
            .add("paymentConversationId", request.get('payment_conversation_id', None)) \
            .get_object()
        return JsonBuilder.json_encode(json_object)

    @classmethod
    def retrieve_to_pki_request_string(cls, request):
        return RequestStringBuilder.create().append_super(
            super(PaymentAuth, cls).to_pki_request_string(request)) \
            .append('paymentId', request.get('payment_id', None)) \
            .append('paymentConversationId', request.get('payment_conversation_id', None))\
            .get_request_string()

    @classmethod
    def get_json_object(cls, request):
        json_object = JsonBuilder.from_json_object(super(PaymentAuth, cls).get_json_object(request)) \
            .add_price("price", request.get('price', None)) \
            .add_price("paidPrice", request.get('paid_price', None)) \
            .add("installment", request.get('installment', None)) \
            .add("paymentChannel", request.get('payment_channel', None)) \
            .add("basketId", request.get('basket_id', None)) \
            .add("paymentGroup", request.get('payment_group', None)) \
            .add("paymentCard", cls.payment_card_get_json_object(request.get('payment_card', None))) \
            .add("buyer", cls.buyer_get_json_object(request.get('buyer', None))) \
            .add("shippingAddress", cls.address_get_json_object(request.get('shipping_address', None))) \
            .add("billingAddress", cls.address_get_json_object(request.get('billing_address', None))) \
            .add("basketItems", cls.basket_items_get_json_object(request.get('basket_items', None))) \
            .get_object()
        return JsonBuilder.json_encode(json_object)

    @classmethod
    def to_pki_request_string(cls, request):
        return RequestStringBuilder.create().append_super(
            super(PaymentAuth, cls).to_pki_request_string(request)) \
            .append_price("price", request.get('price', None)) \
            .append_price("paidPrice", request.get('paid_price', None)) \
            .append("installment", request.get('installment', None)) \
            .append("paymentChannel", request.get('payment_channel', None)) \
            .append("basketId", request.get('basket_id', None)) \
            .append("paymentGroup", request.get('payment_group', None)) \
            .append("paymentCard", cls.payment_card_to_pki_request_string(request.get('payment_card', None))) \
            .append("buyer", cls.buyer_to_pki_request_string(request.get('buyer', None))) \
            .append("shippingAddress", cls.address_to_pki_request_string(request.get('shipping_address', None))) \
            .append("billingAddress", cls.address_to_pki_request_string(request.get('billing_address', None))) \
            .append("basketItems", cls.basket_items_to_pki_request_string(request.get('basket_items', None))) \
            .get_request_string()

    @classmethod
    def payment_card_get_json_object(cls, request):
        return JsonBuilder.create() \
            .add('cardHolderName', request.get('card_holder_name', None)) \
            .add('cardNumber', request.get('card_number', None)) \
            .add('expireYear', request.get('expire_year', None)) \
            .add('expireMonth', request.get('expire_month', None)) \
            .add('cvc', request.get('cvc', None)) \
            .add('registerCard', request.get('register_card', None)) \
            .add('cardAlias', request.get('card_alias', None)) \
            .add('cardToken', request.get('card_token', None)) \
            .add('cardUserKey', request.get('card_user_key', None)) \
            .get_object()

    @classmethod
    def payment_card_to_pki_request_string(cls, request):
        return RequestStringBuilder.create() \
            .append('cardHolderName', request.get('card_holder_name', None)) \
            .append('cardNumber', request.get('card_number', None)) \
            .append('expireYear', request.get('expire_year', None)) \
            .append('expireMonth', request.get('expire_month', None)) \
            .append('cvc', request.get('cvc', None)) \
            .append('registerCard', request.get('register_card', None)) \
            .append('cardAlias', request.get('card_alias', None)) \
            .append('cardToken', request.get('card_token', None)) \
            .append('cardUserKey', request.get('card_user_key', None)) \
            .get_request_string()

    @classmethod
    def buyer_get_json_object(cls, buyer_request):
        if buyer_request:
            return JsonBuilder.create() \
                .add("id", buyer_request.get('id', None)) \
                .add("name", buyer_request.get('name', None)) \
                .add("surname", buyer_request.get('surname', None)) \
                .add("identityNumber", buyer_request.get('identity_number', None)) \
                .add("email", buyer_request.get('email', None)) \
                .add("gsmNumber", buyer_request.get('gsm_number', None)) \
                .add("registrationDate", buyer_request.get('registration_date', None)) \
                .add("lastLoginDate", buyer_request.get('last_login_date', None)) \
                .add("registrationAddress", buyer_request.get('registration_address', None)) \
                .add("city", buyer_request.get('city', None)) \
                .add("country", buyer_request.get('country', None)) \
                .add("zipCode", buyer_request.get('zip_code', None)) \
                .add("ip", buyer_request.get('ip', None)) \
                .get_object()

    @classmethod
    def buyer_to_pki_request_string(cls, buyer_request):
        if buyer_request:
            return RequestStringBuilder.create() \
                .append("id", buyer_request.get('id', None)) \
                .append("name", buyer_request.get('name', None)) \
                .append("surname", buyer_request.get('surname', None)) \
                .append("identityNumber", buyer_request.get('identity_number', None)) \
                .append("email", buyer_request.get('email', None)) \
                .append("gsmNumber", buyer_request.get('gsm_number', None)) \
                .append("registrationDate", buyer_request.get('registration_date', None)) \
                .append("lastLoginDate", buyer_request.get('last_login_date', None)) \
                .append("registrationAddress", buyer_request.get('registration_address', None)) \
                .append("city", buyer_request.get('city', None)) \
                .append("country", buyer_request.get('country', None)) \
                .append("zipCode", buyer_request.get('zip_code', None)) \
                .append("ip", buyer_request.get('ip', None)) \
                .get_request_string()

    @classmethod
    def address_to_pki_request_string(cls, address_request):
        if address_request:
            return RequestStringBuilder.create() \
                .append("address", address_request.get('address', None)) \
                .append("zipCode", address_request.get('zip_code', None)) \
                .append("contactName", address_request.get('contact_name', None)) \
                .append("city", address_request.get('city', None)) \
                .append("country", address_request.get('country', None)) \
                .get_request_string()

    @classmethod
    def address_get_json_object(cls, address_request):
        if address_request:
            return JsonBuilder.create() \
                .add("address", address_request.get('address', None)) \
                .add("zipCode", address_request.get('zip_code', None)) \
                .add("contactName", address_request.get('contact_name', None)) \
                .add("city", address_request.get('city', None)) \
                .add("country", address_request.get('country', None)) \
                .get_object()

    @classmethod
    def basket_items_to_pki_request_string(cls, basket_items):
        if basket_items:
            basket = []
            for basket_item in basket_items:
                basket.append(RequestStringBuilder.create() \
                              .append('id', basket_item.get('id', None)) \
                              .append('price', basket_item.get('price', None)) \
                              .append('name', basket_item.get('name', None)) \
                              .append('category1', basket_item.get('category1', None)) \
                              .append('category2', basket_item.get('category2', None)) \
                              .append('itemType', basket_item.get('item_type', None)) \
                              .append('subMerchantKey', basket_item.get('sub_merchant_key', None)) \
                              .append('subMerchantPrice', basket_item.get('sub_merchant_price', None)) \
                              .get_request_string())
            return '[' + ", ".join(basket) + ']'

    @classmethod
    def basket_items_get_json_object(cls, basket_items):
        if basket_items:
            basket = []
            for basket_item in basket_items:
                basket.append(JsonBuilder.create() \
                              .add('id', basket_item.get('id', None)) \
                              .add('price', basket_item.get('price', None)) \
                              .add('name', basket_item.get('name', None)) \
                              .add('category1', basket_item.get('category1', None)) \
                              .add('category2', basket_item.get('category2', None)) \
                              .add('itemType', basket_item.get('item_type', None)) \
                              .add('subMerchantKey', basket_item.get('sub_merchant_key', None)) \
                              .add('subMerchantPrice', basket_item.get('sub_merchant_price', None)) \
                              .get_object())
            return basket

