from safrs import SAFRSAPI
import safrs
import importlib
import pathlib
import logging as logging

# use absolute path import for easier multi-{app,model,db} support
database = __import__('database')

app_logger = logging.getLogger(__name__)

app_logger.debug("\napi/expose_api_models.py - endpoint for each table")


def expose_models(api, method_decorators = []): 
    """
        Declare API - on existing SAFRSAPI to expose each model - API automation 
        - Including get (filtering, pagination, related data access) 
        - And post/patch/update (including logic enforcement) 

        Invoked at server startup (api_logic_server_run) 

        You typically do not customize this file 
        - See https://apilogicserver.github.io/Docs/Tutorial/#customize-and-debug 
    """
    api.expose_object(database.models.Bill, method_decorators= method_decorators)
    api.expose_object(database.models.Customer, method_decorators= method_decorators)
    api.expose_object(database.models.Order, method_decorators= method_decorators)
    api.expose_object(database.models.Chef, method_decorators= method_decorators)
    api.expose_object(database.models.Restaurant, method_decorators= method_decorators)
    api.expose_object(database.models.Ingredient, method_decorators= method_decorators)
    api.expose_object(database.models.Inventory, method_decorators= method_decorators)
    api.expose_object(database.models.Menu, method_decorators= method_decorators)
    api.expose_object(database.models.Reservation, method_decorators= method_decorators)
    api.expose_object(database.models.RestaurantTable, method_decorators= method_decorators)
    api.expose_object(database.models.Review, method_decorators= method_decorators)
    api.expose_object(database.models.SupplyOrder, method_decorators= method_decorators)
    return api
