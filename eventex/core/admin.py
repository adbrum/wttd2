from django.contrib import admin

from eventex.core.models import Speaker, Contact, Talk, Course


class ContactInline(admin.TabularInline):
    model = Contact
    extra = 1 # Mostra o números de campos vazios a serem preenchidos por padrão é 3


class SpeakerModelAdmin(admin.ModelAdmin):
    inlines = [ContactInline] # utiliza um lista com as classes do Inline (ContactInline)
    prepopulated_fields = {'slug': ('name',)}  # Recebe o valor do campo name e preenche o campo slug.
    list_display = ['name', 'photo_img', 'website_link', 'email', 'phone']

    def website_link(self, obj):  # Cria o link.
        return '<a href="{0}">{0}</a>'.format(obj.website)

    website_link.allow_tags = True
    website_link.short_description = 'website'

    def photo_img(self, obj):
        return '<img width="32px" src="{}" />'.format(obj.photo)

    photo_img.allow_tags = True
    photo_img.short_description = 'foto'

    def email(self, obj): # Inclui nova coluna no
        return obj.contact_set.emails().first()# Utilizando em conjunto com o manager
        # return obj.contact_set(manager='emails').first() # Utilizando em conjunto com o manager
        # return Contact.objects.filter(kind=Contact.EMAIL, speaker=obj).first()

    email.short_description = 'e-mail'

    def phone(self, obj): # Inclui nova coluna no admin
        return obj.contact_set.phones().first()# Utilizando em conjunto com o manager
        # return obj.contact_set(manager='emails').first()  # Utilizando em conjunto com o manager
        # return Contact.objects.filter(kind=Contact.PHONE, speaker=obj).first()

    phone.short_description = 'telefone'


admin.site.register(Speaker, SpeakerModelAdmin)
admin.site.register(Talk)
admin.site.register(Course)

