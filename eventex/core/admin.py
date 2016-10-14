from django.contrib import admin

from eventex.core.models import Speaker, Contact


class ContactInline(admin.TabularInline):
    model = Contact
    extra = 1 # Mostra o números de campos vazios a serem preenchidos por padrão é 3


class SpeakerModelAdmin(admin.ModelAdmin):
    inlines = [ContactInline] # utiliza um lista com as classes do Inline (ContactInline)
    prepopulated_fields = {'slug': ('name',)}  # Recebe o valor do campo name e preenche o campo slug.
    list_display = ['name', 'photo_img', 'website_link']

    def website_link(self, obj):  # Cria o link.
        return '<a href="{0}">{0}</a>'.format(obj.website)

    website_link.allow_tags = True
    website_link.short_description = 'website'

    def photo_img(self, obj):
        return '<img width="32px" src="{}" />'.format(obj.photo)

    photo_img.allow_tags = True
    photo_img.short_description = 'foto'


admin.site.register(Speaker, SpeakerModelAdmin)

