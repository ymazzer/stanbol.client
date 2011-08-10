import os
import urlparse

from restkit.errors import (
    ResourceNotFound
)

from stanbol.client.base import (
    StanbolCommunicator,
    RDFFORMATS,
)

class EntityHub(StanbolCommunicator):

    ## 
    _subpath = 'entityhub'

    def get_entity(self, uri):
        try:
            req = "entity?id=" + uri
            response = self._resource.get(path = req)
        except ResourceNotFound, e:
            raise KeyError, uri
        return response.body_string()
    #

    def lookup(self, uri, create):
        _c = "false"
        if create: 
            _c = "true"

        try:
            req = "lookup?id=" + uri + "&create=" + _c
            response = self._resource.get(path = req)
        except ResourceNotFound, e:
            raise KeyError, uri
        return response.body_string()
    #

    def find(self, name):
        pass
    #

    def query(self, json):
        pass
    #

    def mapping(self, uri):
        pass
    #
#

class EntityHubSite(EntityHub):

    ##
    _subpath = 'entityhub/sites'

    def get_referenced_sites(self):
        req = "referenced"
        try:
            response = self._resource.get(path = req)
        except ResourceNotFound, e:
            raise KeyError, e
        return response.body_string()
    #

    def get_entity(self, uri):
        req = 'entity' 
        print req
        print self._resource
        try:
            response = self._resource.get(path = req, params_dict = {'id': uri})
        except ResourceNotFound, e:
            raise KeyError, e
        return response.body_string()
    #

    def find(self, name, field, lang, limit, offset):
        params = {}
        if name:
            params['name'] = name
        if field:
            params['field'] = field
        if lang:
            params['lang'] = lang
        if limit:
            params['limit'] = limit
        if offset:
            params['offset'] = offset
        
        req = 'find'
        try:
            response = self._resource.post(path = req, params_dict = params)
        except ResourceNotFound, e:
            raise KeyError, e
            
        return response.body_string()
    #

    def query(self, query):
        headers = {
            'Content-Type': 'application/json'
        }
        response = self._resource.post(payload = query, headers=headers)
        return response.body_string()
    #
#
