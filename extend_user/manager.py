from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):

    def create_user(self, **kwargs):
        print('kwargs: ', kwargs)
        if kwargs['email'] is None:
            raise TypeError('Users must have an email address.')
        user = self.model(username=kwargs['username'], email=self.normalize_email(kwargs['email']))
        user.set_password(kwargs['password'])
        user.save()
        return user

    def create_superuser(self, **kwargs):
        print('kwargs: ', kwargs)
        if kwargs['email'] is None:
            raise TypeError('Users must have an email address.')
        user = self.model(username=kwargs['username'], email=self.normalize_email(kwargs['email']))
        user.set_password(kwargs['password'])
        user.is_superuser = True
        print(user.is_superuser)
        # user.save()
        return user