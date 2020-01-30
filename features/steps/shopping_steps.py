from behave import given, when, then

from app.app import App


@given(u'a customer navigates to the homepage')
def navigate_to_homepage(context):
    context.app = App()
    context.app.homepage().check_cart_items()


@when(u'they check their shopping cart')
def check_shopping_cart(context):
    context.cart_text = context.app.cart().cart_items_text()


@then(u'the shopping cart is empty')
def shopping_cart_status(context):
    assert context.cart_text == 'Your shopping cart is empty.'
