from tortoise import fields, models, indexes


class User(models.Model):
    id = fields.IntField(primary_key=True, id=True)
    birth_date = fields.DateField()
    first_name = fields.CharField(max_length=50)
    last_name = fields.CharField(max_length=50)
    username = fields.CharField(unique=True, max_length=50)
    
    class Meta:
        table = 'app_user'
        indexes = [
            indexes.Index(fields=['username'])
        ]
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.username}"
    