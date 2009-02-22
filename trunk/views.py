from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404

from tinyurl.models import TinyURL

def redirect(request, hash):
	tinyurl = get_object_or_404(TinyURL, hash=hash)
	
	return HttpResponseRedirect(tinyurl.url)
