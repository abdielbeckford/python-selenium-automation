from behave import given, when, then


@given('Open Help page for returns')
def open_help_page(context):
    context.app.help_page.open_help_returns()


@when('Select Help topic {option}')
def select_topic(context, option):
    context.app.help_page.select_topic(option)


# @then('Verify Current promotions page opened')
# def verify_promotions_opened(context):
#     context.app.help_page.verify_promotions_header()


@then('Verify help {header} page opened')
def verify_help_page_header(context, header):
    context.app.help_page.verify_returns_header(header)
