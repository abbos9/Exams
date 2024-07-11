from django.contrib import admin
from page.models import (
    FoodGalleryModel, FoodGalleryCategoryModel,  ReservationModel, SubscribeModel,
    MenuModel, MenuModelCategory,
    Comment, Events, ChefModel
)
# Register your models here.

@admin.register(MenuModel)
class MenuModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at']
    search_fields = ('id', 'title', 'created_at', 'about', )
    list_filter = ('id', 'title', 'created_at', 'about', )
    ordering = ['-created_at']

@admin.register(MenuModelCategory)
class MenuModelCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at']
    search_fields = ('id', 'name', 'created_at',)
    list_filter = ('id', 'name', 'created_at')
    ordering = ['-created_at']

@admin.register(FoodGalleryModel)
class FoodGalleryModelAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'price', 'created_at']
    search_fields = ('id', 'title', 'price', 'created_at')
    list_filter = ('created_at', 'updated_at')
    ordering = ['-created_at']

@admin.register(FoodGalleryCategoryModel)
class FoodGalleryCategoryModelAdmin(admin.ModelAdmin):
    list_display = ['id','name']
    search_fields = ('id', 'title')
    list_filter = ('created_at', 'updated_at')
    ordering = ['-created_at']


@admin.register(ReservationModel)
class ReservationModelAdmin(admin.ModelAdmin):
    list_display = ['id','contact_name','created_at']
    list_filter = ('created_at', 'updated_at')
    search_fields = ('id', 'contact_name', 'created_at')
    ordering = ['-created_at']

@admin.register(SubscribeModel)
class SubscribeModelAdmin(admin.ModelAdmin):
    list_display = ['id','email','created_at']
    list_filter = ('created_at', 'updated_at')
    search_fields = ('id','email')
    ordering = ['-created_at']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id','first_name','created_at']
    list_filter = ('created_at', 'updated_at')
    search_fields = ('id','job')
    ordering = ['-created_at']

@admin.register(Events)
class EventsModelAdmin(admin.ModelAdmin):
    list_display = ['id','title']
    search_fields = ('id', 'title')
    list_filter = ('created_at', 'updated_at')
    ordering = ['-created_at']


@admin.register(ChefModel)
class ChefModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'about']
    search_fields = ('id', 'title')
    list_filter = ('created_at', 'updated_at')
    ordering = ['-created_at']
