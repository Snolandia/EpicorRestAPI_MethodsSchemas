import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.ACTTypeSvc
# Description: ActType Business Object
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_ACTTypes(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ACTTypes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ACTTypes
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ACTTypeRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ACTTypes",headers=creds) as resp:
           return await resp.json()

async def post_ACTTypes(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ACTTypes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ACTTypeRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ACTTypeRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ACTTypes", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ACTTypes_Company_ACTTypeUID(Company, ACTTypeUID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ACTType item
   Description: Calls GetByID to retrieve the ACTType item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ACTType
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ACTTypeUID: Desc: ACTTypeUID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ACTTypeRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ACTTypes(" + Company + "," + ACTTypeUID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ACTTypes_Company_ACTTypeUID(Company, ACTTypeUID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ACTType for the service
   Description: Calls UpdateExt to update ACTType. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ACTType
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ACTTypeUID: Desc: ACTTypeUID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ACTTypeRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ACTTypes(" + Company + "," + ACTTypeUID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ACTTypes_Company_ACTTypeUID(Company, ACTTypeUID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ACTType item
   Description: Call UpdateExt to delete ACTType item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ACTType
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ACTTypeUID: Desc: ACTTypeUID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ACTTypes(" + Company + "," + ACTTypeUID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ACTTypes_Company_ACTTypeUID_ACTRevisions(Company, ACTTypeUID, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ACTRevisions items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ACTRevisions1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ACTTypeUID: Desc: ACTTypeUID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ACTRevisionRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ACTTypes(" + Company + "," + ACTTypeUID + ")/ACTRevisions",headers=creds) as resp:
           return await resp.json()

async def get_ACTTypes_Company_ACTTypeUID_ACTRevisions_Company_ACTTypeUID_ACTRevisionUID(Company, ACTTypeUID, ACTRevisionUID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ACTRevision item
   Description: Calls GetByID to retrieve the ACTRevision item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ACTRevision1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ACTTypeUID: Desc: ACTTypeUID   Required: True
      :param ACTRevisionUID: Desc: ACTRevisionUID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ACTRevisionRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ACTTypes(" + Company + "," + ACTTypeUID + ")/ACTRevisions(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ACTRevisions(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ACTRevisions items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ACTRevisions
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ACTRevisionRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ACTRevisions",headers=creds) as resp:
           return await resp.json()

async def post_ACTRevisions(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ACTRevisions
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ACTRevisionRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ACTRevisionRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ACTRevisions", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ACTRevisions_Company_ACTTypeUID_ACTRevisionUID(Company, ACTTypeUID, ACTRevisionUID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ACTRevision item
   Description: Calls GetByID to retrieve the ACTRevision item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ACTRevision
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ACTTypeUID: Desc: ACTTypeUID   Required: True
      :param ACTRevisionUID: Desc: ACTRevisionUID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ACTRevisionRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ACTRevisions(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ACTRevisions_Company_ACTTypeUID_ACTRevisionUID(Company, ACTTypeUID, ACTRevisionUID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ACTRevision for the service
   Description: Calls UpdateExt to update ACTRevision. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ACTRevision
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ACTTypeUID: Desc: ACTTypeUID   Required: True
      :param ACTRevisionUID: Desc: ACTRevisionUID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ACTRevisionRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ACTRevisions(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ACTRevisions_Company_ACTTypeUID_ACTRevisionUID(Company, ACTTypeUID, ACTRevisionUID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ACTRevision item
   Description: Call UpdateExt to delete ACTRevision item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ACTRevision
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ACTTypeUID: Desc: ACTTypeUID   Required: True
      :param ACTRevisionUID: Desc: ACTRevisionUID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ACTRevisions(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ACTRevisions_Company_ACTTypeUID_ACTRevisionUID_ABTDocLines(Company, ACTTypeUID, ACTRevisionUID, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ABTDocLines items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ABTDocLines1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ACTTypeUID: Desc: ACTTypeUID   Required: True
      :param ACTRevisionUID: Desc: ACTRevisionUID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ABTDocLineRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ACTRevisions(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + ")/ABTDocLines",headers=creds) as resp:
           return await resp.json()

async def get_ACTRevisions_Company_ACTTypeUID_ACTRevisionUID_ABTDocLines_Company_ACTTypeUID_ACTRevisionUID_ABTDocLineUID(Company, ACTTypeUID, ACTRevisionUID, ABTDocLineUID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ABTDocLine item
   Description: Calls GetByID to retrieve the ABTDocLine item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ABTDocLine1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ACTTypeUID: Desc: ACTTypeUID   Required: True
      :param ACTRevisionUID: Desc: ACTRevisionUID   Required: True
      :param ABTDocLineUID: Desc: ABTDocLineUID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ABTDocLineRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ACTRevisions(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + ")/ABTDocLines(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + ABTDocLineUID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ACTRevisions_Company_ACTTypeUID_ACTRevisionUID_ACTBooks(Company, ACTTypeUID, ACTRevisionUID, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ACTBooks items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ACTBooks1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ACTTypeUID: Desc: ACTTypeUID   Required: True
      :param ACTRevisionUID: Desc: ACTRevisionUID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ACTBookRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ACTRevisions(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + ")/ACTBooks",headers=creds) as resp:
           return await resp.json()

async def get_ACTRevisions_Company_ACTTypeUID_ACTRevisionUID_ACTBooks_Company_ACTTypeUID_ACTRevisionUID_BookID(Company, ACTTypeUID, ACTRevisionUID, BookID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ACTBook item
   Description: Calls GetByID to retrieve the ACTBook item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ACTBook1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ACTTypeUID: Desc: ACTTypeUID   Required: True
      :param ACTRevisionUID: Desc: ACTRevisionUID   Required: True
      :param BookID: Desc: BookID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ACTBookRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ACTRevisions(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + ")/ACTBooks(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + BookID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ABTDocLines(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ABTDocLines items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ABTDocLines
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ABTDocLineRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ABTDocLines",headers=creds) as resp:
           return await resp.json()

async def post_ABTDocLines(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ABTDocLines
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ABTDocLineRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ABTDocLineRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ABTDocLines", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ABTDocLines_Company_ACTTypeUID_ACTRevisionUID_ABTDocLineUID(Company, ACTTypeUID, ACTRevisionUID, ABTDocLineUID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ABTDocLine item
   Description: Calls GetByID to retrieve the ABTDocLine item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ABTDocLine
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ACTTypeUID: Desc: ACTTypeUID   Required: True
      :param ACTRevisionUID: Desc: ACTRevisionUID   Required: True
      :param ABTDocLineUID: Desc: ABTDocLineUID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ABTDocLineRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ABTDocLines(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + ABTDocLineUID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ABTDocLines_Company_ACTTypeUID_ACTRevisionUID_ABTDocLineUID(Company, ACTTypeUID, ACTRevisionUID, ABTDocLineUID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ABTDocLine for the service
   Description: Calls UpdateExt to update ABTDocLine. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ABTDocLine
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ACTTypeUID: Desc: ACTTypeUID   Required: True
      :param ACTRevisionUID: Desc: ACTRevisionUID   Required: True
      :param ABTDocLineUID: Desc: ABTDocLineUID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ABTDocLineRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ABTDocLines(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + ABTDocLineUID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ABTDocLines_Company_ACTTypeUID_ACTRevisionUID_ABTDocLineUID(Company, ACTTypeUID, ACTRevisionUID, ABTDocLineUID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ABTDocLine item
   Description: Call UpdateExt to delete ABTDocLine item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ABTDocLine
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ACTTypeUID: Desc: ACTTypeUID   Required: True
      :param ACTRevisionUID: Desc: ACTRevisionUID   Required: True
      :param ABTDocLineUID: Desc: ABTDocLineUID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ABTDocLines(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + ABTDocLineUID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ABTDocLines_Company_ACTTypeUID_ACTRevisionUID_ABTDocLineUID_ABTAmounts(Company, ACTTypeUID, ACTRevisionUID, ABTDocLineUID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ABTAmounts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ABTAmounts1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ACTTypeUID: Desc: ACTTypeUID   Required: True
      :param ACTRevisionUID: Desc: ACTRevisionUID   Required: True
      :param ABTDocLineUID: Desc: ABTDocLineUID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ABTAmountRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ABTDocLines(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + ABTDocLineUID + ")/ABTAmounts",headers=creds) as resp:
           return await resp.json()

async def get_ABTDocLines_Company_ACTTypeUID_ACTRevisionUID_ABTDocLineUID_ABTAmounts_Company_ACTTypeUID_ACTRevisionUID_ABTDocLineUID_ABTAmountUID(Company, ACTTypeUID, ACTRevisionUID, ABTDocLineUID, ABTAmountUID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ABTAmount item
   Description: Calls GetByID to retrieve the ABTAmount item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ABTAmount1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ACTTypeUID: Desc: ACTTypeUID   Required: True
      :param ACTRevisionUID: Desc: ACTRevisionUID   Required: True
      :param ABTDocLineUID: Desc: ABTDocLineUID   Required: True
      :param ABTAmountUID: Desc: ABTAmountUID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ABTAmountRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ABTDocLines(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + ABTDocLineUID + ")/ABTAmounts(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + ABTDocLineUID + "," + ABTAmountUID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ABTDocLines_Company_ACTTypeUID_ACTRevisionUID_ABTDocLineUID_ABTPostEntities(Company, ACTTypeUID, ACTRevisionUID, ABTDocLineUID, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ABTPostEntities items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ABTPostEntities1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ACTTypeUID: Desc: ACTTypeUID   Required: True
      :param ACTRevisionUID: Desc: ACTRevisionUID   Required: True
      :param ABTDocLineUID: Desc: ABTDocLineUID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ABTPostEntityRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ABTDocLines(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + ABTDocLineUID + ")/ABTPostEntities",headers=creds) as resp:
           return await resp.json()

async def get_ABTDocLines_Company_ACTTypeUID_ACTRevisionUID_ABTDocLineUID_ABTPostEntities_Company_ACTTypeUID_ACTRevisionUID_ABTDocLineUID_ABTPostEntityUID(Company, ACTTypeUID, ACTRevisionUID, ABTDocLineUID, ABTPostEntityUID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ABTPostEntity item
   Description: Calls GetByID to retrieve the ABTPostEntity item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ABTPostEntity1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ACTTypeUID: Desc: ACTTypeUID   Required: True
      :param ACTRevisionUID: Desc: ACTRevisionUID   Required: True
      :param ABTDocLineUID: Desc: ABTDocLineUID   Required: True
      :param ABTPostEntityUID: Desc: ABTPostEntityUID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ABTPostEntityRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ABTDocLines(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + ABTDocLineUID + ")/ABTPostEntities(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + ABTDocLineUID + "," + ABTPostEntityUID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ABTDocLines_Company_ACTTypeUID_ACTRevisionUID_ABTDocLineUID_ABTQueries(Company, ACTTypeUID, ACTRevisionUID, ABTDocLineUID, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ABTQueries items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ABTQueries1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ACTTypeUID: Desc: ACTTypeUID   Required: True
      :param ACTRevisionUID: Desc: ACTRevisionUID   Required: True
      :param ABTDocLineUID: Desc: ABTDocLineUID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ABTQueryRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ABTDocLines(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + ABTDocLineUID + ")/ABTQueries",headers=creds) as resp:
           return await resp.json()

async def get_ABTDocLines_Company_ACTTypeUID_ACTRevisionUID_ABTDocLineUID_ABTQueries_Company_ACTTypeUID_ACTRevisionUID_ABTDocLineUID_ABTQueryUID(Company, ACTTypeUID, ACTRevisionUID, ABTDocLineUID, ABTQueryUID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ABTQuery item
   Description: Calls GetByID to retrieve the ABTQuery item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ABTQuery1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ACTTypeUID: Desc: ACTTypeUID   Required: True
      :param ACTRevisionUID: Desc: ACTRevisionUID   Required: True
      :param ABTDocLineUID: Desc: ABTDocLineUID   Required: True
      :param ABTQueryUID: Desc: ABTQueryUID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ABTQueryRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ABTDocLines(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + ABTDocLineUID + ")/ABTQueries(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + ABTDocLineUID + "," + ABTQueryUID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ABTAmounts(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ABTAmounts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ABTAmounts
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ABTAmountRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ABTAmounts",headers=creds) as resp:
           return await resp.json()

async def post_ABTAmounts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ABTAmounts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ABTAmountRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ABTAmountRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ABTAmounts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ABTAmounts_Company_ACTTypeUID_ACTRevisionUID_ABTDocLineUID_ABTAmountUID(Company, ACTTypeUID, ACTRevisionUID, ABTDocLineUID, ABTAmountUID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ABTAmount item
   Description: Calls GetByID to retrieve the ABTAmount item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ABTAmount
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ACTTypeUID: Desc: ACTTypeUID   Required: True
      :param ACTRevisionUID: Desc: ACTRevisionUID   Required: True
      :param ABTDocLineUID: Desc: ABTDocLineUID   Required: True
      :param ABTAmountUID: Desc: ABTAmountUID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ABTAmountRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ABTAmounts(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + ABTDocLineUID + "," + ABTAmountUID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ABTAmounts_Company_ACTTypeUID_ACTRevisionUID_ABTDocLineUID_ABTAmountUID(Company, ACTTypeUID, ACTRevisionUID, ABTDocLineUID, ABTAmountUID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ABTAmount for the service
   Description: Calls UpdateExt to update ABTAmount. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ABTAmount
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ACTTypeUID: Desc: ACTTypeUID   Required: True
      :param ACTRevisionUID: Desc: ACTRevisionUID   Required: True
      :param ABTDocLineUID: Desc: ABTDocLineUID   Required: True
      :param ABTAmountUID: Desc: ABTAmountUID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ABTAmountRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ABTAmounts(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + ABTDocLineUID + "," + ABTAmountUID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ABTAmounts_Company_ACTTypeUID_ACTRevisionUID_ABTDocLineUID_ABTAmountUID(Company, ACTTypeUID, ACTRevisionUID, ABTDocLineUID, ABTAmountUID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ABTAmount item
   Description: Call UpdateExt to delete ABTAmount item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ABTAmount
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ACTTypeUID: Desc: ACTTypeUID   Required: True
      :param ACTRevisionUID: Desc: ACTRevisionUID   Required: True
      :param ABTDocLineUID: Desc: ABTDocLineUID   Required: True
      :param ABTAmountUID: Desc: ABTAmountUID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ABTAmounts(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + ABTDocLineUID + "," + ABTAmountUID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ABTPostEntities(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ABTPostEntities items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ABTPostEntities
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ABTPostEntityRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ABTPostEntities",headers=creds) as resp:
           return await resp.json()

async def post_ABTPostEntities(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ABTPostEntities
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ABTPostEntityRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ABTPostEntityRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ABTPostEntities", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ABTPostEntities_Company_ACTTypeUID_ACTRevisionUID_ABTDocLineUID_ABTPostEntityUID(Company, ACTTypeUID, ACTRevisionUID, ABTDocLineUID, ABTPostEntityUID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ABTPostEntity item
   Description: Calls GetByID to retrieve the ABTPostEntity item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ABTPostEntity
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ACTTypeUID: Desc: ACTTypeUID   Required: True
      :param ACTRevisionUID: Desc: ACTRevisionUID   Required: True
      :param ABTDocLineUID: Desc: ABTDocLineUID   Required: True
      :param ABTPostEntityUID: Desc: ABTPostEntityUID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ABTPostEntityRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ABTPostEntities(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + ABTDocLineUID + "," + ABTPostEntityUID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ABTPostEntities_Company_ACTTypeUID_ACTRevisionUID_ABTDocLineUID_ABTPostEntityUID(Company, ACTTypeUID, ACTRevisionUID, ABTDocLineUID, ABTPostEntityUID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ABTPostEntity for the service
   Description: Calls UpdateExt to update ABTPostEntity. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ABTPostEntity
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ACTTypeUID: Desc: ACTTypeUID   Required: True
      :param ACTRevisionUID: Desc: ACTRevisionUID   Required: True
      :param ABTDocLineUID: Desc: ABTDocLineUID   Required: True
      :param ABTPostEntityUID: Desc: ABTPostEntityUID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ABTPostEntityRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ABTPostEntities(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + ABTDocLineUID + "," + ABTPostEntityUID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ABTPostEntities_Company_ACTTypeUID_ACTRevisionUID_ABTDocLineUID_ABTPostEntityUID(Company, ACTTypeUID, ACTRevisionUID, ABTDocLineUID, ABTPostEntityUID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ABTPostEntity item
   Description: Call UpdateExt to delete ABTPostEntity item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ABTPostEntity
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ACTTypeUID: Desc: ACTTypeUID   Required: True
      :param ACTRevisionUID: Desc: ACTRevisionUID   Required: True
      :param ABTDocLineUID: Desc: ABTDocLineUID   Required: True
      :param ABTPostEntityUID: Desc: ABTPostEntityUID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ABTPostEntities(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + ABTDocLineUID + "," + ABTPostEntityUID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ABTPostEntities_Company_ACTTypeUID_ACTRevisionUID_ABTDocLineUID_ABTPostEntityUID_ABTPostCodes(Company, ACTTypeUID, ACTRevisionUID, ABTDocLineUID, ABTPostEntityUID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ABTPostCodes items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ABTPostCodes1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ACTTypeUID: Desc: ACTTypeUID   Required: True
      :param ACTRevisionUID: Desc: ACTRevisionUID   Required: True
      :param ABTDocLineUID: Desc: ABTDocLineUID   Required: True
      :param ABTPostEntityUID: Desc: ABTPostEntityUID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ABTPostCodeRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ABTPostEntities(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + ABTDocLineUID + "," + ABTPostEntityUID + ")/ABTPostCodes",headers=creds) as resp:
           return await resp.json()

async def get_ABTPostEntities_Company_ACTTypeUID_ACTRevisionUID_ABTDocLineUID_ABTPostEntityUID_ABTPostCodes_Company_ACTTypeUID_ACTRevisionUID_ABTDocLineUID_ABTPostEntityUID_ABTPostCodeUID(Company, ACTTypeUID, ACTRevisionUID, ABTDocLineUID, ABTPostEntityUID, ABTPostCodeUID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ABTPostCode item
   Description: Calls GetByID to retrieve the ABTPostCode item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ABTPostCode1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ACTTypeUID: Desc: ACTTypeUID   Required: True
      :param ACTRevisionUID: Desc: ACTRevisionUID   Required: True
      :param ABTDocLineUID: Desc: ABTDocLineUID   Required: True
      :param ABTPostEntityUID: Desc: ABTPostEntityUID   Required: True
      :param ABTPostCodeUID: Desc: ABTPostCodeUID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ABTPostCodeRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ABTPostEntities(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + ABTDocLineUID + "," + ABTPostEntityUID + ")/ABTPostCodes(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + ABTDocLineUID + "," + ABTPostEntityUID + "," + ABTPostCodeUID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ABTPostCodes(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ABTPostCodes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ABTPostCodes
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ABTPostCodeRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ABTPostCodes",headers=creds) as resp:
           return await resp.json()

async def post_ABTPostCodes(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ABTPostCodes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ABTPostCodeRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ABTPostCodeRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ABTPostCodes", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ABTPostCodes_Company_ACTTypeUID_ACTRevisionUID_ABTDocLineUID_ABTPostEntityUID_ABTPostCodeUID(Company, ACTTypeUID, ACTRevisionUID, ABTDocLineUID, ABTPostEntityUID, ABTPostCodeUID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ABTPostCode item
   Description: Calls GetByID to retrieve the ABTPostCode item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ABTPostCode
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ACTTypeUID: Desc: ACTTypeUID   Required: True
      :param ACTRevisionUID: Desc: ACTRevisionUID   Required: True
      :param ABTDocLineUID: Desc: ABTDocLineUID   Required: True
      :param ABTPostEntityUID: Desc: ABTPostEntityUID   Required: True
      :param ABTPostCodeUID: Desc: ABTPostCodeUID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ABTPostCodeRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ABTPostCodes(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + ABTDocLineUID + "," + ABTPostEntityUID + "," + ABTPostCodeUID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ABTPostCodes_Company_ACTTypeUID_ACTRevisionUID_ABTDocLineUID_ABTPostEntityUID_ABTPostCodeUID(Company, ACTTypeUID, ACTRevisionUID, ABTDocLineUID, ABTPostEntityUID, ABTPostCodeUID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ABTPostCode for the service
   Description: Calls UpdateExt to update ABTPostCode. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ABTPostCode
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ACTTypeUID: Desc: ACTTypeUID   Required: True
      :param ACTRevisionUID: Desc: ACTRevisionUID   Required: True
      :param ABTDocLineUID: Desc: ABTDocLineUID   Required: True
      :param ABTPostEntityUID: Desc: ABTPostEntityUID   Required: True
      :param ABTPostCodeUID: Desc: ABTPostCodeUID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ABTPostCodeRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ABTPostCodes(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + ABTDocLineUID + "," + ABTPostEntityUID + "," + ABTPostCodeUID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ABTPostCodes_Company_ACTTypeUID_ACTRevisionUID_ABTDocLineUID_ABTPostEntityUID_ABTPostCodeUID(Company, ACTTypeUID, ACTRevisionUID, ABTDocLineUID, ABTPostEntityUID, ABTPostCodeUID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ABTPostCode item
   Description: Call UpdateExt to delete ABTPostCode item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ABTPostCode
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ACTTypeUID: Desc: ACTTypeUID   Required: True
      :param ACTRevisionUID: Desc: ACTRevisionUID   Required: True
      :param ABTDocLineUID: Desc: ABTDocLineUID   Required: True
      :param ABTPostEntityUID: Desc: ABTPostEntityUID   Required: True
      :param ABTPostCodeUID: Desc: ABTPostCodeUID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ABTPostCodes(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + ABTDocLineUID + "," + ABTPostEntityUID + "," + ABTPostCodeUID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ABTQueries(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ABTQueries items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ABTQueries
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ABTQueryRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ABTQueries",headers=creds) as resp:
           return await resp.json()

async def post_ABTQueries(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ABTQueries
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ABTQueryRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ABTQueryRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ABTQueries", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ABTQueries_Company_ACTTypeUID_ACTRevisionUID_ABTDocLineUID_ABTQueryUID(Company, ACTTypeUID, ACTRevisionUID, ABTDocLineUID, ABTQueryUID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ABTQuery item
   Description: Calls GetByID to retrieve the ABTQuery item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ABTQuery
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ACTTypeUID: Desc: ACTTypeUID   Required: True
      :param ACTRevisionUID: Desc: ACTRevisionUID   Required: True
      :param ABTDocLineUID: Desc: ABTDocLineUID   Required: True
      :param ABTQueryUID: Desc: ABTQueryUID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ABTQueryRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ABTQueries(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + ABTDocLineUID + "," + ABTQueryUID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ABTQueries_Company_ACTTypeUID_ACTRevisionUID_ABTDocLineUID_ABTQueryUID(Company, ACTTypeUID, ACTRevisionUID, ABTDocLineUID, ABTQueryUID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ABTQuery for the service
   Description: Calls UpdateExt to update ABTQuery. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ABTQuery
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ACTTypeUID: Desc: ACTTypeUID   Required: True
      :param ACTRevisionUID: Desc: ACTRevisionUID   Required: True
      :param ABTDocLineUID: Desc: ABTDocLineUID   Required: True
      :param ABTQueryUID: Desc: ABTQueryUID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ABTQueryRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ABTQueries(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + ABTDocLineUID + "," + ABTQueryUID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ABTQueries_Company_ACTTypeUID_ACTRevisionUID_ABTDocLineUID_ABTQueryUID(Company, ACTTypeUID, ACTRevisionUID, ABTDocLineUID, ABTQueryUID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ABTQuery item
   Description: Call UpdateExt to delete ABTQuery item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ABTQuery
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ACTTypeUID: Desc: ACTTypeUID   Required: True
      :param ACTRevisionUID: Desc: ACTRevisionUID   Required: True
      :param ABTDocLineUID: Desc: ABTDocLineUID   Required: True
      :param ABTQueryUID: Desc: ABTQueryUID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ABTQueries(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + ABTDocLineUID + "," + ABTQueryUID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ABTQueries_Company_ACTTypeUID_ACTRevisionUID_ABTDocLineUID_ABTQueryUID_ABTQParams(Company, ACTTypeUID, ACTRevisionUID, ABTDocLineUID, ABTQueryUID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ABTQParams items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ABTQParams1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ACTTypeUID: Desc: ACTTypeUID   Required: True
      :param ACTRevisionUID: Desc: ACTRevisionUID   Required: True
      :param ABTDocLineUID: Desc: ABTDocLineUID   Required: True
      :param ABTQueryUID: Desc: ABTQueryUID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ABTQParamRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ABTQueries(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + ABTDocLineUID + "," + ABTQueryUID + ")/ABTQParams",headers=creds) as resp:
           return await resp.json()

async def get_ABTQueries_Company_ACTTypeUID_ACTRevisionUID_ABTDocLineUID_ABTQueryUID_ABTQParams_Company_ACTTypeUID_ACTRevisionUID_ABTDocLineUID_ABTQueryUID_BAQParamLinkUID(Company, ACTTypeUID, ACTRevisionUID, ABTDocLineUID, ABTQueryUID, BAQParamLinkUID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ABTQParam item
   Description: Calls GetByID to retrieve the ABTQParam item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ABTQParam1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ACTTypeUID: Desc: ACTTypeUID   Required: True
      :param ACTRevisionUID: Desc: ACTRevisionUID   Required: True
      :param ABTDocLineUID: Desc: ABTDocLineUID   Required: True
      :param ABTQueryUID: Desc: ABTQueryUID   Required: True
      :param BAQParamLinkUID: Desc: BAQParamLinkUID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ABTQParamRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ABTQueries(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + ABTDocLineUID + "," + ABTQueryUID + ")/ABTQParams(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + ABTDocLineUID + "," + ABTQueryUID + "," + BAQParamLinkUID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ABTQParams(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ABTQParams items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ABTQParams
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ABTQParamRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ABTQParams",headers=creds) as resp:
           return await resp.json()

async def post_ABTQParams(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ABTQParams
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ABTQParamRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ABTQParamRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ABTQParams", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ABTQParams_Company_ACTTypeUID_ACTRevisionUID_ABTDocLineUID_ABTQueryUID_BAQParamLinkUID(Company, ACTTypeUID, ACTRevisionUID, ABTDocLineUID, ABTQueryUID, BAQParamLinkUID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ABTQParam item
   Description: Calls GetByID to retrieve the ABTQParam item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ABTQParam
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ACTTypeUID: Desc: ACTTypeUID   Required: True
      :param ACTRevisionUID: Desc: ACTRevisionUID   Required: True
      :param ABTDocLineUID: Desc: ABTDocLineUID   Required: True
      :param ABTQueryUID: Desc: ABTQueryUID   Required: True
      :param BAQParamLinkUID: Desc: BAQParamLinkUID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ABTQParamRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ABTQParams(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + ABTDocLineUID + "," + ABTQueryUID + "," + BAQParamLinkUID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ABTQParams_Company_ACTTypeUID_ACTRevisionUID_ABTDocLineUID_ABTQueryUID_BAQParamLinkUID(Company, ACTTypeUID, ACTRevisionUID, ABTDocLineUID, ABTQueryUID, BAQParamLinkUID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ABTQParam for the service
   Description: Calls UpdateExt to update ABTQParam. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ABTQParam
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ACTTypeUID: Desc: ACTTypeUID   Required: True
      :param ACTRevisionUID: Desc: ACTRevisionUID   Required: True
      :param ABTDocLineUID: Desc: ABTDocLineUID   Required: True
      :param ABTQueryUID: Desc: ABTQueryUID   Required: True
      :param BAQParamLinkUID: Desc: BAQParamLinkUID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ABTQParamRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ABTQParams(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + ABTDocLineUID + "," + ABTQueryUID + "," + BAQParamLinkUID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ABTQParams_Company_ACTTypeUID_ACTRevisionUID_ABTDocLineUID_ABTQueryUID_BAQParamLinkUID(Company, ACTTypeUID, ACTRevisionUID, ABTDocLineUID, ABTQueryUID, BAQParamLinkUID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ABTQParam item
   Description: Call UpdateExt to delete ABTQParam item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ABTQParam
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ACTTypeUID: Desc: ACTTypeUID   Required: True
      :param ACTRevisionUID: Desc: ACTRevisionUID   Required: True
      :param ABTDocLineUID: Desc: ABTDocLineUID   Required: True
      :param ABTQueryUID: Desc: ABTQueryUID   Required: True
      :param BAQParamLinkUID: Desc: BAQParamLinkUID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ABTQParams(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + ABTDocLineUID + "," + ABTQueryUID + "," + BAQParamLinkUID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ACTBooks(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ACTBooks items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ACTBooks
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ACTBookRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ACTBooks",headers=creds) as resp:
           return await resp.json()

async def post_ACTBooks(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ACTBooks
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ACTBookRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ACTBookRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ACTBooks", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ACTBooks_Company_ACTTypeUID_ACTRevisionUID_BookID(Company, ACTTypeUID, ACTRevisionUID, BookID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ACTBook item
   Description: Calls GetByID to retrieve the ACTBook item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ACTBook
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ACTTypeUID: Desc: ACTTypeUID   Required: True
      :param ACTRevisionUID: Desc: ACTRevisionUID   Required: True
      :param BookID: Desc: BookID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ACTBookRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ACTBooks(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + BookID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ACTBooks_Company_ACTTypeUID_ACTRevisionUID_BookID(Company, ACTTypeUID, ACTRevisionUID, BookID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ACTBook for the service
   Description: Calls UpdateExt to update ACTBook. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ACTBook
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ACTTypeUID: Desc: ACTTypeUID   Required: True
      :param ACTRevisionUID: Desc: ACTRevisionUID   Required: True
      :param BookID: Desc: BookID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ACTBookRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ACTBooks(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + BookID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ACTBooks_Company_ACTTypeUID_ACTRevisionUID_BookID(Company, ACTTypeUID, ACTRevisionUID, BookID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ACTBook item
   Description: Call UpdateExt to delete ACTBook item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ACTBook
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ACTTypeUID: Desc: ACTTypeUID   Required: True
      :param ACTRevisionUID: Desc: ACTRevisionUID   Required: True
      :param BookID: Desc: BookID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ACTBooks(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + BookID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ACTBooks_Company_ACTTypeUID_ACTRevisionUID_BookID_BookingRules(Company, ACTTypeUID, ACTRevisionUID, BookID, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get BookingRules items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_BookingRules1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ACTTypeUID: Desc: ACTTypeUID   Required: True
      :param ACTRevisionUID: Desc: ACTRevisionUID   Required: True
      :param BookID: Desc: BookID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BookingRuleRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ACTBooks(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + BookID + ")/BookingRules",headers=creds) as resp:
           return await resp.json()

async def get_ACTBooks_Company_ACTTypeUID_ACTRevisionUID_BookID_BookingRules_Company_ACTTypeUID_ACTRevisionUID_BookID_RuleUID(Company, ACTTypeUID, ACTRevisionUID, BookID, RuleUID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the BookingRule item
   Description: Calls GetByID to retrieve the BookingRule item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BookingRule1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ACTTypeUID: Desc: ACTTypeUID   Required: True
      :param ACTRevisionUID: Desc: ACTRevisionUID   Required: True
      :param BookID: Desc: BookID   Required: True   Allow empty value : True
      :param RuleUID: Desc: RuleUID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.BookingRuleRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ACTBooks(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + BookID + ")/BookingRules(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + BookID + "," + RuleUID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ACTBooks_Company_ACTTypeUID_ACTRevisionUID_BookID_BRFunctions(Company, ACTTypeUID, ACTRevisionUID, BookID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get BRFunctions items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_BRFunctions1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ACTTypeUID: Desc: ACTTypeUID   Required: True
      :param ACTRevisionUID: Desc: ACTRevisionUID   Required: True
      :param BookID: Desc: BookID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BRFunctionRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ACTBooks(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + BookID + ")/BRFunctions",headers=creds) as resp:
           return await resp.json()

async def get_ACTBooks_Company_ACTTypeUID_ACTRevisionUID_BookID_BRFunctions_Company_ACTTypeUID_ACTRevisionUID_BookID_FunctionUID(Company, ACTTypeUID, ACTRevisionUID, BookID, FunctionUID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the BRFunction item
   Description: Calls GetByID to retrieve the BRFunction item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BRFunction1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ACTTypeUID: Desc: ACTTypeUID   Required: True
      :param ACTRevisionUID: Desc: ACTRevisionUID   Required: True
      :param BookID: Desc: BookID   Required: True   Allow empty value : True
      :param FunctionUID: Desc: FunctionUID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.BRFunctionRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ACTBooks(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + BookID + ")/BRFunctions(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + BookID + "," + FunctionUID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ACTBooks_Company_ACTTypeUID_ACTRevisionUID_BookID_BookVars(Company, ACTTypeUID, ACTRevisionUID, BookID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get BookVars items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_BookVars1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ACTTypeUID: Desc: ACTTypeUID   Required: True
      :param ACTRevisionUID: Desc: ACTRevisionUID   Required: True
      :param BookID: Desc: BookID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BookVarRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ACTBooks(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + BookID + ")/BookVars",headers=creds) as resp:
           return await resp.json()

async def get_ACTBooks_Company_ACTTypeUID_ACTRevisionUID_BookID_BookVars_Company_ACTTypeUID_ACTRevisionUID_BookID_BookVarUID(Company, ACTTypeUID, ACTRevisionUID, BookID, BookVarUID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the BookVar item
   Description: Calls GetByID to retrieve the BookVar item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BookVar1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ACTTypeUID: Desc: ACTTypeUID   Required: True
      :param ACTRevisionUID: Desc: ACTRevisionUID   Required: True
      :param BookID: Desc: BookID   Required: True   Allow empty value : True
      :param BookVarUID: Desc: BookVarUID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.BookVarRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ACTBooks(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + BookID + ")/BookVars(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + BookID + "," + BookVarUID + ")",headers=creds) as resp:
           return await resp.json()

async def get_BookingRules(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get BookingRules items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_BookingRules
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BookingRuleRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/BookingRules",headers=creds) as resp:
           return await resp.json()

async def post_BookingRules(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_BookingRules
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.BookingRuleRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.BookingRuleRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/BookingRules", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_BookingRules_Company_ACTTypeUID_ACTRevisionUID_BookID_RuleUID(Company, ACTTypeUID, ACTRevisionUID, BookID, RuleUID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the BookingRule item
   Description: Calls GetByID to retrieve the BookingRule item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BookingRule
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ACTTypeUID: Desc: ACTTypeUID   Required: True
      :param ACTRevisionUID: Desc: ACTRevisionUID   Required: True
      :param BookID: Desc: BookID   Required: True   Allow empty value : True
      :param RuleUID: Desc: RuleUID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.BookingRuleRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/BookingRules(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + BookID + "," + RuleUID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_BookingRules_Company_ACTTypeUID_ACTRevisionUID_BookID_RuleUID(Company, ACTTypeUID, ACTRevisionUID, BookID, RuleUID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update BookingRule for the service
   Description: Calls UpdateExt to update BookingRule. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_BookingRule
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ACTTypeUID: Desc: ACTTypeUID   Required: True
      :param ACTRevisionUID: Desc: ACTRevisionUID   Required: True
      :param BookID: Desc: BookID   Required: True   Allow empty value : True
      :param RuleUID: Desc: RuleUID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.BookingRuleRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/BookingRules(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + BookID + "," + RuleUID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_BookingRules_Company_ACTTypeUID_ACTRevisionUID_BookID_RuleUID(Company, ACTTypeUID, ACTRevisionUID, BookID, RuleUID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete BookingRule item
   Description: Call UpdateExt to delete BookingRule item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_BookingRule
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ACTTypeUID: Desc: ACTTypeUID   Required: True
      :param ACTRevisionUID: Desc: ACTRevisionUID   Required: True
      :param BookID: Desc: BookID   Required: True   Allow empty value : True
      :param RuleUID: Desc: RuleUID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/BookingRules(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + BookID + "," + RuleUID + ")",headers=creds) as resp:
           return await resp.json()

async def get_BookingRules_Company_ACTTypeUID_ACTRevisionUID_BookID_RuleUID_BookValRules(Company, ACTTypeUID, ACTRevisionUID, BookID, RuleUID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get BookValRules items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_BookValRules1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ACTTypeUID: Desc: ACTTypeUID   Required: True
      :param ACTRevisionUID: Desc: ACTRevisionUID   Required: True
      :param BookID: Desc: BookID   Required: True   Allow empty value : True
      :param RuleUID: Desc: RuleUID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BookValRuleRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/BookingRules(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + BookID + "," + RuleUID + ")/BookValRules",headers=creds) as resp:
           return await resp.json()

async def get_BookingRules_Company_ACTTypeUID_ACTRevisionUID_BookID_RuleUID_BookValRules_Company_ACTTypeUID_ACTRevisionUID_BookID_RuleUID_VRuleUID(Company, ACTTypeUID, ACTRevisionUID, BookID, RuleUID, VRuleUID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the BookValRule item
   Description: Calls GetByID to retrieve the BookValRule item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BookValRule1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ACTTypeUID: Desc: ACTTypeUID   Required: True
      :param ACTRevisionUID: Desc: ACTRevisionUID   Required: True
      :param BookID: Desc: BookID   Required: True   Allow empty value : True
      :param RuleUID: Desc: RuleUID   Required: True
      :param VRuleUID: Desc: VRuleUID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.BookValRuleRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/BookingRules(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + BookID + "," + RuleUID + ")/BookValRules(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + BookID + "," + RuleUID + "," + VRuleUID + ")",headers=creds) as resp:
           return await resp.json()

async def get_BookingRules_Company_ACTTypeUID_ACTRevisionUID_BookID_RuleUID_BROperations(Company, ACTTypeUID, ACTRevisionUID, BookID, RuleUID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get BROperations items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_BROperations1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ACTTypeUID: Desc: ACTTypeUID   Required: True
      :param ACTRevisionUID: Desc: ACTRevisionUID   Required: True
      :param BookID: Desc: BookID   Required: True   Allow empty value : True
      :param RuleUID: Desc: RuleUID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BROperationRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/BookingRules(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + BookID + "," + RuleUID + ")/BROperations",headers=creds) as resp:
           return await resp.json()

async def get_BookingRules_Company_ACTTypeUID_ACTRevisionUID_BookID_RuleUID_BROperations_Company_ACTTypeUID_ACTRevisionUID_BookID_RuleUID_OperationUID(Company, ACTTypeUID, ACTRevisionUID, BookID, RuleUID, OperationUID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the BROperation item
   Description: Calls GetByID to retrieve the BROperation item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BROperation1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ACTTypeUID: Desc: ACTTypeUID   Required: True
      :param ACTRevisionUID: Desc: ACTRevisionUID   Required: True
      :param BookID: Desc: BookID   Required: True   Allow empty value : True
      :param RuleUID: Desc: RuleUID   Required: True
      :param OperationUID: Desc: OperationUID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.BROperationRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/BookingRules(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + BookID + "," + RuleUID + ")/BROperations(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + BookID + "," + RuleUID + "," + OperationUID + ")",headers=creds) as resp:
           return await resp.json()

async def get_BookingRules_Company_ACTTypeUID_ACTRevisionUID_BookID_RuleUID_BROperationCustoms(Company, ACTTypeUID, ACTRevisionUID, BookID, RuleUID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get BROperationCustoms items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_BROperationCustoms1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ACTTypeUID: Desc: ACTTypeUID   Required: True
      :param ACTRevisionUID: Desc: ACTRevisionUID   Required: True
      :param BookID: Desc: BookID   Required: True   Allow empty value : True
      :param RuleUID: Desc: RuleUID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BROperationCustomRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/BookingRules(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + BookID + "," + RuleUID + ")/BROperationCustoms",headers=creds) as resp:
           return await resp.json()

async def get_BookingRules_Company_ACTTypeUID_ACTRevisionUID_BookID_RuleUID_BROperationCustoms_Company_ACTTypeUID_ACTRevisionUID_BookID_RuleUID_OperationUID(Company, ACTTypeUID, ACTRevisionUID, BookID, RuleUID, OperationUID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the BROperationCustom item
   Description: Calls GetByID to retrieve the BROperationCustom item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BROperationCustom1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ACTTypeUID: Desc: ACTTypeUID   Required: True
      :param ACTRevisionUID: Desc: ACTRevisionUID   Required: True
      :param BookID: Desc: BookID   Required: True   Allow empty value : True
      :param RuleUID: Desc: RuleUID   Required: True
      :param OperationUID: Desc: OperationUID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.BROperationCustomRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/BookingRules(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + BookID + "," + RuleUID + ")/BROperationCustoms(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + BookID + "," + RuleUID + "," + OperationUID + ")",headers=creds) as resp:
           return await resp.json()

async def get_BookValRules(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get BookValRules items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_BookValRules
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BookValRuleRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/BookValRules",headers=creds) as resp:
           return await resp.json()

async def post_BookValRules(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_BookValRules
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.BookValRuleRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.BookValRuleRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/BookValRules", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_BookValRules_Company_ACTTypeUID_ACTRevisionUID_BookID_RuleUID_VRuleUID(Company, ACTTypeUID, ACTRevisionUID, BookID, RuleUID, VRuleUID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the BookValRule item
   Description: Calls GetByID to retrieve the BookValRule item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BookValRule
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ACTTypeUID: Desc: ACTTypeUID   Required: True
      :param ACTRevisionUID: Desc: ACTRevisionUID   Required: True
      :param BookID: Desc: BookID   Required: True   Allow empty value : True
      :param RuleUID: Desc: RuleUID   Required: True
      :param VRuleUID: Desc: VRuleUID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.BookValRuleRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/BookValRules(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + BookID + "," + RuleUID + "," + VRuleUID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_BookValRules_Company_ACTTypeUID_ACTRevisionUID_BookID_RuleUID_VRuleUID(Company, ACTTypeUID, ACTRevisionUID, BookID, RuleUID, VRuleUID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update BookValRule for the service
   Description: Calls UpdateExt to update BookValRule. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_BookValRule
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ACTTypeUID: Desc: ACTTypeUID   Required: True
      :param ACTRevisionUID: Desc: ACTRevisionUID   Required: True
      :param BookID: Desc: BookID   Required: True   Allow empty value : True
      :param RuleUID: Desc: RuleUID   Required: True
      :param VRuleUID: Desc: VRuleUID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.BookValRuleRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/BookValRules(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + BookID + "," + RuleUID + "," + VRuleUID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_BookValRules_Company_ACTTypeUID_ACTRevisionUID_BookID_RuleUID_VRuleUID(Company, ACTTypeUID, ACTRevisionUID, BookID, RuleUID, VRuleUID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete BookValRule item
   Description: Call UpdateExt to delete BookValRule item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_BookValRule
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ACTTypeUID: Desc: ACTTypeUID   Required: True
      :param ACTRevisionUID: Desc: ACTRevisionUID   Required: True
      :param BookID: Desc: BookID   Required: True   Allow empty value : True
      :param RuleUID: Desc: RuleUID   Required: True
      :param VRuleUID: Desc: VRuleUID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/BookValRules(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + BookID + "," + RuleUID + "," + VRuleUID + ")",headers=creds) as resp:
           return await resp.json()

async def get_BROperations(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get BROperations items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_BROperations
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BROperationRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/BROperations",headers=creds) as resp:
           return await resp.json()

async def post_BROperations(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_BROperations
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.BROperationRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.BROperationRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/BROperations", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_BROperations_Company_ACTTypeUID_ACTRevisionUID_BookID_RuleUID_OperationUID(Company, ACTTypeUID, ACTRevisionUID, BookID, RuleUID, OperationUID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the BROperation item
   Description: Calls GetByID to retrieve the BROperation item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BROperation
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ACTTypeUID: Desc: ACTTypeUID   Required: True
      :param ACTRevisionUID: Desc: ACTRevisionUID   Required: True
      :param BookID: Desc: BookID   Required: True   Allow empty value : True
      :param RuleUID: Desc: RuleUID   Required: True
      :param OperationUID: Desc: OperationUID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.BROperationRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/BROperations(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + BookID + "," + RuleUID + "," + OperationUID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_BROperations_Company_ACTTypeUID_ACTRevisionUID_BookID_RuleUID_OperationUID(Company, ACTTypeUID, ACTRevisionUID, BookID, RuleUID, OperationUID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update BROperation for the service
   Description: Calls UpdateExt to update BROperation. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_BROperation
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ACTTypeUID: Desc: ACTTypeUID   Required: True
      :param ACTRevisionUID: Desc: ACTRevisionUID   Required: True
      :param BookID: Desc: BookID   Required: True   Allow empty value : True
      :param RuleUID: Desc: RuleUID   Required: True
      :param OperationUID: Desc: OperationUID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.BROperationRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/BROperations(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + BookID + "," + RuleUID + "," + OperationUID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_BROperations_Company_ACTTypeUID_ACTRevisionUID_BookID_RuleUID_OperationUID(Company, ACTTypeUID, ACTRevisionUID, BookID, RuleUID, OperationUID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete BROperation item
   Description: Call UpdateExt to delete BROperation item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_BROperation
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ACTTypeUID: Desc: ACTTypeUID   Required: True
      :param ACTRevisionUID: Desc: ACTRevisionUID   Required: True
      :param BookID: Desc: BookID   Required: True   Allow empty value : True
      :param RuleUID: Desc: RuleUID   Required: True
      :param OperationUID: Desc: OperationUID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/BROperations(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + BookID + "," + RuleUID + "," + OperationUID + ")",headers=creds) as resp:
           return await resp.json()

async def get_BROperationCustoms(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get BROperationCustoms items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_BROperationCustoms
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BROperationCustomRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/BROperationCustoms",headers=creds) as resp:
           return await resp.json()

async def post_BROperationCustoms(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_BROperationCustoms
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.BROperationCustomRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.BROperationCustomRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/BROperationCustoms", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_BROperationCustoms_Company_ACTTypeUID_ACTRevisionUID_BookID_RuleUID_OperationUID(Company, ACTTypeUID, ACTRevisionUID, BookID, RuleUID, OperationUID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the BROperationCustom item
   Description: Calls GetByID to retrieve the BROperationCustom item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BROperationCustom
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ACTTypeUID: Desc: ACTTypeUID   Required: True
      :param ACTRevisionUID: Desc: ACTRevisionUID   Required: True
      :param BookID: Desc: BookID   Required: True   Allow empty value : True
      :param RuleUID: Desc: RuleUID   Required: True
      :param OperationUID: Desc: OperationUID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.BROperationCustomRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/BROperationCustoms(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + BookID + "," + RuleUID + "," + OperationUID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_BROperationCustoms_Company_ACTTypeUID_ACTRevisionUID_BookID_RuleUID_OperationUID(Company, ACTTypeUID, ACTRevisionUID, BookID, RuleUID, OperationUID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update BROperationCustom for the service
   Description: Calls UpdateExt to update BROperationCustom. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_BROperationCustom
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ACTTypeUID: Desc: ACTTypeUID   Required: True
      :param ACTRevisionUID: Desc: ACTRevisionUID   Required: True
      :param BookID: Desc: BookID   Required: True   Allow empty value : True
      :param RuleUID: Desc: RuleUID   Required: True
      :param OperationUID: Desc: OperationUID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.BROperationCustomRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/BROperationCustoms(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + BookID + "," + RuleUID + "," + OperationUID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_BROperationCustoms_Company_ACTTypeUID_ACTRevisionUID_BookID_RuleUID_OperationUID(Company, ACTTypeUID, ACTRevisionUID, BookID, RuleUID, OperationUID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete BROperationCustom item
   Description: Call UpdateExt to delete BROperationCustom item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_BROperationCustom
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ACTTypeUID: Desc: ACTTypeUID   Required: True
      :param ACTRevisionUID: Desc: ACTRevisionUID   Required: True
      :param BookID: Desc: BookID   Required: True   Allow empty value : True
      :param RuleUID: Desc: RuleUID   Required: True
      :param OperationUID: Desc: OperationUID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/BROperationCustoms(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + BookID + "," + RuleUID + "," + OperationUID + ")",headers=creds) as resp:
           return await resp.json()

async def get_BRFunctions(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get BRFunctions items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_BRFunctions
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BRFunctionRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/BRFunctions",headers=creds) as resp:
           return await resp.json()

async def post_BRFunctions(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_BRFunctions
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.BRFunctionRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.BRFunctionRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/BRFunctions", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_BRFunctions_Company_ACTTypeUID_ACTRevisionUID_BookID_FunctionUID(Company, ACTTypeUID, ACTRevisionUID, BookID, FunctionUID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the BRFunction item
   Description: Calls GetByID to retrieve the BRFunction item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BRFunction
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ACTTypeUID: Desc: ACTTypeUID   Required: True
      :param ACTRevisionUID: Desc: ACTRevisionUID   Required: True
      :param BookID: Desc: BookID   Required: True   Allow empty value : True
      :param FunctionUID: Desc: FunctionUID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.BRFunctionRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/BRFunctions(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + BookID + "," + FunctionUID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_BRFunctions_Company_ACTTypeUID_ACTRevisionUID_BookID_FunctionUID(Company, ACTTypeUID, ACTRevisionUID, BookID, FunctionUID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update BRFunction for the service
   Description: Calls UpdateExt to update BRFunction. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_BRFunction
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ACTTypeUID: Desc: ACTTypeUID   Required: True
      :param ACTRevisionUID: Desc: ACTRevisionUID   Required: True
      :param BookID: Desc: BookID   Required: True   Allow empty value : True
      :param FunctionUID: Desc: FunctionUID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.BRFunctionRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/BRFunctions(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + BookID + "," + FunctionUID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_BRFunctions_Company_ACTTypeUID_ACTRevisionUID_BookID_FunctionUID(Company, ACTTypeUID, ACTRevisionUID, BookID, FunctionUID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete BRFunction item
   Description: Call UpdateExt to delete BRFunction item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_BRFunction
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ACTTypeUID: Desc: ACTTypeUID   Required: True
      :param ACTRevisionUID: Desc: ACTRevisionUID   Required: True
      :param BookID: Desc: BookID   Required: True   Allow empty value : True
      :param FunctionUID: Desc: FunctionUID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/BRFunctions(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + BookID + "," + FunctionUID + ")",headers=creds) as resp:
           return await resp.json()

async def get_BookVars(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get BookVars items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_BookVars
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BookVarRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/BookVars",headers=creds) as resp:
           return await resp.json()

async def post_BookVars(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_BookVars
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.BookVarRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.BookVarRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/BookVars", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_BookVars_Company_ACTTypeUID_ACTRevisionUID_BookID_BookVarUID(Company, ACTTypeUID, ACTRevisionUID, BookID, BookVarUID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the BookVar item
   Description: Calls GetByID to retrieve the BookVar item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BookVar
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ACTTypeUID: Desc: ACTTypeUID   Required: True
      :param ACTRevisionUID: Desc: ACTRevisionUID   Required: True
      :param BookID: Desc: BookID   Required: True   Allow empty value : True
      :param BookVarUID: Desc: BookVarUID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.BookVarRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/BookVars(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + BookID + "," + BookVarUID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_BookVars_Company_ACTTypeUID_ACTRevisionUID_BookID_BookVarUID(Company, ACTTypeUID, ACTRevisionUID, BookID, BookVarUID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update BookVar for the service
   Description: Calls UpdateExt to update BookVar. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_BookVar
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ACTTypeUID: Desc: ACTTypeUID   Required: True
      :param ACTRevisionUID: Desc: ACTRevisionUID   Required: True
      :param BookID: Desc: BookID   Required: True   Allow empty value : True
      :param BookVarUID: Desc: BookVarUID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.BookVarRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/BookVars(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + BookID + "," + BookVarUID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_BookVars_Company_ACTTypeUID_ACTRevisionUID_BookID_BookVarUID(Company, ACTTypeUID, ACTRevisionUID, BookID, BookVarUID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete BookVar item
   Description: Call UpdateExt to delete BookVar item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_BookVar
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ACTTypeUID: Desc: ACTTypeUID   Required: True
      :param ACTRevisionUID: Desc: ACTRevisionUID   Required: True
      :param BookID: Desc: BookID   Required: True   Allow empty value : True
      :param BookVarUID: Desc: BookVarUID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/BookVars(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + BookID + "," + BookVarUID + ")",headers=creds) as resp:
           return await resp.json()

async def get_BRFuncArgs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get BRFuncArgs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_BRFuncArgs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BRFuncArgsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/BRFuncArgs",headers=creds) as resp:
           return await resp.json()

async def post_BRFuncArgs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_BRFuncArgs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.BRFuncArgsRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.BRFuncArgsRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/BRFuncArgs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_BRFuncArgs_Company_ACTTypeUID_ACTRevisionUID_FunctionUID_ArgumentUID(Company, ACTTypeUID, ACTRevisionUID, FunctionUID, ArgumentUID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the BRFuncArg item
   Description: Calls GetByID to retrieve the BRFuncArg item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BRFuncArg
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ACTTypeUID: Desc: ACTTypeUID   Required: True
      :param ACTRevisionUID: Desc: ACTRevisionUID   Required: True
      :param FunctionUID: Desc: FunctionUID   Required: True
      :param ArgumentUID: Desc: ArgumentUID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.BRFuncArgsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/BRFuncArgs(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + FunctionUID + "," + ArgumentUID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_BRFuncArgs_Company_ACTTypeUID_ACTRevisionUID_FunctionUID_ArgumentUID(Company, ACTTypeUID, ACTRevisionUID, FunctionUID, ArgumentUID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update BRFuncArg for the service
   Description: Calls UpdateExt to update BRFuncArg. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_BRFuncArg
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ACTTypeUID: Desc: ACTTypeUID   Required: True
      :param ACTRevisionUID: Desc: ACTRevisionUID   Required: True
      :param FunctionUID: Desc: FunctionUID   Required: True
      :param ArgumentUID: Desc: ArgumentUID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.BRFuncArgsRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/BRFuncArgs(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + FunctionUID + "," + ArgumentUID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_BRFuncArgs_Company_ACTTypeUID_ACTRevisionUID_FunctionUID_ArgumentUID(Company, ACTTypeUID, ACTRevisionUID, FunctionUID, ArgumentUID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete BRFuncArg item
   Description: Call UpdateExt to delete BRFuncArg item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_BRFuncArg
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ACTTypeUID: Desc: ACTTypeUID   Required: True
      :param ACTRevisionUID: Desc: ACTRevisionUID   Required: True
      :param FunctionUID: Desc: FunctionUID   Required: True
      :param ArgumentUID: Desc: ArgumentUID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/BRFuncArgs(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + FunctionUID + "," + ArgumentUID + ")",headers=creds) as resp:
           return await resp.json()

async def get_BRFuncOperations(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get BRFuncOperations items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_BRFuncOperations
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BRFuncOperationRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/BRFuncOperations",headers=creds) as resp:
           return await resp.json()

async def post_BRFuncOperations(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_BRFuncOperations
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.BRFuncOperationRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.BRFuncOperationRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/BRFuncOperations", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_BRFuncOperations_Company_ACTTypeUID_ACTRevisionUID_FuncOperUID_OperationUID(Company, ACTTypeUID, ACTRevisionUID, FuncOperUID, OperationUID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the BRFuncOperation item
   Description: Calls GetByID to retrieve the BRFuncOperation item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BRFuncOperation
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ACTTypeUID: Desc: ACTTypeUID   Required: True
      :param ACTRevisionUID: Desc: ACTRevisionUID   Required: True
      :param FuncOperUID: Desc: FuncOperUID   Required: True
      :param OperationUID: Desc: OperationUID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.BRFuncOperationRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/BRFuncOperations(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + FuncOperUID + "," + OperationUID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_BRFuncOperations_Company_ACTTypeUID_ACTRevisionUID_FuncOperUID_OperationUID(Company, ACTTypeUID, ACTRevisionUID, FuncOperUID, OperationUID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update BRFuncOperation for the service
   Description: Calls UpdateExt to update BRFuncOperation. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_BRFuncOperation
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ACTTypeUID: Desc: ACTTypeUID   Required: True
      :param ACTRevisionUID: Desc: ACTRevisionUID   Required: True
      :param FuncOperUID: Desc: FuncOperUID   Required: True
      :param OperationUID: Desc: OperationUID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.BRFuncOperationRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/BRFuncOperations(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + FuncOperUID + "," + OperationUID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_BRFuncOperations_Company_ACTTypeUID_ACTRevisionUID_FuncOperUID_OperationUID(Company, ACTTypeUID, ACTRevisionUID, FuncOperUID, OperationUID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete BRFuncOperation item
   Description: Call UpdateExt to delete BRFuncOperation item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_BRFuncOperation
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ACTTypeUID: Desc: ACTTypeUID   Required: True
      :param ACTRevisionUID: Desc: ACTRevisionUID   Required: True
      :param FuncOperUID: Desc: FuncOperUID   Required: True
      :param OperationUID: Desc: OperationUID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/BRFuncOperations(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + FuncOperUID + "," + OperationUID + ")",headers=creds) as resp:
           return await resp.json()

async def get_List(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetList for the service
   Description: Get list of items<div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetList
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ACTTypeListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseACTType, whereClauseACTRevision, whereClauseABTDocLine, whereClauseABTAmount, whereClauseABTPostEntity, whereClauseABTPostCode, whereClauseABTQuery, whereClauseABTQParam, whereClauseACTBook, whereClauseBookingRule, whereClauseBookValRule, whereClauseBROperation, whereClauseBROperationCustom, whereClauseBRFunction, whereClauseBookVar, whereClauseBRFuncArgs, whereClauseBRFuncOperation, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseACTType=" + whereClauseACTType
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseACTRevision=" + whereClauseACTRevision
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseABTDocLine=" + whereClauseABTDocLine
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseABTAmount=" + whereClauseABTAmount
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseABTPostEntity=" + whereClauseABTPostEntity
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseABTPostCode=" + whereClauseABTPostCode
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseABTQuery=" + whereClauseABTQuery
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseABTQParam=" + whereClauseABTQParam
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseACTBook=" + whereClauseACTBook
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseBookingRule=" + whereClauseBookingRule
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseBookValRule=" + whereClauseBookValRule
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseBROperation=" + whereClauseBROperation
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseBROperationCustom=" + whereClauseBROperationCustom
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseBRFunction=" + whereClauseBRFunction
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseBookVar=" + whereClauseBookVar
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseBRFuncArgs=" + whereClauseBRFuncArgs
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseBRFuncOperation=" + whereClauseBRFuncOperation
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "pageSize=" + pageSize
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "absolutePage=" + absolutePage

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(acTTypeUID, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "acTTypeUID=" + acTTypeUID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetList(whereClause, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetList
   Description: Returns a list of rows that satisfy the where clause.
   OperationID: Get_GetList
      :param whereClause: Desc: An expression used to filter the rows. Can be left blank for all rows.   Required: True   Allow empty value : True
      :param pageSize: Desc: The maximum number of rows to return. Leave as zero for no maximum.   Required: True
      :param absolutePage: Desc: Page of rows to return.   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClause=" + whereClause
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "pageSize=" + pageSize
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "absolutePage=" + absolutePage

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetRelatedContextItemsCustom(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRelatedContextItemsCustom
   Description: Returns tree of available values for substitute in functions params for rule's custom operations
   OperationID: GetRelatedContextItemsCustom
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRelatedContextItemsCustom_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRelatedContextItemsCustom_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRelatedContextItems(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRelatedContextItems
   Description: Returns tree of available values for substitute in functions params for rule's base operations
   OperationID: GetRelatedContextItems
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRelatedContextItems_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRelatedContextItems_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ProcessFormulaParamClick(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ProcessFormulaParamClick
   Description: Handle click on function's param in Base operations. It just can return data in ACTTypeSubDataTableset or just execute command with modifying linkcombo data
   OperationID: ProcessFormulaParamClick
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ProcessFormulaParamClick_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProcessFormulaParamClick_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ProcessFormulaParamClickCustom(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ProcessFormulaParamClickCustom
   Description: Handle click on function's param in Custom operations. It just can return data in ACTTypeSubDataTableset or just execute command with modifying linkcombo data
   OperationID: ProcessFormulaParamClickCustom
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ProcessFormulaParamClickCustom_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProcessFormulaParamClickCustom_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ProcessFormulaParamClickFuncOper(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ProcessFormulaParamClickFuncOper
   Description: Handle click on function's param in function's operations. It just can return data in ACTTypeSubDataTableset or just execute command with modifying linkcombo data
   OperationID: ProcessFormulaParamClickFuncOper
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ProcessFormulaParamClickFuncOper_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProcessFormulaParamClickFuncOper_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetValueTypesForPostCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetValueTypesForPostCode
   Description: GetValueTypesForPostCode
   OperationID: GetValueTypesForPostCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetValueTypesForPostCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetValueTypesForPostCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnBROperationIsLogicalConditionChanged(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnBROperationIsLogicalConditionChanged
   OperationID: OnBROperationIsLogicalConditionChanged
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnBROperationIsLogicalConditionChanged_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnBROperationIsLogicalConditionChanged_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnBROperationCustomIsLogicalConditionChanged(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnBROperationCustomIsLogicalConditionChanged
   OperationID: OnBROperationCustomIsLogicalConditionChanged
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnBROperationCustomIsLogicalConditionChanged_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnBROperationCustomIsLogicalConditionChanged_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnBRFuncOperationIsLogicalConditionChanged(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnBRFuncOperationIsLogicalConditionChanged
   OperationID: OnBRFuncOperationIsLogicalConditionChanged
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnBRFuncOperationIsLogicalConditionChanged_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnBRFuncOperationIsLogicalConditionChanged_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnBROperationContainerTypeChanging(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnBROperationContainerTypeChanging
   Description: Validates proposed value of the ContairerType value in the BROperation table
   OperationID: OnBROperationContainerTypeChanging
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnBROperationContainerTypeChanging_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnBROperationContainerTypeChanging_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnBROperationCustomContainerTypeChanging(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnBROperationCustomContainerTypeChanging
   Description: Validates proposed value of the ContairerType value in the BROperationCustom table
   OperationID: OnBROperationCustomContainerTypeChanging
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnBROperationCustomContainerTypeChanging_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnBROperationCustomContainerTypeChanging_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnBRFuncOperationContainerTypeChanging(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnBRFuncOperationContainerTypeChanging
   Description: Validates proposed value of the ContairerType value in the BRFuncOperation table
   OperationID: OnBRFuncOperationContainerTypeChanging
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnBRFuncOperationContainerTypeChanging_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnBRFuncOperationContainerTypeChanging_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OperationFunctionUIDChanging(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OperationFunctionUIDChanging
   Description: Invoked when FunctionUID is changed on BRFuncOperation/BROperation/BROperationCustom
   OperationID: OperationFunctionUIDChanging
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OperationFunctionUIDChanging_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OperationFunctionUIDChanging_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_BROperationUpdateContainer(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method BROperationUpdateContainer
   OperationID: BROperationUpdateContainer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BROperationUpdateContainer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BROperationUpdateContainer_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_BROperationCustomUpdateContainer(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method BROperationCustomUpdateContainer
   OperationID: BROperationCustomUpdateContainer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BROperationCustomUpdateContainer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BROperationCustomUpdateContainer_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_BRFuncOperationUpdateContainer(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method BRFuncOperationUpdateContainer
   OperationID: BRFuncOperationUpdateContainer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BRFuncOperationUpdateContainer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BRFuncOperationUpdateContainer_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_BROperationUpdateContainerFormula(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method BROperationUpdateContainerFormula
   OperationID: BROperationUpdateContainerFormula
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BROperationUpdateContainerFormula_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BROperationUpdateContainerFormula_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_BROPerationCustomUpdateContainerFormula(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method BROPerationCustomUpdateContainerFormula
   OperationID: BROPerationCustomUpdateContainerFormula
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BROPerationCustomUpdateContainerFormula_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BROPerationCustomUpdateContainerFormula_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_BRFuncOperationUpdateContainerFormula(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method BRFuncOperationUpdateContainerFormula
   OperationID: BRFuncOperationUpdateContainerFormula
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BRFuncOperationUpdateContainerFormula_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BRFuncOperationUpdateContainerFormula_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SelectionCriteriaAddOnClick(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SelectionCriteriaAddOnClick
   Description: Updates SelectionCriteria value on Add button click
   OperationID: SelectionCriteriaAddOnClick
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SelectionCriteriaAddOnClick_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SelectionCriteriaAddOnClick_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AddMultipleBooks(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AddMultipleBooks
   Description: Adds new ACTBook records.  Multiple books can be created by passing ~ separated list.  Records are saved to the DB.
   OperationID: AddMultipleBooks
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AddMultipleBooks_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddMultipleBooks_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ABTBookGetNewExt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ABTBookGetNewExt
   Description: Add new GLBook to Transaction Type without loading of system functions.
   OperationID: ABTBookGetNewExt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ABTBookGetNewExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ABTBookGetNewExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LoadTwoDatasetsTestMethod1(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LoadTwoDatasetsTestMethod1
   OperationID: LoadTwoDatasetsTestMethod1
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LoadTwoDatasetsTestMethod1_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LoadTwoDatasetsTestMethod1_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateTwoDatasetsTestMethod1(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateTwoDatasetsTestMethod1
   OperationID: UpdateTwoDatasetsTestMethod1
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateTwoDatasetsTestMethod1_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateTwoDatasetsTestMethod1_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckSyntaxRevision(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckSyntaxRevision
   Description: Checks all function and rules in a revision for syntax errors. Updates IsError and ErrorText fields.
   OperationID: CheckSyntaxRevision
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckSyntaxRevision_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckSyntaxRevision_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckSyntaxFunction(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckSyntaxFunction
   Description: Checks the current function for syntax errors. Updates IsError and ErrorText fields.
   OperationID: CheckSyntaxFunction
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckSyntaxFunction_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckSyntaxFunction_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckSyntaxRule(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckSyntaxRule
   Description: Checks the current rule for syntax errors. Updates IsError and ErrorText fields.
   OperationID: CheckSyntaxRule
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckSyntaxRule_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckSyntaxRule_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewACTType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewACTType
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewACTType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewACTType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewACTType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewACTRevision(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewACTRevision
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewACTRevision
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewACTRevision_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewACTRevision_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewABTDocLine(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewABTDocLine
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewABTDocLine
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewABTDocLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewABTDocLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewABTAmount(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewABTAmount
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewABTAmount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewABTAmount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewABTAmount_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewABTPostEntity(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewABTPostEntity
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewABTPostEntity
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewABTPostEntity_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewABTPostEntity_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewABTPostCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewABTPostCode
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewABTPostCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewABTPostCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewABTPostCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewABTQuery(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewABTQuery
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewABTQuery
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewABTQuery_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewABTQuery_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewABTQParam(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewABTQParam
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewABTQParam
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewABTQParam_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewABTQParam_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewACTBook(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewACTBook
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewACTBook
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewACTBook_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewACTBook_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewBookingRule(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewBookingRule
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewBookingRule
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewBookingRule_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewBookingRule_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewBROperation(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewBROperation
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewBROperation
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewBROperation_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewBROperation_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewBROperationCustom(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewBROperationCustom
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewBROperationCustom
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewBROperationCustom_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewBROperationCustom_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewBRFunction(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewBRFunction
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewBRFunction
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewBRFunction_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewBRFunction_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewBookVar(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewBookVar
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewBookVar
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewBookVar_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewBookVar_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewBRFuncArgs(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewBRFuncArgs
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewBRFuncArgs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewBRFuncArgs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewBRFuncArgs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewBRFuncOperation(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewBRFuncOperation
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewBRFuncOperation
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewBRFuncOperation_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewBRFuncOperation_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteByID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteByID
   Description: Deletes a row given its ID.
   OperationID: DeleteByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GetBySysRowID(id, epicorHeaders = None):
   """  
   Summary: Invoke method GetBySysRowID
   OperationID: Get_GetBySysRowID
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "id=" + id

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetBySysRowIDs(ids, epicorHeaders = None):
   """  
   Summary: Invoke method GetBySysRowIDs
   OperationID: Get_GetBySysRowIDs
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowIDs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "ids=" + ids

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_Update(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method Update
   Description: Commits the DataSet changes to the data store.
   OperationID: Update
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Update_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Update_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateExt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateExt
   Description: Apply input data to service by calling GetByID/GetNew/Update methods.
   OperationID: UpdateExt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetFunctionPhrase(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetFunctionPhrase
   Description: Returns Function name for the linked combo
   OperationID: GetFunctionPhrase
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetFunctionPhrase_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFunctionPhrase_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_BRFunctionPhraseElementMove(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method BRFunctionPhraseElementMove
   Description: move up/down the phrase element inside the structure
   OperationID: BRFunctionPhraseElementMove
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BRFunctionPhraseElementMove_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BRFunctionPhraseElementMove_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_BRFunctionPhraseUpdate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method BRFunctionPhraseUpdate
   Description: Update function name
   OperationID: BRFunctionPhraseUpdate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BRFunctionPhraseUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BRFunctionPhraseUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeBRFunctionPhraseElementText(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeBRFunctionPhraseElementText
   Description: Handling of change Phrase Element text
   OperationID: OnChangeBRFunctionPhraseElementText
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeBRFunctionPhraseElementText_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeBRFunctionPhraseElementText_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeBRFunctionPhraseElementType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeBRFunctionPhraseElementType
   Description: Handling of change Phrase Element type
   OperationID: OnChangeBRFunctionPhraseElementType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeBRFunctionPhraseElementType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeBRFunctionPhraseElementType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeBRFunctionPhraseElementArgType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeBRFunctionPhraseElementArgType
   Description: Handling of changing Function Argument type in the function phrase
   OperationID: OnChangeBRFunctionPhraseElementArgType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeBRFunctionPhraseElementArgType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeBRFunctionPhraseElementArgType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_FunctionPhraseElementGetNew(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method FunctionPhraseElementGetNew
   Description: Creates new BRFunctionPhrase row
   OperationID: FunctionPhraseElementGetNew
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/FunctionPhraseElementGetNew_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/FunctionPhraseElementGetNew_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_FunctionPhraseElementDelete(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method FunctionPhraseElementDelete
   Description: Delete Function Phrase Element row
   OperationID: FunctionPhraseElementDelete
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/FunctionPhraseElementDelete_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/FunctionPhraseElementDelete_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetFunctionPhraseElements(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetFunctionPhraseElements
   Description: Returns the list of Function Phrase elements
   OperationID: GetFunctionPhraseElements
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetFunctionPhraseElements_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFunctionPhraseElements_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRelatedContextItemsFunctionPhrase(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRelatedContextItemsFunctionPhrase
   Description: returns the list of available Function Argument types in hierarchical structure
   OperationID: GetRelatedContextItemsFunctionPhrase
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRelatedContextItemsFunctionPhrase_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRelatedContextItemsFunctionPhrase_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CompareRevisions(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CompareRevisions
   Description: Compares the revisions and returns the tree
   OperationID: CompareRevisions
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CompareRevisions_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CompareRevisions_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetLeftTree(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetLeftTree
   Description: Compares the operations and gets the Left/Revision 1 tree
   OperationID: GetLeftTree
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetLeftTree_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLeftTree_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRightTree(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRightTree
   Description: Compares the operations and gets the Right/Revision 2 tree
   OperationID: GetRightTree
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRightTree_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRightTree_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GetFunctionTree(GPostingUID, NodeID, epicorHeaders = None):
   """  
   Summary: Invoke method GetFunctionTree
   Description: Returns Function Tree structure.
   OperationID: Get_GetFunctionTree
      :param GPostingUID: Desc: Function SysRowID (Use 0aaa410e-ecc2-4dcd-9e6d-0c2d0d879149 for test purposes)   Required: True   Allow empty value : True
      :param NodeID: Desc: Fake node.   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFunctionTree_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "GPostingUID=" + GPostingUID
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "NodeID=" + NodeID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetPostingRuleBaseTree(GPostingUID, NodeID, epicorHeaders = None):
   """  
   Summary: Invoke method GetPostingRuleBaseTree
   Description: Returns Posting Rule Base Tree structure.
   OperationID: Get_GetPostingRuleBaseTree
      :param GPostingUID: Desc: Function ID (Use 0aaa410e-ecc2-4dcd-9e6d-0c2d0d879149 for test purposes)   Required: True   Allow empty value : True
      :param NodeID: Desc: Fake node.   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPostingRuleBaseTree_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "GPostingUID=" + GPostingUID
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "NodeID=" + NodeID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetPostingRuleCustomizationTree(GPostingUID, NodeID, epicorHeaders = None):
   """  
   Summary: Invoke method GetPostingRuleCustomizationTree
   Description: Returns Posting Rule Base Tree structure.
   OperationID: Get_GetPostingRuleCustomizationTree
      :param GPostingUID: Desc: Function ID (Use 0aaa410e-ecc2-4dcd-9e6d-0c2d0d879149 for test purposes)   Required: True   Allow empty value : True
      :param NodeID: Desc: Fake node.   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPostingRuleCustomizationTree_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "GPostingUID=" + GPostingUID
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "NodeID=" + NodeID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_InitializeForTests(epicorHeaders = None):
   """  
   Summary: Invoke method InitializeForTests
   Description: This method is used for Unit Tests to initialize data
   OperationID: InitializeForTests
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/InitializeForTests_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_CanActivateRevision(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CanActivateRevision
   Description: Check if ACTRevision can be Activated or not
   OperationID: CanActivateRevision
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CanActivateRevision_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CanActivateRevision_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCustomContextMenuXml(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCustomContextMenuXml
   Description: Returns context menu items as xml for rules constructor.
   OperationID: GetCustomContextMenuXml
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCustomContextMenuXml_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCustomContextMenuXml_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ABTDocLineGetNew(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ABTDocLineGetNew
   Description: Create new BR Operation.
   OperationID: ABTDocLineGetNew
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ABTDocLineGetNew_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ABTDocLineGetNew_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ABTPostCodeGetNew(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ABTPostCodeGetNew
   Description: Create new ABTPostcode.
   OperationID: ABTPostCodeGetNew
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ABTPostCodeGetNew_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ABTPostCodeGetNew_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ABTBookGetNew(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ABTBookGetNew
   Description: Add book to book list.
   OperationID: ABTBookGetNew
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ABTBookGetNew_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ABTBookGetNew_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AddMappedBook(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AddMappedBook
   Description: Adds a mapped book.
   OperationID: AddMappedBook
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AddMappedBook_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddMappedBook_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_BookingRuleGetNew(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method BookingRuleGetNew
   Description: Create new Booking Rule.
   OperationID: BookingRuleGetNew
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BookingRuleGetNew_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BookingRuleGetNew_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeBookingRuleName(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeBookingRuleName
   Description: Check value new DisplayName for rule. It should be unique in one book.
   OperationID: OnChangeBookingRuleName
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeBookingRuleName_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeBookingRuleName_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_BookVariableGetNew(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method BookVariableGetNew
   Description: Create new variable of type of type book, function, rule.
   OperationID: BookVariableGetNew
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BookVariableGetNew_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BookVariableGetNew_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_BRFuncOperationGetNew(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method BRFuncOperationGetNew
   Description: Create new BR Operation.
   OperationID: BRFuncOperationGetNew
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BRFuncOperationGetNew_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BRFuncOperationGetNew_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeBRFunctionFormula(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeBRFunctionFormula
   Description: Check value new Formula for function. It should be unique in one book.
   OperationID: OnChangeBRFunctionFormula
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeBRFunctionFormula_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeBRFunctionFormula_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_BROperationGetNew(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method BROperationGetNew
   Description: Create new BR Operation.
   OperationID: BROperationGetNew
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BROperationGetNew_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BROperationGetNew_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_BROperationCustomGetNew(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method BROperationCustomGetNew
   Description: Create new BR Operation Customization.
   OperationID: BROperationCustomGetNew
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BROperationCustomGetNew_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BROperationCustomGetNew_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeBAQ(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeBAQ
   Description: Refresh parameter list after BAQ change.
   OperationID: ChangeBAQ
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeBAQ_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeBAQ_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeRevisionStatusMode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeRevisionStatusMode
   Description: Change Revision Status or Mode.
   OperationID: ChangeRevisionStatusMode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeRevisionStatusMode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeRevisionStatusMode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckBAQExists(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckBAQExists
   Description: Checks if BAQ exists.
   OperationID: CheckBAQExists
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckBAQExists_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckBAQExists_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckBeforeActivateRevision(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckBeforeActivateRevision
   Description: Return an error if revision cannot be activated
   OperationID: CheckBeforeActivateRevision
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckBeforeActivateRevision_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckBeforeActivateRevision_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ListMappedBooksWithRules(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ListMappedBooksWithRules
   Description: Return list of mapped books having posting rules or functions for a particular revision. Used by UI when copy revision.
   OperationID: ListMappedBooksWithRules
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ListMappedBooksWithRules_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ListMappedBooksWithRules_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_BookIsNotEmpty(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method BookIsNotEmpty
   Description: Returns true if book has defined booking rules or functions.
   OperationID: BookIsNotEmpty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BookIsNotEmpty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BookIsNotEmpty_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CopyListOfFunctions(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CopyListOfFunctions
   Description: Copy defined function list
   OperationID: CopyListOfFunctions
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CopyListOfFunctions_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CopyListOfFunctions_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CopyListOfFunctionsWithWarn(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CopyListOfFunctionsWithWarn
   Description: Copy defined function list
   OperationID: CopyListOfFunctionsWithWarn
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CopyListOfFunctionsWithWarn_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CopyListOfFunctionsWithWarn_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CopyListOfRules(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CopyListOfRules
   Description: Copy defined booking rule list
   OperationID: CopyListOfRules
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CopyListOfRules_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CopyListOfRules_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CopyListOfRulesWithWarn(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CopyListOfRulesWithWarn
   Description: Copy defined booking rule list
   OperationID: CopyListOfRulesWithWarn
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CopyListOfRulesWithWarn_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CopyListOfRulesWithWarn_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CopyOperations(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CopyOperations
   Description: Allow copy defined operation in different GL Transaction Type.
   OperationID: CopyOperations
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CopyOperations_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CopyOperations_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CustomUpdate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CustomUpdate
   Description: Custom Update Database
   OperationID: CustomUpdate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CustomUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CustomUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteACTBook(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteACTBook
   OperationID: DeleteACTBook
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteACTBook_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteACTBook_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteMappedBook(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteMappedBook
   OperationID: DeleteMappedBook
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteMappedBook_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteMappedBook_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteOpItems(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteOpItems
   Description: Delete single Operation or with child operations
   OperationID: DeleteOpItems
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteOpItems_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteOpItems_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteBROperationCustom(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteBROperationCustom
   Description: Delete single Custom Operation or with child operations
   OperationID: DeleteBROperationCustom
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteBROperationCustom_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteBROperationCustom_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteRevisionByName(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteRevisionByName
   Description: Delete revision by Revision Code.
   OperationID: DeleteRevisionByName
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteRevisionByName_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteRevisionByName_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteRevsBeforeImport(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteRevsBeforeImport
   Description: Delete all previous revisions for spec. transaction types.
   OperationID: DeleteRevsBeforeImport
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteRevsBeforeImport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteRevsBeforeImport_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AfterDeleteVBDItem(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AfterDeleteVBDItem
   Description: For Develop Mode Revision should be updated after deletion any Item from VBD Structure
   OperationID: AfterDeleteVBDItem
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AfterDeleteVBDItem_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AfterDeleteVBDItem_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AfterDeleteBookItem(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AfterDeleteBookItem
   Description: For Develop Mode Book should be updated after deletion any its Item
   OperationID: AfterDeleteBookItem
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AfterDeleteBookItem_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AfterDeleteBookItem_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AfterDeleteFunctionItem(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AfterDeleteFunctionItem
   Description: For Develop Mode Book and Function should be updated after deletion any Function Item
   OperationID: AfterDeleteFunctionItem
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AfterDeleteFunctionItem_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AfterDeleteFunctionItem_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AfterDeleteRuleItem(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AfterDeleteRuleItem
   Description: For Develop Mode Book and Rule should be updated after deletion any Rule Item
   OperationID: AfterDeleteRuleItem
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AfterDeleteRuleItem_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AfterDeleteRuleItem_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ExportToXML(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ExportToXML
   Description: Export revision to XML format
   OperationID: ExportToXML
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExportToXML_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExportToXML_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_FillBAQDescription(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method FillBAQDescription
   Description: Populates BAQDescription field with the value from corresponding BAQ for all entried with ADDED or UPDATED status.
   OperationID: FillBAQDescription
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/FillBAQDescription_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/FillBAQDescription_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_TryCompile(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method TryCompile
   Description: Compile Post file for GL Transaction Type Revision to check for compilation errors
Throws CompilationException with first 100 exceptions in ExceptionMessageList
   OperationID: TryCompile
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/TryCompile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/TryCompile_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GenerateTemplate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GenerateTemplate
   Description: Generate Template
   OperationID: GenerateTemplate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenerateTemplate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateTemplate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetAllACTTypesForExport(epicorHeaders = None):
   """  
   Summary: Invoke method GetAllACTTypesForExport
   Description: Returns all revisions for Export Form
   OperationID: GetAllACTTypesForExport
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAllACTTypesForExport_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetBookVarOwnerID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetBookVarOwnerID
   Description: Get list of book variable owner id's.
If owner is function or rule the list will include names and id's.
   OperationID: GetBookVarOwnerID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetBookVarOwnerID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBookVarOwnerID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetBookVarOwnerTypes(epicorHeaders = None):
   """  
   Summary: Invoke method GetBookVarOwnerTypes
   Description: Get list of bookVar owners - Global, Book, Rule, Function.
   OperationID: GetBookVarOwnerTypes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBookVarOwnerTypes_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetBRContainerRows(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetBRContainerRows
   Description: Get list of fields.
   OperationID: GetBRContainerRows
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetBRContainerRows_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBRContainerRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCurrentVersion(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCurrentVersion
   Description: Get ACTType ID by Name.
   OperationID: GetCurrentVersion
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCurrentVersion_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCurrentVersion_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetEntityForBookingRule(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetEntityForBookingRule
   Description: Get a value of Entity for a Booking Rule in table PatchFld.
   OperationID: GetEntityForBookingRule
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetEntityForBookingRule_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetEntityForBookingRule_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetFlowList(epicorHeaders = None):
   """  
   Summary: Invoke method GetFlowList
   Description: Get list of flow statements.
   OperationID: GetFlowList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFlowList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetIDByName(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetIDByName
   Description: Get ACTType ID by Name.
   OperationID: GetIDByName
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetIDByName_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetIDByName_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetOperatorList(epicorHeaders = None):
   """  
   Summary: Invoke method GetOperatorList
   Description: Get list of operators.
   OperationID: GetOperatorList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetOperatorList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetPostCodeTypes(epicorHeaders = None):
   """  
   Summary: Invoke method GetPostCodeTypes
   Description: Get list of possible post code types.
   OperationID: GetPostCodeTypes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPostCodeTypes_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetRevisionIDByName(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRevisionIDByName
   Description: Get ACTRevision ID by Name.
   OperationID: GetRevisionIDByName
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRevisionIDByName_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRevisionIDByName_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetStatusList(epicorHeaders = None):
   """  
   Summary: Invoke method GetStatusList
   Description: Get list of revision statuses.
   OperationID: GetStatusList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetStatusList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetSummarizeList(epicorHeaders = None):
   """  
   Summary: Invoke method GetSummarizeList
   Description: Get list of summarize options.
   OperationID: GetSummarizeList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSummarizeList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetTrCurrencyList(epicorHeaders = None):
   """  
   Summary: Invoke method GetTrCurrencyList
   Description: Transactional currency options.
   OperationID: GetTrCurrencyList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTrCurrencyList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetVarTypes(epicorHeaders = None):
   """  
   Summary: Invoke method GetVarTypes
   Description: Get list of possible types.
   OperationID: GetVarTypes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetVarTypes_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetWarningRevisionStatus(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetWarningRevisionStatus
   Description: Return warning if status is changing.
   OperationID: GetWarningRevisionStatus
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetWarningRevisionStatus_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetWarningRevisionStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ImportFromXML(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ImportFromXML
   Description: Import revision to XML format (obsolete method)
   OperationID: ImportFromXML
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportFromXML_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportFromXML_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ImportGLTransactionType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ImportGLTransactionType
   Description: Import revision
   OperationID: ImportGLTransactionType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportGLTransactionType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportGLTransactionType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetHashSystemXml(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetHashSystemXml
   Description: Get hash Value of System Xml
   OperationID: GetHashSystemXml
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetHashSystemXml_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetHashSystemXml_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LoadSystemGLTransactionType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LoadSystemGLTransactionType
   Description: LoadSystemGLTransactionType
   OperationID: LoadSystemGLTransactionType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LoadSystemGLTransactionType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LoadSystemGLTransactionType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LoadBookDataForImport(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LoadBookDataForImport
   Description: Load list of Books, their COA Segments and Default Segment Mapping information for import for selected companies.
   OperationID: LoadBookDataForImport
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LoadBookDataForImport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LoadBookDataForImport_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ImportProcessIsAllowed(epicorHeaders = None):
   """  
   Summary: Invoke method ImportProcessIsAllowed
   Description: Check that manual import process can be started
   OperationID: ImportProcessIsAllowed
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportProcessIsAllowed_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_OnChangingABTQuery(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingABTQuery
   Description: Check ABTQuery is in use when it is trying to change.
   OperationID: OnChangingABTQuery
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingABTQuery_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingABTQuery_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangingPostCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingPostCode
   Description: Check PostCode is in use when it is trying to change.
   OperationID: OnChangingPostCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingPostCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingPostCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_IsVarInUse(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method IsVarInUse
   Description: Checks if a variable (book, function, rule) is used.
   OperationID: IsVarInUse
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/IsVarInUse_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsVarInUse_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LoadACTBook(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LoadACTBook
   Description: Load Book details for one book or all
   OperationID: LoadACTBook
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LoadACTBook_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LoadACTBook_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LoadAmount(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LoadAmount
   Description: Load ABTAmount records for Document Line
   OperationID: LoadAmount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LoadAmount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LoadAmount_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LoadBooks(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LoadBooks
   OperationID: LoadBooks
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LoadBooks_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LoadBooks_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LoadBookVar(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LoadBookVar
   Description: Load Book details for one book or all
   OperationID: LoadBookVar
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LoadBookVar_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LoadBookVar_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LoadBrFuncArgs(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LoadBrFuncArgs
   Description: Load Function arguments
   OperationID: LoadBrFuncArgs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LoadBrFuncArgs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LoadBrFuncArgs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LoadBrFuncOperation(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LoadBrFuncOperation
   Description: Load Functions
   OperationID: LoadBrFuncOperation
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LoadBrFuncOperation_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LoadBrFuncOperation_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LoadBROperation(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LoadBROperation
   Description: Load Br Operations one or all
   OperationID: LoadBROperation
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LoadBROperation_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LoadBROperation_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LoadDocumentLine(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LoadDocumentLine
   Description: Load Function arguments
   OperationID: LoadDocumentLine
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LoadDocumentLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LoadDocumentLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LoadDocumentLineBAQ(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LoadDocumentLineBAQ
   Description: Load Document Line BAQ
   OperationID: LoadDocumentLineBAQ
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LoadDocumentLineBAQ_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LoadDocumentLineBAQ_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LoadDocumentLineBAQParam(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LoadDocumentLineBAQParam
   Description: Load Document Line BAQ
   OperationID: LoadDocumentLineBAQParam
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LoadDocumentLineBAQParam_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LoadDocumentLineBAQParam_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LoadFunction(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LoadFunction
   Description: Load Functions
   OperationID: LoadFunction
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LoadFunction_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LoadFunction_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LoadRevision(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LoadRevision
   Description: Load revision Details by ID, called when tree node is expanded, can load only first record isFullLoad = 0.
   OperationID: LoadRevision
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LoadRevision_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LoadRevision_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LoadACTType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LoadACTType
   Description: Load actType Details by ID, called instaed of GetByID to not load all data
   OperationID: LoadACTType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LoadACTType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LoadACTType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LoadRevisionVersions(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LoadRevisionVersions
   Description: Load revision Versionss.
   OperationID: LoadRevisionVersions
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LoadRevisionVersions_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LoadRevisionVersions_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LoadRule(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LoadRule
   Description: Load Rules one or all
   OperationID: LoadRule
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LoadRule_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LoadRule_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeBVRuleAction(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeBVRuleAction
   Description: This method should be called when action of validation rule is changed.
   OperationID: OnChangeBVRuleAction
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeBVRuleAction_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeBVRuleAction_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeEntityDataSource(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeEntityDataSource
   Description: This method should be called when Datasource of Post Entity is changed.
   OperationID: OnChangeEntityDataSource
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeEntityDataSource_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeEntityDataSource_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PostCodeSourceRefresh(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PostCodeSourceRefresh
   Description: refresh datasource of post codes.
   OperationID: PostCodeSourceRefresh
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PostCodeSourceRefresh_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PostCodeSourceRefresh_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RefreshBookList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RefreshBookList
   Description: Refresh Books list
   OperationID: RefreshBookList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RefreshBookList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RefreshBookList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RevisionCopyFrom(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RevisionCopyFrom
   Description: Create copy of Revision.
   OperationID: RevisionCopyFrom
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RevisionCopyFrom_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RevisionCopyFrom_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateABTVerForImport(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateABTVerForImport
   Description: Validate vesrions of imported data
   OperationID: ValidateABTVerForImport
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateABTVerForImport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateABTVerForImport_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UndoUpdateVersionsWithRefreshDS(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UndoUpdateVersionsWithRefreshDS
   Description: Undo updated vesions of Revision and load result in dataset
   OperationID: UndoUpdateVersionsWithRefreshDS
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UndoUpdateVersionsWithRefreshDS_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UndoUpdateVersionsWithRefreshDS_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateVersionsWithRefreshDS(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateVersionsWithRefreshDS
   Description: Update Versions for Revision and load result in dataset
   OperationID: UpdateVersionsWithRefreshDS
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateVersionsWithRefreshDS_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateVersionsWithRefreshDS_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetBookVersions(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetBookVersions
   Description: Get Book Versions
   OperationID: GetBookVersions
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetBookVersions_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBookVersions_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRuleVersions(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRuleVersions
   Description: Get Rule Versions
   OperationID: GetRuleVersions
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRuleVersions_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRuleVersions_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetFuncVersions(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetFuncVersions
   Description: Get Function Versions
   OperationID: GetFuncVersions
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetFuncVersions_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFuncVersions_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRevVersions(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRevVersions
   Description: Get Revision Versions
   OperationID: GetRevVersions
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRevVersions_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRevVersions_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateCOAMap(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateCOAMap
   Description: Purpose: Validate COAMapID
<param name="ipCOAMapUID">COA Map ID to validate</param><param name="ipSourceCOA">COA for the Source Book</param><param name="ipMappedCOA">COA for the Mapped Book</param>
Notes:
   OperationID: ValidateCOAMap
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateCOAMap_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateCOAMap_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetBookPackage(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetBookPackage
   Description: Return package of selected book
   OperationID: GetBookPackage
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetBookPackage_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBookPackage_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetByIDExt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetByIDExt
   Description: Returns ACTType with Active and Draft revisions
   OperationID: GetByIDExt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetByIDExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByIDExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetByID_Revisions(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID_Revisions
   Description: Returns ACTType with given revisions
   OperationID: GetByID_Revisions
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetByID_Revisions_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_Revisions_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RevisionStatusChanging(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RevisionStatusChanging
   Description: Executes when user changes Revision status
   OperationID: RevisionStatusChanging
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RevisionStatusChanging_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RevisionStatusChanging_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_BookVarNameTypeChanging(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method BookVarNameTypeChanging
   Description: Executes when BookVar Name or Type changed.
   OperationID: BookVarNameTypeChanging
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BookVarNameTypeChanging_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BookVarNameTypeChanging_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_BookVarOwnerChanging(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method BookVarOwnerChanging
   Description: Executes when BookVar Owner is changed.
   OperationID: BookVarOwnerChanging
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BookVarOwnerChanging_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BookVarOwnerChanging_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_TableDataFieldChanging(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method TableDataFieldChanging
   Description: Executes when DataTable Field name is changed.
   OperationID: TableDataFieldChanging
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/TableDataFieldChanging_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/TableDataFieldChanging_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PopulationMethodChanging(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PopulationMethodChanging
   Description: Refresh ABTPostCode fields after PopulationMethod is changing
   OperationID: PopulationMethodChanging
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PopulationMethodChanging_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PopulationMethodChanging_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_BAQDataFieldChanging(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method BAQDataFieldChanging
   Description: Executes when BAQFataField is changed.
   OperationID: BAQDataFieldChanging
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BAQDataFieldChanging_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BAQDataFieldChanging_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRevisionsList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRevisionsList
   Description: Returns revision list with its status
   OperationID: GetRevisionsList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRevisionsList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRevisionsList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRevisionStatusesList(epicorHeaders = None):
   """  
   Summary: Invoke method GetRevisionStatusesList
   Description: Returns statuses for revision.
   OperationID: GetRevisionStatusesList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRevisionStatusesList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetGLControlTypesList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetGLControlTypesList
   Description: Returns list of GL Control types
   OperationID: GetGLControlTypesList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetGLControlTypesList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetGLControlTypesList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRuleContextsList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRuleContextsList
   Description: Returns contexts of given GL Control type.
   OperationID: GetRuleContextsList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRuleContextsList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRuleContextsList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetMapBookList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetMapBookList
   Description: Returns list of Books for mapping
   OperationID: GetMapBookList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetMapBookList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMapBookList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPostEntityDataSourceList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPostEntityDataSourceList
   Description: Returns list for Post Entity DataSource combobox
   OperationID: GetPostEntityDataSourceList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPostEntityDataSourceList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPostEntityDataSourceList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetFieldsOfBAQList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetFieldsOfBAQList
   Description: Returns delimited list of fields of given BAQ
   OperationID: GetFieldsOfBAQList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetFieldsOfBAQList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFieldsOfBAQList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCOAMapsList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCOAMapsList
   Description: Returns COA Map Data
   OperationID: GetCOAMapsList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCOAMapsList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCOAMapsList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCOAIDForBook(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCOAIDForBook
   Description: returns COA Id for the book.
   OperationID: GetCOAIDForBook
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCOAIDForBook_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCOAIDForBook_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetFieldsOfTable(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetFieldsOfTable
   Description: Get delimited list of fields of given table
   OperationID: GetFieldsOfTable
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetFieldsOfTable_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFieldsOfTable_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LoadRuleVariables(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LoadRuleVariables
   OperationID: LoadRuleVariables
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LoadRuleVariables_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LoadRuleVariables_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LoadABTStructure(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LoadABTStructure
   OperationID: LoadABTStructure
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LoadABTStructure_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LoadABTStructure_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LoadGLCntrlTypes(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LoadGLCntrlTypes
   Description: Load GL Control Contexts
   OperationID: LoadGLCntrlTypes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LoadGLCntrlTypes_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LoadGLCntrlTypes_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPostCodeTypesExt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPostCodeTypesExt
   Description: Get list of possible Data types for post code for Kinetic. It is required to work with link-combo component.
   OperationID: GetPostCodeTypesExt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPostCodeTypesExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPostCodeTypesExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetContainerPhraseItems(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetContainerPhraseItems
   Description: Returns data of available containers for Container combo
   OperationID: GetContainerPhraseItems
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetContainerPhraseItems_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetContainerPhraseItems_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetConditionList(epicorHeaders = None):
   """  
   Summary: Invoke method GetConditionList
   Description: Returns Condition Flow list
   OperationID: GetConditionList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetConditionList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetFunctionResultTypeList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetFunctionResultTypeList
   Description: Returns the list of available data types for the Book/Function variable
   OperationID: GetFunctionResultTypeList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetFunctionResultTypeList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFunctionResultTypeList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetBookVarTypeList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetBookVarTypeList
   Description: Returns the list of available data types for the Book/Function variable
   OperationID: GetBookVarTypeList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetBookVarTypeList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBookVarTypeList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCommonTypeList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCommonTypeList
   Description: Returns the list of available types for the variable type
   OperationID: GetCommonTypeList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCommonTypeList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCommonTypeList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetFormulaPhraseItems(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetFormulaPhraseItems
   Description: Returns data for Formula combo
   OperationID: GetFormulaPhraseItems
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetFormulaPhraseItems_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFormulaPhraseItems_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRelatedContextItemsBookVarType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRelatedContextItemsBookVarType
   OperationID: GetRelatedContextItemsBookVarType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRelatedContextItemsBookVarType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRelatedContextItemsBookVarType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRelatedContextItemsFunctionResultType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRelatedContextItemsFunctionResultType
   OperationID: GetRelatedContextItemsFunctionResultType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRelatedContextItemsFunctionResultType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRelatedContextItemsFunctionResultType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRelatedContextItemsFuncOper(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRelatedContextItemsFuncOper
   OperationID: GetRelatedContextItemsFuncOper
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRelatedContextItemsFuncOper_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRelatedContextItemsFuncOper_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ABTAmountRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ABTAmountRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ABTDocLineRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ABTDocLineRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ABTPostCodeRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ABTPostCodeRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ABTPostEntityRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ABTPostEntityRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ABTQParamRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ABTQParamRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ABTQueryRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ABTQueryRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ACTBookRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ACTBookRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ACTRevisionRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ACTRevisionRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ACTTypeListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ACTTypeListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ACTTypeRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ACTTypeRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BRFuncArgsRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_BRFuncArgsRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BRFuncOperationRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_BRFuncOperationRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BRFunctionRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_BRFunctionRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BROperationCustomRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_BROperationCustomRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BROperationRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_BROperationRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BookValRuleRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_BookValRuleRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BookVarRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_BookVarRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BookingRuleRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_BookingRuleRow] = obj["value"]
      pass

class Erp_Tablesets_ABTAmountRow:
   def __init__(self, obj):
      self.ACTTypeUID:int = obj["ACTTypeUID"]
      """  Reference to the GL Transaction Type.  """  
      self.ACTRevisionUID:int = obj["ACTRevisionUID"]
      """  Reference to the Revision.  """  
      self.ABTDocLineUID:int = obj["ABTDocLineUID"]
      """  Reference to the Document Line.  """  
      self.ABTAmountUID:int = obj["ABTAmountUID"]
      """  Amount UID. Technical identifier.  """  
      self.Qualifier:str = obj["Qualifier"]
      """  Identifies the amount element. Application processes use the identifier. This field is display only when the program displays an accounting transaction type used by application programs.  """  
      self.Description:str = obj["Description"]
      """  Detailed description of the Amount.  """  
      self.IsDefault:bool = obj["IsDefault"]
      """  Indicates default Amounts for VBD templates.  """  
      self.Company:str = obj["Company"]
      """  Reference to the Company.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Loaded:int = obj["Loaded"]
      """   0- not loaded on client       
1-loaded fully
2- partial  """  
      self.DevelopMode:bool = obj["DevelopMode"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ABTDocLineRow:
   def __init__(self, obj):
      self.ACTTypeUID:int = obj["ACTTypeUID"]
      """  Reference to the GL Transaction Type.  """  
      self.ACTRevisionUID:int = obj["ACTRevisionUID"]
      """  Reference to the Revision.  """  
      self.ABTDocLineUID:int = obj["ABTDocLineUID"]
      """  Document Line UID. Technical identifier.  """  
      self.Qualifier:str = obj["Qualifier"]
      """  Identifies the document line. Various application processes use the identifier.  """  
      self.IsDefault:bool = obj["IsDefault"]
      """  Indicates default entities for VBD templates.  """  
      self.DataSource:str = obj["DataSource"]
      """  Associated with the document line database table name.  """  
      self.Description:str = obj["Description"]
      """  Provides a detailed description of the document line.  """  
      self.ParentABTDocLineUID:int = obj["ParentABTDocLineUID"]
      """  Reference to the Parent document line.  """  
      self.SequenceNumber:int = obj["SequenceNumber"]
      """  An order number indicating the document line place in the sequence of lines.  """  
      self.DocLinePath:str = obj["DocLinePath"]
      """  Path in VBD structure.  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Loaded:int = obj["Loaded"]
      """   0- not loaded on client       
1-loaded fully
2- partial  """  
      self.DevelopMode:bool = obj["DevelopMode"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ABTPostCodeRow:
   def __init__(self, obj):
      self.ACTTypeUID:int = obj["ACTTypeUID"]
      """  Reference to the GL Transaction Type.  """  
      self.ACTRevisionUID:int = obj["ACTRevisionUID"]
      """  Reference to the Revision.  """  
      self.ABTDocLineUID:int = obj["ABTDocLineUID"]
      """  Reference to the Document Line UID.  """  
      self.ABTPostEntityUID:int = obj["ABTPostEntityUID"]
      """  Reference to the Post Entity.  """  
      self.ABTPostCodeUID:int = obj["ABTPostCodeUID"]
      """  Posting Code UID. Technical identifier.  """  
      self.PopulationMethod:int = obj["PopulationMethod"]
      """  Population method for the user-defined field  """  
      self.Qualifier:str = obj["Qualifier"]
      """  Identifies the posting code. Application processes use the identifier.  """  
      self.Description:str = obj["Description"]
      """  Describes the posting code. The description provides information to users of this program.  """  
      self.DataSource:str = obj["DataSource"]
      """  Associated with the Posting Code database table name.  """  
      self.DataField:str = obj["DataField"]
      """  Name of the BAQ or Table field from where the field will be populated in case it is user-defined field  """  
      self.IsDefault:bool = obj["IsDefault"]
      """  Indicates default entities for VBD templates.  """  
      self.CodeType:str = obj["CodeType"]
      """  This field stores Posting Code datatype.  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DBSchemaName:str = obj["DBSchemaName"]
      """  DBSchemaName  """  
      self.BAQDataField:str = obj["BAQDataField"]
      """  Contains Ice.QueryField.Alias  """  
      self.BAQDataSource:str = obj["BAQDataSource"]
      self.DevelopMode:bool = obj["DevelopMode"]
      self.Loaded:int = obj["Loaded"]
      """   0- not loaded on client       
1-loaded fully
2- partial  """  
      self.TableDataField:str = obj["TableDataField"]
      self.TableDataSource:str = obj["TableDataSource"]
      self.BAQDataFieldName:str = obj["BAQDataFieldName"]
      """  Contains Ice.QueryField.FieldName  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ABTPostEntityRow:
   def __init__(self, obj):
      self.ACTTypeUID:int = obj["ACTTypeUID"]
      """  Reference to the GL Transaction Type.  """  
      self.ACTRevisionUID:int = obj["ACTRevisionUID"]
      """  Reference to the Revision.  """  
      self.ABTDocLineUID:int = obj["ABTDocLineUID"]
      """  Reference to the Document Line.  """  
      self.ABTPostEntityUID:int = obj["ABTPostEntityUID"]
      """  Post Entity UID. Technical identifier.  """  
      self.Qualifier:str = obj["Qualifier"]
      """  Identifies the entity element. Application processes use the identifier.  """  
      self.Description:str = obj["Description"]
      """  Describes the entity. The description provides information to users of this program.  """  
      self.IsDefault:bool = obj["IsDefault"]
      """  Indicates default entities for VBD templates.  """  
      self.SequenceNumber:int = obj["SequenceNumber"]
      """  An order number indicating the Post Entity place in the sequence of Post Entyties.  """  
      self.IsReference:bool = obj["IsReference"]
      """  Indicates if this entity stores keys for reference GLControl.  """  
      self.DataSource:str = obj["DataSource"]
      """  Identifies the table used to supply data for posting codes or amount elements that belong to the entity.  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DBSchemaName:str = obj["DBSchemaName"]
      """  DBSchemaName  """  
      self.DevelopMode:bool = obj["DevelopMode"]
      self.Loaded:int = obj["Loaded"]
      """   0- not loaded on client       
1-loaded fully
2- partial  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ABTQParamRow:
   def __init__(self, obj):
      self.BAQParamLinkUID:int = obj["BAQParamLinkUID"]
      """  BAQ Param Link UID.  """  
      self.ABTQueryUID:int = obj["ABTQueryUID"]
      """  Reference to the Query.  """  
      self.ACTRevisionUID:int = obj["ACTRevisionUID"]
      """  Reference to the Revision.  """  
      self.ACTTypeUID:int = obj["ACTTypeUID"]
      """  Reference to the GL Transaction Type.  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BAQParam:str = obj["BAQParam"]
      """  Paremeter in BAQ.  """  
      self.ABTBAQParam:str = obj["ABTBAQParam"]
      """  Parameter from the current Query.  """  
      self.ABTDocLineUID:int = obj["ABTDocLineUID"]
      """  Reference to the Document Line.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Loaded:int = obj["Loaded"]
      """   0- not loaded on client       
1-loaded fully
2- partial  """  
      self.DevelopMode:bool = obj["DevelopMode"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ABTQueryRow:
   def __init__(self, obj):
      self.ABTQueryUID:int = obj["ABTQueryUID"]
      """  Query UID. Technical key.  """  
      self.BAQID:str = obj["BAQID"]
      """  Reference to Business Activity Query.  """  
      self.ACTRevisionUID:int = obj["ACTRevisionUID"]
      """  Reference to the Revision.  """  
      self.ACTTypeUID:int = obj["ACTTypeUID"]
      """  Reference to the GL Transaction Type.  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.IsDefault:bool = obj["IsDefault"]
      """  Indicates default Queries for VBD templates.  """  
      self.ABTDocLineUID:int = obj["ABTDocLineUID"]
      """  Reference to the Document Line.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BAQDescription:str = obj["BAQDescription"]
      self.Loaded:int = obj["Loaded"]
      """   0- not loaded on client       
1-loaded fully
2- partial  """  
      self.DevelopMode:bool = obj["DevelopMode"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ACTBookRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Reference to the Company  """  
      self.BookID:str = obj["BookID"]
      """  Reference to the Book  """  
      self.Description:str = obj["Description"]
      """  Provides a description of the book. This field is display-only.  """  
      self.BookCurrency:str = obj["BookCurrency"]
      """  Currency of the Book  """  
      self.BOOKType:str = obj["BOOKType"]
      """  Type of Book  """  
      self.COAID:str = obj["COAID"]
      """  Reference to the COA  """  
      self.ACTRevisionUID:int = obj["ACTRevisionUID"]
      """  Reference to the Revision.  """  
      self.ActiveFlag:int = obj["ActiveFlag"]
      """  Yes, if Book is Active  """  
      self.DefaultBook:bool = obj["DefaultBook"]
      """  Yes, If the book is default  """  
      self.MapBookID:str = obj["MapBookID"]
      """  Reference to the book, that transaction will be used.  """  
      self.COAMapUID:int = obj["COAMapUID"]
      """  Reference to the COA Map.  """  
      self.UseMapFlag:bool = obj["UseMapFlag"]
      """  Yes, If mapping will be used.If no- booking rules will be used for creation of transaction.  """  
      self.ACTTypeUID:int = obj["ACTTypeUID"]
      """  Reference to the GL Transaction Type.  """  
      self.Summarize:int = obj["Summarize"]
      """   0)      Summarize (default)
1)      Summarize debit and credits separately
2)      No summarization
3)     Override  """  
      self.IsDefault:bool = obj["IsDefault"]
      """  Indicates default books for VBD templates.  """  
      self.MapType:int = obj["MapType"]
      """  Shows what will be used for transaction creating, 0 - Booking Rules, 1 -  COA Mapping, 2 - Direct  """  
      self.TranCurr:int = obj["TranCurr"]
      """  Transactional currency, Indicates what currency to use in book mapping. [0] -  is document , [1]  is source book's currency, used  in book mapping.  """  
      self.ABTVer:str = obj["ABTVer"]
      """  VBD Version  """  
      self.PatchABTVer:str = obj["PatchABTVer"]
      """  Patch VBD Version  """  
      self.RulesetVer:int = obj["RulesetVer"]
      """  Specifies the rule set version. Uses a single numeric sequence and increments every time a rule in the rule set changes.  """  
      self.PatchRulesetVer:int = obj["PatchRulesetVer"]
      """  Specifies the patch rule set version. Uses a single numeric sequence and increments each time a change is released in a patch to a client between service packs. The patch version resets to zero every time a service pack is released.  """  
      self.Package:str = obj["Package"]
      """  Package  """  
      self.Modified:bool = obj["Modified"]
      """  Indicates that Rulese was modified  """  
      self.PrevModified:bool = obj["PrevModified"]
      """  Value of Modified filed before last Update versions  """  
      self.ManuallyUpdVer:bool = obj["ManuallyUpdVer"]
      """  Indicates that Versions were updated manually  """  
      self.UpdatePatchVer:bool = obj["UpdatePatchVer"]
      """  Indicates that Patch Verstion were updated last time  """  
      self.BasePackage:str = obj["BasePackage"]
      """  Specifies the package name (for example, Standard, Extended, Russia) of the assigned rules set (posting rules, functions, and variables) and is used to automatically upgrade rule sets in packages that Epicor supports.  """  
      self.LocRulesetVer:int = obj["LocRulesetVer"]
      """  Localization Ruleset Version  """  
      self.LocPrevRulesetVer:int = obj["LocPrevRulesetVer"]
      """  Value of LocRulesetVer filed before last Update versions  """  
      self.LocPatchRulesetVer:int = obj["LocPatchRulesetVer"]
      """  Localization Patch Ruleset Version  """  
      self.LocPrevPatchRulesetVer:int = obj["LocPrevPatchRulesetVer"]
      """  Value of LocPatchRulesetVer filed before last Update versions  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.EnableCustomization:bool = obj["EnableCustomization"]
      """  Enabling/disabling customization for the Book  """  
      self.PartiallyUpdated:bool = obj["PartiallyUpdated"]
      """  Identifies that ruleset was partially updated during conversion for revision using common dll  """  
      self.Loaded:int = obj["Loaded"]
      """   0- not loaded on client       
1-loaded fully
2- partial  """  
      self.MapBookCOAID:str = obj["MapBookCOAID"]
      self.DevelopMode:bool = obj["DevelopMode"]
      self.DisableBookMapping:bool = obj["DisableBookMapping"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ACTRevisionRow:
   def __init__(self, obj):
      self.ACTRevisionUID:int = obj["ACTRevisionUID"]
      """  Unique Revision Identifier.  """  
      self.ACTTypeUID:int = obj["ACTTypeUID"]
      """  Reference to the GL Transaction Type.  """  
      self.RevisionCode:str = obj["RevisionCode"]
      """  A user-defined code of revision (unique within one account transaction type).  """  
      self.RevisionStatus:str = obj["RevisionStatus"]
      """   Status of the Revision. Allowed values are: "Active", "Draft", "Blocked". 
Active - indicates that exactly this Revision of an GL Transaction Type will be used when functional module initiates a corresponding business event. As soon as a Revision becomes "Active", it should become read-only for user. Only one Revision for each GL Transaction Type may be "Active".
 
Draft -  indicates a newly created Revision, which will not be used in any run-time processing. Each newly created Revision should automatically be put into "Draft" status. "Draft" Revision is open for editing. Each GL Transaction Type may have any number of Draft Revisions.
Blocked - indicates a Revision which was previously "Active" but is not anymore and is stored for traceability purposes. The "Blocked" Revision should be read-only.  """  
      self.Description:str = obj["Description"]
      """  Revision description.  """  
      self.SendToReviewJournal:bool = obj["SendToReviewJournal"]
      """  Yes- then all transaction will leave in Review Journal. User must confirm it manually, No - transaction will be created in GLJournal or left in Review Journal if the transaction is not valid.  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.IsDefault:bool = obj["IsDefault"]
      """  Indicates default Revisions for VBD templates.  """  
      self.RType:str = obj["RType"]
      """  Standard or Exteded  """  
      self.ABTVer:str = obj["ABTVer"]
      """  Version of VBD Stucture. If version is changed , VBD Structure merge process will be started during conversion.  """  
      self.VersionUID:int = obj["VersionUID"]
      """  Version of build, is used to save time and don't recompile revison each time.  """  
      self.PrevABTVer:str = obj["PrevABTVer"]
      """  Value of ABTVer field before last Update Versions  """  
      self.PatchABTVer:str = obj["PatchABTVer"]
      """  Patch VBD Version  """  
      self.PrevPatchABTVer:str = obj["PrevPatchABTVer"]
      """  Value of PatchABTVer field before last Update Versions  """  
      self.LocVer:int = obj["LocVer"]
      """  Localization Version  """  
      self.PatchLocVer:int = obj["PatchLocVer"]
      """  Patch Localizasion Version  """  
      self.UpdatePatchVer:bool = obj["UpdatePatchVer"]
      """  Indicates tha patch version was updated last time  """  
      self.Modified:bool = obj["Modified"]
      """  Indicates that Revision data were modified  """  
      self.PrevModified:bool = obj["PrevModified"]
      """  Value of Modified field before last Update Versions  """  
      self.ManuallyUpdVer:bool = obj["ManuallyUpdVer"]
      """  Indicates that Version was updated manually  """  
      self.NeedPrePostUpdate:bool = obj["NeedPrePostUpdate"]
      """  Indicates that VBD structure was changed and demand changes in Pre_Post Code  """  
      self.PrevRevisionStatus:str = obj["PrevRevisionStatus"]
      """  Value of RevisionStatus field before last Update Versions  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PendingConversion:bool = obj["PendingConversion"]
      """  Indicates that the Revision was not updated during conversion 'Import GL Transaction Types' because of segment mapping error. After correction Segment Mapping on GL Book Entry, conversion can be run again.  """  
      self.CanUseSysAssembly:bool = obj["CanUseSysAssembly"]
      """  Identifies that common dll can be used for this revision  """  
      self.PostAssemblyName:str = obj["PostAssemblyName"]
      """  Name of posting assembly  """  
      self.Loaded:int = obj["Loaded"]
      """   0- not loaded on client       
1-loaded fully
2- partial  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ACTTypeListRow:
   def __init__(self, obj):
      self.ACTTypeUID:int = obj["ACTTypeUID"]
      """  Unique GL Transaction Type Identifier.  """  
      self.DisplayName:str = obj["DisplayName"]
      """  Name of the GL Tranaction Type to be displayed in the tree view navigation control.  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.DetailedDescription:str = obj["DetailedDescription"]
      """  Describes the GL Transaction Type. The description provades information to users of this program  """  
      self.Limited:bool = obj["Limited"]
      """  Yes - if the transaction type has not VBD and Booking Rules,has just one Active Revision. Posting in this case is hard coded.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ACTTypeRow:
   def __init__(self, obj):
      self.ACTTypeUID:int = obj["ACTTypeUID"]
      """  Unique GL Transaction Type Identifier.  """  
      self.DisplayName:str = obj["DisplayName"]
      """  Name of the GL Tranaction Type to be displayed in the tree view navigation control.  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.DetailedDescription:str = obj["DetailedDescription"]
      """  Describes the GL Transaction Type. The description provades information to users of this program  """  
      self.Limited:bool = obj["Limited"]
      """  Yes - if the transaction type has not VBD and Booking Rules,has just one Active Revision. Posting in this case is hard coded.  """  
      self.IsLog:bool = obj["IsLog"]
      """  Flag to enable logging of the GL Transaction Type.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ConversionErrors:bool = obj["ConversionErrors"]
      """  Indicates that an error occurred during update of the GL Transaction Type in conversion program 'Import GL Transaction Types'  """  
      self.Loaded:int = obj["Loaded"]
      """   0- not loaded on client       
1-loaded fully
2- partial  """  
      self.IsLocked:bool = obj["IsLocked"]
      self.LockStatus:str = obj["LockStatus"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_BRFuncArgsRow:
   def __init__(self, obj):
      self.FunctionUID:int = obj["FunctionUID"]
      """  Reference to the Parent function UID.  """  
      self.ArgName:str = obj["ArgName"]
      """  Name of function argument  """  
      self.ArgType:str = obj["ArgType"]
      """  Type of function argument  """  
      self.PRGName:str = obj["PRGName"]
      """  Technical name  """  
      self.PRGType:str = obj["PRGType"]
      """  Technical type  """  
      self.ACTRevisionUID:int = obj["ACTRevisionUID"]
      """  Reference to the Revision  """  
      self.ACTTypeUID:int = obj["ACTTypeUID"]
      """  Reference to the GL Transaction Type.  """  
      self.ArgumentUID:int = obj["ArgumentUID"]
      """  Unique Argument identifier.  """  
      self.Company:str = obj["Company"]
      """  Reference to  the company  """  
      self.IsDefault:bool = obj["IsDefault"]
      """  Indicates default Function Arguments for ABT templates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Loaded:int = obj["Loaded"]
      """   0- not loaded on client       
1-loaded fully
2- partial  """  
      self.DevelopMode:bool = obj["DevelopMode"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_BRFuncOperationRow:
   def __init__(self, obj):
      self.OperationUID:int = obj["OperationUID"]
      """  Operation unique ID. Technical identifier.  """  
      self.ParentOperationUID:int = obj["ParentOperationUID"]
      """  Reference to the parent operation (necessary to support the hierarchical operations structure; references the OperationUID field in the same table).  """  
      self.ControlFlowOperator:str = obj["ControlFlowOperator"]
      """  The identifier of the control flow operator.  """  
      self.Container:str = obj["Container"]
      """  The identifier of the target container.  """  
      self.Formula:str = obj["Formula"]
      """  The name of formula.  """  
      self.SequenceNumber:int = obj["SequenceNumber"]
      """  An order number indicating the operation?s place in the sequence of execution ? for the whole set of ruleset?s operations.  """  
      self.ChildSequenceNumber:int = obj["ChildSequenceNumber"]
      """  An order number indicating the operation?s place in the sequence of execution ? for a single block of operations on a single hierarchy level.  """  
      self.FunctionUID:int = obj["FunctionUID"]
      """  System ID of used function.  """  
      self.PRGText:str = obj["PRGText"]
      """  Technical text of the function(formula)  """  
      self.ACTRevisionUID:int = obj["ACTRevisionUID"]
      """  Reference to the Revision.  """  
      self.ACTTypeUID:int = obj["ACTTypeUID"]
      """  Reference to the GL Transaction Type.  """  
      self.FuncOperUID:int = obj["FuncOperUID"]
      """  Reference to the Function of the GL Transaction Type.  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PRGContainer:str = obj["PRGContainer"]
      """  The identifier of the target container.  """  
      self.IsDefault:bool = obj["IsDefault"]
      """  Indicates default Function Operations for ABT templates.  """  
      self.LocModified:bool = obj["LocModified"]
      """  LocModified  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DevelopMode:bool = obj["DevelopMode"]
      self.Loaded:int = obj["Loaded"]
      """   0- not loaded on client       
1-loaded fully
2- partial  """  
      self.ErrorText:str = obj["ErrorText"]
      """  Contains error text in generated code.  """  
      self.IsError:bool = obj["IsError"]
      """  Allow use icon easier.  """  
      self.ContainerType:str = obj["ContainerType"]
      """  Unified container type for both Operation and Logical Condition types  """  
      self.IsLogicalCondition:bool = obj["IsLogicalCondition"]
      """  Indicates 'Logical Condition' type of the operation  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_BRFunctionRow:
   def __init__(self, obj):
      self.FunctionUID:int = obj["FunctionUID"]
      """  Unique Function identifier.  """  
      self.Name:str = obj["Name"]
      """  Name of the function.  """  
      self.PRGName:str = obj["PRGName"]
      """  Technical name of function  """  
      self.IsSystem:bool = obj["IsSystem"]
      """  If the function is system.  """  
      self.Description:str = obj["Description"]
      """  Detail description for function.  """  
      self.ResultType:str = obj["ResultType"]
      """  Type of function result.  """  
      self.PRGPattern:str = obj["PRGPattern"]
      """  Technical text of function.  """  
      self.ACTRevisionUID:int = obj["ACTRevisionUID"]
      """  Reference to the Revisions.  """  
      self.ACTTypeUID:int = obj["ACTTypeUID"]
      """  Reference to the GL Transaction Type  """  
      self.BookID:str = obj["BookID"]
      """  Reference to Book.  """  
      self.Formula:str = obj["Formula"]
      """  Text of function  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.DocLinePath:str = obj["DocLinePath"]
      """  Text field to store the For Each criteria expression .  """  
      self.IsDefault:bool = obj["IsDefault"]
      """  Indicates default Functions for ABT templates.  """  
      self.ManuallyUpdVer:bool = obj["ManuallyUpdVer"]
      """  ManuallyUpdVer  """  
      self.FuncVer:int = obj["FuncVer"]
      """  Specifies the function version. Uses a single numeric sequence and increments every time a change is made in a corresponding rule.  """  
      self.PatchFuncVer:int = obj["PatchFuncVer"]
      """  PatchFuncVer  """  
      self.PrevModified:bool = obj["PrevModified"]
      """  PrevModified  """  
      self.Modified:bool = obj["Modified"]
      """  Modified  """  
      self.LocVer:int = obj["LocVer"]
      """  LocVer  """  
      self.LocPatchVer:int = obj["LocPatchVer"]
      """  LocPatchVer  """  
      self.LocModified:bool = obj["LocModified"]
      """  LocModified  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Loaded:int = obj["Loaded"]
      """   0- not loaded on client       
1-loaded fully
2- partial  """  
      self.DevelopMode:bool = obj["DevelopMode"]
      self.IsError:bool = obj["IsError"]
      """  Is used to show icon in Tree.  """  
      self.ErrorText:str = obj["ErrorText"]
      """  Contains error text for a function.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_BROperationCustomRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Indetifier.  """  
      self.ACTTypeUID:int = obj["ACTTypeUID"]
      """  Reference to the GL Transaction Type.  """  
      self.ACTRevisionUID:int = obj["ACTRevisionUID"]
      """  Reference to the Revision.  """  
      self.BookID:str = obj["BookID"]
      """  Reference to the Book.  """  
      self.RuleUID:int = obj["RuleUID"]
      """  Reference to the parent booking rule.  """  
      self.OperationUID:int = obj["OperationUID"]
      """  Operation unique ID. Technical identifier.  """  
      self.ParentOperationUID:int = obj["ParentOperationUID"]
      """  Reference to the parent operation  """  
      self.ChildSequenceNumber:int = obj["ChildSequenceNumber"]
      """  An order number indicating the operation’s place in the sequence of execution.  """  
      self.ControlFlowOperator:str = obj["ControlFlowOperator"]
      """  The identifier of the control flow operator.  """  
      self.Container:str = obj["Container"]
      """  The identifier of the target container.  """  
      self.Formula:str = obj["Formula"]
      """  The operation's main formula.  """  
      self.FunctionUID:int = obj["FunctionUID"]
      """  Function unique ID.  """  
      self.PRGText:str = obj["PRGText"]
      """  Code for operation  """  
      self.PRGContainer:str = obj["PRGContainer"]
      """  The identifier of the target container.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  Audit column. Populate UserID who created the row.  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  Audit column. Populate time of creation row.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Audit column. Populate UserID of last person who updated the row.  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  Audit column. Populate time of updating the row.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Loaded:int = obj["Loaded"]
      """   0- not loaded on client       
1-loaded fully
2- partial  """  
      self.ErrorText:str = obj["ErrorText"]
      """  Contains error text in generated code.  """  
      self.IsError:bool = obj["IsError"]
      """  Allow use icon easier.  """  
      self.ContainerType:str = obj["ContainerType"]
      """  Unified container type for both Operation and Logical Condition types  """  
      self.IsLogicalCondition:bool = obj["IsLogicalCondition"]
      """  Indicates 'Logical Condition' type of the operation  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_BROperationRow:
   def __init__(self, obj):
      self.OperationUID:int = obj["OperationUID"]
      """  Operation unique ID. Technical identifier.  """  
      self.RuleUID:int = obj["RuleUID"]
      """  Reference to the parent booking rule.  """  
      self.ParentOperationUID:int = obj["ParentOperationUID"]
      """  Reference to the parent operation (necessary to support the hierarchical operations structure; references the OperationUID field in the same table).  """  
      self.ControlFlowOperator:str = obj["ControlFlowOperator"]
      """  The identifier of the control flow operator.  """  
      self.Container:str = obj["Container"]
      """  The identifier of the target container.  """  
      self.Formula:str = obj["Formula"]
      """  The operation's main formula.  """  
      self.SequenceNumber:int = obj["SequenceNumber"]
      """  An order number indicating the operation?s place in the sequence of execution ? for the whole set of ruleset?s operations.  """  
      self.ChildSequenceNumber:int = obj["ChildSequenceNumber"]
      """  An order number indicating the operation?s place in the sequence of execution ? for a single block of operations on a single hierarchy level.  """  
      self.FunctionUID:int = obj["FunctionUID"]
      """  Function unique ID. Technical identifier.  """  
      self.PRGText:str = obj["PRGText"]
      """  Progress Code for operation  """  
      self.ACTRevisionUID:int = obj["ACTRevisionUID"]
      """  Reference to the Revision.  """  
      self.ACTTypeUID:int = obj["ACTTypeUID"]
      """  Reference to the GL Transaction Type.  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PRGContainer:str = obj["PRGContainer"]
      """  The identifier of the target container.  """  
      self.BookID:str = obj["BookID"]
      """  Reference to the Book.  """  
      self.IsDefault:bool = obj["IsDefault"]
      """  Indicates default Operations for ABT templates.  """  
      self.LocModified:bool = obj["LocModified"]
      """  LocModified  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ContainerType:str = obj["ContainerType"]
      """  Unified container type for both Operation and Logical Condition types  """  
      self.DevelopMode:bool = obj["DevelopMode"]
      self.Loaded:int = obj["Loaded"]
      """   0- not loaded on client       
1-loaded fully
2- partial  """  
      self.ErrorText:str = obj["ErrorText"]
      """  Contains error text in generated code.  """  
      self.IsError:bool = obj["IsError"]
      """  Allow use icon easier.  """  
      self.LLink01:str = obj["LLink01"]
      """  Field to support functionality of link-combo in Kinetic (Container in operations)  """  
      self.IsLogicalCondition:bool = obj["IsLogicalCondition"]
      """  Indicates 'Logical Condition' type of the operation  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_BookValRuleRow:
   def __init__(self, obj):
      self.BVRuleUID:int = obj["BVRuleUID"]
      """  Unique value.Primary key  """  
      self.VRuleUID:int = obj["VRuleUID"]
      """  Technical key of Validation Rule  """  
      self.Description:str = obj["Description"]
      """  Validation rule description  """  
      self.Action:str = obj["Action"]
      """  Error, Ignor, Warning, Autocorrect, Autocorrect with warning  """  
      self.VLevel:str = obj["VLevel"]
      """  Validation level : Book, Booking Rule, Company etc  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BookID:str = obj["BookID"]
      """  Reference to Book.  """  
      self.ACTTypeUID:int = obj["ACTTypeUID"]
      """  Account transaction type UID. Technical identifier.  """  
      self.ACTRevisionUID:int = obj["ACTRevisionUID"]
      """  Reference to the parent account transaction revision.  """  
      self.RuleUID:int = obj["RuleUID"]
      """  Technical identifier.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.IsDefault:bool = obj["IsDefault"]
      """  Indicates default validation rules for ABT templates.  """  
      self.ActionList:str = obj["ActionList"]
      """  List of actions (used in combo boxes).  """  
      self.RuleType:str = obj["RuleType"]
      """  RuleType - PrePost(calculation in pre-post mode before posting), Post(standard posting) or Ref (Calculate reference GLControl during posting)  """  
      self.Loaded:int = obj["Loaded"]
      """   0- not loaded on client       
1-loaded fully
2- partial  """  
      self.DevelopMode:bool = obj["DevelopMode"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_BookVarRow:
   def __init__(self, obj):
      self.ACTTypeUID:int = obj["ACTTypeUID"]
      """  Reference to the GL Transaction Type.  """  
      self.ACTRevisionUID:int = obj["ACTRevisionUID"]
      """  Reference to the Revision.  """  
      self.BookID:str = obj["BookID"]
      """  Reference to the Book  """  
      self.BookVarUID:int = obj["BookVarUID"]
      """  BookVar unique ID.  """  
      self.VarName:str = obj["VarName"]
      """  Variable Name  """  
      self.VarType:str = obj["VarType"]
      """  Variable Type  """  
      self.vType:str = obj["vType"]
      """  Variable context, possible values: Global, Book, Rule, Function.  """  
      self.vUID:int = obj["vUID"]
      """  ID of context, for example if vType = Function then vUID = FunctionUID.  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.IsDefault:bool = obj["IsDefault"]
      """  Indicates default Variables for VBD templates.  """  
      self.LocModified:bool = obj["LocModified"]
      """  LocModified  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DevelopMode:bool = obj["DevelopMode"]
      self.isSystem:bool = obj["isSystem"]
      """  the field is used for generation post program  """  
      self.Loaded:int = obj["Loaded"]
      """   0- not loaded on client       
1-loaded fully
2- partial  """  
      self.OwnerDescription:str = obj["OwnerDescription"]
      """  Function or Rule Description.  """  
      self.VarTypeDisplay:str = obj["VarTypeDisplay"]
      """  VarType display.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_BookingRuleRow:
   def __init__(self, obj):
      self.RuleUID:int = obj["RuleUID"]
      """  Technical identifier.  """  
      self.ACTRevisionUID:int = obj["ACTRevisionUID"]
      """  Reference to the Revision.  """  
      self.DisplayName:str = obj["DisplayName"]
      """  Booking rule name to be displayed in the tree view navigation control.  """  
      self.DetailedDescription:str = obj["DetailedDescription"]
      """  Booking rule detailed description.  """  
      self.SelectionCriteria:str = obj["SelectionCriteria"]
      """  Text field to store the selection criteria expression .  """  
      self.BookID:str = obj["BookID"]
      """  Reference to the Book.  """  
      self.ACTTypeUID:int = obj["ACTTypeUID"]
      """  Reference to the GL Transaction Type.  """  
      self.IsPost:bool = obj["IsPost"]
      """  It is Rule for Posting process or special for GLControl calculation.  """  
      self.ForEach:str = obj["ForEach"]
      """  Text field to store the For Each criteria expression .  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.IsHeader:bool = obj["IsHeader"]
      """  Rule run once, usual it is used for calculation Book variables or Header variables (that can be calculated once).  """  
      self.IsActive:bool = obj["IsActive"]
      """  Determines whether the posting process uses the rule.  """  
      self.CreditContext:str = obj["CreditContext"]
      """  Stores a reference to a credit context for use by another posting rule. Posting rules can create a GL control that stores the rule's output for use in subsequent processing..  """  
      self.DebitContext:str = obj["DebitContext"]
      """  Stores a reference to a debit context for use by another posting rule. Posting rules can create a GL control that stores the rule's output for use in subsequent processing.  """  
      self.RefContext:str = obj["RefContext"]
      """  Reference  Context is used for pre-Posting rules  """  
      self.GLControlType:str = obj["GLControlType"]
      """  Determines the GL control type that applies to the rule. The control type affects the processing of accounts generated by the rule. Pre-posting GL controls use the type to determine the reference context, used to set the default for a GL account field. The type also controls the credit and debit contexts for posting rules.  """  
      self.IsDefault:bool = obj["IsDefault"]
      """  Indicates default Rules for ABT templates.  """  
      self.Entity:str = obj["Entity"]
      """  Primary key from the Entity is a source of keys for TranGLC table that save Reference control of the Booking Rule.  """  
      self.IsReference:bool = obj["IsReference"]
      """  IsReference  """  
      self.ManuallyUpdVer:bool = obj["ManuallyUpdVer"]
      """  Indicates that Versions were updated manually  """  
      self.RuleVer:int = obj["RuleVer"]
      """  Specifies the individual rule version. Uses a single numeric sequence and increments every time a change is made in a corresponding rule.  """  
      self.PatchRuleVer:int = obj["PatchRuleVer"]
      """  Specifies the individual rule patch version. Uses a single numeric sequence and increments each time a change is released in a patch to a client between service packs. The patch version resets to zero every time a service pack is released.  """  
      self.PrevModified:bool = obj["PrevModified"]
      """  Value of Modified field before last Update Versions  """  
      self.Modified:bool = obj["Modified"]
      """  Indicates that data were modified  """  
      self.LocVer:int = obj["LocVer"]
      """  LocVer  """  
      self.LocPatchVer:int = obj["LocPatchVer"]
      """  LocPatchVer  """  
      self.LocModified:bool = obj["LocModified"]
      """  LocModified  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.EnableCustomization:bool = obj["EnableCustomization"]
      """  Enabling/disabling customization for the Book  """  
      self.BaseModified:bool = obj["BaseModified"]
      """  Indicates that base information on rule was changed. In this case this rule will not be automatically updated during converstion program to save user's changes.  """  
      self.Customization:bool = obj["Customization"]
      """  Indicates that rule contaion operations on 'Customization' part  """  
      self.Operator:str = obj["Operator"]
      """  Used to bind UI control.  """  
      self.SelCriteriaDisplay:str = obj["SelCriteriaDisplay"]
      """  Selection Criteria Display.  """  
      self.Argument:str = obj["Argument"]
      """  Used to bind UI control.  """  
      self.DevelopMode:bool = obj["DevelopMode"]
      self.Loaded:int = obj["Loaded"]
      """   0- not loaded on client       
1-loaded fully
2- partial  """  
      self.RuleType:str = obj["RuleType"]
      """  RuleType - PrePost(calculation in pre-post mode before posting), Post(standard posting) or Ref (Calculate reference GLControl during posting)  """  
      self.IsError:bool = obj["IsError"]
      """  Is used to show icon in Tree.  """  
      self.ErrorText:str = obj["ErrorText"]
      """  Contains error text for a rule.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class ABTBookGetNewExt_input:
   """ Required : 
   actTypeUID
   actRevisionUID
   bookID
   ds
   """  
   def __init__(self, obj):
      self.actTypeUID:int = obj["actTypeUID"]
      self.actRevisionUID:int = obj["actRevisionUID"]
      self.bookID:str = obj["bookID"]
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

class ABTBookGetNewExt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ABTBookGetNew_input:
   """ Required : 
   actTypeUID
   actRevisionUID
   bookID
   ds
   """  
   def __init__(self, obj):
      self.actTypeUID:int = obj["actTypeUID"]
      """  aCTTypeUID  """  
      self.actRevisionUID:int = obj["actRevisionUID"]
      """  actRevisionUID  """  
      self.bookID:str = obj["bookID"]
      """  Book ID  """  
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

class ABTBookGetNew_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ABTDocLineGetNew_input:
   """ Required : 
   actTypeUID
   actRevisionUID
   parentAbtDocLineUID
   ds
   """  
   def __init__(self, obj):
      self.actTypeUID:int = obj["actTypeUID"]
      """  aCTTypeUID  """  
      self.actRevisionUID:int = obj["actRevisionUID"]
      """  actRevisionUID  """  
      self.parentAbtDocLineUID:int = obj["parentAbtDocLineUID"]
      """  Parent ABTDocLineUID  """  
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

class ABTDocLineGetNew_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ABTPostCodeGetNew_input:
   """ Required : 
   actTypeUID
   actRevisionUID
   abtDocLineUID
   abtPostEntityUID
   developMode
   ds
   """  
   def __init__(self, obj):
      self.actTypeUID:int = obj["actTypeUID"]
      """  actTypeUID  """  
      self.actRevisionUID:int = obj["actRevisionUID"]
      """  actRevisionUID  """  
      self.abtDocLineUID:int = obj["abtDocLineUID"]
      """  abtDocLineUID  """  
      self.abtPostEntityUID:int = obj["abtPostEntityUID"]
      """  abtPostEntityUID  """  
      self.developMode:bool = obj["developMode"]
      """  Developer Mode  """  
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

class ABTPostCodeGetNew_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class AddMappedBook_input:
   """ Required : 
   actTypeUID
   actRevisionUID
   mapBookID
   scrBookID
   coaMapUID
   tranCurr
   """  
   def __init__(self, obj):
      self.actTypeUID:int = obj["actTypeUID"]
      """  act TypeUID  """  
      self.actRevisionUID:int = obj["actRevisionUID"]
      """  ACT RevisionUID  """  
      self.mapBookID:str = obj["mapBookID"]
      """  map BookID  """  
      self.scrBookID:str = obj["scrBookID"]
      """  scr BookID  """  
      self.coaMapUID:int = obj["coaMapUID"]
      """  coa MapUID  """  
      self.tranCurr:int = obj["tranCurr"]
      """  tran Curr  """  
      pass

class AddMappedBook_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.newRevUID:int = obj["parameters"]
      pass

      """  output parameters  """  

class AddMultipleBooks_input:
   """ Required : 
   actTypeUID
   actRevisionUID
   bookIDList
   ds
   """  
   def __init__(self, obj):
      self.actTypeUID:int = obj["actTypeUID"]
      self.actRevisionUID:int = obj["actRevisionUID"]
      self.bookIDList:str = obj["bookIDList"]
      """  "~" separated list of books  """  
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

class AddMultipleBooks_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class AfterDeleteBookItem_input:
   """ Required : 
   developMode
   aCTTypeUID
   aCTRevisionUID
   bookID
   ds
   """  
   def __init__(self, obj):
      self.developMode:bool = obj["developMode"]
      """  DevelopMode flag  """  
      self.aCTTypeUID:int = obj["aCTTypeUID"]
      """  ACTTypeUID of deleted row  """  
      self.aCTRevisionUID:int = obj["aCTRevisionUID"]
      """  ACTRevisionUID of deleted row  """  
      self.bookID:str = obj["bookID"]
      """  BookID of deleted row  """  
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

class AfterDeleteBookItem_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class AfterDeleteFunctionItem_input:
   """ Required : 
   developMode
   aCTTypeUID
   aCTRevisionUID
   bookID
   functionUID
   ds
   """  
   def __init__(self, obj):
      self.developMode:bool = obj["developMode"]
      """  DevelopMode flag  """  
      self.aCTTypeUID:int = obj["aCTTypeUID"]
      """  ACTTypeUID of deleted row  """  
      self.aCTRevisionUID:int = obj["aCTRevisionUID"]
      """  ACTRevisionUID of deleted row  """  
      self.bookID:str = obj["bookID"]
      """  BookID of deleted row  """  
      self.functionUID:int = obj["functionUID"]
      """  FunctionUID of deleted row  """  
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

class AfterDeleteFunctionItem_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class AfterDeleteRuleItem_input:
   """ Required : 
   developMode
   aCTTypeUID
   aCTRevisionUID
   bookID
   ruleUID
   ds
   """  
   def __init__(self, obj):
      self.developMode:bool = obj["developMode"]
      """  DevelopMode flag  """  
      self.aCTTypeUID:int = obj["aCTTypeUID"]
      """  ACTTypeUID of deleted row  """  
      self.aCTRevisionUID:int = obj["aCTRevisionUID"]
      """  ACTRevisionUID of deleted row  """  
      self.bookID:str = obj["bookID"]
      """  BookID of deleted row  """  
      self.ruleUID:int = obj["ruleUID"]
      """  RuleUID of deleted row  """  
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

class AfterDeleteRuleItem_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class AfterDeleteVBDItem_input:
   """ Required : 
   developMode
   aCTTypeUID
   aCTRevisionUID
   ds
   """  
   def __init__(self, obj):
      self.developMode:bool = obj["developMode"]
      """  DevelopMode flag  """  
      self.aCTTypeUID:int = obj["aCTTypeUID"]
      """  ACTTypeUID of deleted row  """  
      self.aCTRevisionUID:int = obj["aCTRevisionUID"]
      """  ACTRevisionUID of deleted row  """  
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

class AfterDeleteVBDItem_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class BAQDataFieldChanging_input:
   """ Required : 
   proposedValue
   BAQID
   ds
   """  
   def __init__(self, obj):
      self.proposedValue:str = obj["proposedValue"]
      self.BAQID:str = obj["BAQID"]
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

class BAQDataFieldChanging_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class BRFuncOperationGetNew_input:
   """ Required : 
   actTypeUID
   actRevisionUID
   functionUID
   operationUID
   chldSequenceNumber
   ds
   """  
   def __init__(self, obj):
      self.actTypeUID:int = obj["actTypeUID"]
      """  aCTTypeUID  """  
      self.actRevisionUID:int = obj["actRevisionUID"]
      """  actRevisionUID  """  
      self.functionUID:int = obj["functionUID"]
      """  functionUID  """  
      self.operationUID:int = obj["operationUID"]
      """  operationUID  """  
      self.chldSequenceNumber:int = obj["chldSequenceNumber"]
      """  childSequenceNumber  """  
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

class BRFuncOperationGetNew_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.chldSequenceNumber:int = obj["parameters"]
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class BRFuncOperationUpdateContainerFormula_input:
   """ Required : 
   sTypeFull
   lcdsContainer
   dsSub
   ds
   """  
   def __init__(self, obj):
      self.sTypeFull:str = obj["sTypeFull"]
      self.lcdsContainer:list[Erp_Tablesets_LinkComboDataTableset] = obj["lcdsContainer"]
      self.dsSub:list[Erp_Tablesets_ACTTypeSubDataTableset] = obj["dsSub"]
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

class BRFuncOperationUpdateContainerFormula_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.lcdsContainer:list[Erp_Tablesets_LinkComboDataTableset] = obj["lcdsContainer"]
      self.dsSub:list[Erp_Tablesets_ACTTypeSubDataTableset] = obj["dsSub"]
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class BRFuncOperationUpdateContainer_input:
   """ Required : 
   sTypeFull
   lcdsContainer
   dsSub
   ds
   """  
   def __init__(self, obj):
      self.sTypeFull:str = obj["sTypeFull"]
      self.lcdsContainer:list[Erp_Tablesets_LinkComboDataTableset] = obj["lcdsContainer"]
      self.dsSub:list[Erp_Tablesets_ACTTypeSubDataTableset] = obj["dsSub"]
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

class BRFuncOperationUpdateContainer_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.lcdsContainer:list[Erp_Tablesets_LinkComboDataTableset] = obj["lcdsContainer"]
      self.dsSub:list[Erp_Tablesets_ACTTypeSubDataTableset] = obj["dsSub"]
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class BRFunctionPhraseElementMove_input:
   """ Required : 
   elementOrderEdited
   direction
   ds
   dsSub
   """  
   def __init__(self, obj):
      self.elementOrderEdited:int = obj["elementOrderEdited"]
      """  the value in the Order field of the edited column  """  
      self.direction:int = obj["direction"]
      """  movement direction 0 - move down, 1 - move ap  """  
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      self.dsSub:list[Erp_Tablesets_ACTTypeSubDataTableset] = obj["dsSub"]
      pass

class BRFunctionPhraseElementMove_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      self.dsSub:list[Erp_Tablesets_ACTTypeSubDataTableset] = obj["dsSub"]
      pass

      """  output parameters  """  

class BRFunctionPhraseUpdate_input:
   """ Required : 
   ds
   dsSub
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      self.dsSub:list[Erp_Tablesets_ACTTypeSubDataTableset] = obj["dsSub"]
      pass

class BRFunctionPhraseUpdate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      self.dsSub:list[Erp_Tablesets_ACTTypeSubDataTableset] = obj["dsSub"]
      pass

      """  output parameters  """  

class BROPerationCustomUpdateContainerFormula_input:
   """ Required : 
   sTypeFull
   lcdsContainer
   dsSub
   ds
   """  
   def __init__(self, obj):
      self.sTypeFull:str = obj["sTypeFull"]
      self.lcdsContainer:list[Erp_Tablesets_LinkComboDataTableset] = obj["lcdsContainer"]
      self.dsSub:list[Erp_Tablesets_ACTTypeSubDataTableset] = obj["dsSub"]
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

class BROPerationCustomUpdateContainerFormula_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.lcdsContainer:list[Erp_Tablesets_LinkComboDataTableset] = obj["lcdsContainer"]
      self.dsSub:list[Erp_Tablesets_ACTTypeSubDataTableset] = obj["dsSub"]
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class BROperationCustomGetNew_input:
   """ Required : 
   actTypeUID
   actRevisionUID
   bookID
   ruleUID
   operationUID
   chldSequenceNumber
   ds
   """  
   def __init__(self, obj):
      self.actTypeUID:int = obj["actTypeUID"]
      """  aCTTypeUID  """  
      self.actRevisionUID:int = obj["actRevisionUID"]
      """  actRevisionUID  """  
      self.bookID:str = obj["bookID"]
      """  bookID  """  
      self.ruleUID:int = obj["ruleUID"]
      """  ruleUID  """  
      self.operationUID:int = obj["operationUID"]
      """  operationUID  """  
      self.chldSequenceNumber:int = obj["chldSequenceNumber"]
      """  childSequenceNumber  """  
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

class BROperationCustomGetNew_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.chldSequenceNumber:int = obj["parameters"]
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class BROperationCustomUpdateContainer_input:
   """ Required : 
   sTypeFull
   lcdsContainer
   dsSub
   ds
   """  
   def __init__(self, obj):
      self.sTypeFull:str = obj["sTypeFull"]
      self.lcdsContainer:list[Erp_Tablesets_LinkComboDataTableset] = obj["lcdsContainer"]
      self.dsSub:list[Erp_Tablesets_ACTTypeSubDataTableset] = obj["dsSub"]
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

class BROperationCustomUpdateContainer_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.lcdsContainer:list[Erp_Tablesets_LinkComboDataTableset] = obj["lcdsContainer"]
      self.dsSub:list[Erp_Tablesets_ACTTypeSubDataTableset] = obj["dsSub"]
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class BROperationGetNew_input:
   """ Required : 
   actTypeUID
   actRevisionUID
   bookID
   ruleUID
   operationUID
   chldSequenceNumber
   ds
   """  
   def __init__(self, obj):
      self.actTypeUID:int = obj["actTypeUID"]
      """  aCTTypeUID  """  
      self.actRevisionUID:int = obj["actRevisionUID"]
      """  actRevisionUID  """  
      self.bookID:str = obj["bookID"]
      """  bookID  """  
      self.ruleUID:int = obj["ruleUID"]
      """  ruleUID  """  
      self.operationUID:int = obj["operationUID"]
      """  operationUID  """  
      self.chldSequenceNumber:int = obj["chldSequenceNumber"]
      """  childSequenceNumber  """  
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

class BROperationGetNew_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.chldSequenceNumber:int = obj["parameters"]
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class BROperationUpdateContainerFormula_input:
   """ Required : 
   sTypeFull
   lcdsContainer
   dsSub
   ds
   """  
   def __init__(self, obj):
      self.sTypeFull:str = obj["sTypeFull"]
      self.lcdsContainer:list[Erp_Tablesets_LinkComboDataTableset] = obj["lcdsContainer"]
      self.dsSub:list[Erp_Tablesets_ACTTypeSubDataTableset] = obj["dsSub"]
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

class BROperationUpdateContainerFormula_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.lcdsContainer:list[Erp_Tablesets_LinkComboDataTableset] = obj["lcdsContainer"]
      self.dsSub:list[Erp_Tablesets_ACTTypeSubDataTableset] = obj["dsSub"]
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class BROperationUpdateContainer_input:
   """ Required : 
   sTypeFull
   lcdsContainer
   dsSub
   ds
   """  
   def __init__(self, obj):
      self.sTypeFull:str = obj["sTypeFull"]
      self.lcdsContainer:list[Erp_Tablesets_LinkComboDataTableset] = obj["lcdsContainer"]
      self.dsSub:list[Erp_Tablesets_ACTTypeSubDataTableset] = obj["dsSub"]
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

class BROperationUpdateContainer_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.lcdsContainer:list[Erp_Tablesets_LinkComboDataTableset] = obj["lcdsContainer"]
      self.dsSub:list[Erp_Tablesets_ACTTypeSubDataTableset] = obj["dsSub"]
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class BookIsNotEmpty_input:
   """ Required : 
   actTypeUID
   actRevisionUID
   bookID
   """  
   def __init__(self, obj):
      self.actTypeUID:int = obj["actTypeUID"]
      """  actTypeUID  """  
      self.actRevisionUID:int = obj["actRevisionUID"]
      """  iACTRevisionUID  """  
      self.bookID:str = obj["bookID"]
      """  bookID  """  
      pass

class BookIsNotEmpty_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class BookVarNameTypeChanging_input:
   """ Required : 
   proposedValue
   column
   ds
   """  
   def __init__(self, obj):
      self.proposedValue:str = obj["proposedValue"]
      self.column:str = obj["column"]
      """  Name or type  """  
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

class BookVarNameTypeChanging_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class BookVarOwnerChanging_input:
   """ Required : 
   proposedValue
   ds
   """  
   def __init__(self, obj):
      self.proposedValue:str = obj["proposedValue"]
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

class BookVarOwnerChanging_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class BookVariableGetNew_input:
   """ Required : 
   actTypeUID
   actRevisionUID
   bookID
   vType
   vUID
   developMode
   ds
   """  
   def __init__(self, obj):
      self.actTypeUID:int = obj["actTypeUID"]
      """  aCTTypeUID  """  
      self.actRevisionUID:int = obj["actRevisionUID"]
      """  actRevisionUID  """  
      self.bookID:str = obj["bookID"]
      """  bookID  """  
      self.vType:str = obj["vType"]
      """  vType  """  
      self.vUID:int = obj["vUID"]
      """  vUID  """  
      self.developMode:bool = obj["developMode"]
      """  developMode  """  
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

class BookVariableGetNew_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class BookingRuleGetNew_input:
   """ Required : 
   actTypeUID
   actRevisionUID
   bookID
   isPost
   isRef
   ds
   """  
   def __init__(self, obj):
      self.actTypeUID:int = obj["actTypeUID"]
      """  aCTTypeUID  """  
      self.actRevisionUID:int = obj["actRevisionUID"]
      """  actRevisionUID  """  
      self.bookID:str = obj["bookID"]
      """  bookID  """  
      self.isPost:bool = obj["isPost"]
      """  Is Post Rule  """  
      self.isRef:bool = obj["isRef"]
      """  Is Reference Rule  """  
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

class BookingRuleGetNew_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CanActivateRevision_input:
   """ Required : 
   cACTTypeName
   cABTVer
   cPatchABTVer
   """  
   def __init__(self, obj):
      self.cACTTypeName:str = obj["cACTTypeName"]
      """  ACTType Display Name  """  
      self.cABTVer:str = obj["cABTVer"]
      """  ABT Version  """  
      self.cPatchABTVer:str = obj["cPatchABTVer"]
      """  Patch ABT Version  """  
      pass

class CanActivateRevision_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class ChangeBAQ_input:
   """ Required : 
   actTypeUID
   actRevisionUID
   abtDocLineUID
   abtQueryUID
   baqName
   ds
   """  
   def __init__(self, obj):
      self.actTypeUID:int = obj["actTypeUID"]
      """  actTypeUID  """  
      self.actRevisionUID:int = obj["actRevisionUID"]
      """  actRevisionUID  """  
      self.abtDocLineUID:int = obj["abtDocLineUID"]
      """  abtDocLineUID  """  
      self.abtQueryUID:int = obj["abtQueryUID"]
      """  abtQueryUID  """  
      self.baqName:str = obj["baqName"]
      """  baqName  """  
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

class ChangeBAQ_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeRevisionStatusMode_input:
   """ Required : 
   companyName
   iACTTypeUID
   iACTRevisionUID
   cStatus
   ds
   """  
   def __init__(self, obj):
      self.companyName:str = obj["companyName"]
      """  CompanyName  """  
      self.iACTTypeUID:int = obj["iACTTypeUID"]
      """  iACTTypeUID  """  
      self.iACTRevisionUID:int = obj["iACTRevisionUID"]
      """  iACTRevisionUID  """  
      self.cStatus:str = obj["cStatus"]
      """  Status  """  
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

class ChangeRevisionStatusMode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.lNeedRefresh:bool = obj["lNeedRefresh"]
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckBAQExists_input:
   """ Required : 
   baqid
   """  
   def __init__(self, obj):
      self.baqid:str = obj["baqid"]
      """  BAQ Id  """  
      pass

class CheckBAQExists_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.isexisted:bool = obj["isexisted"]
      pass

      """  output parameters  """  

class CheckBeforeActivateRevision_input:
   """ Required : 
   companyName
   iACTTypeUID
   iACTRevisionUID
   """  
   def __init__(self, obj):
      self.companyName:str = obj["companyName"]
      """  CompanyName  """  
      self.iACTTypeUID:int = obj["iACTTypeUID"]
      """  iACTTypeUID  """  
      self.iACTRevisionUID:int = obj["iACTRevisionUID"]
      """  iACTRevisionUID  """  
      pass

class CheckBeforeActivateRevision_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.cError:str = obj["parameters"]
      self.cWarning:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckSyntaxFunction_input:
   """ Required : 
   companyName
   aCTTypeUID
   aCTRevisionUID
   bookId
   functionUID
   ds
   """  
   def __init__(self, obj):
      self.companyName:str = obj["companyName"]
      self.aCTTypeUID:int = obj["aCTTypeUID"]
      self.aCTRevisionUID:int = obj["aCTRevisionUID"]
      self.bookId:str = obj["bookId"]
      self.functionUID:int = obj["functionUID"]
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

class CheckSyntaxFunction_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      self.errorsExist:bool = obj["errorsExist"]
      pass

      """  output parameters  """  

class CheckSyntaxRevision_input:
   """ Required : 
   companyName
   aCTTypeUID
   aCTRevisionUID
   ds
   """  
   def __init__(self, obj):
      self.companyName:str = obj["companyName"]
      self.aCTTypeUID:int = obj["aCTTypeUID"]
      self.aCTRevisionUID:int = obj["aCTRevisionUID"]
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

class CheckSyntaxRevision_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      self.errorsExist:bool = obj["errorsExist"]
      self.errorInFunction:bool = obj["errorInFunction"]
      self.errorFirstUID:int = obj["parameters"]
      pass

      """  output parameters  """  

class CheckSyntaxRule_input:
   """ Required : 
   companyName
   aCTTypeUID
   aCTRevisionUID
   bookId
   ruleUID
   ds
   """  
   def __init__(self, obj):
      self.companyName:str = obj["companyName"]
      self.aCTTypeUID:int = obj["aCTTypeUID"]
      self.aCTRevisionUID:int = obj["aCTRevisionUID"]
      self.bookId:str = obj["bookId"]
      self.ruleUID:int = obj["ruleUID"]
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

class CheckSyntaxRule_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      self.errorsExist:bool = obj["errorsExist"]
      pass

      """  output parameters  """  

class CompareRevisions_input:
   """ Required : 
   GPostingUID
   NodeID
   """  
   def __init__(self, obj):
      self.GPostingUID:str = obj["GPostingUID"]
      """  A ~ (tilde) separated list consisting of:
            0 = ACTTypeUID
            1 = Revision 1 name
            2 = Revision 2 name  """  
      self.NodeID:str = obj["NodeID"]
      """  Not currently used  """  
      pass

class CompareRevisions_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      """  Tree Object  """  
      pass

class CopyListOfFunctionsWithWarn_input:
   """ Required : 
   listOfFuncUID
   actTypeUID
   actRevisionUID
   bookID
   destinationACTTypeUID
   destinationRevisionUID
   destinationBookUID
   developMode
   """  
   def __init__(self, obj):
      self.listOfFuncUID:str = obj["listOfFuncUID"]
      """  List UIDs of copied Functions  """  
      self.actTypeUID:int = obj["actTypeUID"]
      """  Source ACTTypeUID  """  
      self.actRevisionUID:int = obj["actRevisionUID"]
      """  Source ACTRevisionUID  """  
      self.bookID:str = obj["bookID"]
      """  Source BookID  """  
      self.destinationACTTypeUID:int = obj["destinationACTTypeUID"]
      """  identifier of destination ActType  """  
      self.destinationRevisionUID:int = obj["destinationRevisionUID"]
      """  identifier of destination revision  """  
      self.destinationBookUID:str = obj["destinationBookUID"]
      """  identifier of destination book  """  
      self.developMode:bool = obj["developMode"]
      """  Developer Mode  """  
      pass

class CopyListOfFunctionsWithWarn_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.warnMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class CopyListOfFunctions_input:
   """ Required : 
   listOfFuncUID
   destinationACTTypeUID
   destinationRevisionUID
   destinationBookUID
   """  
   def __init__(self, obj):
      self.listOfFuncUID:str = obj["listOfFuncUID"]
      """  listOfFuncUID  """  
      self.destinationACTTypeUID:int = obj["destinationACTTypeUID"]
      """  identifier of destination ActType  """  
      self.destinationRevisionUID:int = obj["destinationRevisionUID"]
      """  identifier of destination revision  """  
      self.destinationBookUID:str = obj["destinationBookUID"]
      """  identifier of destination book  """  
      pass

class CopyListOfFunctions_output:
   def __init__(self, obj):
      pass

class CopyListOfRulesWithWarn_input:
   """ Required : 
   listOfRuleUID
   actTypeUID
   actRevisionUID
   bookID
   destinationACTTypeUID
   destinationRevisionUID
   destinationBookUID
   developMode
   """  
   def __init__(self, obj):
      self.listOfRuleUID:str = obj["listOfRuleUID"]
      """  listOfRuleUID  """  
      self.actTypeUID:int = obj["actTypeUID"]
      """  source actTypeUID  """  
      self.actRevisionUID:int = obj["actRevisionUID"]
      """  source actRevisionUID  """  
      self.bookID:str = obj["bookID"]
      """  source BookID  """  
      self.destinationACTTypeUID:int = obj["destinationACTTypeUID"]
      """  identifier of destination ActType  """  
      self.destinationRevisionUID:int = obj["destinationRevisionUID"]
      """  identifier of destination revision  """  
      self.destinationBookUID:str = obj["destinationBookUID"]
      """  identifier of destination book  """  
      self.developMode:bool = obj["developMode"]
      """  development mode  """  
      pass

class CopyListOfRulesWithWarn_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.warnMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class CopyListOfRules_input:
   """ Required : 
   listOfRuleUID
   destinationACTTypeUID
   destinationRevisionUID
   destinationBookUID
   """  
   def __init__(self, obj):
      self.listOfRuleUID:str = obj["listOfRuleUID"]
      """  listOfRuleUID  """  
      self.destinationACTTypeUID:int = obj["destinationACTTypeUID"]
      """  identifier of destination ActType  """  
      self.destinationRevisionUID:int = obj["destinationRevisionUID"]
      """  identifier of destination revision  """  
      self.destinationBookUID:str = obj["destinationBookUID"]
      """  identifier of destination book  """  
      pass

class CopyListOfRules_output:
   def __init__(self, obj):
      pass

class CopyOperations_input:
   """ Required : 
   aCTTypeUID
   aCTRevisionUID
   bookID
   ruleUID
   functionUID
   operationUID
   isCustomOp
   destACTTypeUID
   destACTRevisionUID
   destBookID
   destRuleUID
   destFunctionUID
   destOperationUID
   destIsCustomOp
   bMulti
   bMove
   developMode
   copyDs
   ds
   """  
   def __init__(self, obj):
      self.aCTTypeUID:int = obj["aCTTypeUID"]
      """  source ACTTypeUID  """  
      self.aCTRevisionUID:int = obj["aCTRevisionUID"]
      """  source ACTRevisionUID  """  
      self.bookID:str = obj["bookID"]
      """  source bookID  """  
      self.ruleUID:int = obj["ruleUID"]
      """  source RuleUID  """  
      self.functionUID:int = obj["functionUID"]
      """  source FunctionUID  """  
      self.operationUID:int = obj["operationUID"]
      """  OperationUID. If this value is zero then all operations of rule/function will be copied.  """  
      self.isCustomOp:bool = obj["isCustomOp"]
      """  Copy from custom operations  """  
      self.destACTTypeUID:int = obj["destACTTypeUID"]
      """  ACTTypeUID destination  """  
      self.destACTRevisionUID:int = obj["destACTRevisionUID"]
      """  ACTRevisionUID destination  """  
      self.destBookID:str = obj["destBookID"]
      """  destBookID  """  
      self.destRuleUID:int = obj["destRuleUID"]
      """  RuleUID destination  """  
      self.destFunctionUID:int = obj["destFunctionUID"]
      """  FunctionUID destination  """  
      self.destOperationUID:int = obj["destOperationUID"]
      """  identifier of destination operation  """  
      self.destIsCustomOp:bool = obj["destIsCustomOp"]
      """  Copy to custom operations  """  
      self.bMulti:bool = obj["bMulti"]
      """  Multi Copy  """  
      self.bMove:bool = obj["bMove"]
      """  Move  """  
      self.developMode:bool = obj["developMode"]
      """  DevelopMode  """  
      self.copyDs:list[Erp_Tablesets_ACTTypeCopyPasteTableset] = obj["copyDs"]
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

class CopyOperations_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.warnMessage:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CustomUpdate_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

class CustomUpdate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DeleteACTBook_input:
   """ Required : 
   aCTTypeUID
   aCTRevisionUID
   bookID
   developMode
   """  
   def __init__(self, obj):
      self.aCTTypeUID:int = obj["aCTTypeUID"]
      """  aCTTypeUID  """  
      self.aCTRevisionUID:int = obj["aCTRevisionUID"]
      """  aCTRevisionUID  """  
      self.bookID:str = obj["bookID"]
      """  bookID  """  
      self.developMode:bool = obj["developMode"]
      """  DevelopMode  """  
      pass

class DeleteACTBook_output:
   def __init__(self, obj):
      pass

class DeleteBROperationCustom_input:
   """ Required : 
   aCTTypeUID
   aCTRevisionUID
   bookID
   ruleUID
   operationUID
   bMulti
   ds
   """  
   def __init__(self, obj):
      self.aCTTypeUID:int = obj["aCTTypeUID"]
      """  ACTTypeUID  """  
      self.aCTRevisionUID:int = obj["aCTRevisionUID"]
      """  ACTRevisionUID  """  
      self.bookID:str = obj["bookID"]
      """  bookID  """  
      self.ruleUID:int = obj["ruleUID"]
      """  RuleUID  """  
      self.operationUID:int = obj["operationUID"]
      """  OperationUID. If value is zero then remove all operations from rule customizaion.  """  
      self.bMulti:bool = obj["bMulti"]
      """  Multi Delete  """  
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

class DeleteBROperationCustom_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   acTTypeUID
   """  
   def __init__(self, obj):
      self.acTTypeUID:int = obj["acTTypeUID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class DeleteMappedBook_input:
   """ Required : 
   actTypeUID
   actRevisionUID
   mapBookID
   """  
   def __init__(self, obj):
      self.actTypeUID:int = obj["actTypeUID"]
      """  act TypeUID  """  
      self.actRevisionUID:int = obj["actRevisionUID"]
      """  ACT RevisionUID  """  
      self.mapBookID:str = obj["mapBookID"]
      """  map BookID  """  
      pass

class DeleteMappedBook_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.newRevUID:int = obj["parameters"]
      pass

      """  output parameters  """  

class DeleteOpItems_input:
   """ Required : 
   aCTTypeUID
   aCTRevisionUID
   bookID
   ruleUID
   functionUID
   operationUID
   bMulti
   developMode
   ds
   """  
   def __init__(self, obj):
      self.aCTTypeUID:int = obj["aCTTypeUID"]
      """  ACTTypeUID  """  
      self.aCTRevisionUID:int = obj["aCTRevisionUID"]
      """  ACTRevisionUID  """  
      self.bookID:str = obj["bookID"]
      """  bookID  """  
      self.ruleUID:int = obj["ruleUID"]
      """  RuleUID  """  
      self.functionUID:int = obj["functionUID"]
      """  FunctionUID  """  
      self.operationUID:int = obj["operationUID"]
      """  OperationUID. If value is zero then remove all base operations from rule/function.  """  
      self.bMulti:bool = obj["bMulti"]
      """  Multi Delete  """  
      self.developMode:bool = obj["developMode"]
      """  DevelopMode  """  
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

class DeleteOpItems_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DeleteRevisionByName_input:
   """ Required : 
   acttypeUID
   revisionCode
   compList
   """  
   def __init__(self, obj):
      self.acttypeUID:int = obj["acttypeUID"]
      """  ACTType ACTTypeUID  """  
      self.revisionCode:str = obj["revisionCode"]
      """  ACTRevision Revision Code  """  
      self.compList:str = obj["compList"]
      """  Companies List  """  
      pass

class DeleteRevisionByName_output:
   def __init__(self, obj):
      pass

class DeleteRevsBeforeImport_input:
   """ Required : 
   typeName
   compList
   """  
   def __init__(self, obj):
      self.typeName:str = obj["typeName"]
      """  ACTType Display Name  """  
      self.compList:str = obj["compList"]
      """  Companies List  """  
      pass

class DeleteRevsBeforeImport_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_ABTAmountRow:
   def __init__(self, obj):
      self.ACTTypeUID:int = obj["ACTTypeUID"]
      """  Reference to the GL Transaction Type.  """  
      self.ACTRevisionUID:int = obj["ACTRevisionUID"]
      """  Reference to the Revision.  """  
      self.ABTDocLineUID:int = obj["ABTDocLineUID"]
      """  Reference to the Document Line.  """  
      self.ABTAmountUID:int = obj["ABTAmountUID"]
      """  Amount UID. Technical identifier.  """  
      self.Qualifier:str = obj["Qualifier"]
      """  Identifies the amount element. Application processes use the identifier. This field is display only when the program displays an accounting transaction type used by application programs.  """  
      self.Description:str = obj["Description"]
      """  Detailed description of the Amount.  """  
      self.IsDefault:bool = obj["IsDefault"]
      """  Indicates default Amounts for VBD templates.  """  
      self.Company:str = obj["Company"]
      """  Reference to the Company.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Loaded:int = obj["Loaded"]
      """   0- not loaded on client       
1-loaded fully
2- partial  """  
      self.DevelopMode:bool = obj["DevelopMode"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ABTDocLineRow:
   def __init__(self, obj):
      self.ACTTypeUID:int = obj["ACTTypeUID"]
      """  Reference to the GL Transaction Type.  """  
      self.ACTRevisionUID:int = obj["ACTRevisionUID"]
      """  Reference to the Revision.  """  
      self.ABTDocLineUID:int = obj["ABTDocLineUID"]
      """  Document Line UID. Technical identifier.  """  
      self.Qualifier:str = obj["Qualifier"]
      """  Identifies the document line. Various application processes use the identifier.  """  
      self.IsDefault:bool = obj["IsDefault"]
      """  Indicates default entities for VBD templates.  """  
      self.DataSource:str = obj["DataSource"]
      """  Associated with the document line database table name.  """  
      self.Description:str = obj["Description"]
      """  Provides a detailed description of the document line.  """  
      self.ParentABTDocLineUID:int = obj["ParentABTDocLineUID"]
      """  Reference to the Parent document line.  """  
      self.SequenceNumber:int = obj["SequenceNumber"]
      """  An order number indicating the document line place in the sequence of lines.  """  
      self.DocLinePath:str = obj["DocLinePath"]
      """  Path in VBD structure.  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Loaded:int = obj["Loaded"]
      """   0- not loaded on client       
1-loaded fully
2- partial  """  
      self.DevelopMode:bool = obj["DevelopMode"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ABTPostCodeRow:
   def __init__(self, obj):
      self.ACTTypeUID:int = obj["ACTTypeUID"]
      """  Reference to the GL Transaction Type.  """  
      self.ACTRevisionUID:int = obj["ACTRevisionUID"]
      """  Reference to the Revision.  """  
      self.ABTDocLineUID:int = obj["ABTDocLineUID"]
      """  Reference to the Document Line UID.  """  
      self.ABTPostEntityUID:int = obj["ABTPostEntityUID"]
      """  Reference to the Post Entity.  """  
      self.ABTPostCodeUID:int = obj["ABTPostCodeUID"]
      """  Posting Code UID. Technical identifier.  """  
      self.PopulationMethod:int = obj["PopulationMethod"]
      """  Population method for the user-defined field  """  
      self.Qualifier:str = obj["Qualifier"]
      """  Identifies the posting code. Application processes use the identifier.  """  
      self.Description:str = obj["Description"]
      """  Describes the posting code. The description provides information to users of this program.  """  
      self.DataSource:str = obj["DataSource"]
      """  Associated with the Posting Code database table name.  """  
      self.DataField:str = obj["DataField"]
      """  Name of the BAQ or Table field from where the field will be populated in case it is user-defined field  """  
      self.IsDefault:bool = obj["IsDefault"]
      """  Indicates default entities for VBD templates.  """  
      self.CodeType:str = obj["CodeType"]
      """  This field stores Posting Code datatype.  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DBSchemaName:str = obj["DBSchemaName"]
      """  DBSchemaName  """  
      self.BAQDataField:str = obj["BAQDataField"]
      """  Contains Ice.QueryField.Alias  """  
      self.BAQDataSource:str = obj["BAQDataSource"]
      self.DevelopMode:bool = obj["DevelopMode"]
      self.Loaded:int = obj["Loaded"]
      """   0- not loaded on client       
1-loaded fully
2- partial  """  
      self.TableDataField:str = obj["TableDataField"]
      self.TableDataSource:str = obj["TableDataSource"]
      self.BAQDataFieldName:str = obj["BAQDataFieldName"]
      """  Contains Ice.QueryField.FieldName  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ABTPostEntityRow:
   def __init__(self, obj):
      self.ACTTypeUID:int = obj["ACTTypeUID"]
      """  Reference to the GL Transaction Type.  """  
      self.ACTRevisionUID:int = obj["ACTRevisionUID"]
      """  Reference to the Revision.  """  
      self.ABTDocLineUID:int = obj["ABTDocLineUID"]
      """  Reference to the Document Line.  """  
      self.ABTPostEntityUID:int = obj["ABTPostEntityUID"]
      """  Post Entity UID. Technical identifier.  """  
      self.Qualifier:str = obj["Qualifier"]
      """  Identifies the entity element. Application processes use the identifier.  """  
      self.Description:str = obj["Description"]
      """  Describes the entity. The description provides information to users of this program.  """  
      self.IsDefault:bool = obj["IsDefault"]
      """  Indicates default entities for VBD templates.  """  
      self.SequenceNumber:int = obj["SequenceNumber"]
      """  An order number indicating the Post Entity place in the sequence of Post Entyties.  """  
      self.IsReference:bool = obj["IsReference"]
      """  Indicates if this entity stores keys for reference GLControl.  """  
      self.DataSource:str = obj["DataSource"]
      """  Identifies the table used to supply data for posting codes or amount elements that belong to the entity.  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DBSchemaName:str = obj["DBSchemaName"]
      """  DBSchemaName  """  
      self.DevelopMode:bool = obj["DevelopMode"]
      self.Loaded:int = obj["Loaded"]
      """   0- not loaded on client       
1-loaded fully
2- partial  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ABTQParamRow:
   def __init__(self, obj):
      self.BAQParamLinkUID:int = obj["BAQParamLinkUID"]
      """  BAQ Param Link UID.  """  
      self.ABTQueryUID:int = obj["ABTQueryUID"]
      """  Reference to the Query.  """  
      self.ACTRevisionUID:int = obj["ACTRevisionUID"]
      """  Reference to the Revision.  """  
      self.ACTTypeUID:int = obj["ACTTypeUID"]
      """  Reference to the GL Transaction Type.  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BAQParam:str = obj["BAQParam"]
      """  Paremeter in BAQ.  """  
      self.ABTBAQParam:str = obj["ABTBAQParam"]
      """  Parameter from the current Query.  """  
      self.ABTDocLineUID:int = obj["ABTDocLineUID"]
      """  Reference to the Document Line.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Loaded:int = obj["Loaded"]
      """   0- not loaded on client       
1-loaded fully
2- partial  """  
      self.DevelopMode:bool = obj["DevelopMode"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ABTQueryRow:
   def __init__(self, obj):
      self.ABTQueryUID:int = obj["ABTQueryUID"]
      """  Query UID. Technical key.  """  
      self.BAQID:str = obj["BAQID"]
      """  Reference to Business Activity Query.  """  
      self.ACTRevisionUID:int = obj["ACTRevisionUID"]
      """  Reference to the Revision.  """  
      self.ACTTypeUID:int = obj["ACTTypeUID"]
      """  Reference to the GL Transaction Type.  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.IsDefault:bool = obj["IsDefault"]
      """  Indicates default Queries for VBD templates.  """  
      self.ABTDocLineUID:int = obj["ABTDocLineUID"]
      """  Reference to the Document Line.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BAQDescription:str = obj["BAQDescription"]
      self.Loaded:int = obj["Loaded"]
      """   0- not loaded on client       
1-loaded fully
2- partial  """  
      self.DevelopMode:bool = obj["DevelopMode"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ACTBookRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Reference to the Company  """  
      self.BookID:str = obj["BookID"]
      """  Reference to the Book  """  
      self.Description:str = obj["Description"]
      """  Provides a description of the book. This field is display-only.  """  
      self.BookCurrency:str = obj["BookCurrency"]
      """  Currency of the Book  """  
      self.BOOKType:str = obj["BOOKType"]
      """  Type of Book  """  
      self.COAID:str = obj["COAID"]
      """  Reference to the COA  """  
      self.ACTRevisionUID:int = obj["ACTRevisionUID"]
      """  Reference to the Revision.  """  
      self.ActiveFlag:int = obj["ActiveFlag"]
      """  Yes, if Book is Active  """  
      self.DefaultBook:bool = obj["DefaultBook"]
      """  Yes, If the book is default  """  
      self.MapBookID:str = obj["MapBookID"]
      """  Reference to the book, that transaction will be used.  """  
      self.COAMapUID:int = obj["COAMapUID"]
      """  Reference to the COA Map.  """  
      self.UseMapFlag:bool = obj["UseMapFlag"]
      """  Yes, If mapping will be used.If no- booking rules will be used for creation of transaction.  """  
      self.ACTTypeUID:int = obj["ACTTypeUID"]
      """  Reference to the GL Transaction Type.  """  
      self.Summarize:int = obj["Summarize"]
      """   0)      Summarize (default)
1)      Summarize debit and credits separately
2)      No summarization
3)     Override  """  
      self.IsDefault:bool = obj["IsDefault"]
      """  Indicates default books for VBD templates.  """  
      self.MapType:int = obj["MapType"]
      """  Shows what will be used for transaction creating, 0 - Booking Rules, 1 -  COA Mapping, 2 - Direct  """  
      self.TranCurr:int = obj["TranCurr"]
      """  Transactional currency, Indicates what currency to use in book mapping. [0] -  is document , [1]  is source book's currency, used  in book mapping.  """  
      self.ABTVer:str = obj["ABTVer"]
      """  VBD Version  """  
      self.PatchABTVer:str = obj["PatchABTVer"]
      """  Patch VBD Version  """  
      self.RulesetVer:int = obj["RulesetVer"]
      """  Specifies the rule set version. Uses a single numeric sequence and increments every time a rule in the rule set changes.  """  
      self.PatchRulesetVer:int = obj["PatchRulesetVer"]
      """  Specifies the patch rule set version. Uses a single numeric sequence and increments each time a change is released in a patch to a client between service packs. The patch version resets to zero every time a service pack is released.  """  
      self.Package:str = obj["Package"]
      """  Package  """  
      self.Modified:bool = obj["Modified"]
      """  Indicates that Rulese was modified  """  
      self.PrevModified:bool = obj["PrevModified"]
      """  Value of Modified filed before last Update versions  """  
      self.ManuallyUpdVer:bool = obj["ManuallyUpdVer"]
      """  Indicates that Versions were updated manually  """  
      self.UpdatePatchVer:bool = obj["UpdatePatchVer"]
      """  Indicates that Patch Verstion were updated last time  """  
      self.BasePackage:str = obj["BasePackage"]
      """  Specifies the package name (for example, Standard, Extended, Russia) of the assigned rules set (posting rules, functions, and variables) and is used to automatically upgrade rule sets in packages that Epicor supports.  """  
      self.LocRulesetVer:int = obj["LocRulesetVer"]
      """  Localization Ruleset Version  """  
      self.LocPrevRulesetVer:int = obj["LocPrevRulesetVer"]
      """  Value of LocRulesetVer filed before last Update versions  """  
      self.LocPatchRulesetVer:int = obj["LocPatchRulesetVer"]
      """  Localization Patch Ruleset Version  """  
      self.LocPrevPatchRulesetVer:int = obj["LocPrevPatchRulesetVer"]
      """  Value of LocPatchRulesetVer filed before last Update versions  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.EnableCustomization:bool = obj["EnableCustomization"]
      """  Enabling/disabling customization for the Book  """  
      self.PartiallyUpdated:bool = obj["PartiallyUpdated"]
      """  Identifies that ruleset was partially updated during conversion for revision using common dll  """  
      self.Loaded:int = obj["Loaded"]
      """   0- not loaded on client       
1-loaded fully
2- partial  """  
      self.MapBookCOAID:str = obj["MapBookCOAID"]
      self.DevelopMode:bool = obj["DevelopMode"]
      self.DisableBookMapping:bool = obj["DisableBookMapping"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ACTRevisionRow:
   def __init__(self, obj):
      self.ACTRevisionUID:int = obj["ACTRevisionUID"]
      """  Unique Revision Identifier.  """  
      self.ACTTypeUID:int = obj["ACTTypeUID"]
      """  Reference to the GL Transaction Type.  """  
      self.RevisionCode:str = obj["RevisionCode"]
      """  A user-defined code of revision (unique within one account transaction type).  """  
      self.RevisionStatus:str = obj["RevisionStatus"]
      """   Status of the Revision. Allowed values are: "Active", "Draft", "Blocked". 
Active - indicates that exactly this Revision of an GL Transaction Type will be used when functional module initiates a corresponding business event. As soon as a Revision becomes "Active", it should become read-only for user. Only one Revision for each GL Transaction Type may be "Active".
 
Draft -  indicates a newly created Revision, which will not be used in any run-time processing. Each newly created Revision should automatically be put into "Draft" status. "Draft" Revision is open for editing. Each GL Transaction Type may have any number of Draft Revisions.
Blocked - indicates a Revision which was previously "Active" but is not anymore and is stored for traceability purposes. The "Blocked" Revision should be read-only.  """  
      self.Description:str = obj["Description"]
      """  Revision description.  """  
      self.SendToReviewJournal:bool = obj["SendToReviewJournal"]
      """  Yes- then all transaction will leave in Review Journal. User must confirm it manually, No - transaction will be created in GLJournal or left in Review Journal if the transaction is not valid.  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.IsDefault:bool = obj["IsDefault"]
      """  Indicates default Revisions for VBD templates.  """  
      self.RType:str = obj["RType"]
      """  Standard or Exteded  """  
      self.ABTVer:str = obj["ABTVer"]
      """  Version of VBD Stucture. If version is changed , VBD Structure merge process will be started during conversion.  """  
      self.VersionUID:int = obj["VersionUID"]
      """  Version of build, is used to save time and don't recompile revison each time.  """  
      self.PrevABTVer:str = obj["PrevABTVer"]
      """  Value of ABTVer field before last Update Versions  """  
      self.PatchABTVer:str = obj["PatchABTVer"]
      """  Patch VBD Version  """  
      self.PrevPatchABTVer:str = obj["PrevPatchABTVer"]
      """  Value of PatchABTVer field before last Update Versions  """  
      self.LocVer:int = obj["LocVer"]
      """  Localization Version  """  
      self.PatchLocVer:int = obj["PatchLocVer"]
      """  Patch Localizasion Version  """  
      self.UpdatePatchVer:bool = obj["UpdatePatchVer"]
      """  Indicates tha patch version was updated last time  """  
      self.Modified:bool = obj["Modified"]
      """  Indicates that Revision data were modified  """  
      self.PrevModified:bool = obj["PrevModified"]
      """  Value of Modified field before last Update Versions  """  
      self.ManuallyUpdVer:bool = obj["ManuallyUpdVer"]
      """  Indicates that Version was updated manually  """  
      self.NeedPrePostUpdate:bool = obj["NeedPrePostUpdate"]
      """  Indicates that VBD structure was changed and demand changes in Pre_Post Code  """  
      self.PrevRevisionStatus:str = obj["PrevRevisionStatus"]
      """  Value of RevisionStatus field before last Update Versions  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PendingConversion:bool = obj["PendingConversion"]
      """  Indicates that the Revision was not updated during conversion 'Import GL Transaction Types' because of segment mapping error. After correction Segment Mapping on GL Book Entry, conversion can be run again.  """  
      self.CanUseSysAssembly:bool = obj["CanUseSysAssembly"]
      """  Identifies that common dll can be used for this revision  """  
      self.PostAssemblyName:str = obj["PostAssemblyName"]
      """  Name of posting assembly  """  
      self.Loaded:int = obj["Loaded"]
      """   0- not loaded on client       
1-loaded fully
2- partial  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ACTTypeCopyPasteTableset:
   def __init__(self, obj):
      self.BRFuncOperation:list[Erp_Tablesets_BRFuncOperationRow] = obj["BRFuncOperation"]
      self.BROperation:list[Erp_Tablesets_BROperationRow] = obj["BROperation"]
      self.BROperationCustom:list[Erp_Tablesets_BROperationCustomRow] = obj["BROperationCustom"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ACTTypeImportBookTableset:
   def __init__(self, obj):
      self.ACTTypeImportComp:list[Erp_Tablesets_ACTTypeImportCompRow] = obj["ACTTypeImportComp"]
      self.COASegmentNameList:list[Erp_Tablesets_COASegmentNameListRow] = obj["COASegmentNameList"]
      self.GLBookList:list[Erp_Tablesets_GLBookListRow] = obj["GLBookList"]
      self.GLBookPackageSegmentMap:list[Erp_Tablesets_GLBookPackageSegmentMapRow] = obj["GLBookPackageSegmentMap"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ACTTypeImportCompRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.Selected:bool = obj["Selected"]
      """  Indicates that import shoulc be done for this Company  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ACTTypeImportOpTableset:
   def __init__(self, obj):
      self.ACTTypeImportComp:list[Erp_Tablesets_ACTTypeImportCompRow] = obj["ACTTypeImportComp"]
      self.GLBookMap:list[Erp_Tablesets_GLBookMapRow] = obj["GLBookMap"]
      self.GLSegmentMap:list[Erp_Tablesets_GLSegmentMapRow] = obj["GLSegmentMap"]
      self.RevisionImportOp:list[Erp_Tablesets_RevisionImportOpRow] = obj["RevisionImportOp"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ACTTypeListRow:
   def __init__(self, obj):
      self.ACTTypeUID:int = obj["ACTTypeUID"]
      """  Unique GL Transaction Type Identifier.  """  
      self.DisplayName:str = obj["DisplayName"]
      """  Name of the GL Tranaction Type to be displayed in the tree view navigation control.  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.DetailedDescription:str = obj["DetailedDescription"]
      """  Describes the GL Transaction Type. The description provades information to users of this program  """  
      self.Limited:bool = obj["Limited"]
      """  Yes - if the transaction type has not VBD and Booking Rules,has just one Active Revision. Posting in this case is hard coded.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ACTTypeListTableset:
   def __init__(self, obj):
      self.ACTTypeList:list[Erp_Tablesets_ACTTypeListRow] = obj["ACTTypeList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ACTTypeRow:
   def __init__(self, obj):
      self.ACTTypeUID:int = obj["ACTTypeUID"]
      """  Unique GL Transaction Type Identifier.  """  
      self.DisplayName:str = obj["DisplayName"]
      """  Name of the GL Tranaction Type to be displayed in the tree view navigation control.  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.DetailedDescription:str = obj["DetailedDescription"]
      """  Describes the GL Transaction Type. The description provades information to users of this program  """  
      self.Limited:bool = obj["Limited"]
      """  Yes - if the transaction type has not VBD and Booking Rules,has just one Active Revision. Posting in this case is hard coded.  """  
      self.IsLog:bool = obj["IsLog"]
      """  Flag to enable logging of the GL Transaction Type.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ConversionErrors:bool = obj["ConversionErrors"]
      """  Indicates that an error occurred during update of the GL Transaction Type in conversion program 'Import GL Transaction Types'  """  
      self.Loaded:int = obj["Loaded"]
      """   0- not loaded on client       
1-loaded fully
2- partial  """  
      self.IsLocked:bool = obj["IsLocked"]
      self.LockStatus:str = obj["LockStatus"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ACTTypeSubDataTableset:
   def __init__(self, obj):
      self.BRFunctionPhrase:list[Erp_Tablesets_BRFunctionPhraseRow] = obj["BRFunctionPhrase"]
      self.HierarchicalData:list[Erp_Tablesets_HierarchicalDataRow] = obj["HierarchicalData"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ACTTypeTableset:
   def __init__(self, obj):
      self.ACTType:list[Erp_Tablesets_ACTTypeRow] = obj["ACTType"]
      self.ACTRevision:list[Erp_Tablesets_ACTRevisionRow] = obj["ACTRevision"]
      self.ABTDocLine:list[Erp_Tablesets_ABTDocLineRow] = obj["ABTDocLine"]
      self.ABTAmount:list[Erp_Tablesets_ABTAmountRow] = obj["ABTAmount"]
      self.ABTPostEntity:list[Erp_Tablesets_ABTPostEntityRow] = obj["ABTPostEntity"]
      self.ABTPostCode:list[Erp_Tablesets_ABTPostCodeRow] = obj["ABTPostCode"]
      self.ABTQuery:list[Erp_Tablesets_ABTQueryRow] = obj["ABTQuery"]
      self.ABTQParam:list[Erp_Tablesets_ABTQParamRow] = obj["ABTQParam"]
      self.ACTBook:list[Erp_Tablesets_ACTBookRow] = obj["ACTBook"]
      self.BookingRule:list[Erp_Tablesets_BookingRuleRow] = obj["BookingRule"]
      self.BookValRule:list[Erp_Tablesets_BookValRuleRow] = obj["BookValRule"]
      self.BROperation:list[Erp_Tablesets_BROperationRow] = obj["BROperation"]
      self.BROperationCustom:list[Erp_Tablesets_BROperationCustomRow] = obj["BROperationCustom"]
      self.BRFunction:list[Erp_Tablesets_BRFunctionRow] = obj["BRFunction"]
      self.BookVar:list[Erp_Tablesets_BookVarRow] = obj["BookVar"]
      self.BRFuncArgs:list[Erp_Tablesets_BRFuncArgsRow] = obj["BRFuncArgs"]
      self.BRFuncOperation:list[Erp_Tablesets_BRFuncOperationRow] = obj["BRFuncOperation"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_BRFuncArgsRow:
   def __init__(self, obj):
      self.FunctionUID:int = obj["FunctionUID"]
      """  Reference to the Parent function UID.  """  
      self.ArgName:str = obj["ArgName"]
      """  Name of function argument  """  
      self.ArgType:str = obj["ArgType"]
      """  Type of function argument  """  
      self.PRGName:str = obj["PRGName"]
      """  Technical name  """  
      self.PRGType:str = obj["PRGType"]
      """  Technical type  """  
      self.ACTRevisionUID:int = obj["ACTRevisionUID"]
      """  Reference to the Revision  """  
      self.ACTTypeUID:int = obj["ACTTypeUID"]
      """  Reference to the GL Transaction Type.  """  
      self.ArgumentUID:int = obj["ArgumentUID"]
      """  Unique Argument identifier.  """  
      self.Company:str = obj["Company"]
      """  Reference to  the company  """  
      self.IsDefault:bool = obj["IsDefault"]
      """  Indicates default Function Arguments for ABT templates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Loaded:int = obj["Loaded"]
      """   0- not loaded on client       
1-loaded fully
2- partial  """  
      self.DevelopMode:bool = obj["DevelopMode"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_BRFuncOperationRow:
   def __init__(self, obj):
      self.OperationUID:int = obj["OperationUID"]
      """  Operation unique ID. Technical identifier.  """  
      self.ParentOperationUID:int = obj["ParentOperationUID"]
      """  Reference to the parent operation (necessary to support the hierarchical operations structure; references the OperationUID field in the same table).  """  
      self.ControlFlowOperator:str = obj["ControlFlowOperator"]
      """  The identifier of the control flow operator.  """  
      self.Container:str = obj["Container"]
      """  The identifier of the target container.  """  
      self.Formula:str = obj["Formula"]
      """  The name of formula.  """  
      self.SequenceNumber:int = obj["SequenceNumber"]
      """  An order number indicating the operation?s place in the sequence of execution ? for the whole set of ruleset?s operations.  """  
      self.ChildSequenceNumber:int = obj["ChildSequenceNumber"]
      """  An order number indicating the operation?s place in the sequence of execution ? for a single block of operations on a single hierarchy level.  """  
      self.FunctionUID:int = obj["FunctionUID"]
      """  System ID of used function.  """  
      self.PRGText:str = obj["PRGText"]
      """  Technical text of the function(formula)  """  
      self.ACTRevisionUID:int = obj["ACTRevisionUID"]
      """  Reference to the Revision.  """  
      self.ACTTypeUID:int = obj["ACTTypeUID"]
      """  Reference to the GL Transaction Type.  """  
      self.FuncOperUID:int = obj["FuncOperUID"]
      """  Reference to the Function of the GL Transaction Type.  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PRGContainer:str = obj["PRGContainer"]
      """  The identifier of the target container.  """  
      self.IsDefault:bool = obj["IsDefault"]
      """  Indicates default Function Operations for ABT templates.  """  
      self.LocModified:bool = obj["LocModified"]
      """  LocModified  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DevelopMode:bool = obj["DevelopMode"]
      self.Loaded:int = obj["Loaded"]
      """   0- not loaded on client       
1-loaded fully
2- partial  """  
      self.ErrorText:str = obj["ErrorText"]
      """  Contains error text in generated code.  """  
      self.IsError:bool = obj["IsError"]
      """  Allow use icon easier.  """  
      self.ContainerType:str = obj["ContainerType"]
      """  Unified container type for both Operation and Logical Condition types  """  
      self.IsLogicalCondition:bool = obj["IsLogicalCondition"]
      """  Indicates 'Logical Condition' type of the operation  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_BRFunctionPhraseRow:
   def __init__(self, obj):
      self.ACTTypeUID:int = obj["ACTTypeUID"]
      self.ACTRevisionUID:int = obj["ACTRevisionUID"]
      self.FunctionUID:int = obj["FunctionUID"]
      self.ArgumentUID:int = obj["ArgumentUID"]
      self.ElementText:str = obj["ElementText"]
      """  Text of the function phrase element  """  
      self.ElementType:str = obj["ElementType"]
      """  Element type  """  
      self.Order:int = obj["Order"]
      """  Order of phrase elements  """  
      self.ArgType:str = obj["ArgType"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_BRFunctionRow:
   def __init__(self, obj):
      self.FunctionUID:int = obj["FunctionUID"]
      """  Unique Function identifier.  """  
      self.Name:str = obj["Name"]
      """  Name of the function.  """  
      self.PRGName:str = obj["PRGName"]
      """  Technical name of function  """  
      self.IsSystem:bool = obj["IsSystem"]
      """  If the function is system.  """  
      self.Description:str = obj["Description"]
      """  Detail description for function.  """  
      self.ResultType:str = obj["ResultType"]
      """  Type of function result.  """  
      self.PRGPattern:str = obj["PRGPattern"]
      """  Technical text of function.  """  
      self.ACTRevisionUID:int = obj["ACTRevisionUID"]
      """  Reference to the Revisions.  """  
      self.ACTTypeUID:int = obj["ACTTypeUID"]
      """  Reference to the GL Transaction Type  """  
      self.BookID:str = obj["BookID"]
      """  Reference to Book.  """  
      self.Formula:str = obj["Formula"]
      """  Text of function  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.DocLinePath:str = obj["DocLinePath"]
      """  Text field to store the For Each criteria expression .  """  
      self.IsDefault:bool = obj["IsDefault"]
      """  Indicates default Functions for ABT templates.  """  
      self.ManuallyUpdVer:bool = obj["ManuallyUpdVer"]
      """  ManuallyUpdVer  """  
      self.FuncVer:int = obj["FuncVer"]
      """  Specifies the function version. Uses a single numeric sequence and increments every time a change is made in a corresponding rule.  """  
      self.PatchFuncVer:int = obj["PatchFuncVer"]
      """  PatchFuncVer  """  
      self.PrevModified:bool = obj["PrevModified"]
      """  PrevModified  """  
      self.Modified:bool = obj["Modified"]
      """  Modified  """  
      self.LocVer:int = obj["LocVer"]
      """  LocVer  """  
      self.LocPatchVer:int = obj["LocPatchVer"]
      """  LocPatchVer  """  
      self.LocModified:bool = obj["LocModified"]
      """  LocModified  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Loaded:int = obj["Loaded"]
      """   0- not loaded on client       
1-loaded fully
2- partial  """  
      self.DevelopMode:bool = obj["DevelopMode"]
      self.IsError:bool = obj["IsError"]
      """  Is used to show icon in Tree.  """  
      self.ErrorText:str = obj["ErrorText"]
      """  Contains error text for a function.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_BROperationCustomRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Indetifier.  """  
      self.ACTTypeUID:int = obj["ACTTypeUID"]
      """  Reference to the GL Transaction Type.  """  
      self.ACTRevisionUID:int = obj["ACTRevisionUID"]
      """  Reference to the Revision.  """  
      self.BookID:str = obj["BookID"]
      """  Reference to the Book.  """  
      self.RuleUID:int = obj["RuleUID"]
      """  Reference to the parent booking rule.  """  
      self.OperationUID:int = obj["OperationUID"]
      """  Operation unique ID. Technical identifier.  """  
      self.ParentOperationUID:int = obj["ParentOperationUID"]
      """  Reference to the parent operation  """  
      self.ChildSequenceNumber:int = obj["ChildSequenceNumber"]
      """  An order number indicating the operation’s place in the sequence of execution.  """  
      self.ControlFlowOperator:str = obj["ControlFlowOperator"]
      """  The identifier of the control flow operator.  """  
      self.Container:str = obj["Container"]
      """  The identifier of the target container.  """  
      self.Formula:str = obj["Formula"]
      """  The operation's main formula.  """  
      self.FunctionUID:int = obj["FunctionUID"]
      """  Function unique ID.  """  
      self.PRGText:str = obj["PRGText"]
      """  Code for operation  """  
      self.PRGContainer:str = obj["PRGContainer"]
      """  The identifier of the target container.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  Audit column. Populate UserID who created the row.  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  Audit column. Populate time of creation row.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Audit column. Populate UserID of last person who updated the row.  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  Audit column. Populate time of updating the row.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Loaded:int = obj["Loaded"]
      """   0- not loaded on client       
1-loaded fully
2- partial  """  
      self.ErrorText:str = obj["ErrorText"]
      """  Contains error text in generated code.  """  
      self.IsError:bool = obj["IsError"]
      """  Allow use icon easier.  """  
      self.ContainerType:str = obj["ContainerType"]
      """  Unified container type for both Operation and Logical Condition types  """  
      self.IsLogicalCondition:bool = obj["IsLogicalCondition"]
      """  Indicates 'Logical Condition' type of the operation  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_BROperationRow:
   def __init__(self, obj):
      self.OperationUID:int = obj["OperationUID"]
      """  Operation unique ID. Technical identifier.  """  
      self.RuleUID:int = obj["RuleUID"]
      """  Reference to the parent booking rule.  """  
      self.ParentOperationUID:int = obj["ParentOperationUID"]
      """  Reference to the parent operation (necessary to support the hierarchical operations structure; references the OperationUID field in the same table).  """  
      self.ControlFlowOperator:str = obj["ControlFlowOperator"]
      """  The identifier of the control flow operator.  """  
      self.Container:str = obj["Container"]
      """  The identifier of the target container.  """  
      self.Formula:str = obj["Formula"]
      """  The operation's main formula.  """  
      self.SequenceNumber:int = obj["SequenceNumber"]
      """  An order number indicating the operation?s place in the sequence of execution ? for the whole set of ruleset?s operations.  """  
      self.ChildSequenceNumber:int = obj["ChildSequenceNumber"]
      """  An order number indicating the operation?s place in the sequence of execution ? for a single block of operations on a single hierarchy level.  """  
      self.FunctionUID:int = obj["FunctionUID"]
      """  Function unique ID. Technical identifier.  """  
      self.PRGText:str = obj["PRGText"]
      """  Progress Code for operation  """  
      self.ACTRevisionUID:int = obj["ACTRevisionUID"]
      """  Reference to the Revision.  """  
      self.ACTTypeUID:int = obj["ACTTypeUID"]
      """  Reference to the GL Transaction Type.  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PRGContainer:str = obj["PRGContainer"]
      """  The identifier of the target container.  """  
      self.BookID:str = obj["BookID"]
      """  Reference to the Book.  """  
      self.IsDefault:bool = obj["IsDefault"]
      """  Indicates default Operations for ABT templates.  """  
      self.LocModified:bool = obj["LocModified"]
      """  LocModified  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ContainerType:str = obj["ContainerType"]
      """  Unified container type for both Operation and Logical Condition types  """  
      self.DevelopMode:bool = obj["DevelopMode"]
      self.Loaded:int = obj["Loaded"]
      """   0- not loaded on client       
1-loaded fully
2- partial  """  
      self.ErrorText:str = obj["ErrorText"]
      """  Contains error text in generated code.  """  
      self.IsError:bool = obj["IsError"]
      """  Allow use icon easier.  """  
      self.LLink01:str = obj["LLink01"]
      """  Field to support functionality of link-combo in Kinetic (Container in operations)  """  
      self.IsLogicalCondition:bool = obj["IsLogicalCondition"]
      """  Indicates 'Logical Condition' type of the operation  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_BookValRuleRow:
   def __init__(self, obj):
      self.BVRuleUID:int = obj["BVRuleUID"]
      """  Unique value.Primary key  """  
      self.VRuleUID:int = obj["VRuleUID"]
      """  Technical key of Validation Rule  """  
      self.Description:str = obj["Description"]
      """  Validation rule description  """  
      self.Action:str = obj["Action"]
      """  Error, Ignor, Warning, Autocorrect, Autocorrect with warning  """  
      self.VLevel:str = obj["VLevel"]
      """  Validation level : Book, Booking Rule, Company etc  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BookID:str = obj["BookID"]
      """  Reference to Book.  """  
      self.ACTTypeUID:int = obj["ACTTypeUID"]
      """  Account transaction type UID. Technical identifier.  """  
      self.ACTRevisionUID:int = obj["ACTRevisionUID"]
      """  Reference to the parent account transaction revision.  """  
      self.RuleUID:int = obj["RuleUID"]
      """  Technical identifier.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.IsDefault:bool = obj["IsDefault"]
      """  Indicates default validation rules for ABT templates.  """  
      self.ActionList:str = obj["ActionList"]
      """  List of actions (used in combo boxes).  """  
      self.RuleType:str = obj["RuleType"]
      """  RuleType - PrePost(calculation in pre-post mode before posting), Post(standard posting) or Ref (Calculate reference GLControl during posting)  """  
      self.Loaded:int = obj["Loaded"]
      """   0- not loaded on client       
1-loaded fully
2- partial  """  
      self.DevelopMode:bool = obj["DevelopMode"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_BookVarRow:
   def __init__(self, obj):
      self.ACTTypeUID:int = obj["ACTTypeUID"]
      """  Reference to the GL Transaction Type.  """  
      self.ACTRevisionUID:int = obj["ACTRevisionUID"]
      """  Reference to the Revision.  """  
      self.BookID:str = obj["BookID"]
      """  Reference to the Book  """  
      self.BookVarUID:int = obj["BookVarUID"]
      """  BookVar unique ID.  """  
      self.VarName:str = obj["VarName"]
      """  Variable Name  """  
      self.VarType:str = obj["VarType"]
      """  Variable Type  """  
      self.vType:str = obj["vType"]
      """  Variable context, possible values: Global, Book, Rule, Function.  """  
      self.vUID:int = obj["vUID"]
      """  ID of context, for example if vType = Function then vUID = FunctionUID.  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.IsDefault:bool = obj["IsDefault"]
      """  Indicates default Variables for VBD templates.  """  
      self.LocModified:bool = obj["LocModified"]
      """  LocModified  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DevelopMode:bool = obj["DevelopMode"]
      self.isSystem:bool = obj["isSystem"]
      """  the field is used for generation post program  """  
      self.Loaded:int = obj["Loaded"]
      """   0- not loaded on client       
1-loaded fully
2- partial  """  
      self.OwnerDescription:str = obj["OwnerDescription"]
      """  Function or Rule Description.  """  
      self.VarTypeDisplay:str = obj["VarTypeDisplay"]
      """  VarType display.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_BookingRuleRow:
   def __init__(self, obj):
      self.RuleUID:int = obj["RuleUID"]
      """  Technical identifier.  """  
      self.ACTRevisionUID:int = obj["ACTRevisionUID"]
      """  Reference to the Revision.  """  
      self.DisplayName:str = obj["DisplayName"]
      """  Booking rule name to be displayed in the tree view navigation control.  """  
      self.DetailedDescription:str = obj["DetailedDescription"]
      """  Booking rule detailed description.  """  
      self.SelectionCriteria:str = obj["SelectionCriteria"]
      """  Text field to store the selection criteria expression .  """  
      self.BookID:str = obj["BookID"]
      """  Reference to the Book.  """  
      self.ACTTypeUID:int = obj["ACTTypeUID"]
      """  Reference to the GL Transaction Type.  """  
      self.IsPost:bool = obj["IsPost"]
      """  It is Rule for Posting process or special for GLControl calculation.  """  
      self.ForEach:str = obj["ForEach"]
      """  Text field to store the For Each criteria expression .  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.IsHeader:bool = obj["IsHeader"]
      """  Rule run once, usual it is used for calculation Book variables or Header variables (that can be calculated once).  """  
      self.IsActive:bool = obj["IsActive"]
      """  Determines whether the posting process uses the rule.  """  
      self.CreditContext:str = obj["CreditContext"]
      """  Stores a reference to a credit context for use by another posting rule. Posting rules can create a GL control that stores the rule's output for use in subsequent processing..  """  
      self.DebitContext:str = obj["DebitContext"]
      """  Stores a reference to a debit context for use by another posting rule. Posting rules can create a GL control that stores the rule's output for use in subsequent processing.  """  
      self.RefContext:str = obj["RefContext"]
      """  Reference  Context is used for pre-Posting rules  """  
      self.GLControlType:str = obj["GLControlType"]
      """  Determines the GL control type that applies to the rule. The control type affects the processing of accounts generated by the rule. Pre-posting GL controls use the type to determine the reference context, used to set the default for a GL account field. The type also controls the credit and debit contexts for posting rules.  """  
      self.IsDefault:bool = obj["IsDefault"]
      """  Indicates default Rules for ABT templates.  """  
      self.Entity:str = obj["Entity"]
      """  Primary key from the Entity is a source of keys for TranGLC table that save Reference control of the Booking Rule.  """  
      self.IsReference:bool = obj["IsReference"]
      """  IsReference  """  
      self.ManuallyUpdVer:bool = obj["ManuallyUpdVer"]
      """  Indicates that Versions were updated manually  """  
      self.RuleVer:int = obj["RuleVer"]
      """  Specifies the individual rule version. Uses a single numeric sequence and increments every time a change is made in a corresponding rule.  """  
      self.PatchRuleVer:int = obj["PatchRuleVer"]
      """  Specifies the individual rule patch version. Uses a single numeric sequence and increments each time a change is released in a patch to a client between service packs. The patch version resets to zero every time a service pack is released.  """  
      self.PrevModified:bool = obj["PrevModified"]
      """  Value of Modified field before last Update Versions  """  
      self.Modified:bool = obj["Modified"]
      """  Indicates that data were modified  """  
      self.LocVer:int = obj["LocVer"]
      """  LocVer  """  
      self.LocPatchVer:int = obj["LocPatchVer"]
      """  LocPatchVer  """  
      self.LocModified:bool = obj["LocModified"]
      """  LocModified  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.EnableCustomization:bool = obj["EnableCustomization"]
      """  Enabling/disabling customization for the Book  """  
      self.BaseModified:bool = obj["BaseModified"]
      """  Indicates that base information on rule was changed. In this case this rule will not be automatically updated during converstion program to save user's changes.  """  
      self.Customization:bool = obj["Customization"]
      """  Indicates that rule contaion operations on 'Customization' part  """  
      self.Operator:str = obj["Operator"]
      """  Used to bind UI control.  """  
      self.SelCriteriaDisplay:str = obj["SelCriteriaDisplay"]
      """  Selection Criteria Display.  """  
      self.Argument:str = obj["Argument"]
      """  Used to bind UI control.  """  
      self.DevelopMode:bool = obj["DevelopMode"]
      self.Loaded:int = obj["Loaded"]
      """   0- not loaded on client       
1-loaded fully
2- partial  """  
      self.RuleType:str = obj["RuleType"]
      """  RuleType - PrePost(calculation in pre-post mode before posting), Post(standard posting) or Ref (Calculate reference GLControl during posting)  """  
      self.IsError:bool = obj["IsError"]
      """  Is used to show icon in Tree.  """  
      self.ErrorText:str = obj["ErrorText"]
      """  Contains error text for a rule.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_COASegmentNameListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.SegmentNbr:int = obj["SegmentNbr"]
      """  System generated number from 1 through 20.  """  
      self.SegmentName:str = obj["SegmentName"]
      """  Name of Segment  """  
      self.Abbreviation:str = obj["Abbreviation"]
      """  Short name of segment.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLBookListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  """  
      self.Description:str = obj["Description"]
      """  Descripiton of Book  """  
      self.MainBook:bool = obj["MainBook"]
      """  Indicates if this is the Main Book.  Only one main book is allowed.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account Code  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Indicates the base currency for the book  """  
      self.BookType:int = obj["BookType"]
      """  Indicates the type of book.  Standard, Consolidation, etc.  """  
      self.COACodeDescription:str = obj["COACodeDescription"]
      self.Inactive:bool = obj["Inactive"]
      """  Indicates if the book is inactive  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  Identifier for the Fiscal Calendar assigned to the book  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.OpenBalUpdateOpt:str = obj["OpenBalUpdateOpt"]
      """  Indicates how opening balances will be updated  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLBookMapRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company value. If it is empty that mean that mapping is used for all companies, that do not have specified data.  """  
      self.ImportBook:str = obj["ImportBook"]
      """  Source BookID  """  
      self.ImportCOA:str = obj["ImportCOA"]
      """  COA Code of Source Book  """  
      self.MapBook:str = obj["MapBook"]
      """  Target Book ID  """  
      self.MapCOA:str = obj["MapCOA"]
      """  COA Code of Target Book  """  
      self.Package:str = obj["Package"]
      """  Package of Source Book  """  
      self.RevisionCode:str = obj["RevisionCode"]
      """  New Revision Code  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLBookPackageSegmentMapRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company ID  """  
      self.BookID:str = obj["BookID"]
      """  Book ID  """  
      self.Package:str = obj["Package"]
      """  Posting Rules Package  """  
      self.SourceSegmentNbr:int = obj["SourceSegmentNbr"]
      """  Segment Number in Posting Rules Package  """  
      self.TargetSegmentNbr:int = obj["TargetSegmentNbr"]
      """  Segment Number in COA of the Book  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  User ID of the user who created the record  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  The date/ time that the record was created  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of the user who made the last change to this record  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  The date/ time that the record was last changed  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account Code  """  
      self.TargetSegmentName:str = obj["TargetSegmentName"]
      """  Target Segment Name  """  
      self.BitFlag:int = obj["BitFlag"]
      self.SourceSegmentName:str = obj["SourceSegmentName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLSegmentMapRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company value. If it is empty that mean that mapping is used for all companies, that do not have specified data.  """  
      self.ImportBook:str = obj["ImportBook"]
      """  Source Book ID  """  
      self.ImportCOA:str = obj["ImportCOA"]
      """  COA Code of Source Book  """  
      self.ImportSegmentName:str = obj["ImportSegmentName"]
      """  Source Segment Name  """  
      self.ImportSegmentNum:int = obj["ImportSegmentNum"]
      """  Source Segment Number  """  
      self.MapBook:str = obj["MapBook"]
      """  Target Book ID  """  
      self.MapCOA:str = obj["MapCOA"]
      """  COA Code of Target Book  """  
      self.MapSegmentName:str = obj["MapSegmentName"]
      """  Target Segment Name  """  
      self.MapSegmentNum:int = obj["MapSegmentNum"]
      """  Target Segment Number  """  
      self.Package:str = obj["Package"]
      """  Package of Source Book  """  
      self.RevisionCode:str = obj["RevisionCode"]
      """  New Revision Code  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_HierarchicalDataRow:
   def __init__(self, obj):
      self.ID:str = obj["ID"]
      """  ID  """  
      self.ParentID:str = obj["ParentID"]
      """  ParentID  """  
      self.Name:str = obj["Name"]
      """  Name  """  
      self.DataType:str = obj["DataType"]
      """  DataType  """  
      self.DisplayText:str = obj["DisplayText"]
      """  DisplayText  """  
      self.FormulaText:str = obj["FormulaText"]
      """  FormulaText  """  
      self.Selectable:bool = obj["Selectable"]
      """  Node can be selected in the tree.  """  
      self.DataTypeIsValueType:bool = obj["DataTypeIsValueType"]
      """  DataTypeIsValueType  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LinkComboDataTableset:
   def __init__(self, obj):
      self.PhraseItem:list[Erp_Tablesets_PhraseItemRow] = obj["PhraseItem"]
      self.PhraseItemBinding:list[Erp_Tablesets_PhraseItemBindingRow] = obj["PhraseItemBinding"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PhraseItemBindingRow:
   def __init__(self, obj):
      self.link01:str = obj["link01"]
      self.link02:str = obj["link02"]
      self.link03:str = obj["link03"]
      self.link04:str = obj["link04"]
      self.link05:str = obj["link05"]
      self.link06:str = obj["link06"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PhraseItemRow:
   def __init__(self, obj):
      self.alwaysClickable:bool = obj["alwaysClickable"]
      self.defaultValue:str = obj["defaultValue"]
      self.epBinding:str = obj["epBinding"]
      self.itemId:str = obj["itemId"]
      self.maxWidth:int = obj["maxWidth"]
      self.phraseItemId:str = obj["phraseItemId"]
      self.type:str = obj["type"]
      self.value:str = obj["value"]
      self.dataType:str = obj["dataType"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RevisionImportOpRow:
   def __init__(self, obj):
      self.ACTRevisionUID:int = obj["ACTRevisionUID"]
      """  ACT Revision UID of updated revision  """  
      self.ImportABT:bool = obj["ImportABT"]
      """  Indicate that VBD Structure should be updated during import in Update Mode  """  
      self.ImportBR:bool = obj["ImportBR"]
      """  Indicate that Ruleset should be updated during import in Update Mode  """  
      self.NewRevisionCode:str = obj["NewRevisionCode"]
      self.ReplaceExisting:bool = obj["ReplaceExisting"]
      """  Flag to indicate that existing Revision with "New Revision Code" should be removed before import.  """  
      self.RevisionCode:str = obj["RevisionCode"]
      self.UpdateMode:bool = obj["UpdateMode"]
      """  Indicate that import shoud be done in Update Mode  """  
      self.ACTTypeName:str = obj["ACTTypeName"]
      self.FileName:str = obj["FileName"]
      self.XMLData:str = obj["XMLData"]
      self.IsSystemXML:bool = obj["IsSystemXML"]
      """  Indicates that imported file is system  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtACTTypeTableset:
   def __init__(self, obj):
      self.ACTType:list[Erp_Tablesets_ACTTypeRow] = obj["ACTType"]
      self.ACTRevision:list[Erp_Tablesets_ACTRevisionRow] = obj["ACTRevision"]
      self.ABTDocLine:list[Erp_Tablesets_ABTDocLineRow] = obj["ABTDocLine"]
      self.ABTAmount:list[Erp_Tablesets_ABTAmountRow] = obj["ABTAmount"]
      self.ABTPostEntity:list[Erp_Tablesets_ABTPostEntityRow] = obj["ABTPostEntity"]
      self.ABTPostCode:list[Erp_Tablesets_ABTPostCodeRow] = obj["ABTPostCode"]
      self.ABTQuery:list[Erp_Tablesets_ABTQueryRow] = obj["ABTQuery"]
      self.ABTQParam:list[Erp_Tablesets_ABTQParamRow] = obj["ABTQParam"]
      self.ACTBook:list[Erp_Tablesets_ACTBookRow] = obj["ACTBook"]
      self.BookingRule:list[Erp_Tablesets_BookingRuleRow] = obj["BookingRule"]
      self.BookValRule:list[Erp_Tablesets_BookValRuleRow] = obj["BookValRule"]
      self.BROperation:list[Erp_Tablesets_BROperationRow] = obj["BROperation"]
      self.BROperationCustom:list[Erp_Tablesets_BROperationCustomRow] = obj["BROperationCustom"]
      self.BRFunction:list[Erp_Tablesets_BRFunctionRow] = obj["BRFunction"]
      self.BookVar:list[Erp_Tablesets_BookVarRow] = obj["BookVar"]
      self.BRFuncArgs:list[Erp_Tablesets_BRFuncArgsRow] = obj["BRFuncArgs"]
      self.BRFuncOperation:list[Erp_Tablesets_BRFuncOperationRow] = obj["BRFuncOperation"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class ExportToXML_input:
   """ Required : 
   strRevisionList
   aCTTypeUID
   developMode
   """  
   def __init__(self, obj):
      self.strRevisionList:str = obj["strRevisionList"]
      """  strRevisionList  """  
      self.aCTTypeUID:int = obj["aCTTypeUID"]
      """  aCTTypeUID  """  
      self.developMode:bool = obj["developMode"]
      """  Developer Mode  """  
      pass

class ExportToXML_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.cXML:list = obj[any]
      pass

      """  output parameters  """  

class FillBAQDescription_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

class FillBAQDescription_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class FunctionPhraseElementDelete_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeSubDataTableset] = obj["ds"]
      pass

class FunctionPhraseElementDelete_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeSubDataTableset] = obj["ds"]
      pass

      """  output parameters  """  

class FunctionPhraseElementGetNew_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeSubDataTableset] = obj["ds"]
      pass

class FunctionPhraseElementGetNew_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeSubDataTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GenerateTemplate_input:
   """ Required : 
   companyName
   aCTTypeUID
   aCTRevisionUID
   """  
   def __init__(self, obj):
      self.companyName:str = obj["companyName"]
      """  Company Name  """  
      self.aCTTypeUID:int = obj["aCTTypeUID"]
      """  aCTTypeUID  """  
      self.aCTRevisionUID:int = obj["aCTRevisionUID"]
      """  aCTRevisionUID  """  
      pass

class GenerateTemplate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.errorText:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetAllACTTypesForExport_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      """  Returns the result dataset  """  
      pass

class GetBRContainerRows_input:
   """ Required : 
   tag
   bookID
   actTypeUID
   actRevisionUID
   """  
   def __init__(self, obj):
      self.tag:str = obj["tag"]
      """  tag  """  
      self.bookID:str = obj["bookID"]
      """  bookID  """  
      self.actTypeUID:int = obj["actTypeUID"]
      """  actTypeUID  """  
      self.actRevisionUID:int = obj["actRevisionUID"]
      """  actRevisionUID  """  
      pass

class GetBRContainerRows_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      """  Returns the result dataset  """  
      pass

class GetBookPackage_input:
   """ Required : 
   company
   actTypeName
   revisionCode
   BookID
   """  
   def __init__(self, obj):
      self.company:str = obj["company"]
      """  Company  """  
      self.actTypeName:str = obj["actTypeName"]
      """  GL Transaction Type Name  """  
      self.revisionCode:str = obj["revisionCode"]
      """  Revision Code  """  
      self.BookID:str = obj["BookID"]
      """  BookID  """  
      pass

class GetBookPackage_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  Package  """  
      pass

class GetBookVarOwnerID_input:
   """ Required : 
   actTypeUID
   actRevisionUID
   bookID
   ownerType
   """  
   def __init__(self, obj):
      self.actTypeUID:int = obj["actTypeUID"]
      """  aCTTypeUID  """  
      self.actRevisionUID:int = obj["actRevisionUID"]
      """  actRevisionUID  """  
      self.bookID:str = obj["bookID"]
      """  bookID  """  
      self.ownerType:str = obj["ownerType"]
      """  ownerType  """  
      pass

class GetBookVarOwnerID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.strList:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetBookVarOwnerTypes_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.strList:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetBookVarTypeList_input:
   """ Required : 
   itemBinding
   ds
   """  
   def __init__(self, obj):
      self.itemBinding:str = obj["itemBinding"]
      """  the name of binding for linked combo control  """  
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

class GetBookVarTypeList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_LinkComboDataTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetBookVersions_input:
   """ Required : 
   actTypeUID
   actRevisionUID
   bookID
   """  
   def __init__(self, obj):
      self.actTypeUID:int = obj["actTypeUID"]
      """  ACTTypeUID  """  
      self.actRevisionUID:int = obj["actRevisionUID"]
      """  ACTRevisionUID  """  
      self.bookID:str = obj["bookID"]
      """  BookID  """  
      pass

class GetBookVersions_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opPackage:str = obj["parameters"]
      self.opRulesetVer:int = obj["parameters"]
      self.opPatchRulesetVer:int = obj["parameters"]
      pass

      """  output parameters  """  

class GetByIDExt_input:
   """ Required : 
   acTTypeUID
   developMode
   """  
   def __init__(self, obj):
      self.acTTypeUID:int = obj["acTTypeUID"]
      self.developMode:bool = obj["developMode"]
      """  flag Developer Mode  """  
      pass

class GetByIDExt_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ACTTypeTableset] = obj["returnObj"]
      pass

class GetByID_Revisions_input:
   """ Required : 
   acTTypeUID
   revisions
   developMode
   """  
   def __init__(self, obj):
      self.acTTypeUID:int = obj["acTTypeUID"]
      self.revisions:str = obj["revisions"]
      """  Revision list (Comma delimiter)  """  
      self.developMode:bool = obj["developMode"]
      """  flag Developer Mode  """  
      pass

class GetByID_Revisions_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ACTTypeTableset] = obj["returnObj"]
      pass

class GetByID_input:
   """ Required : 
   acTTypeUID
   """  
   def __init__(self, obj):
      self.acTTypeUID:int = obj["acTTypeUID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ACTTypeTableset] = obj["returnObj"]
      pass

class GetBySysRowID_input:
   """ Required : 
   id
   """  
   def __init__(self, obj):
      self.id:str = obj["id"]
      pass

class GetBySysRowID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ACTTypeTableset] = obj["returnObj"]
      pass

class GetBySysRowIDs_input:
   """ Required : 
   ids
   """  
   def __init__(self, obj):
      self.ids:str = obj["ids"]
      pass

class GetBySysRowIDs_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ACTTypeTableset] = obj["returnObj"]
      pass

class GetCOAIDForBook_input:
   """ Required : 
   BookID
   """  
   def __init__(self, obj):
      self.BookID:str = obj["BookID"]
      pass

class GetCOAIDForBook_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetCOAMapsList_input:
   """ Required : 
   mapBookCOAID
   currentBookCOAID
   """  
   def __init__(self, obj):
      self.mapBookCOAID:str = obj["mapBookCOAID"]
      self.currentBookCOAID:str = obj["currentBookCOAID"]
      pass

class GetCOAMapsList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetCommonTypeList_input:
   """ Required : 
   itemBinding
   currentType
   """  
   def __init__(self, obj):
      self.itemBinding:str = obj["itemBinding"]
      self.currentType:str = obj["currentType"]
      """  BookVar.VarType or BRFunction.ResultType  """  
      pass

class GetCommonTypeList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_LinkComboDataTableset] = obj["returnObj"]
      pass

class GetConditionList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_LinkComboDataTableset] = obj["returnObj"]
      pass

class GetContainerPhraseItems_input:
   """ Required : 
   actTypeID
   actRevisionUID
   bookID
   functionUID
   ruleUID
   container
   isLogicalCondition
   tableName
   """  
   def __init__(self, obj):
      self.actTypeID:int = obj["actTypeID"]
      self.actRevisionUID:int = obj["actRevisionUID"]
      self.bookID:str = obj["bookID"]
      self.functionUID:int = obj["functionUID"]
      self.ruleUID:int = obj["ruleUID"]
      self.container:str = obj["container"]
      self.isLogicalCondition:bool = obj["isLogicalCondition"]
      self.tableName:str = obj["tableName"]
      pass

class GetContainerPhraseItems_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_LinkComboDataTableset] = obj["returnObj"]
      pass

class GetCurrentVersion_input:
   """ Required : 
   actTypeName
   """  
   def __init__(self, obj):
      self.actTypeName:str = obj["actTypeName"]
      """  ACT Type Name  """  
      pass

class GetCurrentVersion_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.abtVer:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetCustomContextMenuXml_input:
   """ Required : 
   iACTTypeUID
   iACTRevisionUID
   sBookID
   iRuleUID
   iFunctionID
   """  
   def __init__(self, obj):
      self.iACTTypeUID:int = obj["iACTTypeUID"]
      """  ACTTypeUID  """  
      self.iACTRevisionUID:int = obj["iACTRevisionUID"]
      """  ACTRevisionUID  """  
      self.sBookID:str = obj["sBookID"]
      """  BookID  """  
      self.iRuleUID:int = obj["iRuleUID"]
      """  RuleUID  """  
      self.iFunctionID:int = obj["iFunctionID"]
      """  FunctionUID  """  
      pass

class GetCustomContextMenuXml_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.sXML:list = obj[any]
      pass

      """  output parameters  """  

class GetEntityForBookingRule_input:
   """ Required : 
   actTypeID
   actRevisionUID
   bookID
   ruleID
   """  
   def __init__(self, obj):
      self.actTypeID:int = obj["actTypeID"]
      """  ACTTypeUID  """  
      self.actRevisionUID:int = obj["actRevisionUID"]
      """  ACTRevisionUID  """  
      self.bookID:str = obj["bookID"]
      """  BookID  """  
      self.ruleID:int = obj["ruleID"]
      """  RuleUID  """  
      pass

class GetEntityForBookingRule_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.brEntity:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetFieldsOfBAQList_input:
   """ Required : 
   BAQID
   """  
   def __init__(self, obj):
      self.BAQID:str = obj["BAQID"]
      pass

class GetFieldsOfBAQList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetFieldsOfTable_input:
   """ Required : 
   schema
   table
   """  
   def __init__(self, obj):
      self.schema:str = obj["schema"]
      self.table:str = obj["table"]
      pass

class GetFieldsOfTable_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetFlowList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.strList:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetFormulaPhraseItems_input:
   """ Required : 
   actTypeUID
   actRevisionUID
   ruleUID
   functionUID
   container
   containerType
   formula
   bookID
   docLinePath
   funcOperUID
   isLogicalCondition
   bindingSuffix
   """  
   def __init__(self, obj):
      self.actTypeUID:int = obj["actTypeUID"]
      self.actRevisionUID:int = obj["actRevisionUID"]
      self.ruleUID:int = obj["ruleUID"]
      self.functionUID:int = obj["functionUID"]
      self.container:str = obj["container"]
      self.containerType:str = obj["containerType"]
      self.formula:str = obj["formula"]
      self.bookID:str = obj["bookID"]
      self.docLinePath:str = obj["docLinePath"]
      """  BRFunction.DocLinePath OR BookingRule.ForEach  """  
      self.funcOperUID:int = obj["funcOperUID"]
      """  0 if not BRFuncOperation  """  
      self.isLogicalCondition:bool = obj["isLogicalCondition"]
      self.bindingSuffix:str = obj["bindingSuffix"]
      """  'Custom' if BROperation, 'FuncOper' of BRFuncOperation, '' if BROperation  """  
      pass

class GetFormulaPhraseItems_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_LinkComboDataTableset] = obj["returnObj"]
      pass

class GetFuncVersions_input:
   """ Required : 
   actTypeUID
   actRevisionUID
   bookID
   functionUID
   """  
   def __init__(self, obj):
      self.actTypeUID:int = obj["actTypeUID"]
      """  ACTTypeUID  """  
      self.actRevisionUID:int = obj["actRevisionUID"]
      """  ACTRevisionUID  """  
      self.bookID:str = obj["bookID"]
      """  BookID  """  
      self.functionUID:int = obj["functionUID"]
      """  FunctionUID  """  
      pass

class GetFuncVersions_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opFuncVer:int = obj["parameters"]
      self.opPatchFuncVer:int = obj["parameters"]
      pass

      """  output parameters  """  

class GetFunctionPhraseElements_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

class GetFunctionPhraseElements_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ACTTypeSubDataTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetFunctionPhrase_input:
   """ Required : 
   actTypeUID
   actRevisionUID
   functionUID
   name
   """  
   def __init__(self, obj):
      self.actTypeUID:int = obj["actTypeUID"]
      self.actRevisionUID:int = obj["actRevisionUID"]
      self.functionUID:int = obj["functionUID"]
      self.name:str = obj["name"]
      pass

class GetFunctionPhrase_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_LinkComboDataTableset] = obj["returnObj"]
      pass

class GetFunctionResultTypeList_input:
   """ Required : 
   itemBinding
   ds
   """  
   def __init__(self, obj):
      self.itemBinding:str = obj["itemBinding"]
      """  the name of binding for linked combo control  """  
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

class GetFunctionResultTypeList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_LinkComboDataTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetFunctionTree_input:
   """ Required : 
   GPostingUID
   NodeID
   """  
   def __init__(self, obj):
      self.GPostingUID:str = obj["GPostingUID"]
      """  Function SysRowID (Use 0aaa410e-ecc2-4dcd-9e6d-0c2d0d879149 for test purposes)  """  
      self.NodeID:str = obj["NodeID"]
      """  Fake node.  """  
      pass

class GetFunctionTree_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      pass

class GetGLControlTypesList_input:
   """ Required : 
   ruleType
   """  
   def __init__(self, obj):
      self.ruleType:str = obj["ruleType"]
      """  Rule Type  """  
      pass

class GetGLControlTypesList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetHashSystemXml_input:
   """ Required : 
   actTypeName
   package
   """  
   def __init__(self, obj):
      self.actTypeName:str = obj["actTypeName"]
      """  GL Transaction Type Name  """  
      self.package:str = obj["package"]
      """  Package  """  
      pass

class GetHashSystemXml_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.value:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetIDByName_input:
   """ Required : 
   companyName
   actTypeName
   """  
   def __init__(self, obj):
      self.companyName:str = obj["companyName"]
      """  CompanyName  """  
      self.actTypeName:str = obj["actTypeName"]
      """  ACT Type Name  """  
      pass

class GetIDByName_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.actTypeID:int = obj["parameters"]
      pass

      """  output parameters  """  

class GetLeftTree_input:
   """ Required : 
   GPostingUID
   NodeID
   """  
   def __init__(self, obj):
      self.GPostingUID:str = obj["GPostingUID"]
      """  A ~ (tilde) separated list consisting of:
            0 = Node text
            1 = Node tag  """  
      self.NodeID:str = obj["NodeID"]
      """  Not currently used  """  
      pass

class GetLeftTree_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      """  Tree Object  """  
      pass

class GetList_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  An expression used to filter the rows. Can be left blank for all rows.  """  
      self.pageSize:int = obj["pageSize"]
      """  The maximum number of rows to return. Leave as zero for no maximum.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Page of rows to return.  """  
      pass

class GetList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ACTTypeListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetMapBookList_input:
   """ Required : 
   actTypeUID
   actRevisionUID
   currentBookID
   """  
   def __init__(self, obj):
      self.actTypeUID:int = obj["actTypeUID"]
      self.actRevisionUID:int = obj["actRevisionUID"]
      self.currentBookID:str = obj["currentBookID"]
      pass

class GetMapBookList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetNewABTAmount_input:
   """ Required : 
   ds
   acTTypeUID
   acTRevisionUID
   abTDocLineUID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      self.acTTypeUID:int = obj["acTTypeUID"]
      self.acTRevisionUID:int = obj["acTRevisionUID"]
      self.abTDocLineUID:int = obj["abTDocLineUID"]
      pass

class GetNewABTAmount_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewABTDocLine_input:
   """ Required : 
   ds
   acTTypeUID
   acTRevisionUID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      self.acTTypeUID:int = obj["acTTypeUID"]
      self.acTRevisionUID:int = obj["acTRevisionUID"]
      pass

class GetNewABTDocLine_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewABTPostCode_input:
   """ Required : 
   ds
   acTTypeUID
   acTRevisionUID
   abTDocLineUID
   abTPostEntityUID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      self.acTTypeUID:int = obj["acTTypeUID"]
      self.acTRevisionUID:int = obj["acTRevisionUID"]
      self.abTDocLineUID:int = obj["abTDocLineUID"]
      self.abTPostEntityUID:int = obj["abTPostEntityUID"]
      pass

class GetNewABTPostCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewABTPostEntity_input:
   """ Required : 
   ds
   acTTypeUID
   acTRevisionUID
   abTDocLineUID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      self.acTTypeUID:int = obj["acTTypeUID"]
      self.acTRevisionUID:int = obj["acTRevisionUID"]
      self.abTDocLineUID:int = obj["abTDocLineUID"]
      pass

class GetNewABTPostEntity_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewABTQParam_input:
   """ Required : 
   ds
   acTTypeUID
   acTRevisionUID
   abTDocLineUID
   abTQueryUID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      self.acTTypeUID:int = obj["acTTypeUID"]
      self.acTRevisionUID:int = obj["acTRevisionUID"]
      self.abTDocLineUID:int = obj["abTDocLineUID"]
      self.abTQueryUID:int = obj["abTQueryUID"]
      pass

class GetNewABTQParam_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewABTQuery_input:
   """ Required : 
   ds
   acTTypeUID
   acTRevisionUID
   abTDocLineUID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      self.acTTypeUID:int = obj["acTTypeUID"]
      self.acTRevisionUID:int = obj["acTRevisionUID"]
      self.abTDocLineUID:int = obj["abTDocLineUID"]
      pass

class GetNewABTQuery_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewACTBook_input:
   """ Required : 
   ds
   acTTypeUID
   acTRevisionUID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      self.acTTypeUID:int = obj["acTTypeUID"]
      self.acTRevisionUID:int = obj["acTRevisionUID"]
      pass

class GetNewACTBook_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewACTRevision_input:
   """ Required : 
   ds
   acTTypeUID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      self.acTTypeUID:int = obj["acTTypeUID"]
      pass

class GetNewACTRevision_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewACTType_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

class GetNewACTType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewBRFuncArgs_input:
   """ Required : 
   ds
   acTTypeUID
   acTRevisionUID
   functionUID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      self.acTTypeUID:int = obj["acTTypeUID"]
      self.acTRevisionUID:int = obj["acTRevisionUID"]
      self.functionUID:int = obj["functionUID"]
      pass

class GetNewBRFuncArgs_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewBRFuncOperation_input:
   """ Required : 
   ds
   acTTypeUID
   acTRevisionUID
   funcOperUID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      self.acTTypeUID:int = obj["acTTypeUID"]
      self.acTRevisionUID:int = obj["acTRevisionUID"]
      self.funcOperUID:int = obj["funcOperUID"]
      pass

class GetNewBRFuncOperation_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewBRFunction_input:
   """ Required : 
   ds
   acTTypeUID
   acTRevisionUID
   bookID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      self.acTTypeUID:int = obj["acTTypeUID"]
      self.acTRevisionUID:int = obj["acTRevisionUID"]
      self.bookID:str = obj["bookID"]
      pass

class GetNewBRFunction_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewBROperationCustom_input:
   """ Required : 
   ds
   acTTypeUID
   acTRevisionUID
   bookID
   ruleUID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      self.acTTypeUID:int = obj["acTTypeUID"]
      self.acTRevisionUID:int = obj["acTRevisionUID"]
      self.bookID:str = obj["bookID"]
      self.ruleUID:int = obj["ruleUID"]
      pass

class GetNewBROperationCustom_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewBROperation_input:
   """ Required : 
   ds
   acTTypeUID
   acTRevisionUID
   bookID
   ruleUID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      self.acTTypeUID:int = obj["acTTypeUID"]
      self.acTRevisionUID:int = obj["acTRevisionUID"]
      self.bookID:str = obj["bookID"]
      self.ruleUID:int = obj["ruleUID"]
      pass

class GetNewBROperation_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewBookVar_input:
   """ Required : 
   ds
   acTTypeUID
   acTRevisionUID
   bookID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      self.acTTypeUID:int = obj["acTTypeUID"]
      self.acTRevisionUID:int = obj["acTRevisionUID"]
      self.bookID:str = obj["bookID"]
      pass

class GetNewBookVar_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewBookingRule_input:
   """ Required : 
   ds
   acTTypeUID
   acTRevisionUID
   bookID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      self.acTTypeUID:int = obj["acTTypeUID"]
      self.acTRevisionUID:int = obj["acTRevisionUID"]
      self.bookID:str = obj["bookID"]
      pass

class GetNewBookingRule_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetOperatorList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.strList:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetPostCodeTypesExt_input:
   """ Required : 
   currentValue
   """  
   def __init__(self, obj):
      self.currentValue:str = obj["currentValue"]
      pass

class GetPostCodeTypesExt_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_LinkComboDataTableset] = obj["returnObj"]
      pass

class GetPostCodeTypes_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.strTypes:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetPostEntityDataSourceList_input:
   """ Required : 
   actTypeUID
   actRevisionUID
   abtDocLineUID
   schemaName
   developMode
   isDefault
   """  
   def __init__(self, obj):
      self.actTypeUID:int = obj["actTypeUID"]
      self.actRevisionUID:int = obj["actRevisionUID"]
      self.abtDocLineUID:int = obj["abtDocLineUID"]
      self.schemaName:str = obj["schemaName"]
      self.developMode:bool = obj["developMode"]
      self.isDefault:bool = obj["isDefault"]
      pass

class GetPostEntityDataSourceList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetPostingRuleBaseTree_input:
   """ Required : 
   GPostingUID
   NodeID
   """  
   def __init__(self, obj):
      self.GPostingUID:str = obj["GPostingUID"]
      """  Function ID (Use 0aaa410e-ecc2-4dcd-9e6d-0c2d0d879149 for test purposes)  """  
      self.NodeID:str = obj["NodeID"]
      """  Fake node.  """  
      pass

class GetPostingRuleBaseTree_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      pass

class GetPostingRuleCustomizationTree_input:
   """ Required : 
   GPostingUID
   NodeID
   """  
   def __init__(self, obj):
      self.GPostingUID:str = obj["GPostingUID"]
      """  Function ID (Use 0aaa410e-ecc2-4dcd-9e6d-0c2d0d879149 for test purposes)  """  
      self.NodeID:str = obj["NodeID"]
      """  Fake node.  """  
      pass

class GetPostingRuleCustomizationTree_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      pass

class GetRelatedContextItemsBookVarType_input:
   """ Required : 
   whoIsCalled
   tag
   ds
   """  
   def __init__(self, obj):
      self.whoIsCalled:str = obj["whoIsCalled"]
      self.tag:str = obj["tag"]
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

class GetRelatedContextItemsBookVarType_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ACTTypeSubDataTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.value:str = obj["parameters"]
      self.dataType:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRelatedContextItemsCustom_input:
   """ Required : 
   whoIsCalled
   tag
   ds
   """  
   def __init__(self, obj):
      self.whoIsCalled:str = obj["whoIsCalled"]
      self.tag:str = obj["tag"]
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

class GetRelatedContextItemsCustom_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ACTTypeSubDataTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.value:str = obj["parameters"]
      self.dataType:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRelatedContextItemsFuncOper_input:
   """ Required : 
   whoIsCalled
   tag
   ds
   """  
   def __init__(self, obj):
      self.whoIsCalled:str = obj["whoIsCalled"]
      self.tag:str = obj["tag"]
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

class GetRelatedContextItemsFuncOper_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ACTTypeSubDataTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.value:str = obj["parameters"]
      self.dataType:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRelatedContextItemsFunctionPhrase_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

class GetRelatedContextItemsFunctionPhrase_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ACTTypeSubDataTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.value:str = obj["parameters"]
      self.dataType:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRelatedContextItemsFunctionResultType_input:
   """ Required : 
   whoIsCalled
   tag
   ds
   """  
   def __init__(self, obj):
      self.whoIsCalled:str = obj["whoIsCalled"]
      self.tag:str = obj["tag"]
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

class GetRelatedContextItemsFunctionResultType_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ACTTypeSubDataTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.value:str = obj["parameters"]
      self.dataType:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRelatedContextItems_input:
   """ Required : 
   whoIsCalled
   tag
   ds
   """  
   def __init__(self, obj):
      self.whoIsCalled:str = obj["whoIsCalled"]
      self.tag:str = obj["tag"]
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

class GetRelatedContextItems_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ACTTypeSubDataTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.value:str = obj["parameters"]
      self.dataType:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRevVersions_input:
   """ Required : 
   actTypeUID
   actRevisionUID
   """  
   def __init__(self, obj):
      self.actTypeUID:int = obj["actTypeUID"]
      """  ACTTypeUID  """  
      self.actRevisionUID:int = obj["actRevisionUID"]
      """  ACTRevisionUID  """  
      pass

class GetRevVersions_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opABTVer:str = obj["parameters"]
      self.opPatchABTVer:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetRevisionIDByName_input:
   """ Required : 
   companyName
   actRevisionCode
   actTypeID
   """  
   def __init__(self, obj):
      self.companyName:str = obj["companyName"]
      """  Company Name  """  
      self.actRevisionCode:str = obj["actRevisionCode"]
      """  ACT Revision Code  """  
      self.actTypeID:int = obj["actTypeID"]
      """  ACTTypeID  """  
      pass

class GetRevisionIDByName_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.actRevisionID:int = obj["parameters"]
      pass

      """  output parameters  """  

class GetRevisionStatusesList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetRevisionsList_input:
   """ Required : 
   actTypeUID
   """  
   def __init__(self, obj):
      self.actTypeUID:int = obj["actTypeUID"]
      pass

class GetRevisionsList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetRightTree_input:
   """ Required : 
   GPostingUID
   NodeID
   """  
   def __init__(self, obj):
      self.GPostingUID:str = obj["GPostingUID"]
      """  A ~ (tilde) separated list consisting of:
            0 = Node text
            1 = Node tag  """  
      self.NodeID:str = obj["NodeID"]
      """  Not currently used  """  
      pass

class GetRightTree_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      """  Tree Object  """  
      pass

class GetRows_input:
   """ Required : 
   whereClauseACTType
   whereClauseACTRevision
   whereClauseABTDocLine
   whereClauseABTAmount
   whereClauseABTPostEntity
   whereClauseABTPostCode
   whereClauseABTQuery
   whereClauseABTQParam
   whereClauseACTBook
   whereClauseBookingRule
   whereClauseBookValRule
   whereClauseBROperation
   whereClauseBROperationCustom
   whereClauseBRFunction
   whereClauseBookVar
   whereClauseBRFuncArgs
   whereClauseBRFuncOperation
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseACTType:str = obj["whereClauseACTType"]
      self.whereClauseACTRevision:str = obj["whereClauseACTRevision"]
      self.whereClauseABTDocLine:str = obj["whereClauseABTDocLine"]
      self.whereClauseABTAmount:str = obj["whereClauseABTAmount"]
      self.whereClauseABTPostEntity:str = obj["whereClauseABTPostEntity"]
      self.whereClauseABTPostCode:str = obj["whereClauseABTPostCode"]
      self.whereClauseABTQuery:str = obj["whereClauseABTQuery"]
      self.whereClauseABTQParam:str = obj["whereClauseABTQParam"]
      self.whereClauseACTBook:str = obj["whereClauseACTBook"]
      self.whereClauseBookingRule:str = obj["whereClauseBookingRule"]
      self.whereClauseBookValRule:str = obj["whereClauseBookValRule"]
      self.whereClauseBROperation:str = obj["whereClauseBROperation"]
      self.whereClauseBROperationCustom:str = obj["whereClauseBROperationCustom"]
      self.whereClauseBRFunction:str = obj["whereClauseBRFunction"]
      self.whereClauseBookVar:str = obj["whereClauseBookVar"]
      self.whereClauseBRFuncArgs:str = obj["whereClauseBRFuncArgs"]
      self.whereClauseBRFuncOperation:str = obj["whereClauseBRFuncOperation"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ACTTypeTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRuleContextsList_input:
   """ Required : 
   ruleType
   glControlType
   """  
   def __init__(self, obj):
      self.ruleType:str = obj["ruleType"]
      """  Rule Type  """  
      self.glControlType:str = obj["glControlType"]
      """  GL Control Type  """  
      pass

class GetRuleContextsList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetRuleVersions_input:
   """ Required : 
   actTypeUID
   actRevisionUID
   bookID
   ruleUID
   """  
   def __init__(self, obj):
      self.actTypeUID:int = obj["actTypeUID"]
      """  ACTTypeUID  """  
      self.actRevisionUID:int = obj["actRevisionUID"]
      """  ACTRevisionUID  """  
      self.bookID:str = obj["bookID"]
      """  BookID  """  
      self.ruleUID:int = obj["ruleUID"]
      """  RuleUID  """  
      pass

class GetRuleVersions_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opRuleVer:int = obj["parameters"]
      self.opPatchRuleVer:int = obj["parameters"]
      pass

      """  output parameters  """  

class GetStatusList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.strList:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetSummarizeList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.strList:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetTrCurrencyList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.strList:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetValueTypesForPostCode_input:
   """ Required : 
   actTypeUID
   actRevisionUID
   docLineUID
   abtPostEntityUID
   abtPostCodeUID
   """  
   def __init__(self, obj):
      self.actTypeUID:int = obj["actTypeUID"]
      self.actRevisionUID:int = obj["actRevisionUID"]
      self.docLineUID:int = obj["docLineUID"]
      self.abtPostEntityUID:int = obj["abtPostEntityUID"]
      self.abtPostCodeUID:int = obj["abtPostCodeUID"]
      pass

class GetValueTypesForPostCode_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_LinkComboDataTableset] = obj["returnObj"]
      pass

class GetVarTypes_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.arTypes:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetWarningRevisionStatus_input:
   """ Required : 
   iACTTypeUID
   iACTRevisionUID
   cStatus
   """  
   def __init__(self, obj):
      self.iACTTypeUID:int = obj["iACTTypeUID"]
      """  iACTTypeUID  """  
      self.iACTRevisionUID:int = obj["iACTRevisionUID"]
      """  iACTRevisionUID  """  
      self.cStatus:str = obj["cStatus"]
      """  Status  """  
      pass

class GetWarningRevisionStatus_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.cWarning:str = obj["parameters"]
      pass

      """  output parameters  """  

class Ice_BOUpdErrorRow:
   def __init__(self, obj):
      self.TableName:str = obj["TableName"]
      self.ErrorLevel:str = obj["ErrorLevel"]
      self.ErrorType:str = obj["ErrorType"]
      self.ErrorText:str = obj["ErrorText"]
      self.ErrorSysRowID:str = obj["ErrorSysRowID"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      pass

class Ice_BOUpdErrorTableset:
   def __init__(self, obj):
      self.BOUpdError:list[Ice_BOUpdErrorRow] = obj["BOUpdError"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Extensions_ExtensionRow:
   def __init__(self, obj):
      self.ColumnValues:object
      self.RowMod:str = obj["RowMod"]
      self.SysRowID:str = obj["SysRowID"]
      pass

class Ice_Extensions_ExtensionTableColumn:
   def __init__(self, obj):
      self.ColumnName:str = obj["ColumnName"]
      self.ColumnType:str = obj["ColumnType"]
      pass

class Ice_Extensions_ExtensionTableData:
   def __init__(self, obj):
      self.Table:list[Ice_Extensions_ExtensionRow] = obj["Table"]
      self.SystemCode:str = obj["SystemCode"]
      self.TableName:str = obj["TableName"]
      self.Columns:list[Ice_Extensions_ExtensionTableColumn] = obj["Columns"]
      self.PrimaryKeyColumns:str = obj["PrimaryKeyColumns"]
      self.PeerTableSystemCode:str = obj["PeerTableSystemCode"]
      self.PeerTableName:str = obj["PeerTableName"]
      pass

class ImportFromXML_input:
   """ Required : 
   typeName
   cRevisionList
   cXML
   compList
   bookMap
   """  
   def __init__(self, obj):
      self.typeName:str = obj["typeName"]
      """  ACTType Display Name  """  
      self.cRevisionList:str = obj["cRevisionList"]
      """  Revisions List  """  
      self.cXML:object
      """  XML Document Element  """  
      self.compList:str = obj["compList"]
      """  Companies List  """  
      self.bookMap:str = obj["bookMap"]
      """  Books Map as List  """  
      pass

class ImportFromXML_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ErrorMess:str = obj["parameters"]
      pass

      """  output parameters  """  

class ImportGLTransactionType_input:
   """ Required : 
   actTypeName
   cXML
   actTypeImportOpDs
   """  
   def __init__(self, obj):
      self.actTypeName:str = obj["actTypeName"]
      """  ACTType Display Name  """  
      self.cXML:object
      """  XML Document Element  """  
      self.actTypeImportOpDs:list[Erp_Tablesets_ACTTypeImportOpTableset] = obj["actTypeImportOpDs"]
      pass

class ImportGLTransactionType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ErrorMess:str = obj["parameters"]
      pass

      """  output parameters  """  

class ImportProcessIsAllowed_output:
   def __init__(self, obj):
      pass

class InitializeForTests_output:
   def __init__(self, obj):
      pass

class IsVarInUse_input:
   """ Required : 
   acttypeuid
   actrevisionuid
   bookid
   bookvaruid
   errorreturn
   """  
   def __init__(self, obj):
      self.acttypeuid:int = obj["acttypeuid"]
      """  acttypeuid  """  
      self.actrevisionuid:int = obj["actrevisionuid"]
      """  actrevisionuid  """  
      self.bookid:str = obj["bookid"]
      """  bookid  """  
      self.bookvaruid:int = obj["bookvaruid"]
      """  bookvaruid  """  
      self.errorreturn:bool = obj["errorreturn"]
      """  errorreturn  """  
      pass

class IsVarInUse_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.isinuse:bool = obj["isinuse"]
      pass

      """  output parameters  """  

class ListMappedBooksWithRules_input:
   """ Required : 
   actTypeUID
   actRevisionUID
   """  
   def __init__(self, obj):
      self.actTypeUID:int = obj["actTypeUID"]
      """  actTypeUID  """  
      self.actRevisionUID:int = obj["actRevisionUID"]
      """  iACTRevisionUID  """  
      pass

class ListMappedBooksWithRules_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class LoadABTStructure_input:
   """ Required : 
   actTypeUID
   actRevisionUID
   docLinePathSelection
   showAmountChild
   isEntityMenu
   showEntityEmptyOrBAQ
   """  
   def __init__(self, obj):
      self.actTypeUID:int = obj["actTypeUID"]
      self.actRevisionUID:int = obj["actRevisionUID"]
      self.docLinePathSelection:str = obj["docLinePathSelection"]
      self.showAmountChild:bool = obj["showAmountChild"]
      self.isEntityMenu:bool = obj["isEntityMenu"]
      self.showEntityEmptyOrBAQ:bool = obj["showEntityEmptyOrBAQ"]
      pass

class LoadABTStructure_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ACTTypeSubDataTableset] = obj["returnObj"]
      pass

class LoadACTBook_input:
   """ Required : 
   actTypeUID
   actRevisionUID
   bookID
   isFullLoad
   developMode
   ds
   """  
   def __init__(self, obj):
      self.actTypeUID:int = obj["actTypeUID"]
      """  aCTTypeUID  """  
      self.actRevisionUID:int = obj["actRevisionUID"]
      """  actRevisionUID  """  
      self.bookID:str = obj["bookID"]
      """  bookID  """  
      self.isFullLoad:int = obj["isFullLoad"]
      """  isFullLoad  """  
      self.developMode:bool = obj["developMode"]
      """  developMode  """  
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

class LoadACTBook_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class LoadACTType_input:
   """ Required : 
   actTypeUID
   """  
   def __init__(self, obj):
      self.actTypeUID:int = obj["actTypeUID"]
      """  aCTTypeUID  """  
      pass

class LoadACTType_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ACTTypeTableset] = obj["returnObj"]
      pass

class LoadAmount_input:
   """ Required : 
   actTypeUID
   actRevisionUID
   abtDocLineUID
   developMode
   ds
   """  
   def __init__(self, obj):
      self.actTypeUID:int = obj["actTypeUID"]
      """  aCTTypeUID  """  
      self.actRevisionUID:int = obj["actRevisionUID"]
      """  actRevisionUID  """  
      self.abtDocLineUID:int = obj["abtDocLineUID"]
      """  abtDocLineUID  """  
      self.developMode:bool = obj["developMode"]
      """  developMode  """  
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

class LoadAmount_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class LoadBROperation_input:
   """ Required : 
   actTypeUID
   actRevisionUID
   bookID
   bookingRuleUID
   developMode
   ds
   """  
   def __init__(self, obj):
      self.actTypeUID:int = obj["actTypeUID"]
      """  aCTTypeUID  """  
      self.actRevisionUID:int = obj["actRevisionUID"]
      """  actRevisionUID  """  
      self.bookID:str = obj["bookID"]
      """  bookID  """  
      self.bookingRuleUID:int = obj["bookingRuleUID"]
      """  bookingRuleUID  """  
      self.developMode:bool = obj["developMode"]
      """  developMode  """  
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

class LoadBROperation_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class LoadBookDataForImport_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeImportBookTableset] = obj["ds"]
      pass

class LoadBookDataForImport_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeImportBookTableset] = obj["ds"]
      pass

      """  output parameters  """  

class LoadBookVar_input:
   """ Required : 
   actTypeUID
   actRevisionUID
   bookID
   developMode
   ds
   """  
   def __init__(self, obj):
      self.actTypeUID:int = obj["actTypeUID"]
      """  aCTTypeUID  """  
      self.actRevisionUID:int = obj["actRevisionUID"]
      """  actRevisionUID  """  
      self.bookID:str = obj["bookID"]
      """  bookID  """  
      self.developMode:bool = obj["developMode"]
      """  developMode  """  
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

class LoadBookVar_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class LoadBooks_input:
   """ Required : 
   aCTRevisionUID
   """  
   def __init__(self, obj):
      self.aCTRevisionUID:int = obj["aCTRevisionUID"]
      pass

class LoadBooks_output:
   def __init__(self, obj):
      pass

class LoadBrFuncArgs_input:
   """ Required : 
   actTypeUID
   actRevisionUID
   functionUID
   developMode
   ds
   """  
   def __init__(self, obj):
      self.actTypeUID:int = obj["actTypeUID"]
      """  aCTTypeUID  """  
      self.actRevisionUID:int = obj["actRevisionUID"]
      """  actRevisionUID  """  
      self.functionUID:int = obj["functionUID"]
      """  functionUID  """  
      self.developMode:bool = obj["developMode"]
      """  developMode  """  
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

class LoadBrFuncArgs_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class LoadBrFuncOperation_input:
   """ Required : 
   actTypeUID
   actRevisionUID
   functionUID
   developMode
   ds
   """  
   def __init__(self, obj):
      self.actTypeUID:int = obj["actTypeUID"]
      """  aCTTypeUID  """  
      self.actRevisionUID:int = obj["actRevisionUID"]
      """  actRevisionUID  """  
      self.functionUID:int = obj["functionUID"]
      """  functionUID  """  
      self.developMode:bool = obj["developMode"]
      """  developMode  """  
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

class LoadBrFuncOperation_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class LoadDocumentLineBAQParam_input:
   """ Required : 
   actTypeUID
   actRevisionUID
   abtDocLineUID
   abtQueryUID
   developMode
   ds
   """  
   def __init__(self, obj):
      self.actTypeUID:int = obj["actTypeUID"]
      """  aCTTypeUID  """  
      self.actRevisionUID:int = obj["actRevisionUID"]
      """  actRevisionUID  """  
      self.abtDocLineUID:int = obj["abtDocLineUID"]
      """  abtDocLineUID  """  
      self.abtQueryUID:int = obj["abtQueryUID"]
      """  abtQueryUID  """  
      self.developMode:bool = obj["developMode"]
      """  developMode  """  
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

class LoadDocumentLineBAQParam_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class LoadDocumentLineBAQ_input:
   """ Required : 
   actTypeUID
   actRevisionUID
   abtDocLineUID
   developMode
   ds
   """  
   def __init__(self, obj):
      self.actTypeUID:int = obj["actTypeUID"]
      """  aCTTypeUID  """  
      self.actRevisionUID:int = obj["actRevisionUID"]
      """  actRevisionUID  """  
      self.abtDocLineUID:int = obj["abtDocLineUID"]
      """  abtDocLineUID  """  
      self.developMode:bool = obj["developMode"]
      """  developMode  """  
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

class LoadDocumentLineBAQ_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class LoadDocumentLine_input:
   """ Required : 
   actTypeUID
   actRevisionUID
   abtDocLineUID
   isFullLoad
   developMode
   ds
   """  
   def __init__(self, obj):
      self.actTypeUID:int = obj["actTypeUID"]
      """  aCTTypeUID  """  
      self.actRevisionUID:int = obj["actRevisionUID"]
      """  actRevisionUID  """  
      self.abtDocLineUID:int = obj["abtDocLineUID"]
      """  abtDocLineUID  """  
      self.isFullLoad:int = obj["isFullLoad"]
      """  isFullLoad  """  
      self.developMode:bool = obj["developMode"]
      """  developMode  """  
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

class LoadDocumentLine_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class LoadFunction_input:
   """ Required : 
   actTypeUID
   actRevisionUID
   bookID
   functionUID
   isFullLoad
   developMode
   ds
   """  
   def __init__(self, obj):
      self.actTypeUID:int = obj["actTypeUID"]
      """  aCTTypeUID  """  
      self.actRevisionUID:int = obj["actRevisionUID"]
      """  actRevisionUID  """  
      self.bookID:str = obj["bookID"]
      """  bookID  """  
      self.functionUID:int = obj["functionUID"]
      """  functionUID  """  
      self.isFullLoad:int = obj["isFullLoad"]
      """  isFullLoad  """  
      self.developMode:bool = obj["developMode"]
      """  developMode  """  
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

class LoadFunction_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class LoadGLCntrlTypes_input:
   """ Required : 
   glControlType
   """  
   def __init__(self, obj):
      self.glControlType:str = obj["glControlType"]
      pass

class LoadGLCntrlTypes_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ACTTypeSubDataTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.value:str = obj["parameters"]
      self.dataType:str = obj["parameters"]
      pass

      """  output parameters  """  

class LoadRevisionVersions_input:
   """ Required : 
   ds
   actTypeUID
   actRevisionUID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      self.actTypeUID:int = obj["actTypeUID"]
      """  actTypeUID  """  
      self.actRevisionUID:int = obj["actRevisionUID"]
      """  actRevisionUID  """  
      pass

class LoadRevisionVersions_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class LoadRevision_input:
   """ Required : 
   actTypeUID
   actRevisionUID
   isFullLoad
   developMode
   ds
   """  
   def __init__(self, obj):
      self.actTypeUID:int = obj["actTypeUID"]
      """  aCTTypeUID  """  
      self.actRevisionUID:int = obj["actRevisionUID"]
      """  actRevisionUID  """  
      self.isFullLoad:int = obj["isFullLoad"]
      """  isFullLoad  """  
      self.developMode:bool = obj["developMode"]
      """  developMode  """  
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

class LoadRevision_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class LoadRuleVariables_input:
   """ Required : 
   actTypeUID
   actRevisionUID
   bookID
   bookingRuleUID
   developMode
   ds
   """  
   def __init__(self, obj):
      self.actTypeUID:int = obj["actTypeUID"]
      self.actRevisionUID:int = obj["actRevisionUID"]
      self.bookID:str = obj["bookID"]
      self.bookingRuleUID:int = obj["bookingRuleUID"]
      self.developMode:bool = obj["developMode"]
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

class LoadRuleVariables_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class LoadRule_input:
   """ Required : 
   actTypeUID
   actRevisionUID
   bookID
   bookingRuleUID
   isFullLoad
   developMode
   ds
   """  
   def __init__(self, obj):
      self.actTypeUID:int = obj["actTypeUID"]
      """  aCTTypeUID  """  
      self.actRevisionUID:int = obj["actRevisionUID"]
      """  actRevisionUID  """  
      self.bookID:str = obj["bookID"]
      """  bookID  """  
      self.bookingRuleUID:int = obj["bookingRuleUID"]
      """  bookingRuleUID  """  
      self.isFullLoad:int = obj["isFullLoad"]
      """  isFullLoad  """  
      self.developMode:bool = obj["developMode"]
      """  developMode  """  
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

class LoadRule_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class LoadSystemGLTransactionType_input:
   """ Required : 
   package
   actTypeName
   ds
   """  
   def __init__(self, obj):
      self.package:str = obj["package"]
      """  Package  """  
      self.actTypeName:str = obj["actTypeName"]
      """  GL Transaction type Name  """  
      self.ds:list[Erp_Tablesets_ACTTypeImportOpTableset] = obj["ds"]
      pass

class LoadSystemGLTransactionType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeImportOpTableset] = obj["ds"]
      self.ErrorMess:str = obj["parameters"]
      pass

      """  output parameters  """  

class LoadTwoDatasetsTestMethod1_input:
   """ Required : 
   lcdsContainer
   ds
   """  
   def __init__(self, obj):
      self.lcdsContainer:list[Erp_Tablesets_LinkComboDataTableset] = obj["lcdsContainer"]
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

class LoadTwoDatasetsTestMethod1_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.lcdsContainer:list[Erp_Tablesets_LinkComboDataTableset] = obj["lcdsContainer"]
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnBRFuncOperationContainerTypeChanging_input:
   """ Required : 
   proposedValue
   ds
   """  
   def __init__(self, obj):
      self.proposedValue:str = obj["proposedValue"]
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

class OnBRFuncOperationContainerTypeChanging_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnBRFuncOperationIsLogicalConditionChanged_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

class OnBRFuncOperationIsLogicalConditionChanged_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_LinkComboDataTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnBROperationContainerTypeChanging_input:
   """ Required : 
   proposedValue
   ds
   """  
   def __init__(self, obj):
      self.proposedValue:str = obj["proposedValue"]
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

class OnBROperationContainerTypeChanging_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnBROperationCustomContainerTypeChanging_input:
   """ Required : 
   proposedValue
   ds
   """  
   def __init__(self, obj):
      self.proposedValue:str = obj["proposedValue"]
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

class OnBROperationCustomContainerTypeChanging_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnBROperationCustomIsLogicalConditionChanged_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

class OnBROperationCustomIsLogicalConditionChanged_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_LinkComboDataTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnBROperationIsLogicalConditionChanged_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

class OnBROperationIsLogicalConditionChanged_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_LinkComboDataTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeBRFunctionFormula_input:
   """ Required : 
   actTypeUID
   actRevisionUID
   bookID
   functionUID
   newFormula
   """  
   def __init__(self, obj):
      self.actTypeUID:int = obj["actTypeUID"]
      """  aCTTypeUID  """  
      self.actRevisionUID:int = obj["actRevisionUID"]
      """  actRevisionUID  """  
      self.bookID:str = obj["bookID"]
      """  bookID  """  
      self.functionUID:int = obj["functionUID"]
      """  functionUID  """  
      self.newFormula:str = obj["newFormula"]
      """  new formula  """  
      pass

class OnChangeBRFunctionFormula_output:
   def __init__(self, obj):
      pass

class OnChangeBRFunctionPhraseElementArgType_input:
   """ Required : 
   newType
   ds
   """  
   def __init__(self, obj):
      self.newType:str = obj["newType"]
      self.ds:list[Erp_Tablesets_ACTTypeSubDataTableset] = obj["ds"]
      pass

class OnChangeBRFunctionPhraseElementArgType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeSubDataTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeBRFunctionPhraseElementText_input:
   """ Required : 
   newText
   ds
   dsSub
   """  
   def __init__(self, obj):
      self.newText:str = obj["newText"]
      """  new element text  """  
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      self.dsSub:list[Erp_Tablesets_ACTTypeSubDataTableset] = obj["dsSub"]
      pass

class OnChangeBRFunctionPhraseElementText_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      self.dsSub:list[Erp_Tablesets_ACTTypeSubDataTableset] = obj["dsSub"]
      pass

      """  output parameters  """  

class OnChangeBRFunctionPhraseElementType_input:
   """ Required : 
   newType
   ds
   """  
   def __init__(self, obj):
      self.newType:str = obj["newType"]
      """  new type  """  
      self.ds:list[Erp_Tablesets_ACTTypeSubDataTableset] = obj["ds"]
      pass

class OnChangeBRFunctionPhraseElementType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeSubDataTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeBVRuleAction_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

class OnChangeBVRuleAction_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeBookingRuleName_input:
   """ Required : 
   actTypeUID
   actRevisionUID
   bookID
   ruleUID
   newName
   """  
   def __init__(self, obj):
      self.actTypeUID:int = obj["actTypeUID"]
      """  aCTTypeUID  """  
      self.actRevisionUID:int = obj["actRevisionUID"]
      """  actRevisionUID  """  
      self.bookID:str = obj["bookID"]
      """  bookID  """  
      self.ruleUID:int = obj["ruleUID"]
      """  ruleUID  """  
      self.newName:str = obj["newName"]
      """  new DispalyName  """  
      pass

class OnChangeBookingRuleName_output:
   def __init__(self, obj):
      pass

class OnChangeEntityDataSource_input:
   """ Required : 
   iNewDataSource
   ds
   """  
   def __init__(self, obj):
      self.iNewDataSource:str = obj["iNewDataSource"]
      """  Proposed Value  """  
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

class OnChangeEntityDataSource_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangingABTQuery_input:
   """ Required : 
   ACTTypeUID
   ACTRevisionUID
   ABTDocLineUID
   BAQID
   NewBAQID
   """  
   def __init__(self, obj):
      self.ACTTypeUID:int = obj["ACTTypeUID"]
      """  ACTTypeUID  """  
      self.ACTRevisionUID:int = obj["ACTRevisionUID"]
      """  ACTRevisionUID  """  
      self.ABTDocLineUID:int = obj["ABTDocLineUID"]
      """  ABTDocLineUID  """  
      self.BAQID:str = obj["BAQID"]
      """  BAQID  """  
      self.NewBAQID:str = obj["NewBAQID"]
      """  NewBAQID  """  
      pass

class OnChangingABTQuery_output:
   def __init__(self, obj):
      pass

class OnChangingPostCode_input:
   """ Required : 
   ACTTypeUID
   ACTRevisionUID
   ABTDocLineUID
   ABTPostEntityUID
   postCodePath
   newPostCode
   """  
   def __init__(self, obj):
      self.ACTTypeUID:int = obj["ACTTypeUID"]
      """  ACTTypeUID  """  
      self.ACTRevisionUID:int = obj["ACTRevisionUID"]
      """  ACTRevisionUID  """  
      self.ABTDocLineUID:int = obj["ABTDocLineUID"]
      """  ACTRevisionUID  """  
      self.ABTPostEntityUID:int = obj["ABTPostEntityUID"]
      """  ABTPostEntityUID  """  
      self.postCodePath:str = obj["postCodePath"]
      """  postCodePath  """  
      self.newPostCode:str = obj["newPostCode"]
      """  newPostCode  """  
      pass

class OnChangingPostCode_output:
   def __init__(self, obj):
      pass

class OperationFunctionUIDChanging_input:
   """ Required : 
   actTypeUID
   actRevisionUID
   ruleUID
   container
   containerType
   bookID
   docLinePath
   funcOperUID
   isLogicalCondition
   bindingSuffix
   proposedValue
   ds
   """  
   def __init__(self, obj):
      self.actTypeUID:int = obj["actTypeUID"]
      self.actRevisionUID:int = obj["actRevisionUID"]
      self.ruleUID:int = obj["ruleUID"]
      self.container:str = obj["container"]
      self.containerType:str = obj["containerType"]
      self.bookID:str = obj["bookID"]
      self.docLinePath:str = obj["docLinePath"]
      """  BRFunction.DocLinePath OR BookingRule.ForEach  """  
      self.funcOperUID:int = obj["funcOperUID"]
      """  0 if not BRFuncOperation  """  
      self.isLogicalCondition:bool = obj["isLogicalCondition"]
      self.bindingSuffix:str = obj["bindingSuffix"]
      """  'Custom' if BROperation, 'FuncOper' of BRFuncOperation, '' if BROperation  """  
      self.proposedValue:int = obj["proposedValue"]
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

class OperationFunctionUIDChanging_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_LinkComboDataTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class PopulationMethodChanging_input:
   """ Required : 
   populationMethod
   developMode
   ds
   """  
   def __init__(self, obj):
      self.populationMethod:int = obj["populationMethod"]
      """  new populationMethod value  """  
      self.developMode:bool = obj["developMode"]
      """  flag DevelopMode  """  
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

class PopulationMethodChanging_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class PostCodeSourceRefresh_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

class PostCodeSourceRefresh_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ProcessFormulaParamClickCustom_input:
   """ Required : 
   clickedTag
   linkComboDS
   ds
   """  
   def __init__(self, obj):
      self.clickedTag:str = obj["clickedTag"]
      self.linkComboDS:list[Erp_Tablesets_LinkComboDataTableset] = obj["linkComboDS"]
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

class ProcessFormulaParamClickCustom_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ACTTypeSubDataTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.value:str = obj["parameters"]
      self.dataType:str = obj["parameters"]
      self.linkComboDS:list[Erp_Tablesets_LinkComboDataTableset] = obj["linkComboDS"]
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ProcessFormulaParamClickFuncOper_input:
   """ Required : 
   clickedTag
   linkComboDS
   ds
   """  
   def __init__(self, obj):
      self.clickedTag:str = obj["clickedTag"]
      self.linkComboDS:list[Erp_Tablesets_LinkComboDataTableset] = obj["linkComboDS"]
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

class ProcessFormulaParamClickFuncOper_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ACTTypeSubDataTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.value:str = obj["parameters"]
      self.dataType:str = obj["parameters"]
      self.linkComboDS:list[Erp_Tablesets_LinkComboDataTableset] = obj["linkComboDS"]
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ProcessFormulaParamClick_input:
   """ Required : 
   clickedTag
   linkComboDS
   ds
   """  
   def __init__(self, obj):
      self.clickedTag:str = obj["clickedTag"]
      self.linkComboDS:list[Erp_Tablesets_LinkComboDataTableset] = obj["linkComboDS"]
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

class ProcessFormulaParamClick_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ACTTypeSubDataTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.value:str = obj["parameters"]
      self.dataType:str = obj["parameters"]
      self.linkComboDS:list[Erp_Tablesets_LinkComboDataTableset] = obj["linkComboDS"]
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class RefreshBookList_input:
   """ Required : 
   aCTRevisionUID
   """  
   def __init__(self, obj):
      self.aCTRevisionUID:int = obj["aCTRevisionUID"]
      """  ACTRevisionUID  """  
      pass

class RefreshBookList_output:
   def __init__(self, obj):
      pass

class RevisionCopyFrom_input:
   """ Required : 
   actTypeCopyFromUID
   revisionCopyFromUID
   isDocOnly
   """  
   def __init__(self, obj):
      self.actTypeCopyFromUID:int = obj["actTypeCopyFromUID"]
      """  actTypeCopyFromUID  """  
      self.revisionCopyFromUID:int = obj["revisionCopyFromUID"]
      """  RevisionCopyFromUID  """  
      self.isDocOnly:bool = obj["isDocOnly"]
      """  isDocOnly  """  
      pass

class RevisionCopyFrom_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.newRevUID:int = obj["parameters"]
      pass

      """  output parameters  """  

class RevisionStatusChanging_input:
   """ Required : 
   proposedValue
   developMode
   answer
   ds
   """  
   def __init__(self, obj):
      self.proposedValue:str = obj["proposedValue"]
      """  proposed value of Revision Status  """  
      self.developMode:bool = obj["developMode"]
      """  Developer mode  """  
      self.answer:str = obj["answer"]
      """  User's answer on question. For second pass.  """  
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

class RevisionStatusChanging_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.question:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class SelectionCriteriaAddOnClick_input:
   """ Required : 
   dataType
   ABTField
   ds
   """  
   def __init__(self, obj):
      self.dataType:str = obj["dataType"]
      self.ABTField:str = obj["ABTField"]
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

class SelectionCriteriaAddOnClick_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class TableDataFieldChanging_input:
   """ Required : 
   proposedValue
   ds
   """  
   def __init__(self, obj):
      self.proposedValue:str = obj["proposedValue"]
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

class TableDataFieldChanging_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class TryCompile_input:
   """ Required : 
   companyName
   aCTTypeUID
   aCTRevisionUID
   """  
   def __init__(self, obj):
      self.companyName:str = obj["companyName"]
      """  Company ID  """  
      self.aCTTypeUID:int = obj["aCTTypeUID"]
      """  ACTType ID  """  
      self.aCTRevisionUID:int = obj["aCTRevisionUID"]
      """  ACTRevision ID  """  
      pass

class TryCompile_output:
   def __init__(self, obj):
      pass

class UndoUpdateVersionsWithRefreshDS_input:
   """ Required : 
   actTypeUID
   actRevisionUID
   ds
   """  
   def __init__(self, obj):
      self.actTypeUID:int = obj["actTypeUID"]
      """  ACTTypeUID  """  
      self.actRevisionUID:int = obj["actRevisionUID"]
      """  ACTRevisionUID  """  
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

class UndoUpdateVersionsWithRefreshDS_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtACTTypeTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtACTTypeTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class UpdateTwoDatasetsTestMethod1_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LinkComboDataTableset] = obj["ds"]
      pass

class UpdateTwoDatasetsTestMethod1_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LinkComboDataTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateVersionsWithRefreshDS_input:
   """ Required : 
   actTypeUID
   actRevisionUID
   updatePatchVer
   ds
   """  
   def __init__(self, obj):
      self.actTypeUID:int = obj["actTypeUID"]
      """  ACTTypeUID  """  
      self.actRevisionUID:int = obj["actRevisionUID"]
      """  ACTRevisionUID  """  
      self.updatePatchVer:bool = obj["updatePatchVer"]
      """  it is true if need update Patch Versions  """  
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

class UpdateVersionsWithRefreshDS_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateABTVerForImport_input:
   """ Required : 
   actTypeName
   newRevCode
   newABTVer
   newPatchABTVer
   updateMode
   importABT
   importRulseset
   """  
   def __init__(self, obj):
      self.actTypeName:str = obj["actTypeName"]
      """  ACTType Name  """  
      self.newRevCode:str = obj["newRevCode"]
      """  New RevisionCode  """  
      self.newABTVer:str = obj["newABTVer"]
      """  New ABT Version  """  
      self.newPatchABTVer:str = obj["newPatchABTVer"]
      """  New Patch ABT Version  """  
      self.updateMode:bool = obj["updateMode"]
      """  In Update Mode  """  
      self.importABT:bool = obj["importABT"]
      """  Need Import ABT Structure  """  
      self.importRulseset:bool = obj["importRulseset"]
      """  Need Import Ruleset  """  
      pass

class ValidateABTVerForImport_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.outCanBeImported:bool = obj["outCanBeImported"]
      self.outCanBeActivated:bool = obj["outCanBeActivated"]
      self.outMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class ValidateCOAMap_input:
   """ Required : 
   ipCOAMapUID
   ipSourceCOA
   ipMappedCOA
   """  
   def __init__(self, obj):
      self.ipCOAMapUID:int = obj["ipCOAMapUID"]
      self.ipSourceCOA:str = obj["ipSourceCOA"]
      self.ipMappedCOA:str = obj["ipMappedCOA"]
      pass

class ValidateCOAMap_output:
   def __init__(self, obj):
      pass

