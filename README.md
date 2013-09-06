ipviking-pyramid
================

And here we are again, with a new example of using IPViking to authenticate a webpage... this one built on the Pyramid framework.

Again, this is close to a virgin Pyramid app, using their simple tutorial example. The only additions are the following:

ipviking_auth: a pretty faithful refactor of ipviking-api-python.auth.authorizer, to use Pyramid's language to get the host instead.

views: a nextpage view added, which sends the client a 403 Forbidden with a specialized message if the client failed authentication.

templates/
	-mytemplate.pt: added hyperlink to the next page.
	-nextpage.pt: just like mytemplate, but telling you that you made it.
	
That's all you need! Enjoy, all!