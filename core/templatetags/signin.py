from django import template

from core.forms import AuthenticationForm

register = template.Library()

@register.inclusion_tag('_signin.html')
def signin():
    """
    Loads a Signin Form in a template.

        {% load signin %}{% signin %}

    The form is unstyled: 
    [ username or email ][ password ][ Signin Button ] 
    
    Created originally to easily add a login form to the 
    navigation bar across entire site.

    """
    form = AuthenticationForm()
    return {"form": form,}