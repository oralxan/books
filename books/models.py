from django.db.models import *#(*-hammes)
from django.contrib.auth.models import User #bul jerde User degen classti shaqirip atirmiz.Bul degen djangoda AbstractUser degen class bar yagniy ol biz saytqa admin bolip kirsek sol admindi aladi

class Book(Model):
    #modelsdi (*) arqali hammesine jalgandi type models.Model dep jaziw shart emes
    name = CharField(
        'name of the book',
        max_length=128
    )
    description = TextField(
        'description of the book ',
        null=True,
        blank=True
    )
    #authorga qosiw ushin joqaridagiday import qiliw kerek
    author = ForeignKey(#<-- basqa jaqqa jalg'aniw ushin
        User,
        verbose_name='Author',
        on_delete=CASCADE#eger post oshse userdin ozi saqlaniwi
       # default=someone registryatsiya qilinbasa qosilmaytin qiliw
    )
    price = PositiveBigIntegerField(
        'price of the books',
        default=2 #bahasi 0bolip turadi

    )#<-- bulda integerge uqsaydi biraq bul hardayim +(+sanalar jaziladi) boladi oz ishine 32767den ulken sanlardi aladi.PositiveSmallIntegerField()0den 32767

    released_book = DateField(
        'Date of realeased'
    )
    pages =PositiveSmallIntegerField(
        'Number of pages',

    )
    cover = ImageField(
        'Cover of the book',
        upload_to='books-images/'
    )
    def __str__(self):
        return f'{self.name}'
    class Meta:
        verbose_name = 'book'
        verbose_name_plural = 'books'