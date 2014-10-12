from django.contrib import admin

from stories.models import Story

class StoryAdmin(admin.ModelAdmin):
	#display
	list_display = ('__unicode__', 'domain', 'moderator', 'created_at')
	list_filter = ('created_at',)
	search_fields = ('title','moderator__username','moderator__first_name')

	# fields = ('title', 'url', 'moderator', 'created_at', 'updated_at')
	fieldsets  = [
		('Story', {
			'fields' : ('title', 'url')	
		}),
		('Moderator',{
			'classes': ('collapse',),
			'fields': ('moderator',)	
		}),
		('Change history', {
			'fields': ('created_at', 'updated_at'),
		})
	]

	readonly_fields = ('created_at', 'updated_at')

admin.site.register(Story, StoryAdmin)


