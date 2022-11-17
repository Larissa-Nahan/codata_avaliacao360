from django.contrib import admin
from avaliacao.models import Categoria, AvaliacaoDesempenho, FatorDesempenhoMerito, FatorDesempenhoDemerito


class CategoriaAdmin(admin.ModelAdmin):
    pass
admin.site.register(Categoria, CategoriaAdmin)

class AvaliacaoDesempenhoAdmin(admin.ModelAdmin):
    pass
admin.site.register(AvaliacaoDesempenho, AvaliacaoDesempenhoAdmin)

class FatorDesempenhoMeritoAdmin(admin.ModelAdmin):
    pass
admin.site.register(FatorDesempenhoMerito, FatorDesempenhoMeritoAdmin)

class FatorDesempenhoDemeritoAdmin(admin.ModelAdmin):
    pass
admin.site.register(FatorDesempenhoDemerito, FatorDesempenhoDemeritoAdmin)