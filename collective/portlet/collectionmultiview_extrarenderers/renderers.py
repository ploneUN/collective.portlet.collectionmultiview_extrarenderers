from zope.component import adapts
from zope.interface import implements
from collective.portlet.collectionmultiview.renderers.base import CollectionMultiViewBaseRenderer
from zope.app.pagetemplate.viewpagetemplatefile import ViewPageTemplateFile
from plone.memoize.instance import memoize


from Products.CMFCore.utils import getToolByName
import base64
import zope.component
from zope.component import getUtility
from plone.i18n.normalizer.interfaces import IIDNormalizer
import hashlib
import random

class AlphabeticalTabRenderer(CollectionMultiViewBaseRenderer):

     template = ViewPageTemplateFile('skins/alphatabbed.pt')

     @memoize
     def alpharesults(self):
         retval = {}
         for result in self.results():
             firstletter=result.Title[:1].lower()
             if retval.has_key(firstletter):
                retval[firstletter].append(result)
             else:
                retval[firstletter] = [result]
         return retval

     def uid(self):
         return hashlib.md5(str(random.randint(11111,99999))).hexdigest()

     def genscript(self, uid):
         return '''
          jQuery(document).ready(function() {
             jQuery('#%(uid)s .alphatab-tabs').tabs('#%(uid)s .alphatab-panes > div');
          })
         ''' % dict(uid=uid)

class DefaultShortenedRenderer(CollectionMultiViewBaseRenderer):

     template = ViewPageTemplateFile('skins/default.pt')

     def shorttitle(self,title):
         if len(title) > 20:
            return "%s..." % title[:20]
         return title 

