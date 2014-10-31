from django.conf import settings

def disqus(request):
	if settings.DEBUG:
		print "here in test mode"
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

	

