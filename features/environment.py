from helper.helper_base import HelperFunc


def before_all(context):
    context.helper = HelperFunc()


def after_all(context):
    HelperFunc().close()
