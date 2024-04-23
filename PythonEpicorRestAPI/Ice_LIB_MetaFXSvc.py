import asyncio
import aiohttp
import configEpicorSchemas



# Title: Ice.LIB.MetaFXSvc
# Description: 
# Version: v1



#########################################################################
# OData methods:
#########################################################################
async def getServiceDocument(epicorHeaders = None):
   """  
   Summary: Get service document
   Description: Get service document for the service
   OperationID: GetServiceDocument
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => application/json
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.LIB.MetaFXSvc/",headers=creds) as resp:
           return await resp.json()

async def get_metadata(epicorHeaders = None):
   """  
   Summary: Get metadata document
   Description: Get service ODATA metadata in XML format
   OperationID: GetMetadata
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: Returns metadata document => content
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.LIB.MetaFXSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetApp(request, epicorHeaders = None):
   """  
   Summary: Invoke method GetApp
   Description: View JSON layout and other metadata information
   OperationID: Get_GetApp
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetApp_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "request=" + request

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.LIB.MetaFXSvc/$metadata" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetViews(epicorHeaders = None):
   """  
   Summary: Invoke method GetViews
   Description: Get all views. Used in Menu maintenance
   OperationID: Get_GetViews
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetViews_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.LIB.MetaFXSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_GetSearch(request, epicorHeaders = None):
   """  
   Summary: Invoke method GetSearch
   Description: Search dialog request and other metadata information
   OperationID: Get_GetSearch
      :param request: Desc: EpMetaFxSearchRequest   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSearch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "request=" + request

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.LIB.MetaFXSvc/$metadata" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetDefaultSearch(request, epicorHeaders = None):
   """  
   Summary: Invoke method GetDefaultSearch
   Description: Get default search folder and subfolder name for specified table
   OperationID: Get_GetDefaultSearch
      :param request: Desc: Request parameters for finding default search   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDefaultSearch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "request=" + request

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.LIB.MetaFXSvc/$metadata" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetSearchForm(request, epicorHeaders = None):
   """  
   Summary: Invoke method GetSearchForm
   Description: Check for LIKE property folder
   OperationID: Get_GetSearchForm
      :param request: Desc: EpMetaFxSearchRequest   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSearchForm_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "request=" + request

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.LIB.MetaFXSvc/$metadata" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetPeek(request, epicorHeaders = None):
   """  
   Summary: Invoke method GetPeek
   Description: Get Peek metadata information
   OperationID: Get_GetPeek
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPeek_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "request=" + request

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.LIB.MetaFXSvc/$metadata" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetPeeks(epicorHeaders = None):
   """  
   Summary: Invoke method GetPeeks
   Description: Gets folders and sub folders from peek folder.
   OperationID: Get_GetPeeks
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPeeks_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.LIB.MetaFXSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_GetTemplateView(templateType, epicorHeaders = None):
   """  
   Summary: Invoke method GetTemplateView
   Description: Gets the pre-defined templates like report/process etc
   OperationID: Get_GetTemplateView
      :param templateType: Desc: EpMetaFxViewRequest   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTemplateView_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "templateType=" + templateType

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.LIB.MetaFXSvc/$metadata" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetCombosData(request, epicorHeaders = None):
   """  
   Summary: Invoke method GetCombosData
   Description: Gets JSON files extended properties from the comobs
   OperationID: Get_GetCombosData
      :param request: Desc: EpMetaFxComboRequest   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCombosData_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "request=" + request

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.LIB.MetaFXSvc/$metadata" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetCombos(epicorHeaders = None):
   """  
   Summary: Invoke method GetCombos
   Description: Gets folders and sub folders names from combo shared folder
   OperationID: Get_GetCombos
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCombos_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.LIB.MetaFXSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_Upgrade(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method Upgrade
   Description: Upgrades the view
   OperationID: Upgrade
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Upgrade_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Upgrade_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.MetaFXSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpgradeLayer(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpgradeLayer
   Description: Upgrade layer
   OperationID: UpgradeLayer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpgradeLayer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpgradeLayer_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.MetaFXSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RunDataFixForLayers(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RunDataFixForLayers
   Description: Executes custom data fix routines on customization layers for a given product version. Not supported for Base layers.
This is different from the upgrade because the fix up uses the original version of the base from which the layer was created.
   OperationID: RunDataFixForLayers
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RunDataFixForLayers_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RunDataFixForLayers_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.MetaFXSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SaveApp(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SaveApp
   Description: Saves the information.
- In case of customization it saves as draft
- In case of layers, it saves in DB as WIP
   OperationID: SaveApp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SaveApp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SaveApp_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.MetaFXSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PublishApp(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PublishApp
   Description: publish the information.
- In case of customization it replaces the actual file
- In case of layers, it saves in DB
   OperationID: PublishApp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PublishApp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PublishApp_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.MetaFXSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_BulkPublishLayers(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method BulkPublishLayers
   Description: Publishes all the layers in the list. Parent layers are not published automatically.
   OperationID: BulkPublishLayers
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BulkPublishLayers_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BulkPublishLayers_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.MetaFXSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_BulkDeleteLayers(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method BulkDeleteLayers
   Description: Delete layers and applications in bulk.
- SDK users can delete all applications and layers.
- Non SDK users can delete applications if they can customize applications or if application does not have any layers.
   OperationID: BulkDeleteLayers
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BulkDeleteLayers_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BulkDeleteLayers_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.MetaFXSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_InvalidateCache(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method InvalidateCache
   Description: Deletes cache folder
   OperationID: InvalidateCache
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/InvalidateCache_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InvalidateCache_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.MetaFXSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GetViewTypes(epicorHeaders = None):
   """  
   Summary: Invoke method GetViewTypes
   Description: returns all the folder names except common from root path(.\MetaUI\Shared\ViewTypes).
   OperationID: Get_GetViewTypes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetViewTypes_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.LIB.MetaFXSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_GetLayer(request, epicorHeaders = None):
   """  
   Summary: Invoke method GetLayer
   Description: Gets the layer.
   OperationID: Get_GetLayer
      :param request: Desc: Request to get layer.   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLayer_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "request=" + request

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.LIB.MetaFXSvc/$metadata" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetLayers(request, epicorHeaders = None):
   """  
   Summary: Invoke method GetLayers
   Description: Get the layers.
   OperationID: Get_GetLayers
      :param request: Desc: Request to get layers.   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLayers_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "request=" + request

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.LIB.MetaFXSvc/$metadata" + params,headers=creds) as resp:
           return await resp.json()

async def post_DeleteLayer(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteLayer
   Description: Deletes the layer.
   OperationID: DeleteLayer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteLayer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteLayer_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.MetaFXSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ApplicationExists(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ApplicationExists
   Description: Checks if the application exists.
   OperationID: ApplicationExists
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ApplicationExists_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ApplicationExists_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.MetaFXSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ComponentExists(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ComponentExists
   Description: Checks if the component exists.
   OperationID: ComponentExists
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ComponentExists_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ComponentExists_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.MetaFXSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GenerateView(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GenerateView
   Description: Generates the view.
   OperationID: GenerateView
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenerateView_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateView_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.MetaFXSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GetAuditLogs(request, epicorHeaders = None):
   """  
   Summary: Invoke method GetAuditLogs
   Description: This method returns audit log for layers.
   OperationID: Get_GetAuditLogs
      :param request: Desc: request   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAuditLogs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "request=" + request

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.LIB.MetaFXSvc/$metadata" + params,headers=creds) as resp:
           return await resp.json()

async def get_DownloadSchema(request, epicorHeaders = None):
   """  
   Summary: Invoke method DownloadSchema
   Description: Download event schema
   OperationID: Get_DownloadSchema
      :param request: Desc: DownloadSchemaRequest   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/DownloadSchema_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "request=" + request

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.LIB.MetaFXSvc/$metadata" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetEventDesigner(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetEventDesigner
   Description: This method gets the event designer.
   OperationID: GetEventDesigner
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetEventDesigner_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetEventDesigner_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.MetaFXSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GetApplicationSubTypes(applicationType, epicorHeaders = None):
   """  
   Summary: Invoke method GetApplicationSubTypes
   Description: Get Application Types.
   OperationID: Get_GetApplicationSubTypes
      :param applicationType: Desc: applicationType   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetApplicationSubTypes_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "applicationType=" + applicationType

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.LIB.MetaFXSvc/$metadata" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetApplications(request, epicorHeaders = None):
   """  
   Summary: Invoke method GetApplications
   Description: Get Applications.
   OperationID: Get_GetApplications
      :param request: Desc: request   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetApplications_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "request=" + request

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.LIB.MetaFXSvc/$metadata" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetNewApplication(request, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewApplication
   Description: Get New Application.
   OperationID: Get_GetNewApplication
      :param request: Desc: request   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewApplication_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "request=" + request

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.LIB.MetaFXSvc/$metadata" + params,headers=creds) as resp:
           return await resp.json()

async def get_ExportApp(viewId, epicorHeaders = None):
   """  
   Summary: Invoke method ExportApp
   Description: Export App
   OperationID: Get_ExportApp
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExportApp_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "viewId=" + viewId

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.LIB.MetaFXSvc/$metadata" + params,headers=creds) as resp:
           return await resp.json()

async def post_ImportApp(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ImportApp
   Description: Import App
   OperationID: ImportApp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportApp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportApp_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.MetaFXSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ExportLayers(apps, epicorHeaders = None):
   """  
   Summary: Invoke method ExportLayers
   Description: Export Layers
Export currently supported for Custom Apps and layers not for System Apps
   OperationID: Get_ExportLayers
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExportLayers_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "apps=" + apps

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.LIB.MetaFXSvc/$metadata" + params,headers=creds) as resp:
           return await resp.json()

async def post_ImportLayers(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ImportLayers
   Description: Import Layers
The method imports Custom Apps and layers. System Apps are not supported.
   OperationID: ImportLayers
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportLayers_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportLayers_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.MetaFXSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DuplicateApp(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DuplicateApp
   Description: Duplicate Applications
   OperationID: DuplicateApp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DuplicateApp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DuplicateApp_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.MetaFXSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteApp(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteApp
   Description: Delete Applicatons
   OperationID: DeleteApp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteApp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteApp_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.MetaFXSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GetSystemApplicationStatus(viewId, epicorHeaders = None):
   """  
   Summary: Invoke method GetSystemApplicationStatus
   Description: Check for SystemFlag.
   OperationID: Get_GetSystemApplicationStatus
      :param viewId: Desc: viewId   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSystemApplicationStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "viewId=" + viewId

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.LIB.MetaFXSvc/$metadata" + params,headers=creds) as resp:
           return await resp.json()

async def get_SetSecurityCodeForApplication(viewId, securityCode, epicorHeaders = None):
   """  
   Summary: Invoke method SetSecurityCodeForApplication
   Description: Update the security code for custom app.
   OperationID: Get_SetSecurityCodeForApplication
      :param viewId: Desc: viewId   Required: True   Allow empty value : True
      :param securityCode: Desc: securityCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetSecurityCodeForApplication_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "viewId=" + viewId
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "securityCode=" + securityCode

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.LIB.MetaFXSvc/$metadata" + params,headers=creds) as resp:
           return await resp.json()

async def get_RestoreVersion(request, epicorHeaders = None):
   """  
   Summary: Invoke method RestoreVersion
   Description: Restores the version into the draft.
   OperationID: Get_RestoreVersion
      :param request: Desc: Request object   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/RestoreVersion_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "request=" + request

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.LIB.MetaFXSvc/$metadata" + params,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class ApplicationExists_input:
   """ Required : 
   applicationFullName
   """  
   def __init__(self, obj):
      self.applicationFullName:str = obj["applicationFullName"]
      """  Complete name of the application including the prefix. E.g. Ice.UIDbd.SampleDashboard  """  
      pass

class ApplicationExists_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      """  True if the application exists  """  
      pass

class BulkDeleteLayers_input:
   """ Required : 
   layersToDelete
   """  
   def __init__(self, obj):
      self.layersToDelete:list[Epicor_MetaFX_Core_Models_Layers_EpMetaFxLayerForApplication] = obj["layersToDelete"]
      """  Layers to Delete  """  
      pass

class BulkDeleteLayers_output:
   def __init__(self, obj):
      self.returnObj:list[Epicor_MetaFX_Core_Models_Layers_EpMetaFxLayerForApplication] = obj["returnObj"]
      pass

class BulkPublishLayers_input:
   """ Required : 
   layersToPublish
   validateBeforePublish
   """  
   def __init__(self, obj):
      self.layersToPublish:list[Epicor_MetaFX_Core_Models_Layers_EpMetaFxLayerForApplication] = obj["layersToPublish"]
      """  Layers to publish  """  
      self.validateBeforePublish:bool = obj["validateBeforePublish"]
      """  Validate each layer before publish (not implemented currently)  """  
      pass

class BulkPublishLayers_output:
   def __init__(self, obj):
      self.returnObj:list[Epicor_MetaFX_Core_Models_Layers_EpMetaFxLayerForApplication] = obj["returnObj"]
      pass

class ComponentExists_input:
   """ Required : 
   componentFullName
   """  
   def __init__(self, obj):
      self.componentFullName:str = obj["componentFullName"]
      """  Complete name of the component including the prefix. E.g. Ice.UIDbd.SampleDashboard  """  
      pass

class ComponentExists_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      """  True if the component exists  """  
      pass

class DeleteApp_input:
   """ Required : 
   viewId
   """  
   def __init__(self, obj):
      self.viewId:str = obj["viewId"]
      pass

class DeleteApp_output:
   def __init__(self, obj):
      pass

class DeleteLayer_input:
   """ Required : 
   request
   """  
   def __init__(self, obj):
      self.request:list[Epicor_MetaFX_Core_Models_Layers_EpMetaFxLayerRequest] = obj["request"]
      pass

class DeleteLayer_output:
   def __init__(self, obj):
      pass

class DownloadSchema_input:
   """ Required : 
   request
   """  
   def __init__(self, obj):
      self.request:list[Epicor_MetaFX_Core_Models_DownloadSchemaRequest] = obj["request"]
      pass

class DownloadSchema_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      pass

class DuplicateApp_input:
   """ Required : 
   request
   """  
   def __init__(self, obj):
      self.request:list[Epicor_MetaFX_Core_Models_Configurator_DuplicateRequest] = obj["request"]
      pass

class DuplicateApp_output:
   def __init__(self, obj):
      pass

class Epicor_MetaFX_Core_Models_AppContent:
   """ Required : 
   CompanyId
   Files
   ViewId
   """  
   def __init__(self, obj):
      self.ViewId:str = obj["ViewId"]
      self.CompanyId:str = obj["CompanyId"]
      self.Files      #schema had no properties on an object.
      pass

class Epicor_MetaFX_Core_Models_Applications_Application:
   """ Required : 
   Id
   SubType
   Type
   """  
   def __init__(self, obj):
      self.Id:str = obj["Id"]
      self.Type:str = obj["Type"]
      self.SubType:str = obj["SubType"]
      self.LastUpdated:str = obj["LastUpdated"]
      self.IsLayerDisabled:bool = obj["IsLayerDisabled"]
      self.SystemFlag:bool = obj["SystemFlag"]
      self.HasDraftContent:bool = obj["HasDraftContent"]
      self.PublishError:str = obj["PublishError"]
      self.PublishStatus:int = obj["PublishStatus"]
      self.Layers:list[Epicor_MetaFX_Core_Models_Layers_EpMetaFxLayerForApplication] = obj["Layers"]
      self.CreatedBy:str = obj["CreatedBy"]
      self.CanAccessBase:bool = obj["CanAccessBase"]
      self.SecurityCode:str = obj["SecurityCode"]
      pass

class Epicor_MetaFX_Core_Models_Applications_ApplicationRequest:
   def __init__(self, obj):
      self.Type:str = obj["Type"]
      self.SubType:str = obj["SubType"]
      self.SearchText:str = obj["SearchText"]
      self.IsPublished:bool = obj["IsPublished"]
      self.IncludeAllLayers:bool = obj["IncludeAllLayers"]
      pass

class Epicor_MetaFX_Core_Models_Applications_ApplicationSubType:
   def __init__(self, obj):
      self.SubType:str = obj["SubType"]
      self.Prefix:str = obj["Prefix"]
      self.IsLayerDisabled:bool = obj["IsLayerDisabled"]
      pass

class Epicor_MetaFX_Core_Models_BAQReport_ReportResponse:
   def __init__(self, obj):
      self.Id:str = obj["Id"]
      self.FileName:str = obj["FileName"]
      pass

class Epicor_MetaFX_Core_Models_Configurator_ConfiguratorInfo:
   def __init__(self, obj):
      self.ConfigId:str = obj["ConfigId"]
      self.Approved:bool = obj["Approved"]
      self.AuditDesc:str = obj["AuditDesc"]
      self.Description:str = obj["Description"]
      self.AprvRev:bool = obj["AprvRev"]
      self.IsValidPwd:bool = obj["IsValidPwd"]
      self.DispConfSummary:bool = obj["DispConfSummary"]
      self.StatusExpr:list[Epicor_MetaFX_Core_Models_Configurator_StatusExpr] = obj["StatusExpr"]
      self.PcPageExpr:list[Epicor_MetaFX_Core_Models_Configurator_PcPageExpr] = obj["PcPageExpr"]
      self.DynamicAttributeClassId:str = obj["DynamicAttributeClassId"]
      self.ConfigUDFunc:list[Epicor_MetaFX_Core_Models_Configurator_ConfiguratorUDFunction] = obj["ConfigUDFunc"]
      pass

class Epicor_MetaFX_Core_Models_Configurator_ConfiguratorUDFunction:
   def __init__(self, obj):
      self.PcFunctionDef:list[Epicor_MetaFX_Core_Models_Configurator_PcFunctionDef] = obj["PcFunctionDef"]
      self.PcFunctionDefAttch:list[Epicor_MetaFX_Core_Models_Configurator_PcFunctionDefAttch] = obj["PcFunctionDefAttch"]
      self.PcFunctionParam:list[Epicor_MetaFX_Core_Models_Configurator_PcFunctionParam] = obj["PcFunctionParam"]
      self.ExtensionTables:object
      pass

class Epicor_MetaFX_Core_Models_Configurator_DuplicateRequest:
   """ Required : 
   NewViewId
   ViewId
   """  
   def __init__(self, obj):
      self.ViewId:str = obj["ViewId"]
      self.NewViewId:str = obj["NewViewId"]
      pass

class Epicor_MetaFX_Core_Models_Configurator_PcFunctionDef:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.FunctionName:str = obj["FunctionName"]
      self.Description:str = obj["Description"]
      self.ConfigID:str = obj["ConfigID"]
      self.FunctionType:str = obj["FunctionType"]
      self.Expression:str = obj["Expression"]
      self.ReturnType:str = obj["ReturnType"]
      self.OldFunctionName:str = obj["OldFunctionName"]
      self.IsSync:bool = obj["IsSync"]
      self.GlobalFunc:bool = obj["GlobalFunc"]
      self.SysRevID:str = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.BagID:str = obj["BagID"]
      self.NoInputs:bool = obj["NoInputs"]
      self.ScriptExpression:str = obj["ScriptExpression"]
      self.DispFunctionName:str = obj["DispFunctionName"]
      self.DispFunctionType:str = obj["DispFunctionType"]
      self.DispReturnType:str = obj["DispReturnType"]
      self.BtnEditScript:bool = obj["BtnEditScript"]
      self.BitFlag:int = obj["BitFlag"]
      self.PcStatusConfigType:str = obj["PcStatusConfigType"]
      self.PcStatusApproved:bool = obj["PcStatusApproved"]
      self.RowMod:str = obj["RowMod"]
      pass

class Epicor_MetaFX_Core_Models_Configurator_PcFunctionDefAttch:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.ConfigID:str = obj["ConfigID"]
      self.FunctionName:str = obj["FunctionName"]
      self.DrawingSeq:int = obj["DrawingSeq"]
      self.XFileRefNum:int = obj["XFileRefNum"]
      self.SysRevID:str = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      self.DrawDesc:str = obj["DrawDesc"]
      self.FileName:str = obj["FileName"]
      self.PDMDocID:str = obj["PDMDocID"]
      self.DocTypeID:str = obj["DocTypeID"]
      self.RowMod:str = obj["RowMod"]
      pass

class Epicor_MetaFX_Core_Models_Configurator_PcFunctionParam:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.FunctionName:str = obj["FunctionName"]
      self.ParameterName:str = obj["ParameterName"]
      self.DefaultValue:str = obj["DefaultValue"]
      self.Modifier:str = obj["Modifier"]
      self.ParamType:str = obj["ParamType"]
      self.ConfigID:str = obj["ConfigID"]
      self.ParamSeq:int = obj["ParamSeq"]
      self.SysRevID:str = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      pass

class Epicor_MetaFX_Core_Models_Configurator_PcPageExpr:
   def __init__(self, obj):
      self.TypeCode:str = obj["TypeCode"]
      self.Expression:str = obj["Expression"]
      self.PageName:str = obj["PageName"]
      pass

class Epicor_MetaFX_Core_Models_Configurator_StatusExpr:
   def __init__(self, obj):
      self.TypeCode:str = obj["TypeCode"]
      self.Expression:str = obj["Expression"]
      pass

class Epicor_MetaFX_Core_Models_DownloadSchemaRequest:
   def __init__(self, obj):
      self.EventID:str = obj["EventID"]
      pass

class Epicor_MetaFX_Core_Models_EpMetaFXLayerFixRequest:
   def __init__(self, obj):
      self.previousVersionMetaUIFolder:str = obj["previousVersionMetaUIFolder"]
      self.loadPreviousVersionFromDb:bool = obj["loadPreviousVersionFromDb"]
      self.applications:str = obj["applications"]
      self.clearBackupData:bool = obj["clearBackupData"]
      pass

class Epicor_MetaFX_Core_Models_EpMetaFxRequest:
   def __init__(self, obj):
      self.id:str = obj["id"]
      self.properties:list[Epicor_MetaFX_Core_Models_EpMetaFxRequestProperty] = obj["properties"]
      pass

class Epicor_MetaFX_Core_Models_EpMetaFxRequestProperty:
   def __init__(self, obj):
      self.layers:str = obj["layers"]
      self.layerType:str = obj["layerType"]
      self.deviceType:str = obj["deviceType"]
      self.mode:str = obj["mode"]
      self.userName:str = obj["userName"]
      self.pageName:str = obj["pageName"]
      self.company:str = obj["company"]
      self.countryGroupCode:str = obj["countryGroupCode"]
      self.debug:bool = obj["debug"]
      self.countryCode:str = obj["countryCode"]
      self.includeWasm:bool = obj["includeWasm"]
      self.applicationType:str = obj["applicationType"]
      self.additionalContext      #schema had no properties on an object.
      self.checkDuplicateIds:bool = obj["checkDuplicateIds"]
      self.layerVersion:int = obj["layerVersion"]
      self.baseAppVersion:int = obj["baseAppVersion"]
      pass

class Epicor_MetaFX_Core_Models_EpMetaFxSaveRequestEx:
   def __init__(self, obj):
      self.id:str = obj["id"]
      self.commentText:str = obj["commentText"]
      self.deviceType:str = obj["deviceType"]
      self.userName:str = obj["userName"]
      self.viewType:str = obj["viewType"]
      self.layout      #schema had no properties on an object.
      self.classicLayout      #schema had no properties on an object.
      self.pages      #schema had no properties on an object.
      self.rules      #schema had no properties on an object.
      self.events      #schema had no properties on an object.
      self.tools      #schema had no properties on an object.
      self.dataviews      #schema had no properties on an object.
      self.layerInfo:list[Epicor_MetaFX_Core_Models_Layer] = obj["layerInfo"]
      self.countryGroupCode:str = obj["countryGroupCode"]
      self.countryCode:str = obj["countryCode"]
      self.serializedEvents      #schema had no properties on an object.
      self.applicationType:str = obj["applicationType"]
      self.subApplicationType:str = obj["subApplicationType"]
      self.properties      #schema had no properties on an object.
      self.configuratorInfo:list[Epicor_MetaFX_Core_Models_Configurator_ConfiguratorInfo] = obj["configuratorInfo"]
      self.uxAppVersion:int = obj["uxAppVersion"]
      pass

class Epicor_MetaFX_Core_Models_EpMetaFxTemplateRequest:
   def __init__(self, obj):
      self.TemplateType:str = obj["TemplateType"]
      self.ViewType:str = obj["ViewType"]
      pass

class Epicor_MetaFX_Core_Models_EpMetaFxUpgradeSchemaRequest:
   def __init__(self, obj):
      self.content:str = obj["content"]
      pass

class Epicor_MetaFX_Core_Models_Events_EpMetaFxEventDesigner:
   def __init__(self, obj):
      self.ViewId:str = obj["ViewId"]
      self.Company:str = obj["Company"]
      self.LayerName:str = obj["LayerName"]
      self.EventId:str = obj["EventId"]
      self.DeviceType:str = obj["DeviceType"]
      self.Content      #schema had no properties on an object.
      self.CGCCode:str = obj["CGCCode"]
      pass

class Epicor_MetaFX_Core_Models_Events_EpMetaFxEventDesignerRequest:
   """ Required : 
   DeviceType
   EventId
   ViewId
   """  
   def __init__(self, obj):
      self.ViewId:str = obj["ViewId"]
      self.Company:str = obj["Company"]
      self.Layers:str = obj["Layers"]
      self.EventId:str = obj["EventId"]
      self.DeviceType:str = obj["DeviceType"]
      pass

class Epicor_MetaFX_Core_Models_ImportLayerRequest:
   def __init__(self, obj):
      self.content:str = obj["content"]
      self.overwrite:bool = obj["overwrite"]
      pass

class Epicor_MetaFX_Core_Models_Layer:
   def __init__(self, obj):
      self.company:str = obj["company"]
      self.typeCode:str = obj["typeCode"]
      self.layerName:str = obj["layerName"]
      self.layerDescription:str = obj["layerDescription"]
      self.parentLayers:str = obj["parentLayers"]
      self.wip:bool = obj["wip"]
      self.IsNew:bool = obj["IsNew"]
      self.CGCCode:str = obj["CGCCode"]
      self.PublishParentLayers:bool = obj["PublishParentLayers"]
      pass

class Epicor_MetaFX_Core_Models_Layers_EpMetaFXAuditLog:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.TypeCode:str = obj["TypeCode"]
      self.ViewId:str = obj["ViewId"]
      self.Name:str = obj["Name"]
      self.Description:str = obj["Description"]
      self.ParentLayers:str = obj["ParentLayers"]
      self.CommentText:str = obj["CommentText"]
      self.DeviceType:str = obj["DeviceType"]
      self.LastUpdated:str = obj["LastUpdated"]
      self.LastUpdatedBy:str = obj["LastUpdatedBy"]
      self.Published:str = obj["Published"]
      pass

class Epicor_MetaFX_Core_Models_Layers_EpMetaFXAuditLogRequest:
   def __init__(self, obj):
      self.ViewId:str = obj["ViewId"]
      self.LayerName:str = obj["LayerName"]
      self.ApplicationType:str = obj["ApplicationType"]
      self.ApplicationSubType:str = obj["ApplicationSubType"]
      self.Company:str = obj["Company"]
      pass

class Epicor_MetaFX_Core_Models_Layers_EpMetaFxLayerForApplication:
   """ Required : 
   DeviceType
   TypeCode
   """  
   def __init__(self, obj):
      self.Id:str = obj["Id"]
      self.SubType:str = obj["SubType"]
      self.LastUpdated:str = obj["LastUpdated"]
      self.IsPublished:bool = obj["IsPublished"]
      self.TypeCode:str = obj["TypeCode"]
      self.Company:str = obj["Company"]
      self.LayerName:str = obj["LayerName"]
      self.DeviceType:str = obj["DeviceType"]
      self.CGCCode:str = obj["CGCCode"]
      self.UpgradeStatus:int = obj["UpgradeStatus"]
      self.UpgradeError:str = obj["UpgradeError"]
      self.DeleteError:str = obj["DeleteError"]
      self.SystemFlag:bool = obj["SystemFlag"]
      self.PublishError:str = obj["PublishError"]
      self.PublishStatus:int = obj["PublishStatus"]
      self.HasDraftContent:bool = obj["HasDraftContent"]
      self.LastUpdatedBy:str = obj["LastUpdatedBy"]
      pass

class Epicor_MetaFX_Core_Models_Layers_EpMetaFxLayerRequest:
   """ Required : 
   DeviceType
   TypeCode
   UserName
   ViewId
   """  
   def __init__(self, obj):
      self.ViewId:str = obj["ViewId"]
      self.Company:str = obj["Company"]
      self.TypeCode:str = obj["TypeCode"]
      self.LayerName:str = obj["LayerName"]
      self.DeviceType:str = obj["DeviceType"]
      self.ParentLayers:str = obj["ParentLayers"]
      self.UserName:str = obj["UserName"]
      self.PageName:str = obj["PageName"]
      self.CGCCode:str = obj["CGCCode"]
      self.IncludeDraftContent:bool = obj["IncludeDraftContent"]
      self.UxAppVersion:int = obj["UxAppVersion"]
      pass

class Epicor_MetaFX_Core_Models_MetaFxUpgradeLayerRequest:
   def __init__(self, obj):
      self.Id:str = obj["Id"]
      self.UpgradeType:int = obj["UpgradeType"]
      pass

class Epicor_MetaFX_Core_Models_MetaUI_Strings_ApplicationString:
   def __init__(self, obj):
      self.id:str = obj["id"]
      self.text:str = obj["text"]
      self.layer:bool = obj["layer"]
      self.missing:bool = obj["missing"]
      pass

class Epicor_MetaFX_Core_Models_ViewMetadataResponse:
   def __init__(self, obj):
      self.AllowVersions:bool = obj["AllowVersions"]
      self.Layout      #schema had no properties on an object.
      self.Events      #schema had no properties on an object.
      self.ToolBar      #schema had no properties on an object.
      self.DataViews      #schema had no properties on an object.
      self.Rules      #schema had no properties on an object.
      self.References      #schema had no properties on an object.
      self.Pages      #schema had no properties on an object.
      self.Properties      #schema had no properties on an object.
      self.Wasm:str = obj["Wasm"]
      self.IsLayerDisabled:bool = obj["IsLayerDisabled"]
      self.ConfiguratorInfo:list[Epicor_MetaFX_Core_Models_Configurator_ConfiguratorInfo] = obj["ConfiguratorInfo"]
      self.ApplicationStrings:list[Epicor_MetaFX_Core_Models_MetaUI_Strings_ApplicationString] = obj["ApplicationStrings"]
      pass

class ExportApp_input:
   """ Required : 
   viewId
   """  
   def __init__(self, obj):
      self.viewId:str = obj["viewId"]
      pass

class ExportApp_output:
   def __init__(self, obj):
      self.returnObj:list[Epicor_MetaFX_Core_Models_AppContent] = obj["returnObj"]
      pass

class ExportLayers_input:
   """ Required : 
   apps
   """  
   def __init__(self, obj):
      self.apps:list[Epicor_MetaFX_Core_Models_Layers_EpMetaFxLayerForApplication] = obj["apps"]
      pass

class ExportLayers_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GenerateView_input:
   """ Required : 
   request
   """  
   def __init__(self, obj):
      self.request:list[Ice_Lib_MetaFX_EpMetaFxGenerateViewRequest] = obj["request"]
      pass

class GenerateView_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Lib_MetaFX_EpMetaFxResponse_Epicor_MetaFX_Core_Models_BAQReport_ReportResponse] = obj["returnObj"]
      pass

class GetApp_input:
   """ Required : 
   request
   """  
   def __init__(self, obj):
      self.request:list[Epicor_MetaFX_Core_Models_EpMetaFxRequest] = obj["request"]
      pass

class GetApp_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      """  View's JSON Metadata  """  
      pass

class GetApplicationSubTypes_input:
   """ Required : 
   applicationType
   """  
   def __init__(self, obj):
      self.applicationType:str = obj["applicationType"]
      """  applicationType  """  
      pass

class GetApplicationSubTypes_output:
   def __init__(self, obj):
      self.returnObj:list[Epicor_MetaFX_Core_Models_Applications_ApplicationSubType] = obj["returnObj"]
      pass

class GetApplications_input:
   """ Required : 
   request
   """  
   def __init__(self, obj):
      self.request:list[Epicor_MetaFX_Core_Models_Applications_ApplicationRequest] = obj["request"]
      pass

class GetApplications_output:
   def __init__(self, obj):
      self.returnObj:list[Epicor_MetaFX_Core_Models_Applications_Application] = obj["returnObj"]
      pass

class GetAuditLogs_input:
   """ Required : 
   request
   """  
   def __init__(self, obj):
      self.request:list[Epicor_MetaFX_Core_Models_Layers_EpMetaFXAuditLogRequest] = obj["request"]
      pass

class GetAuditLogs_output:
   def __init__(self, obj):
      self.returnObj:list[Epicor_MetaFX_Core_Models_Layers_EpMetaFXAuditLog] = obj["returnObj"]
      pass

class GetCombosData_input:
   """ Required : 
   request
   """  
   def __init__(self, obj):
      self.request:list[Ice_Lib_MetaFX_EpMetaFxComboRequest] = obj["request"]
      pass

class GetCombosData_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      pass

class GetCombos_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      pass

class GetDefaultSearch_input:
   """ Required : 
   request
   """  
   def __init__(self, obj):
      self.request:list[Ice_Lib_MetaFX_EpMetaFxDefaultSearchRequest] = obj["request"]
      pass

class GetDefaultSearch_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Lib_MetaFX_EpMetaFxDefaultSearchResponse] = obj["returnObj"]
      pass

class GetEventDesigner_input:
   """ Required : 
   request
   """  
   def __init__(self, obj):
      self.request:list[Epicor_MetaFX_Core_Models_Events_EpMetaFxEventDesignerRequest] = obj["request"]
      pass

class GetEventDesigner_output:
   def __init__(self, obj):
      self.returnObj:list[Epicor_MetaFX_Core_Models_Events_EpMetaFxEventDesigner] = obj["returnObj"]
      pass

class GetLayer_input:
   """ Required : 
   request
   """  
   def __init__(self, obj):
      self.request:list[Epicor_MetaFX_Core_Models_Layers_EpMetaFxLayerRequest] = obj["request"]
      pass

class GetLayer_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      pass

class GetLayers_input:
   """ Required : 
   request
   """  
   def __init__(self, obj):
      self.request:list[Ice_Lib_MetaFX_EpMetaFxGetLayersRequest] = obj["request"]
      pass

class GetLayers_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      pass

class GetNewApplication_input:
   """ Required : 
   request
   """  
   def __init__(self, obj):
      self.request:list[Epicor_MetaFX_Core_Models_Applications_Application] = obj["request"]
      pass

class GetNewApplication_output:
   def __init__(self, obj):
      self.returnObj:list[Epicor_MetaFX_Core_Models_ViewMetadataResponse] = obj["returnObj"]
      pass

class GetPeek_input:
   """ Required : 
   request
   """  
   def __init__(self, obj):
      self.request:list[Ice_Lib_MetaFX_EpMetaFxPeekRequest] = obj["request"]
      pass

class GetPeek_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      pass

class GetPeeks_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      pass

class GetSearchForm_input:
   """ Required : 
   request
   """  
   def __init__(self, obj):
      self.request:list[Ice_Lib_MetaFX_EpMetaFxSearchRequest] = obj["request"]
      pass

class GetSearchForm_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      pass

class GetSearch_input:
   """ Required : 
   request
   """  
   def __init__(self, obj):
      self.request:list[Ice_Lib_MetaFX_EpMetaFxSearchRequest] = obj["request"]
      pass

class GetSearch_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      pass

class GetSystemApplicationStatus_input:
   """ Required : 
   viewId
   """  
   def __init__(self, obj):
      self.viewId:str = obj["viewId"]
      """  viewId  """  
      pass

class GetSystemApplicationStatus_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      """  True if SystemFlag is set to true  """  
      pass

class GetTemplateView_input:
   """ Required : 
   templateType
   """  
   def __init__(self, obj):
      self.templateType:list[Epicor_MetaFX_Core_Models_EpMetaFxTemplateRequest] = obj["templateType"]
      pass

class GetTemplateView_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      pass

class GetViewTypes_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetViews_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  All views  """  
      pass

class Ice_Lib_MetaFX_EpMetaFxCacheInvalidateRequest:
   def __init__(self, obj):
      self.viewId:str = obj["viewId"]
      self.Type:str = obj["Type"]
      self.Like:str = obj["Like"]
      self.LanguageId:str = obj["LanguageId"]
      pass

class Ice_Lib_MetaFX_EpMetaFxComboRequest:
   def __init__(self, obj):
      self.folder:str = obj["folder"]
      self.subfolder:str = obj["subfolder"]
      pass

class Ice_Lib_MetaFX_EpMetaFxDefaultSearchRequest:
   def __init__(self, obj):
      self.SystemCode:str = obj["SystemCode"]
      self.TableName:str = obj["TableName"]
      pass

class Ice_Lib_MetaFX_EpMetaFxDefaultSearchResponse:
   def __init__(self, obj):
      self.FolderName:str = obj["FolderName"]
      self.SubfolderName:str = obj["SubfolderName"]
      pass

class Ice_Lib_MetaFX_EpMetaFxGenerateViewRequest:
   def __init__(self, obj):
      self.Type:str = obj["Type"]
      self.Id:str = obj["Id"]
      self.Company:str = obj["Company"]
      self.ProductId:str = obj["ProductId"]
      self.GlbCompany:str = obj["GlbCompany"]
      self.CgCCode:str = obj["CgCCode"]
      self.LayoutType:str = obj["LayoutType"]
      pass

class Ice_Lib_MetaFX_EpMetaFxGetLayersRequest:
   def __init__(self, obj):
      self.ViewId:str = obj["ViewId"]
      self.TypeCode:str = obj["TypeCode"]
      self.DeviceType:str = obj["DeviceType"]
      self.IncludeUnpublishedLayers:bool = obj["IncludeUnpublishedLayers"]
      pass

class Ice_Lib_MetaFX_EpMetaFxPeekRequest:
   def __init__(self, obj):
      self.like:str = obj["like"]
      self.properties:list[Ice_Lib_MetaFX_EpMetaFxPeekRequestProperty] = obj["properties"]
      pass

class Ice_Lib_MetaFX_EpMetaFxPeekRequestProperty:
   def __init__(self, obj):
      self.peekForm:str = obj["peekForm"]
      self.deviceType:str = obj["deviceType"]
      self.mode:str = obj["mode"]
      pass

class Ice_Lib_MetaFX_EpMetaFxResponse_Epicor_MetaFX_Core_Models_BAQReport_ReportResponse:
   def __init__(self, obj):
      self.Data:list[Epicor_MetaFX_Core_Models_BAQReport_ReportResponse] = obj["Data"]
      self.IsSuccess:bool = obj["IsSuccess"]
      self.Message:str = obj["Message"]
      self.Details:list[Ice_Lib_MetaFX_MessageDetail] = obj["Details"]
      pass

class Ice_Lib_MetaFX_EpMetaFxSearchRequest:
   def __init__(self, obj):
      self.like:str = obj["like"]
      self.properties:list[Ice_Lib_MetaFX_EpMetaFxSearchRequestProperty] = obj["properties"]
      pass

class Ice_Lib_MetaFX_EpMetaFxSearchRequestProperty:
   def __init__(self, obj):
      self.SearchForm:str = obj["SearchForm"]
      self.layers:str = obj["layers"]
      self.deviceType:str = obj["deviceType"]
      self.mode:str = obj["mode"]
      self.debug:bool = obj["debug"]
      pass

class Ice_Lib_MetaFX_MessageDetail:
   def __init__(self, obj):
      self.Message:str = obj["Message"]
      self.Type:str = obj["Type"]
      pass

class ImportApp_input:
   """ Required : 
   request
   """  
   def __init__(self, obj):
      self.request:list[Epicor_MetaFX_Core_Models_AppContent] = obj["request"]
      pass

class ImportApp_output:
   def __init__(self, obj):
      pass

class ImportLayers_input:
   """ Required : 
   fileContent
   """  
   def __init__(self, obj):
      self.fileContent:list[Epicor_MetaFX_Core_Models_ImportLayerRequest] = obj["fileContent"]
      pass

class ImportLayers_output:
   def __init__(self, obj):
      pass

class InvalidateCache_input:
   """ Required : 
   request
   """  
   def __init__(self, obj):
      self.request:list[Ice_Lib_MetaFX_EpMetaFxCacheInvalidateRequest] = obj["request"]
      pass

class InvalidateCache_output:
   def __init__(self, obj):
      pass

class PublishApp_input:
   """ Required : 
   request
   """  
   def __init__(self, obj):
      self.request:list[Epicor_MetaFX_Core_Models_EpMetaFxSaveRequestEx] = obj["request"]
      pass

class PublishApp_output:
   def __init__(self, obj):
      pass

class RestoreVersion_input:
   """ Required : 
   request
   """  
   def __init__(self, obj):
      self.request:list[Epicor_MetaFX_Core_Models_EpMetaFxRequest] = obj["request"]
      pass

class RestoreVersion_output:
   def __init__(self, obj):
      pass

class RunDataFixForLayers_input:
   """ Required : 
   request
   """  
   def __init__(self, obj):
      self.request:list[Epicor_MetaFX_Core_Models_EpMetaFXLayerFixRequest] = obj["request"]
      pass

class RunDataFixForLayers_output:
   def __init__(self, obj):
      pass

class SaveApp_input:
   """ Required : 
   request
   """  
   def __init__(self, obj):
      self.request:list[Epicor_MetaFX_Core_Models_EpMetaFxSaveRequestEx] = obj["request"]
      pass

class SaveApp_output:
   def __init__(self, obj):
      pass

class SetSecurityCodeForApplication_input:
   """ Required : 
   viewId
   securityCode
   """  
   def __init__(self, obj):
      self.viewId:str = obj["viewId"]
      """  viewId  """  
      self.securityCode:str = obj["securityCode"]
      """  securityCode  """  
      pass

class SetSecurityCodeForApplication_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      """  returns true if the update was successful  """  
      pass

class UpgradeLayer_input:
   """ Required : 
   request
   """  
   def __init__(self, obj):
      self.request:list[Epicor_MetaFX_Core_Models_MetaFxUpgradeLayerRequest] = obj["request"]
      pass

class UpgradeLayer_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      """  TRUE if upgrade is successful  """  
      pass

class Upgrade_input:
   """ Required : 
   request
   """  
   def __init__(self, obj):
      self.request:list[Epicor_MetaFX_Core_Models_EpMetaFxUpgradeSchemaRequest] = obj["request"]
      pass

class Upgrade_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      pass

