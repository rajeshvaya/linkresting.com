from django.conf import settings

def disqus(request):
	if settings.DEBUG:
		return {
			'DISQUS':{
				'SHORTNAME': 'linkresting',
				'IDENTIFIER_PREFIX': 'linkrestingtest'
			}
		}
	else:
		return {
			'DISQUS':{
				'SHORTNAME': 'linkresting',
				'IDENTIFIER_PREFIX': 'linkresting'
			}
		}

def globals(request):
	return{
		'GLOBALS':{
			'BASE_URL': settings.BASE_URL
		}
	}

	

