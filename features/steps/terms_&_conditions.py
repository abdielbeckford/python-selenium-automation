from behave import given, when, then


@given('Open sign in page')
def open_sign_in_page(context):
    context.app.sign_in_page.open_sign_in_page()


@when('Store original window')
def store_original_window(context):
    context.original_window = context.app.sign_in_page.get_current_window()


@when('Click on Target terms and conditions link')
def terms_and_conditions(context):
    context.app.sign_in_page.click_terms_and_conditions_link()


@when('Switch to the newly opened window')
def switch_to_new_window(context):
    context.app.sign_in_page.switch_to_new_window()


@then('Verify Terms and Conditions page is opened')
def verify_terms_and_conditions(context):
    context.app.sign_in_page.verify_TC_opened()


@then('User can close new window and switch back to original')
def switch_to_original_window(context):
    context.app.sign_in_page.switch_window_by_id(context.original_window)
