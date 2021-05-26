import behave
from selenium import webdriver
from tests.acceptance.page_model.home_page import HomePage
from tests.acceptance.page_model.blog_page import BlogPage
from tests.acceptance.page_model.new_post_page import NewPostPage

behave.use_step_matcher('re')

@behave.given('I am on the homepage')
def given_step_impl(context):
    context.driver = webdriver.Chrome()
    page = HomePage(context.driver)
    # browser = webdriver.Firefox()
    context.driver.get(page.url)
    
@behave.given('I am on the blog page')
def given_step_impl_2(context):
    context.driver = webdriver.Chrome()
    page = BlogPage(context.driver)
    # browser = webdriver.Firefox()
    context.driver.get(page.url)
    
@behave.given('I am on the new post page')
def given_step_impl_3(context):
    context.driver = webdriver.Chrome()
    page = NewPostPage(context.driver)
    context.driver.get(page.url)

@behave.then('I am on the blog page')
def then_step_impl(context):
    expected_url = BlogPage(context.driver).url
    assert context.driver.current_url == expected_url

@behave.then('I am on the homepage')
def then_step_impl_2(context):
    expected_url = HomePage(context.driver).url
    assert context.driver.current_url == expected_url