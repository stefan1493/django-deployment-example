from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value, arg):
    """This cuts out all values of "arg" from the string! """

    return value.replace(arg,"")

# one way to register the filter
# register.filter('cut', cut)

#another way is using decoratos
