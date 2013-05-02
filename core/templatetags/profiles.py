from django import template

@register.assignment_tag
def get_all_users():
	return User.objects.all()