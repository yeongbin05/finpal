from allauth.account.adapter import DefaultAccountAdapter


class CustomUserAccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=True):
        """
        Saves a new `User` instance using information provided in the
        signup form.
        """
        from allauth.account.utils import user_field

        user = super().save_user(request, user, form, False)
        user_field(user, 'realname', request.data.get('realname'))
        user_field(user, 'telphone', request.data.get('telphone'))
        user_field(user, 'dateOfBirth', request.data.get('dateOfBirth'))
        user.save()
        return user