import behave
from selenium import webdriver
from tests.acceptance.page_model.base_page import BasePage
from tests.acceptance.page_model.new_post_page import NewPostPage

behave.use_step_matcher('re')

@behave.when('I click on the "(.*)" link')
def when_step_impl(context, link_text):
    # context.browser = webdriver.Chrome()
    # link = context.driver.find_element_by_id(link_id
    
    page = BasePage(context.driver)
    links = page.navigation
    matching_links = [l for l in links if l.text == link_text]
    
    if len(matching_links) > 0:
        matching_links[0].click()
    else:
        raise RuntimeError()
    
@behave.when('I enter "(.*)" in the "(.*)" field')
def step_impl(context, content, field_name):
    page = NewPostPage(context.driver)
    page.form_field(field_name).send_keys(content)
 
@behave.when('I press the submit button')
def step_impl(context):
    page = NewPostPage(context.driver)
    page.submit_button.click()