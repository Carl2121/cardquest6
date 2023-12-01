from django.contrib import admin
from .models import Trainer, PokemonCard


@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ('name', 'birthdate', 'location', 'email')
    search_fields = ('name', 'location')


# Register your models here.

@admin.register(PokemonCard)
class PokemonCardAdmin(admin.ModelAdmin):
    list_display = ('name', 'rarity', 'hp', 'card_type', 'attack',
                    'description', 'weakness', 'card_number', 'release_date')
    search_fields = ('name', 'rarity', 'hp', 'card_type', 'attack',
                     'description', 'weakness', 'card_number', 'release_date')