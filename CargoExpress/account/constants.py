"""
Account constant messages
"""
from django.utils.translation import ugettext_lazy as _


USER_TYPE = (("P", _("Profesional")), ("G", _("Rancher")))
INVALID_PHONE_NUMBER = _(
    "The telephone number must correspond " "to the format +49187625375 or 0187625375."
)
INCORRECT_NAME = _("This field can only contain letters, periods and hyphens.")
COMPANY_NAME_INCORRECT = _("Company name must be between 5 " "and 60 characters")
INVALID_MOBILE = _("The phone number is too short.")
TERMS_AND_CONDITIONS = _("You must accept the term conditions")
INVALID_ID_CONFIRMATION_LINK = _(
    "Unfortunately, the link has expired "
    "or it is invalid. Please request a new link."
)
EMAIL_ADDRESS_DOES_NOT_EXIST = _(
    "The specified e-mail address " "could not be found as a user account."
)
EMAIL_ADDRESS_ALREADY_ACTIVATED = _("This email address is already confirmed")
OLD_PASSWORD_INCORRECT = _("The old password is incorrect")
RESET_PASSWORD_LINK_NO_LONGER_VALID = _(
    "The link to reset " "the password is no longer valid."
)
EMAIL_ADDRESS_NOT_VERIFIED_YET = _(
    "The specified e-mail address is not " "verified yet."
)
ACCOUNT_ALREADY_EXIST = _(
    "An account already exists for " "this email address. Please, log in."
)
