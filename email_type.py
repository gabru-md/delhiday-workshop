CONFIRM_EMAIL = """
Hi {0},

Please click this link to confirm your email address.

Enjoy our services.

{1} Team
{1}@fossasia.org
"""

NEW_USER = """
Hello {0},

We Welcome you to {1} Platform. We hope you enjoy our services
and help spread a good word!

Have a great Open Source Experience.

{1} Team
{1}@fossasia.org
"""

def body(_type=None):

	if not _type:
		return None

	if _type == 'CE':
		return CONFIRM_EMAIL

	if _type == 'NU':
		return NEW_USER
