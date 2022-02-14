from django.core.validators import validate_email

class LoginValidator:

    def validate_is_blank_field(self, username, password) -> bool:
        if username is None:
            raise Exception(
                'username is required to log in.'
            )

        if password is None:
            raise Exception(
                'password is required to log in.'
            )

        return True

    def validate_is_activ(self, user) -> bool:

        if not user.is_active:
            raise Exception(
                'This user is deactivated.'
            )

    def validate_user_exists(self, user) -> bool:
        if user is None:
            raise Exception(
                "no such user"
            )
        return True

class EmailValidator:

    def validate_email(self, email):
        validate_email(email)
        
