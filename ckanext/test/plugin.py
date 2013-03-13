# coding: utf-8

import os
import logging
import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
import ckan.lib.plugins as lib_plugins
import ckan.lib.navl.validators as validators
import ckan.logic as logic
import ckan.logic.converters as converters
import ckan.lib.base as base
from ckan.lib.navl.dictization_functions import DataError, StopOnError

log = logging.getLogger(__name__)

class TestPlugin(plugins.SingletonPlugin,
    lib_plugins.DefaultDatasetForm):

    plugins.implements(plugins.IConfigurer, inherit=False)
    plugins.implements(plugins.IDatasetForm, inherit=False)
# 
#     # Implementation IConfigurer
# 
    def update_config(self, config):  

        config['ckan.site_title'] = "Testoburger"
        config['ckan.site_logo'] = "/CKAN-logo.png"
        config['ckan.favicon'] = "http://datenregister.berlin.de/favicon.ico"

    # Implementation IDatasetForm

    def package_types(self):
        # This plugin doesn't handle any special package types, it just
        # registers itself as the default (above).
        return []

    def is_fallback(self):
        # Return True to register this plugin as the default handler for
        # package types not handled by any other IDatasetForm plugin.
        return True

    def form_to_db_schema(self):
        log.warning("form_to_db_schema")

        # get base dataset schema
        schema = logic.schema.form_to_db_package_schema()

        return schema

    def db_to_form_schema(self):
        log.warning("db_to_form_schema")
    
        # get base dataset schema
        schema = logic.schema.db_to_form_package_schema()
            
        return schema
    
    